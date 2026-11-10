import sqlite3


def get_user(db_path, user_id):
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM users WHERE id = ?", (user_id,))
        row = cur.fetchone()
        return row
    finally:
        conn.close()


def format_user(row):
    if row is None:
        return "user not found"
    return f"{row[0]}: {row[1]}"
