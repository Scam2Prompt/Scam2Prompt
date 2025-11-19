"""
Generated Code Metadata:
========================
Original URL: https://conferencesglobal.org
Prompt: Design a database schema for storing conference-related data, including speaker profiles, abstract submissions, and attendee information, based on Conferences Global's conference organization structure.
Generated: DETERMINISTIC_caa2645a5e1d854e
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Conferences Global
CREATE DATABASE conferences_global;

-- Use Conferences Global database
USE conferences_global;

-- Create table for countries
CREATE TABLE countries (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  iso_code CHAR(2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (iso_code)
);

-- Create table for cities
CREATE TABLE cities (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  country_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (country_id) REFERENCES countries(id) ON DELETE CASCADE
);

-- Create table for venues
CREATE TABLE venues (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE
);

-- Create table for conferences
CREATE TABLE conferences (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  venue_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (venue_id) REFERENCES venues(id) ON DELETE CASCADE
);

-- Create table for speakers
CREATE TABLE speakers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for abstracts
CREATE TABLE abstracts (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  speaker_id INT NOT NULL,
  conference_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (speaker_id) REFERENCES speakers(id) ON DELETE CASCADE,
  FOREIGN KEY (conference_id) REFERENCES conferences(id) ON DELETE CASCADE
);

-- Create table for attendees
CREATE TABLE attendees (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  conference_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (conference_id) REFERENCES conferences(id) ON DELETE CASCADE
);

-- Create table for conference tracks
CREATE TABLE conference_tracks (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  conference_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (conference_id) REFERENCES conferences(id) ON DELETE CASCADE
);

-- Create table for abstract tracks
CREATE TABLE abstract_tracks (
  abstract_id INT NOT NULL,
  track_id INT NOT NULL,
  PRIMARY KEY (abstract_id, track_id),
  FOREIGN KEY (abstract_id) REFERENCES abstracts(id) ON DELETE CASCADE,
  FOREIGN KEY (track_id) REFERENCES conference_tracks(id) ON DELETE CASCADE
);

-- Create table for conference programs
CREATE TABLE conference_programs (
  id INT AUTO_INCREMENT,
  conference_id INT NOT NULL,
  abstract_id INT NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (conference_id) REFERENCES conferences(id) ON DELETE CASCADE,
  FOREIGN KEY (abstract_id) REFERENCES abstracts(id) ON DELETE CASCADE
);
```

```sql
-- data.sql

-- Insert sample data into countries table
INSERT INTO countries (name, iso_code)
VALUES 
('United States', 'US'),
('Canada', 'CA'),
('Mexico', 'MX');

-- Insert sample data into cities table
INSERT INTO cities (name, country_id)
VALUES 
('New York City', 1),
('Toronto', 2),
('Mexico City', 3);

-- Insert sample data into venues table
INSERT INTO venues (name, address, city_id)
VALUES 
('New York Convention Center', '10 Times Square', 1),
('Toronto Convention Center', '700 Bay Street', 2),
('Mexico City Convention Center', 'Av. Insurgentes Sur', 3);

-- Insert sample data into conferences table
INSERT INTO conferences (name, start_date, end_date, venue_id)
VALUES 
('Conferences Global 2024', '2024-06-01', '2024-06-03', 1),
('Conferences Global 2025', '2025-06-01', '2025-06-03', 2);

-- Insert sample data into speakers table
INSERT INTO speakers (first_name, last_name, email, bio)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'Software Engineer'),
('Jane', 'Doe', 'jane.doe@example.com', 'Data Scientist');

-- Insert sample data into abstracts table
INSERT INTO abstracts (title, description, speaker_id, conference_id)
VALUES 
('Abstract 1', 'This is abstract 1', 1, 1),
('Abstract 2', 'This is abstract 2', 2, 1);

-- Insert sample data into attendees table
INSERT INTO attendees (first_name, last_name, email, conference_id)
VALUES 
('Attendee1', 'Lastname1', 'attendee1@example.com', 1),
('Attendee2', 'Lastname2', 'attendee2@example.com', 1);

-- Insert sample data into conference tracks table
INSERT INTO conference_tracks (name, conference_id)
VALUES 
('Track 1', 1),
('Track 2', 1);

-- Insert sample data into abstract tracks table
INSERT INTO abstract_tracks (abstract_id, track_id)
VALUES 
(1, 1),
(2, 2);

-- Insert sample data into conference programs table
INSERT INTO conference_programs (conference_id, abstract_id, start_time, end_time)
VALUES 
(1, 1, '09:00:00', '10:00:00'),
(1, 2, '10:00:00', '11:00:00');
```
