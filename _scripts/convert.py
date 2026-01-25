#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

JSON_FILE = ROOT / "_data" / "scholar_publications.json"
BIB_FILE  = ROOT / "_bibliography" / "papers.bib"


def sanitize_key(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "", text)
    return text[:20] if text else "key"


def format_authors(authors):
    """
    ["A B", "C D"] → "A B and C D"
    """
    if isinstance(authors, list):
        return " and ".join(authors)
    return authors or ""


def detect_entry_type(pub):
    if pub.get("booktitle") or pub.get("conference"):
        return "inproceedings"
    if pub.get("publisher") and not pub.get("journal"):
        return "book"
    return "article"

def safe_year(pub):
    try:
        return int(pub.get("year", 0))
    except (TypeError, ValueError):
        return 0

def json_to_bibtex():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        pubs = json.load(f)

    # 🔹 Sort by year (newest first)
    # 🔹 Sort by year (newest first), safely handling "N/A"
        pubs = sorted(
                pubs,
                key=safe_year,
                reverse=True
        )


    entries = []

    for idx, pub in enumerate(pubs):
        entry_type = detect_entry_type(pub)

        title   = pub.get("title", "Untitled")
        authors = format_authors(pub.get("authors", ""))
        year    = pub.get("year", "")
        journal = pub.get("journal", pub.get("venue", ""))
        volume  = pub.get("volume", "")
        number  = pub.get("number", "")
        pages   = pub.get("pages", "")
        doi     = pub.get("doi", "")
        url     = pub.get("url", "")
        booktitle = pub.get("booktitle", "")
        publisher = pub.get("publisher", "")

        first_author = authors.split(" and ")[0] if authors else "unknown"
        key = f"{sanitize_key(first_author)}{year}"

        entry = [f"@{entry_type}{{{key}"]

        entry.append(f"  title = {{{title}}}")
        if authors:
            entry.append(f"  author = {{{authors}}}")
        if year:
            entry.append(f"  year = {{{year}}}")

        # 🔹 Mark only latest 3 as selected
        if idx < 3:
            entry.append("  selected = {true}")

        if entry_type == "article" and journal:
            entry.append(f"  journal = {{{journal}}}")
        if entry_type == "inproceedings" and booktitle:
            entry.append(f"  booktitle = {{{booktitle}}}")
        if publisher:
            entry.append(f"  publisher = {{{publisher}}}")
        if volume:
            entry.append(f"  volume = {{{volume}}}")
        if number:
            entry.append(f"  number = {{{number}}}")
        if pages:
            entry.append(f"  pages = {{{pages}}}")
        if doi:
            entry.append(f"  doi = {{{doi}}}")
        if url:
            entry.append(f"  url = {{{url}}}")

        bibtex = ",\n".join(entry) + "\n}\n"
        entries.append(bibtex)

    BIB_FILE.parent.mkdir(exist_ok=True)
    BIB_FILE.write_text("\n".join(entries), encoding="utf-8")

    print(f"✔ Generated {BIB_FILE}")


if __name__ == "__main__":
    json_to_bibtex()
