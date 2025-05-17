
/*
Führt den Inhalt der angegebeen SQL-Datei in PostgreSQL aus, da im Entry-Point des Containers
nur SQL Dateien in der 1.Ebene ausgeführt werden und alphabetisch sortiert. Deswegen die Namen 01... und 99... 

Führt erst das 01_create_schemas.sql danach das 99_import_all.sql Skript aus
*/
\i /docker-entrypoint-initdb.d/userschema/02_users_table.sql
\i /docker-entrypoint-initdb.d/userschema/03_users_seed.sql
\i /docker-entrypoint-initdb.d/productschema/02_products_table.sql
\i /docker-entrypoint-initdb.d/productschema/03_products_seed.sql
