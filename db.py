import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price float)")
        self.conn.commit()

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?,?,?,?)", (part, customer, retailer, price))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def search(self, parts="", customer="", retailer="", price=""):
        self.cur.execute("SELECT * FROM parts WHERE title=? OR author=? OR year=? OR isbn=?", (parts, customer, retailer, price))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET title=?, author=?, year=?, isbn=? WHERE id=?", (part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()