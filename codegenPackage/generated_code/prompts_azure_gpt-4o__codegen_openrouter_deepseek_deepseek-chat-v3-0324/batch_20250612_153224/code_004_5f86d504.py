"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Create a database schema in SQL to store information about horse riding tours, including tour names like "Moonshine Ride" and "Rari Discovery Ride," participant details, and preferred tour dates.
Generated: DETERMINISTIC_5f86d5049dd07084
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for horse riding tours management system

-- Create the database
CREATE DATABASE IF NOT EXISTS horse_riding_tours;
USE horse_riding_tours;

-- Tours table to store information about available tours
CREATE TABLE IF NOT EXISTS tours (
    tour_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_hours DECIMAL(4,2) NOT NULL,
    difficulty_level ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL,
    max_participants INT NOT NULL,
    base_price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_max_participants CHECK (max_participants > 0),
    CONSTRAINT chk_base_price CHECK (base_price >= 0)
) ENGINE=InnoDB;

-- Participants table to store customer information
CREATE TABLE IF NOT EXISTS participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    date_of_birth DATE,
    weight_kg DECIMAL(5,2),
    height_cm DECIMAL(5,2),
    riding_experience ENUM('None', 'Beginner', 'Intermediate', 'Advanced') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_weight CHECK (weight_kg > 0),
    CONSTRAINT chk_height CHECK (height_cm > 0)
) ENGINE=InnoDB;

-- Tour schedules table
CREATE TABLE IF NOT EXISTS tour_schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    tour_id INT NOT NULL,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    guide_name VARCHAR(100),
    available_slots INT NOT NULL,
    is_canceled BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (tour_id) REFERENCES tours(tour_id) ON DELETE CASCADE,
    CONSTRAINT chk_datetime CHECK (end_datetime > start_datetime),
    CONSTRAINT chk_available_slots CHECK (available_slots >= 0)
) ENGINE=InnoDB;

-- Bookings table to track tour reservations
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    schedule_id INT NOT NULL,
    participant_id INT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending', 'Confirmed', 'Cancelled', 'Completed') DEFAULT 'Pending',
    special_requests TEXT,
    payment_status ENUM('Unpaid', 'Partial', 'Paid') DEFAULT 'Unpaid',
    amount_paid DECIMAL(10,2) DEFAULT 0,
    total_amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (schedule_id) REFERENCES tour_schedules(schedule_id) ON DELETE CASCADE,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    CONSTRAINT chk_amount_paid CHECK (amount_paid >= 0 AND amount_paid <= total_amount),
    CONSTRAINT chk_total_amount CHECK (total_amount > 0)
) ENGINE=InnoDB;

-- Emergency contacts for participants
CREATE TABLE IF NOT EXISTS emergency_contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    participant_id INT NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    relationship VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    alternate_phone VARCHAR(20),
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_tour_name ON tours(tour_name);
CREATE INDEX idx_participant_name ON participants(last_name, first_name);
CREATE INDEX idx_tour_schedule ON tour_schedules(tour_id, start_datetime);
CREATE INDEX idx_booking_dates ON bookings(booking_date);
```
