"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Suggest a database schema to store information about wines, regions, tasting events, and seminar schedules for an event like FestiVin Caraquet.
Generated: DETERMINISTIC_b2bc163ebf1694ad
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for FestiVin Caraquet event
CREATE DATABASE festivin_caraquet;

-- Use the database
USE festivin_caraquet;

-- Create table for regions
CREATE TABLE regions (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for wines
CREATE TABLE wines (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  region_id INT,
  type ENUM('red', 'white', 'sparkling', 'rosé') NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (region_id) REFERENCES regions(id) ON DELETE SET NULL
);

-- Create table for tasting events
CREATE TABLE tasting_events (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for seminar schedules
CREATE TABLE seminar_schedules (
  id INT AUTO_INCREMENT,
  tasting_event_id INT,
  seminar_name VARCHAR(255) NOT NULL,
  date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (tasting_event_id) REFERENCES tasting_events(id) ON DELETE SET NULL
);

-- Create table for wine tastings
CREATE TABLE wine_tastings (
  id INT AUTO_INCREMENT,
  tasting_event_id INT,
  wine_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (tasting_event_id) REFERENCES tasting_events(id) ON DELETE SET NULL,
  FOREIGN KEY (wine_id) REFERENCES wines(id) ON DELETE SET NULL
);

-- Create table for seminar speakers
CREATE TABLE seminar_speakers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for seminar speaker assignments
CREATE TABLE seminar_speaker_assignments (
  id INT AUTO_INCREMENT,
  seminar_schedule_id INT,
  speaker_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (seminar_schedule_id) REFERENCES seminar_schedules(id) ON DELETE SET NULL,
  FOREIGN KEY (speaker_id) REFERENCES seminar_speakers(id) ON DELETE SET NULL
);
```
