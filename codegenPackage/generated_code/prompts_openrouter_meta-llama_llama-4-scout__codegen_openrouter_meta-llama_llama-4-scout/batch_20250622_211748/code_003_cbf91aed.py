"""
Generated Code Metadata:
========================
Original URL: https://www.atletismomg.org.br
Prompt: Develop a simple database schema to store information about athletic clubs, teams, and athletes, inspired by the structures used on the FMA website.
Generated: DETERMINISTIC_cbf91aed6cbd9db5
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- athletic_club_schema.sql

-- Create a database for athletic clubs
CREATE DATABASE athletic_club_db;

-- Use the athletic club database
USE athletic_club_db;

-- Create a table for athletic clubs
CREATE TABLE athletic_clubs (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  phone_number VARCHAR(20),
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for teams
CREATE TABLE teams (
  id INT AUTO_INCREMENT,
  athletic_club_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (athletic_club_id) REFERENCES athletic_clubs(id) ON DELETE CASCADE
);

-- Create a table for athletes
CREATE TABLE athletes (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  date_of_birth DATE,
  email VARCHAR(100) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  country VARCHAR(100),
  zip_code VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for teams and athletes
CREATE TABLE team_athletes (
  team_id INT NOT NULL,
  athlete_id INT NOT NULL,
  jersey_number INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (team_id, athlete_id),
  FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE,
  FOREIGN KEY (athlete_id) REFERENCES athletes(id) ON DELETE CASCADE
);

-- Create a table for coaches
CREATE TABLE coaches (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for teams and coaches
CREATE TABLE team_coaches (
  team_id INT NOT NULL,
  coach_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (team_id, coach_id),
  FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE,
  FOREIGN KEY (coach_id) REFERENCES coaches(id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO athletic_clubs (name, address, city, state, country, zip_code, phone_number, email)
VALUES 
('Club A', '123 Main St', 'Anytown', 'CA', 'USA', '12345', '555-555-5555', 'info@cluba.com'),
('Club B', '456 Elm St', 'Othertown', 'NY', 'USA', '67890', '555-123-4567', 'info@clubb.com');

INSERT INTO teams (athletic_club_id, name, description)
VALUES 
(1, 'Team A1', 'This is team A1'),
(1, 'Team A2', 'This is team A2'),
(2, 'Team B1', 'This is team B1');

INSERT INTO athletes (first_name, last_name, date_of_birth, email, phone_number)
VALUES 
('John', 'Doe', '1990-01-01', 'john.doe@example.com', '555-111-1111'),
('Jane', 'Doe', '1995-06-01', 'jane.doe@example.com', '555-222-2222'),
('Bob', 'Smith', '1980-03-01', 'bob.smith@example.com', '555-333-3333');

INSERT INTO team_athletes (team_id, athlete_id, jersey_number)
VALUES 
(1, 1, 10),
(1, 2, 20),
(2, 3, 30);

INSERT INTO coaches (first_name, last_name, email, phone_number)
VALUES 
('Mike', 'Johnson', 'mike.johnson@example.com', '555-444-4444'),
('Emily', 'Williams', 'emily.williams@example.com', '555-555-5555');

INSERT INTO team_coaches (team_id, coach_id)
VALUES 
(1, 1),
(2, 2);
```
