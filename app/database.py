
import sqlite3


def get_connection(db_path="tasks.db"):
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def create_table(db_path="tasks.db"):
    connection = get_connection(db_path)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()
