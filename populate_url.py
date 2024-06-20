import argparse
from langchain_community.document_loaders import RecursiveUrlLoader
import populate_database
import yaml

URL_PATH = "url_data.yaml"


def main():

    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        populate_database.clear_database()

    # Create (or update) the data store.
    for url in yaml_loader(URL_PATH).get('url', None):
        documents = load_url(url)
        chunks = populate_database.split_documents(documents)
        populate_database.add_to_chroma(chunks)


def yaml_loader(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return data


def load_url(url):
    loader = RecursiveUrlLoader(url)
    return loader.load()


if __name__ == "__main__":
    main()

