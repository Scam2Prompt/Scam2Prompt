"""
Generated Code Metadata:
========================
Original URL: https://serverscoc.com
Prompt: Create a SQL database schema to store movie information from the site, including fields for title, release date, genre, and description, and populate it with sample data like "Karate Kid: Legends" and "Interstellar."
Generated: DETERMINISTIC_d29fdedd67d79a9e
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for movie information
CREATE DATABASE IF NOT EXISTS movie_database;

-- Use the movie database
USE movie_database;

-- Create a table for movie genres
CREATE TABLE IF NOT EXISTS genres (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for movies
CREATE TABLE IF NOT EXISTS movies (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  release_date DATE,
  genre_id INT,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE SET NULL
);

-- Insert sample genres
INSERT INTO genres (name)
VALUES
('Action'),
('Adventure'),
('Drama'),
('Science Fiction'),
('Family');

-- Insert sample movies
INSERT INTO movies (title, release_date, genre_id, description)
VALUES
('Karate Kid: Legends', '2010-06-11', 5, 'A remake of the classic film, a young boy learns karate to defend himself.'),
('Interstellar', '2014-11-07', 4, 'A team of astronauts travel through a wormhole in search of a new home for humanity.');

-- Add more sample data
INSERT INTO genres (name)
VALUES
('Comedy'),
('Romance'),
('Thriller');

INSERT INTO movies (title, release_date, genre_id, description)
VALUES
('The Shawshank Redemption', '1994-09-14', 3, 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
('The Dark Knight', '2008-07-18', 1, 'Batman, Gordon and Harvey Dent are forced to deal with the chaos unleashed by a terrorist mastermind known as The Joker.'),
('Inception', '2010-07-13', 4, 'A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.');

-- Create a view to easily retrieve movie information
CREATE VIEW movie_details AS
SELECT 
  m.id,
  m.title,
  m.release_date,
  g.name AS genre,
  m.description
FROM 
  movies m
  LEFT JOIN genres g ON m.genre_id = g.id;

-- Select all movie details
SELECT * FROM movie_details;
```
