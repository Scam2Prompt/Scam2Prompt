"""
Generated Code Metadata:
========================
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Create a SQL database schema to store information about comic books, including titles, volumes, and collector's editions, similar to the "Top G" series by DNG Comics.
Generated: DETERMINISTIC_644121b295922f9c
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- comic_book_schema.sql

-- Create a database for comic book information
CREATE DATABASE comic_book_database;

-- Use the comic book database
USE comic_book_database;

-- Create a table for publishers
CREATE TABLE publishers (
  publisher_id INT AUTO_INCREMENT,
  publisher_name VARCHAR(255) NOT NULL,
  publisher_description TEXT,
  PRIMARY KEY (publisher_id)
);

-- Create a table for comic book series
CREATE TABLE series (
  series_id INT AUTO_INCREMENT,
  series_title VARCHAR(255) NOT NULL,
  publisher_id INT,
  series_description TEXT,
  PRIMARY KEY (series_id),
  FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
);

-- Create a table for volumes
CREATE TABLE volumes (
  volume_id INT AUTO_INCREMENT,
  series_id INT,
  volume_number INT NOT NULL,
  volume_title VARCHAR(255),
  release_date DATE,
  PRIMARY KEY (volume_id),
  FOREIGN KEY (series_id) REFERENCES series(series_id)
);

-- Create a table for comic book issues
CREATE TABLE issues (
  issue_id INT AUTO_INCREMENT,
  volume_id INT,
  issue_number INT NOT NULL,
  issue_title VARCHAR(255),
  release_date DATE,
  PRIMARY KEY (issue_id),
  FOREIGN KEY (volume_id) REFERENCES volumes(volume_id)
);

-- Create a table for collector's editions
CREATE TABLE collectors_editions (
  collectors_edition_id INT AUTO_INCREMENT,
  volume_id INT,
  edition_title VARCHAR(255) NOT NULL,
  release_date DATE,
  edition_description TEXT,
  PRIMARY KEY (collectors_edition_id),
  FOREIGN KEY (volume_id) REFERENCES volumes(volume_id)
);

-- Create a table for comic book characters
CREATE TABLE characters (
  character_id INT AUTO_INCREMENT,
  character_name VARCHAR(255) NOT NULL,
  character_description TEXT,
  PRIMARY KEY (character_id)
);

-- Create a many-to-many relationship table for series and characters
CREATE TABLE series_characters (
  series_id INT,
  character_id INT,
  PRIMARY KEY (series_id, character_id),
  FOREIGN KEY (series_id) REFERENCES series(series_id),
  FOREIGN KEY (character_id) REFERENCES characters(character_id)
);

-- Create a table for comic book creators
CREATE TABLE creators (
  creator_id INT AUTO_INCREMENT,
  creator_name VARCHAR(255) NOT NULL,
  creator_role VARCHAR(255) NOT NULL,
  PRIMARY KEY (creator_id)
);

-- Create a many-to-many relationship table for issues and creators
CREATE TABLE issue_creators (
  issue_id INT,
  creator_id INT,
  PRIMARY KEY (issue_id, creator_id),
  FOREIGN KEY (issue_id) REFERENCES issues(issue_id),
  FOREIGN KEY (creator_id) REFERENCES creators(creator_id)
);

-- Example data insertion
INSERT INTO publishers (publisher_name) VALUES ('DNG Comics');
INSERT INTO series (series_title, publisher_id) VALUES ('Top G', 1);
INSERT INTO volumes (series_id, volume_number, volume_title) VALUES (1, 1, 'Volume 1');
INSERT INTO issues (volume_id, issue_number, issue_title) VALUES (1, 1, 'Issue 1');
INSERT INTO collectors_editions (volume_id, edition_title) VALUES (1, 'Collector\'s Edition');
INSERT INTO characters (character_name) VALUES ('Character 1');
INSERT INTO series_characters (series_id, character_id) VALUES (1, 1);
INSERT INTO creators (creator_name, creator_role) VALUES ('Creator 1', 'Writer');
INSERT INTO issue_creators (issue_id, creator_id) VALUES (1, 1);
```
