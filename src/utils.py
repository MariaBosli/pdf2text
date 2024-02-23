'''
Useful functions for the main code: pre-proces / postporcess functions
'''
import pandas as pd
from io import StringIO
import time
from habanero import Crossref # Pour l'accès à l'API Crossref


def postprocess_tables(input):
    """
    Post-processes table data extracted from a PDF.

    Args:
        input (str): The CSV data extracted from the table.

    Returns:
        pandas.DataFrame: The processed DataFrame containing the table data.
    """
    # Convertir la chaîne CSV en DataFrame
    df = pd.read_csv(StringIO(input))
    return df   


def fetch_doi_from_crossref(item, article_metadata):
    """
    Fetches the DOI for an article using its metadata from Crossref API.

    Args:
        item (dict): A dictionary containing the title and authors of the article.
        article_metadata (dict): The metadata of the article extracted from the PDF.

    Returns:
        tuple: A tuple containing the DOI and title of the article, if found. Otherwise, (None, None).
    """
    # Vérifier si le DOI est présent dans les métadonnées
    if 'doi' in article_metadata:
        return article_metadata['doi'], article_metadata.get('title', '')

    title = item.get('title')
    if not title:
        print("Impossible de chercher le DOI: Titre de l'article absent.")
        return None, None

    authors = item.get('authors', [])
    query = '"{}" {}'.format(title, ', '.join(authors))

    cr = Crossref()
    server_reached = False
    while not server_reached:
        try:
            query_result = cr.works(query=query, limit=3)
            server_reached = True
        except Exception as e:
            print("CrossRef server unavailable. Retry in 5 seconds")
            time.sleep(5)
    
    try:
        first_item = query_result['message']['items'][0]
        found_title = first_item.get('title', [''])[0]
        doi = first_item['DOI']
        return doi, found_title
    except (KeyError, IndexError):
        print("Aucun DOI trouvé pour l'article:", title)
        return None, None
    

def prepare_metadata_for_crossref(metadata):
    """
    Prepares metadata for article to be used for Crossref API query.

    Args:
        metadata (dict): The metadata of the article extracted from the PDF.

    Returns:
        dict: A dictionary containing the title and authors of the article.
    """
    title = metadata.get('Title', '')
    authors = metadata.get('Author', '').split(' and ')
    # Nettoyer les noms des auteurs
    authors = [author.strip() for author in authors]

    # Si aucun auteur n'est disponible, return une liste vide
    if not authors:
        authors = ['']

    return {'title': title, 'authors': authors}