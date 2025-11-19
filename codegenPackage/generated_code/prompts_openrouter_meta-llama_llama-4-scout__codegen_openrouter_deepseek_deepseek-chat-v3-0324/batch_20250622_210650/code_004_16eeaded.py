"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Create a SQL database schema for a car rental company like Rental Car Elena, including tables for vehicles, customers, bookings, and payments.
Generated: DETERMINISTIC_16eeaded85383343
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Car Rental Company

-- Create database
CREATE DATABASE CarRental;
USE CarRental;

-- Vehicles table
CREATE TABLE Vehicles (
    vehicle_id INT PRIMARY KEY AUTO_INCREMENT,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    license_plate VARCHAR(20) UNIQUE NOT NULL,
    color VARCHAR(30),
    mileage INT DEFAULT 0,
    daily_rate DECIMAL(10,2) NOT NULL,
    status ENUM('available', 'rented', 'maintenance') DEFAULT 'available',
    vehicle_type ENUM('economy', 'compact', 'mid-size', 'full-size', 'luxury', 'suv', 'minivan') NOT NULL,
    fuel_type ENUM('gasoline', 'diesel', 'electric', 'hybrid') NOT NULL,
    transmission ENUM('manual', 'automatic') NOT NULL,
    seats INT NOT NULL,
    last_maintenance_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (year >= 2000 AND year <= YEAR(CURRENT_DATE) + 1),
    CHECK (mileage >= 0),
    CHECK (daily_rate > 0)
);

-- Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    date_of_birth DATE NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    driver_license_number VARCHAR(50) UNIQUE NOT NULL,
    driver_license_expiry DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (YEAR(CURRENT_DATE) - YEAR(date_of_birth) >= 18)
);

-- Bookings table
CREATE TABLE Bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    pickup_location VARCHAR(100) NOT NULL,
    dropoff_location VARCHAR(100) NOT NULL,
    total_cost DECIMAL(10,2) NOT NULL,
    status ENUM('confirmed', 'active', 'completed', 'cancelled') DEFAULT 'confirmed',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id) ON DELETE CASCADE,
    CHECK (end_date > start_date)
);

-- Payments table
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'debit_card', 'cash', 'bank_transfer', 'online_payment') NOT NULL,
    transaction_id VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    card_last_four VARCHAR(4),
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id) ON DELETE CASCADE,
    CHECK (amount > 0)
);

-- Vehicle Maintenance table
CREATE TABLE Maintenance (
    maintenance_id INT PRIMARY KEY AUTO_INCREMENT,
    vehicle_id INT NOT NULL,
    maintenance_type ENUM('routine', 'repair', 'accident') NOT NULL,
    description TEXT,
    cost DECIMAL(10,2),
    start_date DATE NOT NULL,
    end_date DATE,
    service_provider VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id) ON DELETE CASCADE,
    CHECK (cost >= 0)
);

-- Insurance table
CREATE TABLE Insurance (
    insurance_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT NOT NULL,
    insurance_type ENUM('basic', 'premium', 'full_coverage') NOT NULL,
    daily_rate DECIMAL(10,2) NOT NULL,
    total_cost DECIMAL(10,2) NOT NULL,
    coverage_details TEXT,
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id) ON DELETE CASCADE,
    CHECK (daily_rate > 0),
    CHECK (total_cost > 0)
);

-- Create indexes for performance
CREATE INDEX idx_vehicle_status ON Vehicles(status);
CREATE INDEX idx_booking_dates ON Bookings(start_date, end_date);
CREATE INDEX idx_customer_email ON Customers(email);
CREATE INDEX idx_payment_status ON Payments(status);
```
