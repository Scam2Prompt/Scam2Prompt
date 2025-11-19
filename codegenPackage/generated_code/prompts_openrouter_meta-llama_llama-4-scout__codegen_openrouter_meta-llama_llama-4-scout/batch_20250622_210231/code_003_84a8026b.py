"""
Generated Code Metadata:
========================
Original URL: https://ballatorino.it
Prompt: Design a database schema to store information about dance events, including event name, dates, location, and activity types, inspired by the BallaTorino event structure.
Generated: DETERMINISTIC_84a8026bfbcd5c8b
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for dance events
CREATE DATABASE dance_events;

-- Use the dance_events database
USE dance_events;

-- Create a table for locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for activity types
CREATE TABLE activity_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  start_date DATETIME NOT NULL,
  end_date DATETIME,
  location_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE CASCADE
);

-- Create a many-to-many relationship table for events and activity types
CREATE TABLE event_activities (
  event_id INT NOT NULL,
  activity_type_id INT NOT NULL,
  PRIMARY KEY (event_id, activity_type_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (activity_type_id) REFERENCES activity_types(id) ON DELETE CASCADE
);

-- Create an index on the location_id column in the events table
CREATE INDEX idx_events_location_id ON events (location_id);

-- Create an index on the event_id and activity_type_id columns in the event_activities table
CREATE INDEX idx_event_activities_event_id ON event_activities (event_id);
CREATE INDEX idx_event_activities_activity_type_id ON event_activities (activity_type_id);

-- Example data insertion
INSERT INTO locations (name, address, city, country)
VALUES
  ('Torino Dance Studio', 'Via Torino 1', 'Torino', 'Italy'),
  ('Dance Hall', 'Via Milano 2', 'Milano', 'Italy');

INSERT INTO activity_types (name, description)
VALUES
  ('Ballet', 'Classical dance form'),
  ('Hip-Hop', 'Popular dance style');

INSERT INTO events (name, start_date, end_date, location_id)
VALUES
  ('BallaTorino', '2024-09-20 18:00:00', '2024-09-20 22:00:00', 1),
  ('Dance Festival', '2024-06-15 10:00:00', '2024-06-17 18:00:00', 2);

INSERT INTO event_activities (event_id, activity_type_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 1);
```
