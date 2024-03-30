'''
Main function to search Doi
'''
from pathlib import Path
from utils import fetch_doi_from_crossref, prepare_metadata_for_crossref
import pdfx # Pour extraire les métadonnées des fichiers PDF

def searchDoi(pdf_path):
    """
    Searches for DOI (Digital Object Identifier) for an article PDF.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        None
    """
    # Extraire les métadonnées du PDF
    pdf = pdfx.PDFx(pdf_path)
    article_metadata = pdf.get_metadata()
    # Préparer les métadonnées pour la recherche du DOI
    prepared_metadata = prepare_metadata_for_crossref(article_metadata)
    # Rechercher le DOI en utilisant les métadonnées préparées
    doi, title = fetch_doi_from_crossref(prepared_metadata, article_metadata)
    # Afficher le DOI s'il est trouvé, sinon afficher un message indiquant que le DOI n'est pas trouvé
    if doi:
        print("DOI trouvé avec fetch_doi_from_crossref:", doi)
    else:
        print("Aucun DOI trouvé.")


if __name__ == "__main__":
   pdf_path = "../data/raw/article6.pdf"
 
   # Rechercher le DOI dans le PDF spécifié
   searchDoi(pdf_path)