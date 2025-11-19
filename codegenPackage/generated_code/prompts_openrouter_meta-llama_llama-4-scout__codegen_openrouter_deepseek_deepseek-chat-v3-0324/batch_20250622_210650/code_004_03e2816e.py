"""
Generated Code Metadata:
========================
Original URL: https://rimedyahotel.com
Prompt: Create a SQL database schema for a hotel like Grand Rimedya, including tables for rooms (e.g., deluxe oda, twin oda), amenities (e.g., grand salon, restaurant), and customer reservations.
Generated: DETERMINISTIC_03e2816e3170a82d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Grand Rimedya Hotel Management System

-- Create database
CREATE DATABASE GrandRimedyaHotel;
USE GrandRimedyaHotel;

-- Room Types Table
CREATE TABLE RoomTypes (
    room_type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    max_occupancy INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Rooms Table
CREATE TABLE Rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    room_type_id INT NOT NULL,
    floor_number INT NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (room_type_id) REFERENCES RoomTypes(room_type_id)
);

-- Amenities Table
CREATE TABLE Amenities (
    amenity_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    location VARCHAR(100),
    operating_hours VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Customers Table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    id_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Reservations Table
CREATE TABLE Reservations (
    reservation_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    adults INT NOT NULL DEFAULT 1,
    children INT NOT NULL DEFAULT 0,
    total_price DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'confirmed', 'cancelled', 'completed') DEFAULT 'pending',
    special_requests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    CHECK (check_out_date > check_in_date)
);

-- Room Amenities Junction Table (Many-to-Many relationship between Rooms and Amenities)
CREATE TABLE RoomAmenities (
    room_id INT NOT NULL,
    amenity_id INT NOT NULL,
    PRIMARY KEY (room_id, amenity_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (amenity_id) REFERENCES Amenities(amenity_id)
);

-- Payments Table
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    reservation_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'cash', 'bank_transfer', 'other') NOT NULL,
    transaction_id VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
);

-- Insert sample room types
INSERT INTO RoomTypes (type_name, description, base_price, max_occupancy) VALUES
('Deluxe Oda', 'Spacious room with king bed and luxury amenities', 500.00, 2),
('Twin Oda', 'Room with two single beds and standard amenities', 350.00, 2),
('Suite', 'Luxury suite with separate living area and premium services', 800.00, 4),
('Family Room', 'Large room with multiple beds for families', 600.00, 5);

-- Insert sample amenities
INSERT INTO Amenities (name, description, location, operating_hours) VALUES
('Grand Salon', 'Elegant lobby lounge for guests', 'Ground Floor', '24/7'),
('Restaurant', 'Fine dining restaurant serving local and international cuisine', 'First Floor', '07:00-23:00'),
('Spa', 'Full-service spa with various treatments', 'Second Floor', '09:00-21:00'),
('Fitness Center', 'Modern gym with cardio and weight equipment', 'Second Floor', '06:00-22:00'),
('Pool', 'Outdoor swimming pool with sun deck', 'Roof Top', '08:00-20:00');
```
