# PDF Structure Parser

PDF Structure Parser is a Python project designed to extract the structure (e.g., chapters, sections, subsections) from PDF files and output it in a structured JSON format. This tool is particularly useful for processing large PDF documents with organized table of contents (TOC) that need to be converted into structured data.

## Features

- Extracts chapters, sections, and subsections from PDF files based on their TOC.
- Outputs the structure in a JSON format for easy integration with other systems.
- Supports different PDF TOC formats with flexible parsing configurations.

## Requirements

- Python 3.6+
- `PyMuPDF` (for PDF parsing)
- `python-dotenv` (for managing environment variables)

## Project Structure

```plaintext
TEST_PDF_PARSER/
├── data/                    # Folder for input PDF files
├── extracted_data/          # Folder for extracted JSON output
├── parsers/                 # Folder containing parser scripts
│   ├── __init__.py
│   ├── pdf_parser.py        # PDF parser script
│   └── pdf_parser_universal.py  # Alternative parser script
├── .env                     # Environment variables file
├── .gitignore               # Git ignore file
├── config.py                # Configuration file for environment variables
└── requirements.txt         # Project dependencies
```


## Installation
Clone the repository:

```bash
Copy code
git clone https://github.com/blackmachinelearning/pdf_structure_parser.git
cd pdf_structure_parser
```
Set up a virtual environment (recommended):

```bash
Copy code
python -m venv pymupdf-venv
source pymupdf-venv/bin/activate  # On Windows, use pymupdf-venv\Scripts\activate
```
Install dependencies:

```bash
Copy code
pip install -r requirements.txt
```
Configure environment variables:

Create a .env file in the project root directory (if needed for environment-specific configurations).
Add any necessary environment variables to .env.
Usage
Place your PDF files in the data/ directory.

Run the Parser:

You can use either pdf_parser.py or pdf_parser_universal.py from the parsers/ directory. The difference is: pdf_parser_universal will work with pretty much every file, which has any kind of structure, that we use in pymupdf library using get_toc() method. The pdf_parser works better to match the structure, which were given as a sample.
Example for running pdf_parser.py:
```bash
Copy code
python parsers/pdf_parser.py
```

```bash
Copy code
python parsers/pdf_parser_universal.py
```
Check the Output:

The structured JSON output will be saved in the extracted_data/ directory (or any specified output location).


