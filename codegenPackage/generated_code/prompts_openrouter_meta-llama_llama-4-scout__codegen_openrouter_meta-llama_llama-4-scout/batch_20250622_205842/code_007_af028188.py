"""
Generated Code Metadata:
========================
Original URL: https://online-game.online
Prompt: "Design a database schema for storing information about online games and their updates."
Generated: DETERMINISTIC_af02818873a77d47
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for online games
CREATE DATABASE online_games;

-- Use the online_games database
USE online_games;

-- Create a table for game developers
CREATE TABLE developers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for game genres
CREATE TABLE genres (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for online games
CREATE TABLE games (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  developer_id INT,
  genre_id INT,
  release_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (developer_id) REFERENCES developers(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);

-- Create a table for game updates
CREATE TABLE updates (
  id INT AUTO_INCREMENT,
  game_id INT,
  version VARCHAR(255) NOT NULL,
  patch_notes TEXT,
  release_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
);

-- Create a table for user reviews
CREATE TABLE reviews (
  id INT AUTO_INCREMENT,
  game_id INT,
  user_id INT,
  rating TINYINT,
  review TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
);

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create index on foreign key columns
CREATE INDEX idx_developer_id ON games (developer_id);
CREATE INDEX idx_genre_id ON games (genre_id);
CREATE INDEX idx_game_id ON updates (game_id);
CREATE INDEX idx_user_id ON reviews (user_id);
```

```sql
-- example_data.sql

-- Insert example data into the database
INSERT INTO developers (name, email)
VALUES
  ('Electronic Arts', 'info@ea.com'),
  ('Ubisoft', 'info@ubisoft.com'),
  ('Rockstar Games', 'info@rockstargames.com');

INSERT INTO genres (name, description)
VALUES
  ('Action', 'Fast-paced games that require quick reflexes'),
  ('Adventure', 'Games that typically involve exploration and puzzle-solving'),
  ('Role-Playing', 'Games that allow players to assume the role of a character');

INSERT INTO games (title, description, developer_id, genre_id, release_date)
VALUES
  ('FIFA 23', 'The latest installment in the FIFA series', 1, 1, '2022-10-01'),
  ('Assassin\'s Creed Odyssey', 'An open-world adventure game set in ancient Greece', 2, 2, '2018-10-05'),
  ('Grand Theft Auto V', 'An open-world action-adventure game set in Los Santos', 3, 1, '2013-09-17');

INSERT INTO updates (game_id, version, patch_notes, release_date)
VALUES
  (1, '1.1.0', 'Fixed several bugs and improved performance', '2022-11-01'),
  (2, '2.0.0', 'Added new characters and game modes', '2019-02-15'),
  (3, '1.5.0', 'Improved graphics and added new vehicles', '2015-03-20');

INSERT INTO users (username, email, password_hash)
VALUES
  ('johnDoe', 'john@example.com', 'password_hash'),
  ('janeDoe', 'jane@example.com', 'password_hash');

INSERT INTO reviews (game_id, user_id, rating, review)
VALUES
  (1, 1, 5, 'Great game!'),
  (2, 2, 4, 'Good game, but some bugs');
```
