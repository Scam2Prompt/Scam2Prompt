"""
Generated Code Metadata:
========================
Original URL: https://whitecasino.net
Prompt: Design a database schema to store information about various online casinos, their games, and user reviews, inspired by WhiteCasino.net's content and features.
Generated: DETERMINISTIC_bb7dc23d346ba6c7
Batch ID: 20250622_211753
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.white-casino.net/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.luckystreak.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.casino-royale.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for online casinos
CREATE DATABASE online_casinos;

-- Use the database
USE online_casinos;

-- Create a table for casinos
CREATE TABLE casinos (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  url VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name),
  UNIQUE KEY (url)
);

-- Create a table for games
CREATE TABLE games (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  type ENUM('slot', 'table', 'live') NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for casino games
CREATE TABLE casino_games (
  casino_id INT NOT NULL,
  game_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (casino_id, game_id),
  FOREIGN KEY (casino_id) REFERENCES casinos(id) ON DELETE CASCADE,
  FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
);

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (username),
  UNIQUE KEY (email)
);

-- Create a table for reviews
CREATE TABLE reviews (
  id INT AUTO_INCREMENT,
  casino_id INT NOT NULL,
  user_id INT NOT NULL,
  rating TINYINT NOT NULL,
  review TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (casino_id) REFERENCES casinos(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  CHECK (rating BETWEEN 1 AND 5)
);

-- Create a table for review likes
CREATE TABLE review_likes (
  review_id INT NOT NULL,
  user_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id, user_id),
  FOREIGN KEY (review_id) REFERENCES reviews(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_casino_name ON casinos (name);
CREATE INDEX idx_game_name ON games (name);
CREATE INDEX idx_casino_games_casino_id ON casino_games (casino_id);
CREATE INDEX idx_casino_games_game_id ON casino_games (game_id);
CREATE INDEX idx_reviews_casino_id ON reviews (casino_id);
CREATE INDEX idx_reviews_user_id ON reviews (user_id);
```

```sql
-- data.sql

-- Insert some sample data
INSERT INTO casinos (name, url, description)
VALUES
  ('White Casino', 'https://www.white-casino.net/', 'A popular online casino'),
  ('Casino Royale', 'https://www.casino-royale.com/', 'A casino with a wide range of games'),
  ('Lucky Streak', 'https://www.luckystreak.com/', 'A casino with a focus on slots');

INSERT INTO games (name, type, description)
VALUES
  ('Slot 1', 'slot', 'A popular slot game'),
  ('Blackjack', 'table', 'A classic table game'),
  ('Roulette', 'table', 'A classic table game'),
  ('Live Poker', 'live', 'A live dealer poker game');

INSERT INTO casino_games (casino_id, game_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 1),
  (2, 3),
  (3, 1),
  (3, 4);

INSERT INTO users (username, email, password_hash)
VALUES
  ('user1', 'user1@example.com', 'password_hash_1'),
  ('user2', 'user2@example.com', 'password_hash_2'),
  ('user3', 'user3@example.com', 'password_hash_3');

INSERT INTO reviews (casino_id, user_id, rating, review)
VALUES
  (1, 1, 5, 'Great casino with many games'),
  (2, 2, 4, 'Good casino, but slow payouts'),
  (3, 3, 5, 'Excellent casino with friendly support');

INSERT INTO review_likes (review_id, user_id)
VALUES
  (1, 2),
  (1, 3),
  (2, 1);
```
