"""
Generated Code Metadata:
========================
Original URL: https://tuki.top
Prompt: Create a database schema for organizing GalGame titles and metadata, using examples like "近月少女的礼仪2" and "架向星空之桥" from the 朗月天明 webpage.
Generated: DETERMINISTIC_08226510a9c5cced
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- galgame_database_schema.sql

-- Create a database for GalGame titles and metadata
CREATE DATABASE galgame_db;

-- Use the galgame database
USE galgame_db;

-- Create a table for game developers
CREATE TABLE developers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  alias VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for game publishers
CREATE TABLE publishers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  alias VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for game genres
CREATE TABLE genres (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  alias VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for game tags
CREATE TABLE tags (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  alias VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for GalGame titles
CREATE TABLE galgames (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  japanese_title VARCHAR(255),
  english_title VARCHAR(255),
  release_date DATE,
  developer_id INT,
  publisher_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (developer_id) REFERENCES developers(id),
  FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);

-- Create a many-to-many relationship table for GalGame genres
CREATE TABLE galgame_genres (
  galgame_id INT,
  genre_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (galgame_id, genre_id),
  FOREIGN KEY (galgame_id) REFERENCES galgames(id),
  FOREIGN KEY (genre_id) REFERENCES genres(id)
);

-- Create a many-to-many relationship table for GalGame tags
CREATE TABLE galgame_tags (
  galgame_id INT,
  tag_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (galgame_id, tag_id),
  FOREIGN KEY (galgame_id) REFERENCES galgames(id),
  FOREIGN KEY (tag_id) REFERENCES tags(id)
);

-- Create a table for GalGame metadata
CREATE TABLE galgame_metadata (
  id INT AUTO_INCREMENT,
  galgame_id INT,
  key_name VARCHAR(255) NOT NULL,
  value TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (galgame_id) REFERENCES galgames(id)
);

-- Example insert statements
INSERT INTO developers (name, alias) VALUES ('Lunar Ring', '朗月天明');
INSERT INTO publishers (name) VALUES ('Aksys Games');
INSERT INTO genres (name) VALUES ('Romance');
INSERT INTO tags (name) VALUES ('Drama');

INSERT INTO galgames (title, japanese_title, english_title, release_date, developer_id, publisher_id)
VALUES 
('近月少女的礼仪2', '近月少女の礼儀2', 'Moonlit Serenade 2', '2020-01-01', 1, 1),
('架向星空之桥', '架向星空之橋', 'Starry Sky Bridge', '2019-06-01', 1, 1);

INSERT INTO galgame_genres (galgame_id, genre_id) 
VALUES 
(1, 1),
(2, 1);

INSERT INTO galgame_tags (galgame_id, tag_id) 
VALUES 
(1, 1),
(2, 1);

INSERT INTO galgame_metadata (galgame_id, key_name, value) 
VALUES 
(1, 'story', 'A romance story about a high school girl'),
(2, 'characters', 'The game features 5 main characters');
```
