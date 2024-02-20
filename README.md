
# PDF to Text and Table Extraction

This Python script extracts text and tables from a PDF file.

## Requirements

- Python 3.x

## Usage

1. Place the PDF file you want to process in the specified location `data/row`.
2. Update the `pdf_path` variable in the script with the path to your PDF file.
3. Set the `output_folder` variable to the desired folder to save the extracted CSV files and text file: `data/processed`.
4. Run the script:

```bash
python src/main.py
```

## Output
* The script will generate a text file containing the extracted text from the PDF, saved in the specified output folder.
* Separate CSV files will be created for each table found in the PDF, named with the PDF's stem (filename without extension) and table number.