CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    capacity INTEGER
);
