"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: Design a database schema in SQL to store information about tour packages, taxi services, and customer bookings based on the offerings listed on the "Best Holidays All India" website.
Generated: DETERMINISTIC_2908caa1111a71ab
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Best Holidays All India

-- Create the database
CREATE DATABASE IF NOT EXISTS best_holidays_all_india;
USE best_holidays_all_india;

-- Table for storing tour packages
CREATE TABLE IF NOT EXISTS tour_packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    package_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_days INT NOT NULL,
    price_per_person DECIMAL(10, 2) NOT NULL,
    destinations TEXT NOT NULL,
    inclusions TEXT,
    exclusions TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_duration CHECK (duration_days > 0),
    CONSTRAINT chk_price CHECK (price_per_person >= 0)
) ENGINE=InnoDB;

-- Table for storing taxi services
CREATE TABLE IF NOT EXISTS taxi_services (
    taxi_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_type VARCHAR(50) NOT NULL,
    capacity INT NOT NULL,
    price_per_km DECIMAL(10, 2) NOT NULL,
    is_ac BOOLEAN DEFAULT FALSE,
    is_available BOOLEAN DEFAULT TRUE,
    registration_number VARCHAR(20) UNIQUE NOT NULL,
    driver_name VARCHAR(100),
    driver_contact VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_capacity CHECK (capacity > 0),
    CONSTRAINT chk_price_per_km CHECK (price_per_km >= 0)
) ENGINE=InnoDB;

-- Table for storing customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50) DEFAULT 'India',
    pincode VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing tour bookings
CREATE TABLE IF NOT EXISTS tour_bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    package_id INT NOT NULL,
    booking_date DATE NOT NULL,
    travel_date DATE NOT NULL,
    number_of_people INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    booking_status ENUM('confirmed', 'pending', 'cancelled', 'completed') DEFAULT 'pending',
    payment_status ENUM('paid', 'unpaid', 'partial') DEFAULT 'unpaid',
    special_requests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    CONSTRAINT chk_people CHECK (number_of_people > 0),
    CONSTRAINT chk_amount CHECK (total_amount >= 0),
    CONSTRAINT chk_travel_date CHECK (travel_date >= booking_date)
) ENGINE=InnoDB;

-- Table for storing taxi bookings
CREATE TABLE IF NOT EXISTS taxi_bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    taxi_id INT NOT NULL,
    pickup_location TEXT NOT NULL,
    drop_location TEXT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pickup_time DATETIME NOT NULL,
    distance_km DECIMAL(10, 2) NOT NULL,
    estimated_amount DECIMAL(10, 2) NOT NULL,
    final_amount DECIMAL(10, 2),
    booking_status ENUM('confirmed', 'pending', 'cancelled', 'completed') DEFAULT 'pending',
    payment_status ENUM('paid', 'unpaid', 'partial') DEFAULT 'unpaid',
    special_requests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (taxi_id) REFERENCES taxi_services(taxi_id) ON DELETE CASCADE,
    CONSTRAINT chk_distance CHECK (distance_km > 0),
    CONSTRAINT chk_estimated_amount CHECK (estimated_amount >= 0),
    CONSTRAINT chk_final_amount CHECK (final_amount >= 0)
) ENGINE=InnoDB;

-- Table for storing payments
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_type ENUM('tour', 'taxi') NOT NULL,
    booking_id INT NOT NULL,
    customer_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'debit_card', 'net_banking', 'upi', 'cash') NOT NULL,
    transaction_id VARCHAR(100),
    payment_status ENUM('success', 'failed', 'pending') DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    CONSTRAINT chk_amount_positive CHECK (amount > 0)
) ENGINE=InnoDB;

-- Table for storing customer reviews
CREATE TABLE IF NOT EXISTS reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    booking_type ENUM('tour', 'taxi') NOT NULL,
    booking_id INT NOT NULL,
    rating INT NOT NULL,
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    CONSTRAINT chk_rating CHECK (rating BETWEEN 1 AND 5)
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_tour_packages_active ON tour_packages(is_active);
CREATE INDEX idx_taxi_services_available ON taxi_services(is_available);
CREATE INDEX idx_tour_bookings_status ON tour_bookings(booking_status);
CREATE INDEX idx_taxi_bookings_status ON taxi_bookings(booking_status);
CREATE INDEX idx_payments_status ON payments(payment_status);
```
