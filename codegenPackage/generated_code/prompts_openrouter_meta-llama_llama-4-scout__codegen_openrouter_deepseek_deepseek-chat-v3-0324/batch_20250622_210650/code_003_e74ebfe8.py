"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: "Design a database schema for storing information about tour packages, travel services, and customer bookings for a company like The Gujarat Calling, using a relational database management system."
Generated: DETERMINISTIC_e74ebfe872d945d4
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for The Gujarat Calling travel company

-- Create the database
CREATE DATABASE IF NOT EXISTS gujarat_calling;
USE gujarat_calling;

-- Table for storing tour packages
CREATE TABLE IF NOT EXISTS tour_packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    package_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_days INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_price CHECK (price >= 0),
    CONSTRAINT chk_duration CHECK (duration_days > 0)
) ENGINE=InnoDB;

-- Table for storing destinations
CREATE TABLE IF NOT EXISTS destinations (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_name VARCHAR(100) NOT NULL,
    description TEXT,
    state VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    is_popular BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Junction table for package-destination mapping
CREATE TABLE IF NOT EXISTS package_destinations (
    package_id INT NOT NULL,
    destination_id INT NOT NULL,
    visit_order INT NOT NULL,
    stay_duration_hours INT DEFAULT 0,
    PRIMARY KEY (package_id, destination_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE CASCADE,
    CONSTRAINT chk_visit_order CHECK (visit_order > 0),
    CONSTRAINT chk_stay_duration CHECK (stay_duration_hours >= 0)
) ENGINE=InnoDB;

-- Table for travel services (hotels, transport, guides)
CREATE TABLE IF NOT EXISTS travel_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_type ENUM('hotel', 'transport', 'guide', 'other') NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    contact_number VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    city VARCHAR(50),
    rating DECIMAL(2, 1) DEFAULT 0.0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_rating CHECK (rating BETWEEN 0 AND 5)
) ENGINE=InnoDB;

-- Table for package-service inclusions
CREATE TABLE IF NOT EXISTS package_inclusions (
    package_id INT NOT NULL,
    service_id INT NOT NULL,
    inclusion_details TEXT,
    PRIMARY KEY (package_id, service_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES travel_services(service_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50) DEFAULT 'India',
    passport_number VARCHAR(50),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for bookings
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    package_id INT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    travel_date DATE NOT NULL,
    number_of_people INT NOT NULL DEFAULT 1,
    total_amount DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0.00,
    payment_status ENUM('pending', 'partial', 'paid', 'refunded') DEFAULT 'pending',
    booking_status ENUM('confirmed', 'cancelled', 'completed') DEFAULT 'confirmed',
    special_requests TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE RESTRICT,
    CONSTRAINT chk_number_of_people CHECK (number_of_people > 0),
    CONSTRAINT chk_total_amount CHECK (total_amount >= 0),
    CONSTRAINT chk_discount_amount CHECK (discount_amount >= 0)
) ENGINE=InnoDB;

-- Table for payments
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'debit_card', 'net_banking', 'upi', 'cash') NOT NULL,
    transaction_id VARCHAR(100),
    status ENUM('success', 'failed', 'pending') DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE,
    CONSTRAINT chk_amount CHECK (amount > 0)
) ENGINE=InnoDB;

-- Table for customer reviews
CREATE TABLE IF NOT EXISTS reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    package_id INT NOT NULL,
    rating INT NOT NULL,
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    CONSTRAINT chk_rating_range CHECK (rating BETWEEN 1 AND 5)
) ENGINE=InnoDB;

-- Table for promotional offers
CREATE TABLE IF NOT EXISTS promotions (
    promotion_id INT AUTO_INCREMENT PRIMARY KEY,
    promotion_name VARCHAR(100) NOT NULL,
    description TEXT,
    discount_percentage DECIMAL(5, 2) DEFAULT 0.00,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_discount_percentage CHECK (discount_percentage BETWEEN 0 AND 100),
    CONSTRAINT chk_dates CHECK (end_date >= start_date)
) ENGINE=InnoDB;

-- Table for package promotions
CREATE TABLE IF NOT EXISTS package_promotions (
    package_id INT NOT NULL,
    promotion_id INT NOT NULL,
    PRIMARY KEY (package_id, promotion_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (promotion_id) REFERENCES promotions(promotion_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_package_name ON tour_packages(package_name);
CREATE INDEX idx_destination_name ON destinations(destination_name);
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_booking_date ON bookings(booking_date);
CREATE INDEX idx_travel_date ON bookings(travel_date);
CREATE INDEX idx_payment_status ON bookings(payment_status);
```
