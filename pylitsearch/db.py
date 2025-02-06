import sqlite3
from datetime import datetime

DB_FILE = "papers.db"  # 必要に応じてパスを変更してください

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            authors TEXT,
            year TEXT,
            publisher TEXT,
            abstract TEXT,
            journal TEXT,
            volume TEXT,
            pages TEXT,
            link TEXT,
            search_query TEXT,
            date_added TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_paper(paper, search_query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO papers (title, authors, year, publisher, abstract, journal, volume, pages, link, search_query, date_added)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        paper.get("title"),
        paper.get("authors"),
        paper.get("year"),
        paper.get("publisher"),
        paper.get("abstract"),
        paper.get("journal"),
        paper.get("volume"),
        paper.get("pages"),
        paper.get("link"),
        search_query,
        datetime.now().isoformat()
    ))
    conn.commit()
    conn.close()

def get_all_papers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM papers")
    rows = cur.fetchall()
    conn.close()
    return rows
