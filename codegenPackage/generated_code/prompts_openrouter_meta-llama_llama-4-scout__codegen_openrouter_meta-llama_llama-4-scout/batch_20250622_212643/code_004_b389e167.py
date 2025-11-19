"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Design a database schema to store historical records of the Armourers & Brasiers' Company, including information about its members, events, and charitable activities.
Generated: DETERMINISTIC_b389e167935bc405
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Armourers & Brasiers' Company
CREATE DATABASE armourers_braziers;

-- Use the database
USE armourers_braziers;

-- Create table for members
CREATE TABLE members (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  date_of_birth DATE,
  date_of_joining DATE NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  event_name VARCHAR(255) NOT NULL,
  event_date DATE NOT NULL,
  event_type ENUM('charitable', 'social', 'meeting') NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for charitable activities
CREATE TABLE charitable_activities (
  id INT AUTO_INCREMENT,
  activity_name VARCHAR(255) NOT NULL,
  activity_date DATE NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for member events
CREATE TABLE member_events (
  member_id INT NOT NULL,
  event_id INT NOT NULL,
  attendance BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (member_id, event_id),
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE,
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

-- Create table for charitable donations
CREATE TABLE charitable_donations (
  id INT AUTO_INCREMENT,
  charitable_activity_id INT NOT NULL,
  member_id INT,
  donation_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (charitable_activity_id) REFERENCES charitable_activities(id) ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE SET NULL
);

-- Create table for event attendees
CREATE TABLE event_attendees (
  event_id INT NOT NULL,
  member_id INT NOT NULL,
  PRIMARY KEY (event_id, member_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_members_email ON members(email);
CREATE INDEX idx_events_event_date ON events(event_date);
CREATE INDEX idx_charitable_activities_activity_date ON charitable_activities(activity_date);
```

```sql
-- sample_data.sql

-- Insert sample data into members table
INSERT INTO members (first_name, last_name, email, date_of_birth, date_of_joining)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '1990-01-01', '2020-01-01'),
  ('Jane', 'Doe', 'jane.doe@example.com', '1995-01-01', '2020-06-01'),
  ('Bob', 'Smith', 'bob.smith@example.com', '1980-01-01', '2015-01-01');

-- Insert sample data into events table
INSERT INTO events (event_name, event_date, event_type, description)
VALUES
  ('Charity Run', '2022-06-01', 'charitable', 'Participated in a charity run to raise funds for a local cause'),
  ('Company Meeting', '2022-07-01', 'meeting', 'Attended a meeting to discuss company business'),
  ('Food Drive', '2022-08-01', 'charitable', 'Organized a food drive to collect donations for a local food bank');

-- Insert sample data into charitable activities table
INSERT INTO charitable_activities (activity_name, activity_date, description)
VALUES
  ('Donation to Local Food Bank', '2022-06-15', 'Donated funds to a local food bank'),
  ('Volunteer Day', '2022-09-01', 'Participated in a volunteer day to help a local charity');

-- Insert sample data into member events table
INSERT INTO member_events (member_id, event_id, attendance)
VALUES
  (1, 1, TRUE),
  (2, 1, TRUE),
  (3, 2, TRUE),
  (1, 3, TRUE);

-- Insert sample data into charitable donations table
INSERT INTO charitable_donations (charitable_activity_id, member_id, donation_date, amount)
VALUES
  (1, 1, '2022-06-15', 100.00),
  (1, 2, '2022-06-15', 50.00),
  (2, 3, '2022-09-01', 200.00);

-- Insert sample data into event attendees table
INSERT INTO event_attendees (event_id, member_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 1);
```
