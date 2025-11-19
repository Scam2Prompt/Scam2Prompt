"""
Generated Code Metadata:
========================
Original URL: https://visitabroadtravels.com.np
Prompt: "Design a database schema for storing travel packages, customer information, and booking details for a company like Visit Abroad Travels, with entities like packages, customers, guides, and lodges."
Generated: DETERMINISTIC_5de1d18a1f7027f0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Visit Abroad Travels

-- Create database
CREATE DATABASE IF NOT EXISTS visit_abroad_travels;
USE visit_abroad_travels;

-- Create tables with proper constraints and indexes

-- Customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    passport_number VARCHAR(50) UNIQUE,
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_phone (phone)
) ENGINE=InnoDB;

-- Travel packages table
CREATE TABLE packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    destination_country VARCHAR(50) NOT NULL,
    destination_city VARCHAR(50) NOT NULL,
    duration_days INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    start_date DATE,
    end_date DATE,
    max_capacity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_destination (destination_country, destination_city),
    INDEX idx_price (price),
    INDEX idx_dates (start_date, end_date)
) ENGINE=InnoDB;

-- Guides table
CREATE TABLE guides (
    guide_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    languages_spoken VARCHAR(255) NOT NULL,
    country VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_location (country, city),
    INDEX idx_languages (languages_spoken)
) ENGINE=InnoDB;

-- Lodges table
CREATE TABLE lodges (
    lodge_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    star_rating INT,
    room_types_available VARCHAR(255),
    price_per_night DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_location (country, city),
    INDEX idx_price (price_per_night)
) ENGINE=InnoDB;

-- Package inclusions table
CREATE TABLE package_inclusions (
    inclusion_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    description VARCHAR(255) NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    INDEX idx_package (package_id)
) ENGINE=InnoDB;

-- Package itinerary table
CREATE TABLE package_itinerary (
    itinerary_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    day_number INT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    INDEX idx_package_day (package_id, day_number)
) ENGINE=InnoDB;

-- Package guides mapping table
CREATE TABLE package_guides (
    package_guide_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    guide_id INT NOT NULL,
    days_working VARCHAR(255) NOT NULL COMMENT 'Comma-separated list of day numbers',
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (guide_id) REFERENCES guides(guide_id) ON DELETE CASCADE,
    UNIQUE KEY unique_package_guide (package_id, guide_id),
    INDEX idx_package (package_id),
    INDEX idx_guide (guide_id)
) ENGINE=InnoDB;

-- Package lodges mapping table
CREATE TABLE package_lodges (
    package_lodge_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    lodge_id INT NOT NULL,
    nights_staying INT NOT NULL COMMENT 'Number of nights staying at this lodge',
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (lodge_id) REFERENCES lodges(lodge_id) ON DELETE CASCADE,
    INDEX idx_package (package_id),
    INDEX idx_lodge (lodge_id)
) ENGINE=InnoDB;

-- Bookings table
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    package_id INT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    departure_date DATE NOT NULL,
    return_date DATE NOT NULL,
    number_of_people INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('pending', 'paid', 'refunded', 'cancelled') DEFAULT 'pending',
    booking_status ENUM('confirmed', 'waiting', 'cancelled') DEFAULT 'confirmed',
    special_requests TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    INDEX idx_customer (customer_id),
    INDEX idx_package (package_id),
    INDEX idx_dates (departure_date, return_date),
    INDEX idx_status (payment_status, booking_status)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'debit_card', 'bank_transfer', 'paypal', 'other') NOT NULL,
    transaction_id VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'refunded') NOT NULL,
    notes TEXT,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE,
    INDEX idx_booking (booking_id),
    INDEX idx_status (status),
    INDEX idx_transaction (transaction_id)
) ENGINE=InnoDB;

-- Customer reviews table
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    package_id INT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    INDEX idx_customer (customer_id),
    INDEX idx_package (package_id),
    INDEX idx_rating (rating)
) ENGINE=InnoDB;

-- Create views for common queries

-- View for active packages with details
CREATE VIEW active_packages_view AS
SELECT 
    p.package_id,
    p.name,
    p.description,
    p.destination_country,
    p.destination_city,
    p.duration_days,
    p.price,
    p.start_date,
    p.end_date,
    GROUP_CONCAT(DISTINCT i.description SEPARATOR '; ') AS inclusions,
    COUNT(DISTINCT r.review_id) AS review_count,
    IFNULL(AVG(r.rating), 0) AS average_rating
FROM 
    packages p
LEFT JOIN 
    package_inclusions i ON p.package_id = i.package_id
LEFT JOIN 
    reviews r ON p.package_id = r.package_id
WHERE 
    p.is_active = TRUE
GROUP BY 
    p.package_id;

-- View for customer bookings with package details
CREATE VIEW customer_bookings_view AS
SELECT 
    b.booking_id,
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email AS customer_email,
    c.phone AS customer_phone,
    p.package_id,
    p.name AS package_name,
    b.booking_date,
    b.departure_date,
    b.return_date,
    b.number_of_people,
    b.total_price,
    b.payment_status,
    b.booking_status,
    SUM(IF(pm.status = 'completed', pm.amount, 0)) AS amount_paid
FROM 
    bookings b
JOIN 
    customers c ON b.customer_id = c.customer_id
JOIN 
    packages p ON b.package_id = p.package_id
LEFT JOIN 
    payments pm ON b.booking_id = pm.booking_id
GROUP BY 
    b.booking_id;
```
