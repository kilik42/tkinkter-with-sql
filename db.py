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
        self.cur.execute("SELECT * FROM parts WHERE part=?, customer = ?, retailer =?, price=?", (parts, customer, retailer, price))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part=?, customer = ?, retailer =?, price=? WHERE id=?", (part, customer, retailer, price, id))
        self.conn.commit()

    #destructor method to close the connection
    def __del__(self):
        self.conn.close()

# db = Database('store.db')
# db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", 160)
# db.insert("Asus Mobo", "Mike Henry", "Microcenter", 360)
# db.insert("500w PSU", "Karen Johnson", "Newegg", 80)
# db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", 70)
# db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", 180)
# db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", 679)
# db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", 130)
# db.insert("Asus Mobo", "John Doe", "Microcenter", 360)