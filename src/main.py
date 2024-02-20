'''
Main function to extract text avd csv file from text
'''
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    text = ''
    ## Code snippet to extract text from pdf

    return text


def extract_tables_to_csv(pdf_path, output_folder):
    tables = []
    ### Code snippet to extract all tables from pdf

    for i, table in enumerate(tables):
        csv_path = f"{output_folder}/{Path(pdf_path).stem}_table_{i + 1}.csv"
        table.to_csv(csv_path, index=False)
        print(f"Table {i + 1} extracted and saved to {csv_path}")


if __name__ == "__main__":
    pdf_path = "../data/raw/your_pdf_file.pdf"
    output_folder = "../data/processed"

    # Convert PDF to text
    text_content = extract_text_from_pdf(pdf_path)

    with open(output_folder + f"/{Path(pdf_path).stem}.txt", 'w') as f:
        f.write(text_content)

    # Extract tables to CSV
    extract_tables_to_csv(pdf_path, output_folder)
