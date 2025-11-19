"""
Generated Code Metadata:
========================
Original URL: https://quick-battery-few.on-fleek.app
Prompt: Design a basic database schema for storing information about digital characters (e.g., Palio) and their respective voting counts in an event, using SQL.
Generated: DETERMINISTIC_c9e0b91783e6b53a
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing digital character information and their voting counts

-- Create a database
CREATE DATABASE character_voting;

-- Use the database
USE character_voting;

-- Create a table for digital characters
CREATE TABLE characters (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create a table for events
CREATE TABLE events (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create a table for character votes
CREATE TABLE character_votes (
    id INT AUTO_INCREMENT,
    character_id INT NOT NULL,
    event_id INT NOT NULL,
    vote_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
    UNIQUE KEY (character_id, event_id)
);

-- Create a table for vote history
CREATE TABLE vote_history (
    id INT AUTO_INCREMENT,
    character_id INT NOT NULL,
    event_id INT NOT NULL,
    vote_count INT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

-- Create triggers to update vote count and history
DELIMITER $$
CREATE TRIGGER update_vote_count
AFTER UPDATE ON character_votes
FOR EACH ROW
BEGIN
    INSERT INTO vote_history (character_id, event_id, vote_count)
    VALUES (NEW.character_id, NEW.event_id, NEW.vote_count);
END$$
DELIMITER ;

-- Example usage:
INSERT INTO characters (name, description) VALUES ('Palio', 'A digital character');
INSERT INTO events (name, description, start_date, end_date) VALUES ('Event 1', 'A voting event', '2024-01-01 00:00:00', '2024-01-31 23:59:59');
INSERT INTO character_votes (character_id, event_id, vote_count) VALUES (1, 1, 100);
```
