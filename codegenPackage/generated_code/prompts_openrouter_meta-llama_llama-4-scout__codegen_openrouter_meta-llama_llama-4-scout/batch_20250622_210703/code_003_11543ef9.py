"""
Generated Code Metadata:
========================
Original URL: https://gstouristcentre.gr
Prompt: "Design a database schema for storing information about tourist activities, including bus tours and boat trips, for a company like GS Tourist Centre in Corfu."
Generated: DETERMINISTIC_11543ef99af11183
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for tourist activities
CREATE DATABASE tourist_activities;

-- Use the database
USE tourist_activities;

-- Create table for activity types
CREATE TABLE activity_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for activities
CREATE TABLE activities (
  id INT AUTO_INCREMENT,
  activity_type_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  duration INT, -- in minutes
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (activity_type_id) REFERENCES activity_types(id) ON DELETE CASCADE
);

-- Create table for buses
CREATE TABLE buses (
  id INT AUTO_INCREMENT,
  capacity INT NOT NULL,
  bus_type VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for bus tours
CREATE TABLE bus_tours (
  id INT AUTO_INCREMENT,
  activity_id INT NOT NULL,
  bus_id INT NOT NULL,
  departure_time TIME NOT NULL,
  return_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE CASCADE,
  FOREIGN KEY (bus_id) REFERENCES buses(id) ON DELETE CASCADE
);

-- Create table for boats
CREATE TABLE boats (
  id INT AUTO_INCREMENT,
  capacity INT NOT NULL,
  boat_type VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for boat trips
CREATE TABLE boat_trips (
  id INT AUTO_INCREMENT,
  activity_id INT NOT NULL,
  boat_id INT NOT NULL,
  departure_time TIME NOT NULL,
  return_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE CASCADE,
  FOREIGN KEY (boat_id) REFERENCES boats(id) ON DELETE CASCADE
);

-- Create table for bookings
CREATE TABLE bookings (
  id INT AUTO_INCREMENT,
  activity_id INT NOT NULL,
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(255) NOT NULL,
  booking_date DATE NOT NULL,
  num_tickets INT NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_activity_types_id ON activities (activity_type_id);
CREATE INDEX idx_buses_id ON bus_tours (bus_id);
CREATE INDEX idx_activities_id ON bus_tours (activity_id);
CREATE INDEX idx_boats_id ON boat_trips (boat_id);
CREATE INDEX idx_activities_id_boat_trips ON boat_trips (activity_id);
CREATE INDEX idx_bookings_activity_id ON bookings (activity_id);
```

```sql
-- sample_data.sql

-- Insert sample data into activity types
INSERT INTO activity_types (name, description)
VALUES 
('Bus Tour', 'Guided tour around the island'),
('Boat Trip', 'Relaxing trip around the coastline');

-- Insert sample data into activities
INSERT INTO activities (activity_type_id, name, description, duration, price)
VALUES 
(1, 'Island Tour', 'Explore the island with our expert guides', 180, 50.00),
(2, 'Coastline Cruise', 'Relax and enjoy the scenic views', 120, 40.00);

-- Insert sample data into buses
INSERT INTO buses (capacity, bus_type)
VALUES 
(50, 'Coach'),
(30, 'Mini Bus');

-- Insert sample data into bus tours
INSERT INTO bus_tours (activity_id, bus_id, departure_time, return_time)
VALUES 
(1, 1, '09:00:00', '12:00:00'),
(1, 2, '14:00:00', '17:00:00');

-- Insert sample data into boats
INSERT INTO boats (capacity, boat_type)
VALUES 
(20, 'Sailboat'),
(50, 'Catamaran');

-- Insert sample data into boat trips
INSERT INTO boat_trips (activity_id, boat_id, departure_time, return_time)
VALUES 
(2, 1, '10:00:00', '13:00:00'),
(2, 2, '16:00:00', '19:00:00');

-- Insert sample data into bookings
INSERT INTO bookings (activity_id, customer_name, customer_email, booking_date, num_tickets, total_cost)
VALUES 
(1, 'John Doe', 'john@example.com', '2024-09-16', 2, 100.00),
(2, 'Jane Smith', 'jane@example.com', '2024-09-17', 1, 40.00);
```
