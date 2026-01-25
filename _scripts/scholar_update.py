from scholarly import scholarly
import json
import os
import time
import sys
from pathlib import Path
import re

def extract_url_and_doi(pub_url):
    doi = ""
    url = pub_url or ""

    # Match DOI pattern anywhere in the URL
    match = re.search(r'(10\.\d{4,9}/[-._;()/:A-Z0-9]+)', url, re.I)
    if match:
        doi = match.group(1)

        # If it's a pure DOI resolver link, you may want to clear the URL
        if "doi.org" in url.lower():
            url = ""

    return url, doi


def get_author_data(author_id):
    try:
        # Search for the author with all available sections
        author = scholarly.search_author_id(author_id)
        author_filled = scholarly.fill(author, sections=[])
        print("Counts section:", json.dumps(author_filled.get("cites_per_year", {})))
        # Debug: Print partial author data
        print("Full author data:", json.dumps(author_filled, indent=2)[:500] + "...")
        # Get document count (total publications)
        document_count = len(author_filled.get("publications", []))
        # Extract metrics safely
        h_index = (
            author_filled.get("hindex") or
            author_filled.get("indices", {}).get("hindex")
        )
        i10_index = (
            author_filled.get("i10index") or
            author_filled.get("indices", {}).get("i10index")
        )

        profile = {
            "name": author_filled.get("name", "N/A"),
            "affiliation": author_filled.get("affiliation", "N/A"),
            "h_index": h_index if h_index is not None else 0,
            "citations": author_filled.get("citedby", 0),
            "documents": document_count,  # This is the document count
            "i10_index": i10_index if i10_index is not None else 0,
            "scholar_id": author_id,
            "url": f"https://scholar.google.com/citations?user={author_id}"
        }

        # Extract citation-per-year directly from "counts"
        citation_by_year = author_filled.get("cites_per_year", {})

        return profile, author_filled.get("publications", []), citation_by_year

    except Exception as e:
        print(f"Error fetching author data: {str(e)}")
        return None, [], {}


def get_publication_data(publications, max_publications=None):
    pub_data = []
    for pub in sorted(publications, key=lambda p: p.get("num_citations", 0), reverse=True)[:max_publications]:
        try:
            time.sleep(1)  # Avoid being blocked
            filled_pub = scholarly.fill(pub)
            bib = filled_pub.get("bib", {})
            
            # Extract authors (handle both string and list formats)
            authors = bib.get("author", "N/A")
            if isinstance(authors, list):
                authors = ", ".join(authors)  # Convert list to string
            elif not isinstance(authors, str):
                authors = "N/A"  # Fallback if invalid format
            raw_url = filled_pub.get("pub_url", "")
            url, doi = extract_url_and_doi(raw_url)
             # Check multiple possible fields for venue
            venue = bib.get("venue") or \
                    bib.get("journal") or \
                    bib.get("conference") or \
                    bib.get("booktitle") or \
                    bib.get("source", "N/A")  # Fallback

            pub_data.append({
                "title": bib.get("title", "N/A"),
                "authors": authors,  # Now includes authors!
                "year": bib.get("pub_year", "N/A"),
                "citations": filled_pub.get("num_citations", 0),
                "venue": venue,
                "url": url,
                "doi": doi
            })
        except Exception as e:
            print(f"Error processing publication: {e}")
            continue
    return pub_data


def save_to_json(data, filename):
    data_dir = Path(__file__).parent.parent / "_data"
    data_dir.mkdir(exist_ok=True)
    with open(data_dir / filename, "w") as f:
        json.dump(data, f, indent=2)


def main():
    author_id = "qOhxqbkAAAAJ"

    # Get profile, publications, and citation trend
    profile, publications, citation_by_year = get_author_data(author_id)

    if not profile:
        print("Failed to fetch author profile")
        return

    pub_data = get_publication_data(publications)

    # Save everything
    save_to_json(profile, "scholar.json")
    save_to_json(pub_data, "scholar_publications.json")
    save_to_json(citation_by_year, "scholar_citations.json")

    print("✅ Google Scholar data saved successfully.")
    print(f"• Profile: {profile['name']}")
    print(f"• Publications processed: {len(pub_data)}")
    print(f"• Citation years extracted: {len(citation_by_year)}")


if __name__ == "__main__":
    main()
