from scholarly import scholarly

def search_google_scholar(query):
    search_results = scholarly.search_pubs(query)
    papers = []
    for result in search_results:
        try:
            pub = scholarly.fill(result)
        except Exception:
            pub = result
        bib = pub.get("bib", {})
        paper = {
            "title": bib.get("title"),
            "authors": ", ".join(bib.get("author", [])) if isinstance(bib.get("author"), list) else bib.get("author"),
            "year": bib.get("pub_year"),
            "publisher": bib.get("publisher"),
            "abstract": bib.get("abstract"),
            "journal": bib.get("journal"),
            "volume": bib.get("volume"),
            "pages": bib.get("pages"),
            "link": pub.get("pub_url")
        }
        papers.append(paper)
    return papers
