import sqlite3

conn = sqlite3.connect("customers.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT NOT NULL,
    location TEXT NOT NULL
)
""")


customers_data = [
    (1, 'Sahil', 'Male', 'Mumbai'),
    (2, 'Tanvi', 'Female', 'Pune'),
    (3, 'Aniket', 'Male', 'Gurgaon'),
    (4, 'Tanuja', 'Female', 'Pune'),
    (5, 'Srija', 'Female', 'Hyderabad'),
    (6, 'Anurag', 'Male', 'Hyderabad'),
]

# cursor.execute("DELETE FROM customers")  
cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customers_data)

conn.commit()
conn.close()