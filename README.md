# merge-pdfs

A simple, user-friendly Flask application for merging multiple PDF files into a single PDF.

## Project Overview

This project allows users to upload several PDF files through a web interface, merges them using [PyPDF2](https://pypi.org/project/PyPDF2/), and returns the merged PDF for download. The application is containerized using a [Dockerfile](Dockerfile) and is built with simplicity and ease-of-use in mind.

## Repository Structure

- **app.py** - The main Flask application that sets up web routes and handles the merging logic using [PyPDF2](https://pypi.org/project/PyPDF2/).
- **templates/index.html** - The HTML template that renders the form for uploading PDFs.
- **Dockerfile** - The Docker configuration file for containerizing the application.
- **requirements.txt** - Lists the Python dependencies: Flask and PyPDF2.
- **LICENSE** - The project is released under the MIT License.
- **.gitignore** - Specifies files and directories to be ignored by Git.
- **notebooks/** - Contains notebook files for experiments or testing (e.g., [notebooks/test.ipynb](notebooks/test.ipynb)).

## Setup and Installation

### Running Locally

1. **Clone the repository:**
    ```sh
    git clone https://github.com/NaseebGrewal/merge-pdfs.git
    cd merge-pdfs/merge-pdfs
    ```

2. **Create a virtual environment and install dependencies:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```sh
    python app.py
    ```
    The application will start on [http://localhost:5000](http://localhost:5000).

### Running with Docker

1. **Build the Docker image:**
    ```sh
    docker build -t merge-pdfs .
    ```

2. **Run the container:**
    ```sh
    docker run -p 5000:5000 merge-pdfs
    ```
    The application will be accessible at [http://localhost:5000](http://localhost:5000).

## Application Details

### Merging PDFs

The core merging functionality is implemented in the `merge_pdfs` function within [app.py](http://_vscodecontentref_/1). This function:
- Receives a list of uploaded PDF files.
- Uses [PyPDF2](https://pypi.org/project/PyPDF2/) to read and combine each page of every file.
- Writes the merged content to a temporary file and returns it for download.

### Web Interface

The user interface is defined in [index.html](http://_vscodecontentref_/2), which uses Bootstrap for styling. It includes:
- A file upload form that allows selecting multiple PDF files.
- A text input to optionally specify the output filename.
- A submit button that triggers the merging process.

### Error Handling

If any file cannot be processed, the application will display an error message using Flask’s flash messaging system. For more details, check out how errors are caught in the `merge_pdfs` function.

## Contributing

New developers are welcome to contribute. Please follow these steps:
- Fork the repository.
- Create a feature branch.
- Commit changes with clear commit messages.
- Push your changes and open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
- Bootstrap for the UI styling ([Bootstrap 5](https://getbootstrap.com/))
