import sqlite3
import contextlib

class SQLiteResource:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def get_connection(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
        return self.conn
