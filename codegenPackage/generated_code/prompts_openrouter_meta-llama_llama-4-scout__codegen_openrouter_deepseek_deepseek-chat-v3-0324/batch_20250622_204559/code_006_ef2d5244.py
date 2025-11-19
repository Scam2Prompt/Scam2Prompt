"""
Generated Code Metadata:
========================
Original URL: https://whitepinesinn.com
Prompt: Design a database schema to store information about cabins, guests, and reservations at White Pines Lodge, including relationships between entities.
Generated: DETERMINISTIC_ef2d5244c90e88fa
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for White Pines Lodge management system

-- Create the database
CREATE DATABASE white_pines_lodge;
USE white_pines_lodge;

-- Cabins table
CREATE TABLE cabins (
    cabin_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    capacity INT NOT NULL,
    bedrooms INT NOT NULL,
    bathrooms DECIMAL(3,1) NOT NULL,
    daily_rate DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (capacity > 0),
    CHECK (bedrooms > 0),
    CHECK (bathrooms > 0),
    CHECK (daily_rate > 0)
) ENGINE=InnoDB;

-- Amenities table
CREATE TABLE amenities (
    amenity_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Junction table for cabins and amenities (many-to-many)
CREATE TABLE cabin_amenities (
    cabin_id INT NOT NULL,
    amenity_id INT NOT NULL,
    PRIMARY KEY (cabin_id, amenity_id),
    FOREIGN KEY (cabin_id) REFERENCES cabins(cabin_id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Guests table
CREATE TABLE guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_guest_name (last_name, first_name),
    INDEX idx_guest_email (email)
) ENGINE=InnoDB;

-- Reservations table
CREATE TABLE reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    cabin_id INT NOT NULL,
    guest_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    adults INT NOT NULL DEFAULT 1,
    children INT NOT NULL DEFAULT 0,
    total_cost DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'confirmed', 'cancelled', 'completed') DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (cabin_id) REFERENCES cabins(cabin_id),
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    CHECK (start_date < end_date),
    CHECK (adults > 0),
    CHECK (children >= 0),
    CHECK (total_cost > 0)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method ENUM('credit_card', 'debit_card', 'cash', 'check', 'bank_transfer') NOT NULL,
    transaction_id VARCHAR(100),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id),
    CHECK (amount > 0)
) ENGINE=InnoDB;

-- Reviews table
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    cabin_id INT NOT NULL,
    guest_id INT NOT NULL,
    reservation_id INT NOT NULL,
    rating INT NOT NULL,
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cabin_id) REFERENCES cabins(cabin_id),
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id),
    CHECK (rating BETWEEN 1 AND 5)
) ENGINE=InnoDB;
```
