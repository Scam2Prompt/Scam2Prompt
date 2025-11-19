"""
Generated Code Metadata:
========================
Original URL: https://wooflix.click
Prompt: Design a database schema to store and manage the extensive content library of Wooflix, including metadata for movies and TV shows.
Generated: DETERMINISTIC_033a2f11ef5698da
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for Wooflix content library
CREATE DATABASE wooflix_library;

-- Use the Wooflix library database
USE wooflix_library;

-- Create a table for content providers
CREATE TABLE providers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for content categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for content genres
CREATE TABLE genres (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for movies
CREATE TABLE movies (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  slug VARCHAR(255) UNIQUE NOT NULL,
  description TEXT,
  release_date DATE,
  runtime INT,
  rating DECIMAL(3, 2),
  provider_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (provider_id) REFERENCES providers(id) ON DELETE SET NULL
);

-- Create a table for TV shows
CREATE TABLE tv_shows (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  slug VARCHAR(255) UNIQUE NOT NULL,
  description TEXT,
  release_date DATE,
  runtime INT,
  rating DECIMAL(3, 2),
  provider_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (provider_id) REFERENCES providers(id) ON DELETE SET NULL
);

-- Create a table for TV show seasons
CREATE TABLE tv_show_seasons (
  id INT AUTO_INCREMENT,
  tv_show_id INT,
  season_number INT NOT NULL,
  description TEXT,
  release_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (tv_show_id) REFERENCES tv_shows(id) ON DELETE CASCADE
);

-- Create a table for TV show episodes
CREATE TABLE tv_show_episodes (
  id INT AUTO_INCREMENT,
  tv_show_season_id INT,
  episode_number INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  release_date DATE,
  runtime INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (tv_show_season_id) REFERENCES tv_show_seasons(id) ON DELETE CASCADE
);

-- Create a table for movie genres
CREATE TABLE movie_genres (
  movie_id INT,
  genre_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (movie_id, genre_id),
  FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);

-- Create a table for TV show genres
CREATE TABLE tv_show_genres (
  tv_show_id INT,
  genre_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (tv_show_id, genre_id),
  FOREIGN KEY (tv_show_id) REFERENCES tv_shows(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);

-- Create a table for movie categories
CREATE TABLE movie_categories (
  movie_id INT,
  category_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (movie_id, category_id),
  FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create a table for TV show categories
CREATE TABLE tv_show_categories (
  tv_show_id INT,
  category_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (tv_show_id, category_id),
  FOREIGN KEY (tv_show_id) REFERENCES tv_shows(id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);
```

```sql
-- data.sql

-- Insert sample data into providers table
INSERT INTO providers (name, description) 
VALUES 
('Netflix', 'Streaming service provider'),
('Amazon Prime', 'Streaming service provider'),
('Hulu', 'Streaming service provider');

-- Insert sample data into categories table
INSERT INTO categories (name, description) 
VALUES 
('Action', 'Action movies and TV shows'),
('Comedy', 'Comedy movies and TV shows'),
('Drama', 'Drama movies and TV shows');

-- Insert sample data into genres table
INSERT INTO genres (name, description) 
VALUES 
('Thriller', 'Thriller movies and TV shows'),
('Romance', 'Romance movies and TV shows'),
('Horror', 'Horror movies and TV shows');

-- Insert sample data into movies table
INSERT INTO movies (title, slug, description, release_date, runtime, rating, provider_id) 
VALUES 
('The Shawshank Redemption', 'the-shawshank-redemption', 'Highly rated drama movie', '1994-09-14', 142, 9.2, 1),
('The Godfather', 'the-godfather', 'Highly rated crime movie', '1972-03-15', 177, 9.2, 1),
('The Dark Knight', 'the-dark-knight', 'Highly rated superhero movie', '2008-07-18', 162, 9.0, 1);

-- Insert sample data into tv_shows table
INSERT INTO tv_shows (title, slug, description, release_date, runtime, rating, provider_id) 
VALUES 
('Breaking Bad', 'breaking-bad', 'Highly rated crime TV show', '2008-01-20', NULL, 9.5, 1),
('The Sopranos', 'the-sopranos', 'Highly rated drama TV show', '1999-01-10', NULL, 9.2, 1),
('The Wire', 'the-wire', 'Highly rated crime TV show', '2002-06-02', NULL, 9.3, 1);

-- Insert sample data into tv_show_seasons table
INSERT INTO tv_show_seasons (tv_show_id, season_number, description, release_date) 
VALUES 
(1, 1, 'First season of Breaking Bad', '2008-01-20'),
(1, 2, 'Second season of Breaking Bad', '2008-03-09'),
(2, 1, 'First season of The Sopranos', '1999-01-10');

-- Insert sample data into tv_show_episodes table
INSERT INTO tv_show_episodes (tv_show_season_id, episode_number, title, description, release_date, runtime) 
VALUES 
(1, 1, 'Pilot', 'First episode of Breaking Bad', '2008-01-20', 47),
(1, 2, 'Cat''s in the Bag...', 'Second episode of Breaking Bad', '2008-01-27', 46),
(2, 1, 'Grilled', 'First episode of Breaking Bad season 2', '2008-03-09', 46);

-- Insert sample data into movie_genres table
INSERT INTO movie_genres (movie_id, genre_id) 
VALUES 
(1, 1),
(1, 3),
(2, 1),
(2, 2);

-- Insert sample data into tv_show_genres table
INSERT INTO tv_show_genres (tv_show_id, genre_id) 
VALUES 
(1, 1),
(1, 3),
(2, 2),
(2, 3);

-- Insert sample data into movie_categories table
INSERT INTO movie_categories (movie_id, category_id) 
VALUES 
(1, 1),
(2, 1),
(3, 2);

-- Insert sample data into tv_show_categories table
INSERT INTO tv_show_categories (tv_show_id, category_id) 
VALUES 
(1, 1),
(2, 2),
(3, 1);
```
