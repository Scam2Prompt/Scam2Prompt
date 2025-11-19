"""
Generated Code Metadata:
========================
Original URL: https://venez888.vip
Prompt: Create a SQL query to manage a database of casino games, including slots and table games, as outlined in the venez888.vip content.
Generated: DETERMINISTIC_59eeddfae28041ec
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for casino games
CREATE DATABASE casino_games;

-- Use the casino games database
USE casino_games;

-- Create a table for game categories
CREATE TABLE game_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for slots games
CREATE TABLE slots_games (
  id INT AUTO_INCREMENT,
  game_category_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  volatility ENUM('low', 'medium', 'high') NOT NULL,
  rtp DECIMAL(5,2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (game_category_id) REFERENCES game_categories(id)
);

-- Create a table for table games
CREATE TABLE table_games (
  id INT AUTO_INCREMENT,
  game_category_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  min_bet DECIMAL(10,2) NOT NULL,
  max_bet DECIMAL(10,2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (game_category_id) REFERENCES game_categories(id)
);

-- Create a table for game providers
CREATE TABLE game_providers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for game versions
CREATE TABLE game_versions (
  id INT AUTO_INCREMENT,
  game_id INT,
  game_provider_id INT,
  version VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (game_id) REFERENCES slots_games(id) OR REFERENCES table_games(id),
  FOREIGN KEY (game_provider_id) REFERENCES game_providers(id)
);

-- Insert some sample data
INSERT INTO game_categories (name, description) 
VALUES 
('Slots', 'Slots games'),
('Table Games', 'Table games like Blackjack and Roulette');

INSERT INTO slots_games (game_category_id, name, description, volatility, rtp) 
VALUES 
(1, 'Starmania', 'A classic slots game', 'medium', 95.00),
(1, 'Book of Ra', 'An adventure slots game', 'high', 92.00);

INSERT INTO table_games (game_category_id, name, description, min_bet, max_bet) 
VALUES 
(2, 'Blackjack', 'A classic card game', 5.00, 1000.00),
(2, 'Roulette', 'A classic roulette game', 10.00, 5000.00);

INSERT INTO game_providers (name, description) 
VALUES 
('Playtech', 'A leading game provider'),
('Microgaming', 'A well-known game provider');

INSERT INTO game_versions (game_id, game_provider_id, version) 
VALUES 
(1, 1, '1.0'),
(2, 2, '2.0'),
(3, 1, '1.5'),
(4, 2, '3.0');
```
