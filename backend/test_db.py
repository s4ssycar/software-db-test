# psycopg2 ist das Standard-Modul zur Verbindung mit PostgreSQL in Python
import psycopg2

# Verbindung zur PostgreSQL-Datenbank aufbauen
# Die Datenbank läuft im Docker-Container auf localhost:5433
conn = psycopg2.connect(
    dbname="projekt_db",     # Name der Datenbank
    user="user",             # Benutzername
    password="password",     # Passwort
    host="localhost",        # Adresse des Datenbankservers (Docker veröffentlicht auf localhost)
    port=5433                # Port, über den PostgreSQL erreichbar ist (gemappt über Docker)
)

# Ein Cursor ist notwendig, um SQL-Befehle auszuführen
cursor = conn.cursor()

# Abfrage aller Datensätze aus der Tabelle users im Schema userschema
cursor.execute("SELECT * FROM userschema.users;")
users = cursor.fetchall()  # Ergebnisse der Abfrage abrufen
print("Users:", users)     # Ausgabe der Benutzerdaten

# Abfrage aller Datensätze aus der Tabelle products im Schema productschema
cursor.execute("SELECT * FROM productschema.products;")
products = cursor.fetchall()  # Ergebnisse der Abfrage abrufen
print("Products:", products)  # Ausgabe der Produktdaten

# Cursor schließen (Verbindung zur DB bleibt offen)
cursor.close()

# Datenbankverbindung schließen
conn.close()
