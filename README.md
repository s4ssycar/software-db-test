# DB-Test

Dieses Repository enthält ein einfaches Testprojekt zur Verbindung und Abfrage einer Datenbank.  
Ziel ist es, grundlegende Funktionen wie:

- das Herstellen einer Verbindung  
- das Ausführen von SQL-Befehlen  
- und das Verarbeiten von Ergebnissen  

zu testen.

------------------------------------------------------------

# VORAUSSETZUNG

Entweder Docker unter Linux installieren oder ein Windows-Subsystem für Linux (WSL) – Version 2 verwenden!

WSL2 prüfen und aktivieren

1. PowerShell öffnen und folgenden Befehl ausführen:

    wsl --list --verbose

Beispielausgabe:

    NAME      STATE           VERSION
    * Ubuntu    Running         2

Wenn bei VERSION die Zahl 1 steht, muss WSL2 aktiviert werden:

    wsl --install
    wsl --set-version Ubuntu 2

------------------------------------------------------------

# Docker Desktop einrichten (windows)

Alternativ reicht auch die normale Docker Version.

1. Gehe zu: https://www.docker.com/products/docker-desktop
2. Lade Docker Desktop herunter und installiere es.
3. Während der Installation unbedingt aktivieren:
   - WSL2 Integration
   - Deine Ubuntu-Distribution auswählen
4. Nach der Installation:
   - Docker Desktop starten
   - Warten, bis „Docker is running“ erscheint (unten in der App)
5. In der Ubuntu-Konsole prüfen:
   - docker --version  
   - docker run hello-world

------------------------------------------------------------

# Projekt einrichten

1. Repository klonen:

    git clone https://github.com/s4ssycar/software-db-test
    cd <REPOSITORY-ORDNER>

3. Ordner in Visual Studio Code öffnen
4. Abhängigkeit im Terminal installieren:

    pip install psycopg2 <-- ist für die Connection der PostgreSQL Datenbank nötig (mit Python)

5. In das Verzeichnis des Repositorys über die Linux Bash (WSL) öffnen und den Command: docker compose up --build ausführen

------------------------------------------------------------

# SQL-Code ändern

Wenn Änderungen am SQL-Code vorgenommen wurden, den Docker-Container neu starten:

    docker-compose down -v
    docker compose up --build

Falls neue Schemas hinzugefügt wurden:

- In 01_create_schemas.sql ergänzen
- Neue SQL-Dateien in 99_import_all.sql einbinden

------------------------------------------------------------

# Änderungen committen und pushen

    git add .
    git commit -m "Deine Nachricht"
    git push

------------------------------------------------------------

