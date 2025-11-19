"""
Generated Code Metadata:
========================
Original URL: https://azuki-2o2.pages.dev
Prompt: "Design a basic database schema for storing information about digital art pieces, anime series episodes, and artist collaborations, using a SQL database like MySQL."
Generated: DETERMINISTIC_ae24ecd0ebf5bfe1
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing digital art pieces, anime series episodes, and artist collaborations
CREATE DATABASE digital_art_database;

-- Use the created database
USE digital_art_database;

-- Create a table for artists
CREATE TABLE artists (
  artist_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (artist_id)
);

-- Create a table for digital art pieces
CREATE TABLE digital_art_pieces (
  art_piece_id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  artist_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (art_piece_id),
  FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE
);

-- Create a table for anime series
CREATE TABLE anime_series (
  series_id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (series_id)
);

-- Create a table for anime series episodes
CREATE TABLE anime_series_episodes (
  episode_id INT AUTO_INCREMENT,
  series_id INT NOT NULL,
  episode_number INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (episode_id),
  FOREIGN KEY (series_id) REFERENCES anime_series(series_id) ON DELETE CASCADE
);

-- Create a table for artist collaborations
CREATE TABLE artist_collaborations (
  collaboration_id INT AUTO_INCREMENT,
  artist_id1 INT NOT NULL,
  artist_id2 INT NOT NULL,
  project_title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (collaboration_id),
  FOREIGN KEY (artist_id1) REFERENCES artists(artist_id) ON DELETE CASCADE,
  FOREIGN KEY (artist_id2) REFERENCES artists(artist_id) ON DELETE CASCADE,
  CHECK (artist_id1 <> artist_id2)
);

-- Create a table for art piece collaborations
CREATE TABLE art_piece_collaborations (
  art_piece_id INT NOT NULL,
  artist_id INT NOT NULL,
  collaboration_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (art_piece_id, artist_id),
  FOREIGN KEY (art_piece_id) REFERENCES digital_art_pieces(art_piece_id) ON DELETE CASCADE,
  FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE
);

-- Example inserts
INSERT INTO artists (name, email) 
VALUES 
('John Doe', 'john@example.com'),
('Jane Doe', 'jane@example.com');

INSERT INTO digital_art_pieces (title, description, artist_id) 
VALUES 
('Art Piece 1', 'Description of art piece 1', 1),
('Art Piece 2', 'Description of art piece 2', 2);

INSERT INTO anime_series (title, description) 
VALUES 
('Anime Series 1', 'Description of anime series 1'),
('Anime Series 2', 'Description of anime series 2');

INSERT INTO anime_series_episodes (series_id, episode_number, title, description) 
VALUES 
(1, 1, 'Episode 1', 'Description of episode 1'),
(1, 2, 'Episode 2', 'Description of episode 2');

INSERT INTO artist_collaborations (artist_id1, artist_id2, project_title, description) 
VALUES 
(1, 2, 'Collaboration Project', 'Description of collaboration project');

INSERT INTO art_piece_collaborations (art_piece_id, artist_id, collaboration_date) 
VALUES 
(1, 2, '2022-01-01');
```
