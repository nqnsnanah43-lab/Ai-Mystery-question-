import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).parent / "instance" / "mystery_quest.db"

def connect():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS game_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player TEXT NOT NULL,
                score INTEGER NOT NULL,
                theory TEXT,
                completed_at TEXT NOT NULL
            )
        """)

def save_game(player, score, theory):
    with connect() as conn:
        conn.execute(
            "INSERT INTO game_history (player, score, theory, completed_at) VALUES (?, ?, ?, ?)",
            (player, score, theory, __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M"))
        )

def get_history():
    with connect() as conn:
        return conn.execute("SELECT * FROM game_history ORDER BY id DESC LIMIT 50").fetchall()
