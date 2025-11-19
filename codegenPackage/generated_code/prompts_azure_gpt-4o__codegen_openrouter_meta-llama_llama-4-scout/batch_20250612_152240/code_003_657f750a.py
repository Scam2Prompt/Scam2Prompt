"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Create a database schema for managing RM's projects, including tables for tracking beneficiaries, volunteers, donations, and event schedules.
Generated: DETERMINISTIC_657f750a50ed29cc
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for RM's projects
CREATE DATABASE rm_projects;

-- Use the database
USE rm_projects;

-- Create table for beneficiaries
CREATE TABLE beneficiaries (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for volunteers
CREATE TABLE volunteers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  skills VARCHAR(255),
  availability VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for donations
CREATE TABLE donations (
  id INT AUTO_INCREMENT,
  beneficiary_id INT,
  donor_name VARCHAR(255) NOT NULL,
  donation_amount DECIMAL(10, 2) NOT NULL,
  donation_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE SET NULL
);

-- Create table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  event_name VARCHAR(255) NOT NULL,
  event_date DATE NOT NULL,
  event_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  description VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for event schedules
CREATE TABLE event_schedules (
  id INT AUTO_INCREMENT,
  event_id INT,
  volunteer_id INT,
  schedule_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE SET NULL,
  FOREIGN KEY (volunteer_id) REFERENCES volunteers(id) ON DELETE SET NULL
);

-- Create table for volunteer assignments
CREATE TABLE volunteer_assignments (
  id INT AUTO_INCREMENT,
  event_id INT,
  volunteer_id INT,
  assigned_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE SET NULL,
  FOREIGN KEY (volunteer_id) REFERENCES volunteers(id) ON DELETE SET NULL
);

-- Create indexes for foreign keys
CREATE INDEX idx_beneficiaries_id ON donations (beneficiary_id);
CREATE INDEX idx_events_id ON event_schedules (event_id);
CREATE INDEX idx_volunteers_id ON event_schedules (volunteer_id);
CREATE INDEX idx_events_id ON volunteer_assignments (event_id);
CREATE INDEX idx_volunteers_id ON volunteer_assignments (volunteer_id);
```

```sql
-- sample_data.sql

-- Insert sample data into beneficiaries table
INSERT INTO beneficiaries (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into volunteers table
INSERT INTO volunteers (first_name, last_name, email, phone_number, address, skills, availability)
VALUES 
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567', '789 Oak St', 'Marketing, Event Planning', 'Monday - Friday'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-901-2345', '321 Maple St', 'Catering, Photography', 'Weekends');

-- Insert sample data into donations table
INSERT INTO donations (beneficiary_id, donor_name, donation_amount, donation_date)
VALUES 
(1, 'Anonymous', 100.00, '2022-01-01'),
(2, 'RM Foundation', 500.00, '2022-02-01');

-- Insert sample data into events table
INSERT INTO events (event_name, event_date, event_time, location, description)
VALUES 
('Charity Run', '2022-03-01', '09:00:00', 'City Park', 'A 5K run to raise funds for beneficiaries'),
('Food Drive', '2022-04-01', '10:00:00', 'Community Center', 'A food drive to collect donations for beneficiaries');

-- Insert sample data into event_schedules table
INSERT INTO event_schedules (event_id, volunteer_id, schedule_date, start_time, end_time)
VALUES 
(1, 1, '2022-03-01', '08:00:00', '12:00:00'),
(2, 2, '2022-04-01', '09:00:00', '13:00:00');

-- Insert sample data into volunteer_assignments table
INSERT INTO volunteer_assignments (event_id, volunteer_id, assigned_date)
VALUES 
(1, 1, '2022-02-20'),
(2, 2, '2022-03-20');
```
