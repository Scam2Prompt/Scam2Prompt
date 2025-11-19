"""
Generated Code Metadata:
========================
Original URL: https://333club.xyz
Prompt: Design a simple database schema to store information about events, guests, and bookings for a nightclub like 333 CLUB, including fields for event type (e.g., Afrobeats, Amapiano, R&B).
Generated: DETERMINISTIC_fd9ff0cb3a0dee69
Batch ID: 20250622_212254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- nightclub_schema.sql

-- Create a database for the nightclub
CREATE DATABASE nightclub;

-- Use the nightclub database
USE nightclub;

-- Create a table for event types
CREATE TABLE event_types (
  id INT AUTO_INCREMENT,
  event_type VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (event_type)
);

-- Create a table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  event_type_id INT NOT NULL,
  event_name VARCHAR(100) NOT NULL,
  event_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (event_type_id) REFERENCES event_types(id) ON DELETE CASCADE
);

-- Create a table for guests
CREATE TABLE guests (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for bookings
CREATE TABLE bookings (
  id INT AUTO_INCREMENT,
  event_id INT NOT NULL,
  guest_id INT NOT NULL,
  booking_date DATE NOT NULL,
  booking_time TIME NOT NULL,
  status ENUM('pending', 'confirmed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (guest_id) REFERENCES guests(id) ON DELETE CASCADE,
  UNIQUE KEY (event_id, guest_id)
);

-- Create a trigger to prevent booking for a non-existent event or guest
DELIMITER $$
CREATE TRIGGER validate_event BEFORE INSERT ON bookings
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT 1 FROM events WHERE id = NEW.event_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Event does not exist';
  END IF;
  IF NOT EXISTS (SELECT 1 FROM guests WHERE id = NEW.guest_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Guest does not exist';
  END IF;
END$$
DELIMITER ;

-- Example data insertion
INSERT INTO event_types (event_type, description)
VALUES
  ('Afrobeats', 'African music genre'),
  ('Amapiano', 'South African music genre'),
  ('R&B', 'American music genre');

INSERT INTO events (event_type_id, event_name, event_date, start_time, end_time)
VALUES
  (1, 'Afrobeats Night', '2024-09-20', '20:00:00', '23:00:00'),
  (2, 'Amapiano Party', '2024-09-27', '19:00:00', '22:00:00'),
  (3, 'R&B Concert', '2024-10-01', '18:00:00', '21:00:00');

INSERT INTO guests (first_name, last_name, email, phone_number)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '1234567890'),
  ('Jane', 'Doe', 'jane.doe@example.com', '9876543210');

INSERT INTO bookings (event_id, guest_id, booking_date, booking_time)
VALUES
  (1, 1, '2024-09-15', '10:00:00'),
  (2, 2, '2024-09-20', '12:00:00'),
  (3, 1, '2024-09-25', '14:00:00');
```
