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
-- Database schema for Smart School Bus Operations Management System

-- Create the database
CREATE DATABASE IF NOT EXISTS smart_bus_operations;
USE smart_bus_operations;

-- Table for storing school information
CREATE TABLE IF NOT EXISTS schools (
    school_id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    principal_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for storing bus information
CREATE TABLE IF NOT EXISTS buses (
    bus_id INT AUTO_INCREMENT PRIMARY KEY,
    school_id INT NOT NULL,
    registration_number VARCHAR(20) NOT NULL UNIQUE,
    capacity INT NOT NULL,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    gps_device_id VARCHAR(50) UNIQUE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE,
    CONSTRAINT chk_capacity CHECK (capacity > 0),
    CONSTRAINT chk_year CHECK (year >= 2000 AND year <= YEAR(CURRENT_DATE) + 1)
) ENGINE=InnoDB;

-- Table for storing driver information
CREATE TABLE IF NOT EXISTS drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    school_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(20) NOT NULL UNIQUE,
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(255),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE,
    CONSTRAINT chk_email_driver CHECK (email IS NULL OR email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for storing bus routes
CREATE TABLE IF NOT EXISTS routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    school_id INT NOT NULL,
    route_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_point VARCHAR(255) NOT NULL,
    end_point VARCHAR(255) NOT NULL,
    estimated_duration_minutes INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE,
    CONSTRAINT chk_duration CHECK (estimated_duration_minutes > 0)
) ENGINE=InnoDB;

-- Table for storing route stops
CREATE TABLE IF NOT EXISTS route_stops (
    stop_id INT AUTO_INCREMENT PRIMARY KEY,
    route_id INT NOT NULL,
    stop_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    sequence_number INT NOT NULL,
    estimated_arrival_time TIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE,
    CONSTRAINT chk_coordinates CHECK (latitude BETWEEN -90 AND 90 AND longitude BETWEEN -180 AND 180),
    CONSTRAINT chk_sequence CHECK (sequence_number > 0),
    UNIQUE KEY (route_id, sequence_number)
) ENGINE=InnoDB;

-- Table for storing student information
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    school_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    grade_level VARCHAR(20) NOT NULL,
    parent_guardian_name VARCHAR(100) NOT NULL,
    parent_guardian_contact VARCHAR(20) NOT NULL,
    parent_guardian_email VARCHAR(100),
    home_address VARCHAR(255) NOT NULL,
    is_bus_required BOOLEAN DEFAULT FALSE,
    rfid_tag_id VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE,
    CONSTRAINT chk_parent_email CHECK (parent_guardian_email IS NULL OR parent_guardian_email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for assigning buses to routes
CREATE TABLE IF NOT EXISTS bus_route_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    bus_id INT NOT NULL,
    route_id INT NOT NULL,
    driver_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE,
    FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR end_date >= start_date)
) ENGINE=InnoDB;

-- Table for assigning students to bus stops
CREATE TABLE IF NOT EXISTS student_stop_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    stop_id INT NOT NULL,
    assignment_date DATE NOT NULL,
    is_morning_pickup BOOLEAN NOT NULL,
    is_afternoon_dropoff BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (stop_id) REFERENCES route_stops(stop_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, stop_id, assignment_date)
) ENGINE=InnoDB;

-- Table for real-time bus tracking
CREATE TABLE IF NOT EXISTS bus_locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    bus_id INT NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    speed DECIMAL(6, 2),
    direction_degrees DECIMAL(5, 2),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE,
    CONSTRAINT chk_location_coords CHECK (latitude BETWEEN -90 AND 90 AND longitude BETWEEN -180 AND 180),
    CONSTRAINT chk_speed CHECK (speed IS NULL OR speed >= 0),
    CONSTRAINT chk_direction CHECK (direction_degrees IS NULL OR (direction_degrees >= 0 AND direction_degrees < 360))
) ENGINE=InnoDB;

-- Table for student boarding records
CREATE TABLE IF NOT EXISTS boarding_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    bus_id INT NOT NULL,
    stop_id INT NOT NULL,
    boarding_type ENUM('pickup', 'dropoff') NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    verified_by_driver BOOLEAN DEFAULT FALSE,
    notes TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE,
    FOREIGN KEY (stop_id) REFERENCES route_stops(stop_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for bus schedule
CREATE TABLE IF NOT EXISTS bus_schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    assignment_id INT NOT NULL,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES bus_route_assignments(assignment_id) ON DELETE CASCADE,
    CONSTRAINT chk_times CHECK (arrival_time > departure_time)
) ENGINE=InnoDB;

-- Table for notifications and alerts
CREATE TABLE IF NOT EXISTS notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    recipient_type ENUM('parent', 'driver', 'admin') NOT NULL,
    recipient_id INT NOT NULL,
    notification_type VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSON
) ENGINE=InnoDB;

-- Table for system users (admins,
