'''
Main function to extract text and csv file from text
'''
from pathlib import Path
import pdfx # Pour extraire le contenu textuel des fichiers PDF
import collections.abc
# Hyper nécessite les quatre alias suivants pour être effectués manuellement.
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping
from pd3f import extract # Pour extraire les tableaux des fichiers PDF
from utils import postprocess_tables # Pour le prétraitement des tableaux extraits


def extract_text_from_pdf(pdf_path):
    """
    Extracts text content from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text content.
    """
    text = ''
    try:
        pdf = pdfx.PDFx(pdf_path)
        text = pdf.get_text()
    except Exception as e:
        print("Une erreur s'est produite lors de l'extraction du texte du PDF:", e)
    return text



def extract_tables_to_csv(pdf_path, output_folder):
    """
    Extracts tables from a PDF file and saves them as CSV files.

    Args:
        pdf_path (str): The path to the PDF file.
        output_folder (str): The folder where the CSV files will be saved.
    """
    #tables = []
    text, tables = extract(pdf_path, tables=True, experimental=False, force_gpu=False, lang="multi", fast=False, parsr_location="localhost:3001")


    for i, table in enumerate(tables):
       # Prétraiter le tableau
       df = postprocess_tables(table)
       csv_path = f"{output_folder}/{Path(pdf_path).stem}_table_{i + 1}.csv"
       df.to_csv(csv_path, index=False)
       print(f"Table {i + 1} extracted and saved to {csv_path}")



if __name__ == "__main__":
    pdf_path = "../data/raw/input.pdf"
    output_folder = "../data/processed"

    # Convert PDF to text
    text_content = extract_text_from_pdf(pdf_path)

    with open(output_folder + f"/{Path(pdf_path).stem}.txt", 'w') as f:
        f.write(text_content)

    #Extract tables to CSV
    extract_tables_to_csv(pdf_path, output_folder)

  