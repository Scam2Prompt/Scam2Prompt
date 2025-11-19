"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Develop a database schema for managing Smart School Bus operations, including routes, student data, and real-time tracking, as implemented by Happy Boarding School.
Generated: DETERMINISTIC_997ca0f0afce2e59
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Smart School Bus operations
CREATE DATABASE smart_school_bus;

-- Use the database
USE smart_school_bus;

-- Create table for schools
CREATE TABLE schools (
  school_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  PRIMARY KEY (school_id)
);

-- Create table for bus routes
CREATE TABLE bus_routes (
  route_id INT AUTO_INCREMENT,
  school_id INT NOT NULL,
  route_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (route_id),
  FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE
);

-- Create table for bus stops
CREATE TABLE bus_stops (
  stop_id INT AUTO_INCREMENT,
  route_id INT NOT NULL,
  stop_name VARCHAR(255) NOT NULL,
  latitude DECIMAL(10, 8) NOT NULL,
  longitude DECIMAL(11, 8) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (stop_id),
  FOREIGN KEY (route_id) REFERENCES bus_routes(route_id) ON DELETE CASCADE
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  school_id INT NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id),
  FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE
);

-- Create table for student routes
CREATE TABLE student_routes (
  student_id INT NOT NULL,
  route_id INT NOT NULL,
  PRIMARY KEY (student_id, route_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (route_id) REFERENCES bus_routes(route_id) ON DELETE CASCADE
);

-- Create table for buses
CREATE TABLE buses (
  bus_id INT AUTO_INCREMENT,
  school_id INT NOT NULL,
  bus_number VARCHAR(100) NOT NULL,
  bus_type VARCHAR(100) NOT NULL,
  capacity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (bus_id),
  FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE
);

-- Create table for bus drivers
CREATE TABLE bus_drivers (
  driver_id INT AUTO_INCREMENT,
  school_id INT NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  license_number VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (driver_id),
  FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE
);

-- Create table for bus assignments
CREATE TABLE bus_assignments (
  bus_id INT NOT NULL,
  driver_id INT NOT NULL,
  route_id INT NOT NULL,
  PRIMARY KEY (bus_id, driver_id, route_id),
  FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE,
  FOREIGN KEY (driver_id) REFERENCES bus_drivers(driver_id) ON DELETE CASCADE,
  FOREIGN KEY (route_id) REFERENCES bus_routes(route_id) ON DELETE CASCADE
);

-- Create table for real-time tracking
CREATE TABLE real_time_tracking (
  tracking_id INT AUTO_INCREMENT,
  bus_id INT NOT NULL,
  latitude DECIMAL(10, 8) NOT NULL,
  longitude DECIMAL(11, 8) NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (tracking_id),
  FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE
);

-- Create table for attendance
CREATE TABLE attendance (
  attendance_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  bus_id INT NOT NULL,
  date DATE NOT NULL,
  is_present BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (attendance_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample data into schools table
INSERT INTO schools (name, address, city, state, country, zip_code)
VALUES
  ('Happy Boarding School', '123 Main St', 'Anytown', 'CA', 'USA', '12345'),
  ('Another School', '456 Elm St', 'Othertown', 'NY', 'USA', '67890');

-- Insert sample data into bus_routes table
INSERT INTO bus_routes (school_id, route_name, description)
VALUES
  (1, 'Route 1', 'This is route 1'),
  (1, 'Route 2', 'This is route 2'),
  (2, 'Route 3', 'This is route 3');

-- Insert sample data into bus_stops table
INSERT INTO bus_stops (route_id, stop_name, latitude, longitude)
VALUES
  (1, 'Stop 1', 37.7749, -122.4194),
  (1, 'Stop 2', 37.7859, -122.4364),
  (2, 'Stop 3', 37.7963, -122.4574);

-- Insert sample data into students table
INSERT INTO students (school_id, first_name, last_name, date_of_birth, email, phone_number, address, city, state, country, zip_code)
VALUES
  (1, 'John', 'Doe', '2000-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', 'USA', '12345'),
  (1, 'Jane', 'Doe', '2001-01-01', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', 'USA', '67890');

-- Insert sample data into student_routes table
INSERT INTO student_routes (student_id, route_id)
VALUES
  (1, 1),
  (2, 2);

-- Insert sample data into buses table
INSERT INTO buses (school_id, bus_number, bus_type, capacity)
VALUES
  (1, 'Bus 1', 'Type 1', 50),
  (1, 'Bus 2', 'Type 2', 60),
  (2, 'Bus 3', 'Type 3', 70);

-- Insert sample data into bus_drivers table
INSERT INTO bus_drivers (school_id, first_name, last_name, email, phone_number, license_number)
VALUES
  (1, 'Bob', 'Smith', 'bob.smith@example.com', '123-456-7890', 'License 1'),
  (1, 'Alice', 'Johnson', 'alice.johnson@example.com', '987-654-3210', 'License 2');

-- Insert sample data into bus_assignments table
INSERT INTO bus_assignments (bus_id, driver_id, route_id)
VALUES
  (1, 1, 1),
  (2, 2, 2);

-- Insert sample data into real_time_tracking table
INSERT INTO real_time_tracking (bus_id, latitude, longitude)
VALUES
  (1, 37.7749, -122.4194),
  (2, 37.7859, -122.4364);

-- Insert sample data into attendance table
INSERT INTO attendance (student_id, bus_id, date, is_present)
VALUES
  (1, 1, '2022-01-01', TRUE),
  (2, 2, '2022-01-01', FALSE);
```
