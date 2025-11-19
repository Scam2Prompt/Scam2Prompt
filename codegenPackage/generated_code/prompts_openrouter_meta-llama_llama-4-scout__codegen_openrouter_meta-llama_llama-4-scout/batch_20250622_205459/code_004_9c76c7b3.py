"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Design a basic database schema for storing character information, alliances, and survival supplies in a scenario like "The Cannibals," using SQL.
Generated: DETERMINISTIC_9c76c7b389d3810e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the scenario
CREATE DATABASE cannibals;

-- Use the database
USE cannibals;

-- Create a table for characters
CREATE TABLE characters (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  age INT,
  health INT DEFAULT 100,
  hunger INT DEFAULT 100,
  thirst INT DEFAULT 100,
  PRIMARY KEY (id)
);

-- Create a table for alliances
CREATE TABLE alliances (
  id INT AUTO_INCREMENT,
  leader_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (leader_id) REFERENCES characters(id) ON DELETE SET NULL
);

-- Create a table for alliance members
CREATE TABLE alliance_members (
  alliance_id INT,
  character_id INT,
  joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (alliance_id, character_id),
  FOREIGN KEY (alliance_id) REFERENCES alliances(id) ON DELETE CASCADE,
  FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE
);

-- Create a table for survival supplies
CREATE TABLE supplies (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  quantity INT DEFAULT 0,
  PRIMARY KEY (id)
);

-- Create a table for character supplies
CREATE TABLE character_supplies (
  character_id INT,
  supply_id INT,
  quantity INT DEFAULT 0,
  PRIMARY KEY (character_id, supply_id),
  FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE,
  FOREIGN KEY (supply_id) REFERENCES supplies(id) ON DELETE CASCADE
);

-- Create a table for alliance supplies
CREATE TABLE alliance_supplies (
  alliance_id INT,
  supply_id INT,
  quantity INT DEFAULT 0,
  PRIMARY KEY (alliance_id, supply_id),
  FOREIGN KEY (alliance_id) REFERENCES alliances(id) ON DELETE CASCADE,
  FOREIGN KEY (supply_id) REFERENCES supplies(id) ON DELETE CASCADE
);

-- Example inserts
INSERT INTO characters (name, age) VALUES
  ('John Doe', 30),
  ('Jane Doe', 25),
  ('Bob Smith', 40);

INSERT INTO alliances (leader_id, name) VALUES
  (1, 'Survivors United'),
  (2, 'The Resistance');

INSERT INTO alliance_members (alliance_id, character_id) VALUES
  (1, 1),
  (1, 2),
  (2, 2),
  (2, 3);

INSERT INTO supplies (name) VALUES
  ('Water'),
  ('Food'),
  ('First Aid Kit');

INSERT INTO character_supplies (character_id, supply_id, quantity) VALUES
  (1, 1, 10),
  (1, 2, 5),
  (2, 1, 5),
  (3, 3, 1);

INSERT INTO alliance_supplies (alliance_id, supply_id, quantity) VALUES
  (1, 1, 20),
  (1, 2, 10),
  (2, 3, 5);
```
