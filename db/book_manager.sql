DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  age INT,
  alive BOOLEAN
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  year INT,
  read BOOLEAN,
  description VARCHAR(255),
  author_id INT NOT NULL REFERENCES authors(id)
);
