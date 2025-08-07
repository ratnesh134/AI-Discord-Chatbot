import sqlite3
from config import DB_FILE

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tickets (
                    user_id TEXT PRIMARY KEY,
                    ticket_id INTEGER
                )''')
    conn.commit()
    conn.close()

def store_ticket(user_id, ticket_id):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("INSERT OR REPLACE INTO tickets (user_id, ticket_id) VALUES (?, ?)", (user_id, ticket_id))

def get_ticket(user_id):
    with sqlite3.connect(DB_FILE) as conn:
        row = conn.execute("SELECT ticket_id FROM tickets WHERE user_id=?", (user_id,)).fetchone()
        return row[0] if row else None

def delete_ticket(user_id):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("DELETE FROM tickets WHERE user_id=?", (user_id,))
