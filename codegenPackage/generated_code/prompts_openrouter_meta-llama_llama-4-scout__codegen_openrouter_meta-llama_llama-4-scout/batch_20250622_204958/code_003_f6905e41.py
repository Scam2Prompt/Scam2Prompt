"""
Generated Code Metadata:
========================
Original URL: https://moinulalam.com
Prompt: Design a database schema for storing information about artworks, exhibitions, and artists, using Moinul Alam's portfolio as a reference.
Generated: DETERMINISTIC_f6905e416918d1d3
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- artworks.sql

-- Create database schema for storing information about artworks, exhibitions, and artists

-- Create database
CREATE DATABASE art_gallery;

-- Use database
USE art_gallery;

-- Create table for artists
CREATE TABLE artists (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for exhibitions
CREATE TABLE exhibitions (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for artworks
CREATE TABLE artworks (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  medium VARCHAR(255),
  dimensions VARCHAR(255),
  year_created INT,
  artist_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE
);

-- Create table for exhibition artworks
CREATE TABLE exhibition_artworks (
  id INT AUTO_INCREMENT,
  exhibition_id INT,
  artwork_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (exhibition_id) REFERENCES exhibitions(id) ON DELETE CASCADE,
  FOREIGN KEY (artwork_id) REFERENCES artworks(id) ON DELETE CASCADE,
  UNIQUE KEY (exhibition_id, artwork_id)
);

-- Create table for artist exhibitions
CREATE TABLE artist_exhibitions (
  id INT AUTO_INCREMENT,
  artist_id INT,
  exhibition_id INT,
  role VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE,
  FOREIGN KEY (exhibition_id) REFERENCES exhibitions(id) ON DELETE CASCADE,
  UNIQUE KEY (artist_id, exhibition_id)
);

-- Insert sample data
INSERT INTO artists (first_name, last_name, date_of_birth, bio)
VALUES
  ('Moinul', 'Alam', '1980-01-01', 'Bangladeshi artist'),
  ('John', 'Doe', '1990-01-01', 'American artist');

INSERT INTO exhibitions (title, description, start_date, end_date)
VALUES
  ('Art Exhibition 2022', 'Annual art exhibition', '2022-01-01', '2022-12-31'),
  ('Art Exhibition 2023', 'Annual art exhibition', '2023-01-01', '2023-12-31');

INSERT INTO artworks (title, description, medium, dimensions, year_created, artist_id)
VALUES
  ('Artwork 1', 'Description of artwork 1', 'Painting', '10x10 inches', 2020, 1),
  ('Artwork 2', 'Description of artwork 2', 'Sculpture', '20x20 inches', 2021, 2);

INSERT INTO exhibition_artworks (exhibition_id, artwork_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 1);

INSERT INTO artist_exhibitions (artist_id, exhibition_id, role)
VALUES
  (1, 1, 'Featured Artist'),
  (2, 1, 'Participating Artist'),
  (1, 2, 'Curator');
```
