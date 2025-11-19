"""
Generated Code Metadata:
========================
Original URL: https://spottersbrasil.com.br
Prompt: Design a database schema to store information about aviation events, teams, and photographers featured on Spotters Brasil, and provide SQL code to populate the database.
Generated: DETERMINISTIC_1aa351be6712f8ed
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema
CREATE DATABASE spotters_brasil;

-- Use database schema
USE spotters_brasil;

-- Create table for aviation events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  date DATE NOT NULL,
  location VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for teams
CREATE TABLE teams (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for photographers
CREATE TABLE photographers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  team_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE SET NULL
);

-- Create table for event photographers
CREATE TABLE event_photographers (
  event_id INT,
  photographer_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id, photographer_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (photographer_id) REFERENCES photographers(id) ON DELETE CASCADE
);

-- Create table for event teams
CREATE TABLE event_teams (
  event_id INT,
  team_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id, team_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE
);

-- Populate database with sample data
INSERT INTO events (name, date, location, description)
VALUES
  ('Meeting de Aviação', '2022-01-01', 'São Paulo', 'Encontro de aviação'),
  ('Festa de Aeronaves', '2022-06-01', 'Rio de Janeiro', 'Festa de aeronaves'),
  ('Exposição de Aviões', '2022-12-01', 'Brasília', 'Exposição de aviões');

INSERT INTO teams (name, description)
VALUES
  ('Team Spotters', 'Equipe de spotters'),
  ('Team Aviation', 'Equipe de aviação'),
  ('Team Aero', 'Equipe aero');

INSERT INTO photographers (name, email, team_id)
VALUES
  ('João Silva', 'joao.silva@example.com', 1),
  ('Maria Oliveira', 'maria.oliveira@example.com', 2),
  ('Pedro Santos', 'pedro.santos@example.com', 3);

INSERT INTO event_photographers (event_id, photographer_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 1);

INSERT INTO event_teams (event_id, team_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 1),
  (3, 2);
```
