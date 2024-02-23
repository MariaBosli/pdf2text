
# PDF Extraction: Text and Table, DOI Search

This Python project enables the extraction of text, tables, and DOI (Digital Object Identifier) from PDF files.

## Requirements

- Python 3.x
- Docker
## Usage

### Step 1: Setup
1. Ensure you have Docker installed on your system.
2. Download the pd3f-core project folder from pd3f-core GitHub repository (https://github.com/pd3f/pd3f-core)
### Step 2: Launch Docker
3. Navigate to the pd3f-core folder and launch Docker Compose using the following command:

```bash
docker-compose up

### Step 3: Run Extraction Scripts 
1. Place the PDF file you want to process in the specified location `data/row`.
2. Update the `pdf_path` variable in the script with the path to your PDF file.
3. Set the `output_folder` variable to the desired folder to save the extracted CSV files and text file: `data/processed`.
4. Run the script:

- Run `main.py` to extract text and tables:
```bash
python main.py

- Run `doi.py` to Search DOI:
```bash
python doi.py

## Output
- For `main.py`:
 * The script will generate a text file containing the extracted text from the PDF, saved in the specified output folder.
 * Separate CSV files will be created for each table found in the PDF, named with the PDF's stem (filename without extension) and table number.

- For `doi.py`:
  * The script will print the DOI found in the PDF metadata, if available.

### Project Structure
- `main.py`: The main script for extracting text and tables.
- `doi.py`: Script for extracting DOI from PDF metadata.
- `utils.py`: Module containing utility functions.
- `data/`: Directory containing input PDF files and results.
  - `raw/`: Location of PDF files to be processed.
  - `processed/`: Location where extracted text files and table CSVs will be saved.
