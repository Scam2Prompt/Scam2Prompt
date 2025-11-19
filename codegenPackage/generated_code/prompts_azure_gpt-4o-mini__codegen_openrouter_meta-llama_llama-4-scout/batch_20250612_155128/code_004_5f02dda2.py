"""
Generated Code Metadata:
========================
Original URL: https://ogma.ca
Prompt: Construct a database schema for managing OGMA members, including fields for membership status, awards received, and participation in events like the Fishing Derby.
Generated: DETERMINISTIC_5f02dda274bf77d6
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for managing OGMA members
CREATE DATABASE ogma_members;

-- Use the ogma_members database
USE ogma_members;

-- Create a table for membership status
CREATE TABLE membership_status (
  status_id INT AUTO_INCREMENT,
  status_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (status_id)
);

-- Create a table for OGMA members
CREATE TABLE members (
  member_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  membership_status_id INT,
  join_date DATE,
  PRIMARY KEY (member_id),
  FOREIGN KEY (membership_status_id) REFERENCES membership_status(status_id)
);

-- Create a table for awards
CREATE TABLE awards (
  award_id INT AUTO_INCREMENT,
  award_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (award_id)
);

-- Create a table for member awards
CREATE TABLE member_awards (
  member_id INT,
  award_id INT,
  award_date DATE,
  PRIMARY KEY (member_id, award_id),
  FOREIGN KEY (member_id) REFERENCES members(member_id),
  FOREIGN KEY (award_id) REFERENCES awards(award_id)
);

-- Create a table for events
CREATE TABLE events (
  event_id INT AUTO_INCREMENT,
  event_name VARCHAR(255) NOT NULL,
  event_date DATE,
  description TEXT,
  PRIMARY KEY (event_id)
);

-- Create a table for event participation
CREATE TABLE event_participation (
  member_id INT,
  event_id INT,
  participation_date DATE,
  PRIMARY KEY (member_id, event_id),
  FOREIGN KEY (member_id) REFERENCES members(member_id),
  FOREIGN KEY (event_id) REFERENCES events(event_id)
);

-- Create a table for the Fishing Derby event
CREATE TABLE fishing_derby (
  event_id INT,
  catch_weight DECIMAL(10, 2),
  ranking INT,
  PRIMARY KEY (event_id),
  FOREIGN KEY (event_id) REFERENCES events(event_id)
);

-- Insert initial membership statuses
INSERT INTO membership_status (status_name, description)
VALUES
  ('Active', 'Member is currently active'),
  ('Inactive', 'Member is currently inactive'),
  ('Pending', 'Member application is pending');

-- Example usage:
-- INSERT INTO members (first_name, last_name, email, membership_status_id, join_date)
-- VALUES ('John', 'Doe', 'john.doe@example.com', 1, '2022-01-01');

-- INSERT INTO awards (award_name, description)
-- VALUES ('Best Catch', 'Award for the best catch in the Fishing Derby');

-- INSERT INTO member_awards (member_id, award_id, award_date)
-- VALUES (1, 1, '2022-06-01');

-- INSERT INTO events (event_name, event_date, description)
-- VALUES ('Fishing Derby 2022', '2022-06-01', 'Annual fishing derby event');

-- INSERT INTO event_participation (member_id, event_id, participation_date)
-- VALUES (1, 1, '2022-06-01');
```
