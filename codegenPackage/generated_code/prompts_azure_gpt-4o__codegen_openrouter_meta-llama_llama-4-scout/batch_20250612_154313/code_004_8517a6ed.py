"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: Create a database schema to store member profiles, event details, and subscription statuses for a social-first networking platform like Sync Connects.
Generated: DETERMINISTIC_8517a6eda86b8309
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Sync Connects
CREATE DATABASE sync_connects;

-- Use the database
USE sync_connects;

-- Create table for member profiles
CREATE TABLE members (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(100) NOT NULL,
  profile_picture_url VARCHAR(255) DEFAULT NULL,
  bio TEXT DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for event details
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  start_date DATETIME NOT NULL,
  end_date DATETIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for subscription statuses
CREATE TABLE subscriptions (
  id INT AUTO_INCREMENT,
  member_id INT NOT NULL,
  event_id INT NOT NULL,
  subscription_status ENUM('pending', 'attending', 'declined', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE,
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  UNIQUE KEY (member_id, event_id)
);

-- Create table for member connections
CREATE TABLE connections (
  id INT AUTO_INCREMENT,
  member_id INT NOT NULL,
  connected_member_id INT NOT NULL,
  status ENUM('pending', 'accepted', 'declined', 'blocked') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE,
  FOREIGN KEY (connected_member_id) REFERENCES members(id) ON DELETE CASCADE,
  UNIQUE KEY (member_id, connected_member_id)
);

-- Create indexes for efficient queries
CREATE INDEX idx_members_email ON members (email);
CREATE INDEX idx_events_start_date ON events (start_date);
CREATE INDEX idx_subscriptions_member_id ON subscriptions (member_id);
CREATE INDEX idx_subscriptions_event_id ON subscriptions (event_id);
CREATE INDEX idx_connections_member_id ON connections (member_id);
CREATE INDEX idx_connections_connected_member_id ON connections (connected_member_id);
```

```sql
-- stored_procedures.sql

DELIMITER //

CREATE PROCEDURE sp_add_member(
  IN p_email VARCHAR(255),
  IN p_password_hash VARCHAR(255),
  IN p_name VARCHAR(100)
)
BEGIN
  INSERT INTO members (email, password_hash, name)
  VALUES (p_email, p_password_hash, p_name);
END //

CREATE PROCEDURE sp_add_event(
  IN p_title VARCHAR(255),
  IN p_description TEXT,
  IN p_start_date DATETIME,
  IN p_end_date DATETIME,
  IN p_location VARCHAR(255)
)
BEGIN
  INSERT INTO events (title, description, start_date, end_date, location)
  VALUES (p_title, p_description, p_start_date, p_end_date, p_location);
END //

CREATE PROCEDURE sp_subscribe_to_event(
  IN p_member_id INT,
  IN p_event_id INT
)
BEGIN
  INSERT INTO subscriptions (member_id, event_id)
  VALUES (p_member_id, p_event_id);
END //

CREATE PROCEDURE sp_connect_members(
  IN p_member_id INT,
  IN p_connected_member_id INT
)
BEGIN
  INSERT INTO connections (member_id, connected_member_id)
  VALUES (p_member_id, p_connected_member_id);
END //

DELIMITER ;
```

```sql
-- example_usage.sql

-- Add a new member
CALL sp_add_member('john.doe@example.com', 'password_hash', 'John Doe');

-- Add a new event
CALL sp_add_event('Example Event', 'This is an example event', '2024-09-17 14:00:00', '2024-09-17 16:00:00', 'New York');

-- Subscribe to an event
CALL sp_subscribe_to_event(1, 1);

-- Connect two members
CALL sp_connect_members(1, 2);
```
