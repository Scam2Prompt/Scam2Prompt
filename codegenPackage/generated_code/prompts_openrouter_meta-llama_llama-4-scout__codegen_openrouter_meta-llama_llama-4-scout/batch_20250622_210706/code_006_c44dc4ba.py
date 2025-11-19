"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Design a database schema for storing anime metadata, user information, and streaming history, suitable for a platform like HiAnime.
Generated: DETERMINISTIC_c44dc4ba2d573cc6
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- anime_database_schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS hi_anime;

-- Use database
USE hi_anime;

-- Create table for anime metadata
CREATE TABLE IF NOT EXISTS anime (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  alternative_title VARCHAR(255),
  synopsis TEXT,
  status ENUM('ongoing', 'completed', 'on-hiatus') NOT NULL DEFAULT 'ongoing',
  episodes INT,
  genres JSON,
  release_date DATE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user information
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  profile_picture_url VARCHAR(255),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for streaming history
CREATE TABLE IF NOT EXISTS streaming_history (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  anime_id INT NOT NULL,
  episode INT NOT NULL,
  watched_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (anime_id) REFERENCES anime(id) ON DELETE CASCADE
);

-- Create table for user ratings and reviews
CREATE TABLE IF NOT EXISTS user_reviews (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  anime_id INT NOT NULL,
  rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 10),
  review TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (anime_id) REFERENCES anime(id) ON DELETE CASCADE,
  UNIQUE (user_id, anime_id)
);

-- Create table for user watchlists
CREATE TABLE IF NOT EXISTS user_watchlists (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  anime_id INT NOT NULL,
  added_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (anime_id) REFERENCES anime(id) ON DELETE CASCADE,
  UNIQUE (user_id, anime_id)
);
```

```sql
-- Example inserts for testing
INSERT INTO anime (title, alternative_title, synopsis, status, episodes, genres, release_date)
VALUES 
('Attack on Titan', 'Shingeki no Kyojin', 'In a world where humans are on the brink of extinction', 'ongoing', 50, '[\"Action\", \"Drama\"]', '2013-04-07'),
('Fullmetal Alchemist: Brotherhood', 'Hai to Gensō no Grimgar', 'Two brothers on a quest to restore their bodies', 'completed', 64, '[\"Adventure\", \"Fantasy\"]', '2009-04-05');

INSERT INTO users (username, email, password_hash)
VALUES 
('john_doe', 'john@example.com', 'password_hash'),
('jane_doe', 'jane@example.com', 'password_hash');

INSERT INTO streaming_history (user_id, anime_id, episode)
VALUES 
(1, 1, 10),
(1, 2, 20),
(2, 1, 5);

INSERT INTO user_reviews (user_id, anime_id, rating, review)
VALUES 
(1, 1, 9, 'One of the best anime series I''ve ever seen'),
(2, 2, 8, 'Great story, but the pacing could be better');

INSERT INTO user_watchlists (user_id, anime_id)
VALUES 
(1, 3),
(2, 4);
```
