"""
Generated Code Metadata:
========================
Original URL: https://kurorobeastxyz.pages.dev
Prompt: Design a database schema to store information about Kuroro Beasts, including their elemental powers, levels, and ownership details.
Generated: DETERMINISTIC_47b768793f5d478a
Batch ID: 20250622_204851
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- kuroro_beasts_schema.sql

-- Create a database for Kuroro Beasts
CREATE DATABASE kuroro_beasts;

-- Use the kuroro_beasts database
USE kuroro_beasts;

-- Create a table for elements
CREATE TABLE elements (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for Kuroro Beasts
CREATE TABLE kuroro_beasts (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  level INT NOT NULL DEFAULT 1,
  element_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (element_id) REFERENCES elements(id) ON DELETE SET NULL
);

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (username),
  UNIQUE KEY (email)
);

-- Create a table for ownership details
CREATE TABLE ownerships (
  id INT AUTO_INCREMENT,
  user_id INT,
  kuroro_beast_id INT,
  acquired_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (kuroro_beast_id) REFERENCES kuroro_beasts(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, kuroro_beast_id)
);

-- Create a table for kuroro beast powers
CREATE TABLE kuroro_beast_powers (
  id INT AUTO_INCREMENT,
  kuroro_beast_id INT,
  power_name VARCHAR(255) NOT NULL,
  power_description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (kuroro_beast_id) REFERENCES kuroro_beasts(id) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO elements (name, description) 
VALUES 
('Fire', 'Deals fire damage'),
('Water', 'Deals water damage'),
('Earth', 'Deals earth damage');

INSERT INTO kuroro_beasts (name, level, element_id) 
VALUES 
('Kuroro', 10, 1),
('Chrollo', 15, 2),
('Shalnark', 8, 3);

INSERT INTO users (username, email, password_hash) 
VALUES 
('user1', 'user1@example.com', 'password_hash'),
('user2', 'user2@example.com', 'password_hash');

INSERT INTO ownerships (user_id, kuroro_beast_id) 
VALUES 
(1, 1),
(2, 2);

INSERT INTO kuroro_beast_powers (kuroro_beast_id, power_name, power_description) 
VALUES 
(1, 'Fireball', 'Deals massive fire damage'),
(2, 'Healing Wave', 'Heals allies');
```
