"""
Generated Code Metadata:
========================
Original URL: https://usdevent.com
Prompt: "Create a simple event management system database schema using MySQL."
Generated: DETERMINISTIC_54195a7ac30091d6
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- event_management_system.sql

-- Create database
CREATE DATABASE IF NOT EXISTS event_management_system;

-- Use database
USE event_management_system;

-- Create tables
CREATE TABLE IF NOT EXISTS events (
  `id` INT AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `start_date` DATETIME NOT NULL,
  `end_date` DATETIME NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS event_types (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS events_event_types (
  `event_id` INT NOT NULL,
  `event_type_id` INT NOT NULL,
  PRIMARY KEY (`event_id`, `event_type_id`),
  FOREIGN KEY (`event_id`) REFERENCES events (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`event_type_id`) REFERENCES event_types (`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS attendees (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS event_attendees (
  `event_id` INT NOT NULL,
  `attendee_id` INT NOT NULL,
  PRIMARY KEY (`event_id`, `attendee_id`),
  FOREIGN KEY (`event_id`) REFERENCES events (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`attendee_id`) REFERENCES attendees (`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tickets (
  `id` INT AUTO_INCREMENT,
  `event_id` INT NOT NULL,
  `attendee_id` INT,
  `ticket_type` ENUM('free', 'paid') NOT NULL DEFAULT 'free',
  `price` DECIMAL(10, 2),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`event_id`) REFERENCES events (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`attendee_id`) REFERENCES attendees (`id`) ON DELETE SET NULL
);

-- Insert sample data
INSERT INTO event_types (name, description) 
VALUES 
('Conference', 'A conference for developers'),
('Workshop', 'A workshop for learning new skills'),
('Seminar', 'A seminar for networking');

INSERT INTO events (title, description, start_date, end_date, location) 
VALUES 
('DevConf', 'A conference for developers', '2024-09-17 09:00:00', '2024-09-18 18:00:00', 'New York'),
('SkillUp Workshop', 'A workshop for learning new skills', '2024-10-01 09:00:00', '2024-10-02 18:00:00', 'San Francisco');

INSERT INTO events_event_types (event_id, event_type_id) 
VALUES 
(1, 1),
(2, 2);

INSERT INTO attendees (first_name, last_name, email, phone_number) 
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210');

INSERT INTO event_attendees (event_id, attendee_id) 
VALUES 
(1, 1),
(1, 2),
(2, 1);

INSERT INTO tickets (event_id, attendee_id, ticket_type, price) 
VALUES 
(1, 1, 'paid', 100.00),
(1, 2, 'free', NULL),
(2, 1, 'paid', 200.00);
```
