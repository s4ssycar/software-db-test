import psycopg2

conn = psycopg2.connect(
    dbname="projekt_db",
    user="user",
    password="password",
    host="localhost",
    port=5433
)

cursor = conn.cursor()

# Beispielabfrage auf beide Schemas
cursor.execute("SELECT * FROM userschema.users;")
users = cursor.fetchall()
print("Users:", users)

cursor.execute("SELECT * FROM productschema.products;")
products = cursor.fetchall()
print("Products:", products)

cursor.close()
conn.close()
