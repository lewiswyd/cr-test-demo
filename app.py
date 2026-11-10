import sqlite3


def get_user(db_path, user_id):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = "SELECT id, name FROM users WHERE id = " + str(user_id)
    cur.execute(query)
    row = cur.fetchone()
    return row


def format_user(db_path, user_id):
    row = get_user(db_path, user_id)
    return f"{row[0]}: {row[1]}"


def list_users(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return users
