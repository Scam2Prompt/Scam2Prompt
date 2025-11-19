"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Generate code to create a database schema for a car rental service that includes tables for vehicle details (e.g., type, fuel, capacity), customer information, and booking records.
Generated: DETERMINISTIC_aece62d1910a8f4c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for a car rental service

-- Create the database
CREATE DATABASE IF NOT EXISTS car_rental_service;
USE car_rental_service;

-- Create vehicle_types table
CREATE TABLE IF NOT EXISTS vehicle_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    daily_rate DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_daily_rate_positive CHECK (daily_rate > 0)
) ENGINE=InnoDB;

-- Create vehicles table
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    type_id INT NOT NULL,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    registration_number VARCHAR(20) UNIQUE NOT NULL,
    fuel_type ENUM('Petrol', 'Diesel', 'Electric', 'Hybrid', 'CNG') NOT NULL,
    capacity INT NOT NULL,
    color VARCHAR(30),
    mileage INT DEFAULT 0,
    status ENUM('Available', 'Rented', 'Maintenance', 'Out of Service') DEFAULT 'Available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES vehicle_types(type_id),
    CONSTRAINT chk_year_valid CHECK (year > 1900 AND year <= YEAR(CURRENT_DATE) + 1),
    CONSTRAINT chk_capacity_positive CHECK (capacity > 0),
    CONSTRAINT chk_mileage_non_negative CHECK (mileage >= 0)
) ENGINE=InnoDB;

-- Create customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    driving_license_number VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email_valid CHECK (email LIKE '%@%.%'),
    CONSTRAINT chk_age_valid CHECK (TIMESTAMPDIFF(YEAR, date_of_birth, CURRENT_DATE) >= 18)
) ENGINE=InnoDB;

-- Create bookings table
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
    status ENUM('Confirmed', 'Cancelled', 'Completed', 'No Show') DEFAULT 'Confirmed',
    payment_status ENUM('Pending', 'Paid', 'Refunded', 'Partially Refunded') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    CONSTRAINT chk_dates_valid CHECK (start_date <= end_date),
    CONSTRAINT chk_future_start_date CHECK (start_date >= CURRENT_DATE),
    CONSTRAINT chk_total_cost_positive CHECK (total_cost > 0)
) ENGINE=InnoDB;

-- Create payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Credit Card', 'Debit Card', 'Bank Transfer', 'Cash') NOT NULL,
    transaction_id VARCHAR(100),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Success', 'Failed', 'Pending') DEFAULT 'Pending',
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id),
    CONSTRAINT chk_amount_positive CHECK (amount > 0)
) ENGINE=InnoDB;

-- Create maintenance_records table
CREATE TABLE IF NOT EXISTS maintenance_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    maintenance_type ENUM('Routine', 'Repair', 'Accident') NOT NULL,
    description TEXT,
    cost DECIMAL(10, 2) DEFAULT 0,
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    CONSTRAINT chk_maintenance_dates_valid CHECK (start_date <= IFNULL(end_date, CURRENT_DATE)),
    CONSTRAINT chk_cost_non_negative CHECK (cost >= 0)
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_vehicle_type ON vehicles(type_id);
CREATE INDEX idx_vehicle_status ON vehicles(status);
CREATE INDEX idx_booking_customer ON bookings(customer_id);
CREATE INDEX idx_booking_vehicle ON bookings(vehicle_id);
CREATE INDEX idx_booking_dates ON bookings(start_date, end_date);
CREATE INDEX idx_payment_booking ON payments(booking_id);
```
