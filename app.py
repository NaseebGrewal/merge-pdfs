"""
Flask application for merging multiple PDF files into a single PDF.
application allows users to upload multiple PDF files, merge them into a single PDF, and download the merged PDF.

usage: app.py
"""

# Import required libraries
from flask import Flask, request, send_file, render_template, flash
import PyPDF2
import os
import tempfile

# Initialize Flask application
app = Flask(__name__)

# Set the secret key for flashing messages
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Define helper function to merge PDF files
def merge_pdfs(files) -> PyPDF2.PdfWriter:
    """
    Merge multiple PDF files into a single PDF.
    :param files: List of uploaded files.
    :return: PyPDF2.PdfWriter object.
    """
    pdf_writer = PyPDF2.PdfWriter()
    for file in files:
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
        except Exception as e:
            raise Exception(f"Error processing file {file.filename}: {e}")
    return pdf_writer

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route for the application.
    :return: Rendered HTML template or merged PDF file.
    """
    # Handle POST request
    if request.method == "POST":
        uploaded_files = request.files.getlist("pdfs")
        output_filename = request.form.get("output_name", "").strip()  # Retrieve and strip whitespace
        
        # Validate input
        if not uploaded_files:
            flash("Please upload at least one PDF.")
            return render_template("index.html")
        
        # Default to "merged.pdf" if no filename is provided
        if not output_filename:
            output_filename = "merged.pdf"
        else:
            # Ensure the filename ends with ".pdf"
            if not output_filename.lower().endswith('.pdf'):
                output_filename += ".pdf"
        
        # Append .pdf extension if not provided
        if not output_filename.lower().endswith('.pdf'):
            output_filename += ".pdf"

        # Merge PDF files
        try:
            pdf_writer = merge_pdfs(uploaded_files)
        except Exception as error:
            flash(str(error))
            return render_template("index.html")
        
        # Save merged PDF to a temporary file
        temp_dir = tempfile.gettempdir()
        output_path = os.path.join(temp_dir, output_filename)
        with open(output_path, "wb") as out_file:
            pdf_writer.write(out_file)
        
        return send_file(output_path, as_attachment=True)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
