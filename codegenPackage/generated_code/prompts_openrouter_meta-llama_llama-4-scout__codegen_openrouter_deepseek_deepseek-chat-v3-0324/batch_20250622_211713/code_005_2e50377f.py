"""
Generated Code Metadata:
========================
Original URL: https://reservation-team.com
Prompt: Write a SQL query to manage flight bookings, including passenger information, flight details, and payment processing, similar to Reservation Team's booking system.
Generated: DETERMINISTIC_2e50377ff2745cff
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script for managing flight bookings system
-- Includes tables for passengers, flights, bookings, and payments
-- Supports CRUD operations for a flight reservation system

-- Create database (if not exists)
CREATE DATABASE IF NOT EXISTS flight_booking_system;
USE flight_booking_system;

-- Create passengers table
CREATE TABLE IF NOT EXISTS passengers (
    passenger_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    passport_number VARCHAR(20) UNIQUE NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_passenger_name (last_name, first_name),
    INDEX idx_passport (passport_number)
) ENGINE=InnoDB;

-- Create airlines table
CREATE TABLE IF NOT EXISTS airlines (
    airline_id INT AUTO_INCREMENT PRIMARY KEY,
    airline_name VARCHAR(100) NOT NULL,
    iata_code VARCHAR(2) UNIQUE NOT NULL,
    icao_code VARCHAR(3) UNIQUE NOT NULL,
    country VARCHAR(50) NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create aircraft table
CREATE TABLE IF NOT EXISTS aircraft (
    aircraft_id INT AUTO_INCREMENT PRIMARY KEY,
    airline_id INT NOT NULL,
    model VARCHAR(50) NOT NULL,
    iata_code VARCHAR(3) NOT NULL,
    capacity INT NOT NULL,
    manufactured_year YEAR NOT NULL,
    last_maintenance DATE,
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id) ON DELETE CASCADE,
    INDEX idx_aircraft_model (model)
) ENGINE=InnoDB;

-- Create airports table
CREATE TABLE IF NOT EXISTS airports (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    iata_code VARCHAR(3) UNIQUE NOT NULL,
    icao_code VARCHAR(4) UNIQUE NOT NULL,
    airport_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    latitude DECIMAL(10, 6) NOT NULL,
    longitude DECIMAL(10, 6) NOT NULL,
    timezone VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_airport_city (city),
    INDEX idx_airport_country (country)
) ENGINE=InnoDB;

-- Create flights table
CREATE TABLE IF NOT EXISTS flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(10) NOT NULL,
    airline_id INT NOT NULL,
    aircraft_id INT NOT NULL,
    departure_airport_id INT NOT NULL,
    arrival_airport_id INT NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    duration_minutes INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    status ENUM('Scheduled', 'Delayed', 'Departed', 'Arrived', 'Cancelled') DEFAULT 'Scheduled',
    available_seats INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id) ON DELETE CASCADE,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(aircraft_id) ON DELETE CASCADE,
    FOREIGN KEY (departure_airport_id) REFERENCES airports(airport_id) ON DELETE CASCADE,
    FOREIGN KEY (arrival_airport_id) REFERENCES airports(airport_id) ON DELETE CASCADE,
    INDEX idx_flight_number (flight_number),
    INDEX idx_departure_time (departure_time),
    INDEX idx_arrival_time (arrival_time),
    INDEX idx_flight_status (status),
    CONSTRAINT chk_arrival_after_departure CHECK (arrival_time > departure_time)
) ENGINE=InnoDB;

-- Create seat_types table
CREATE TABLE IF NOT EXISTS seat_types (
    seat_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(20) NOT NULL,
    description VARCHAR(100),
    price_multiplier DECIMAL(3, 2) DEFAULT 1.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create seats table
CREATE TABLE IF NOT EXISTS seats (
    seat_id INT AUTO_INCREMENT PRIMARY KEY,
    aircraft_id INT NOT NULL,
    seat_type_id INT NOT NULL,
    seat_number VARCHAR(5) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(aircraft_id) ON DELETE CASCADE,
    FOREIGN KEY (seat_type_id) REFERENCES seat_types(seat_type_id) ON DELETE CASCADE,
    UNIQUE KEY uk_aircraft_seat (aircraft_id, seat_number),
    INDEX idx_seat_availability (is_available)
) ENGINE=InnoDB;

-- Create bookings table
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_reference VARCHAR(10) UNIQUE NOT NULL,
    flight_id INT NOT NULL,
    passenger_id INT NOT NULL,
    seat_id INT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    booking_status ENUM('Confirmed', 'Pending', 'Cancelled', 'Completed') DEFAULT 'Confirmed',
    total_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id) ON DELETE CASCADE,
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id) ON DELETE CASCADE,
    FOREIGN KEY (seat_id) REFERENCES seats(seat_id) ON DELETE CASCADE,
    INDEX idx_booking_reference (booking_reference),
    INDEX idx_booking_status (booking_status),
    INDEX idx_booking_date (booking_date)
) ENGINE=InnoDB;

-- Create payment_methods table
CREATE TABLE IF NOT EXISTS payment_methods (
    payment_method_id INT AUTO_INCREMENT PRIMARY KEY,
    method_name VARCHAR(50) NOT NULL,
    description VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    payment_method_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_id VARCHAR(50) UNIQUE,
    status ENUM('Pending', 'Completed', 'Failed', 'Refunded') DEFAULT 'Pending',
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE,
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(payment_method_id) ON DELETE CASCADE,
    INDEX idx_payment_status (status),
    INDEX idx_payment_date (payment_date)
) ENGINE=InnoDB;

-- Create stored procedure for making a new booking
DELIMITER //
CREATE PROCEDURE make_booking(
    IN p_passenger_id INT,
    IN p_flight_id INT,
    IN p_seat_id INT,
    IN p_payment_method_id INT,
    IN p_notes TEXT,
    OUT p_booking_reference VARCHAR(10)
)
BEGIN
    DECLARE v_flight_price DECIMAL(10, 2);
    DECLARE v_seat_multiplier DECIMAL(3, 2);
    DECLARE v_total_price DECIMAL(10, 2);
    DECLARE v_available_seats INT;
    DECLARE v_seat_available BOOLEAN;
    DECLARE v_booking_ref VARCHAR(10);
    
    -- Check if flight exists and has available seats
    SELECT available_seats INTO v_available_seats
    FROM flights
    WHERE flight_id = p_flight_id;
    
    IF v_available_seats IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Flight not found';
    ELSEIF v_available_seats <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No available seats on this flight';
    END IF;
    
    -- Check if seat is available
    SELECT is_available INTO v_seat_available
    FROM seats
    WHERE seat_id = p_seat_id;
    
    IF v_seat_available IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Seat not found';
    ELSEIF NOT v_seat_available THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Seat is not available';
    END IF;
    
    -- Calculate total price
    SELECT base_price INTO v_flight_price
    FROM flights
    WHERE flight_id = p_flight_id;
    
    SELECT price_multiplier INTO v_seat_multiplier
    FROM seat_types st
    JOIN seats s ON st.seat_type_id = s.seat_type_id
    WHERE s.seat_id = p_seat_id
