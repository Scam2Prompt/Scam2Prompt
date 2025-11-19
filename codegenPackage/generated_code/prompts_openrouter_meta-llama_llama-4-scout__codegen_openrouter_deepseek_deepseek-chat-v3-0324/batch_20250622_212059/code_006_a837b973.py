"""
Generated Code Metadata:
========================
Original URL: https://kidanah.sa
Prompt: Design a database schema to store information about Hajj and Umrah pilgrims, their travel plans, and services provided by companies like Kidana Al Hejaz.
Generated: DETERMINISTIC_a837b9734d316782
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Hajj and Umrah pilgrimage management system

-- Create database
CREATE DATABASE IF NOT EXISTS pilgrimage_management;
USE pilgrimage_management;

-- Table for storing pilgrim information
CREATE TABLE IF NOT EXISTS pilgrims (
    pilgrim_id INT AUTO_INCREMENT PRIMARY KEY,
    national_id VARCHAR(20) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    birth_date DATE NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    passport_number VARCHAR(20) UNIQUE NOT NULL,
    passport_expiry DATE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    address TEXT,
    medical_conditions TEXT,
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_national_id (national_id),
    INDEX idx_passport (passport_number)
) ENGINE=InnoDB;

-- Table for storing pilgrimage types
CREATE TABLE IF NOT EXISTS pilgrimage_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    duration_days INT NOT NULL,
    season_start_month TINYINT,
    season_end_month TINYINT
) ENGINE=InnoDB;

-- Table for storing travel packages
CREATE TABLE IF NOT EXISTS travel_packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    pilgrimage_type_id INT NOT NULL,
    duration_days INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'SAR',
    available_seats INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (pilgrimage_type_id) REFERENCES pilgrimage_types(type_id),
    INDEX idx_pilgrimage_type (pilgrimage_type_id),
    INDEX idx_dates (start_date, end_date)
) ENGINE=InnoDB;

-- Table for storing service providers (companies like Kidana Al Hejaz)
CREATE TABLE IF NOT EXISTS service_providers (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    contact_person VARCHAR(100),
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    address TEXT,
    services_offered TEXT,
    rating DECIMAL(3, 2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing pilgrim bookings
CREATE TABLE IF NOT EXISTS pilgrim_bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    pilgrim_id INT NOT NULL,
    package_id INT NOT NULL,
    booking_date DATE NOT NULL,
    booking_status ENUM('Pending', 'Confirmed', 'Cancelled', 'Completed') DEFAULT 'Pending',
    payment_status ENUM('Pending', 'Partial', 'Paid', 'Refunded') DEFAULT 'Pending',
    total_amount DECIMAL(10, 2) NOT NULL,
    amount_paid DECIMAL(10, 2) DEFAULT 0,
    payment_method VARCHAR(50),
    transaction_id VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (pilgrim_id) REFERENCES pilgrims(pilgrim_id),
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id),
    INDEX idx_pilgrim (pilgrim_id),
    INDEX idx_package (package_id),
    INDEX idx_status (booking_status, payment_status)
) ENGINE=InnoDB;

-- Table for storing accommodation details
CREATE TABLE IF NOT EXISTS accommodations (
    accommodation_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    provider_id INT NOT NULL,
    location VARCHAR(100) NOT NULL,
    type ENUM('Hotel', 'Apartment', 'Camp', 'Other') NOT NULL,
    capacity INT NOT NULL,
    rating DECIMAL(3, 2),
    amenities TEXT,
    price_per_night DECIMAL(10, 2),
    currency VARCHAR(3) DEFAULT 'SAR',
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id),
    INDEX idx_provider (provider_id)
) ENGINE=InnoDB;

-- Table for storing transportation details
CREATE TABLE IF NOT EXISTS transportation (
    transport_id INT AUTO_INCREMENT PRIMARY KEY,
    provider_id INT NOT NULL,
    type ENUM('Bus', 'Plane', 'Train', 'Other') NOT NULL,
    capacity INT NOT NULL,
    description TEXT,
    price_per_trip DECIMAL(10, 2),
    currency VARCHAR(3) DEFAULT 'SAR',
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id),
    INDEX idx_provider (provider_id)
) ENGINE=InnoDB;

-- Table for storing package accommodations
CREATE TABLE IF NOT EXISTS package_accommodations (
    package_id INT NOT NULL,
    accommodation_id INT NOT NULL,
    nights INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    PRIMARY KEY (package_id, accommodation_id),
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id),
    FOREIGN KEY (accommodation_id) REFERENCES accommodations(accommodation_id)
) ENGINE=InnoDB;

-- Table for storing package transportation
CREATE TABLE IF NOT EXISTS package_transportation (
    package_id INT NOT NULL,
    transport_id INT NOT NULL,
    trip_date DATE NOT NULL,
    departure_location VARCHAR(100) NOT NULL,
    arrival_location VARCHAR(100) NOT NULL,
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    PRIMARY KEY (package_id, transport_id, trip_date),
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id),
    FOREIGN KEY (transport_id) REFERENCES transportation(transport_id)
) ENGINE=InnoDB;

-- Table for storing additional services
CREATE TABLE IF NOT EXISTS additional_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    provider_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'SAR',
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id),
    INDEX idx_provider (provider_id)
) ENGINE=InnoDB;

-- Table for storing pilgrim services
CREATE TABLE IF NOT EXISTS pilgrim_services (
    service_booking_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    service_id INT NOT NULL,
    quantity INT DEFAULT 1,
    total_price DECIMAL(10, 2) NOT NULL,
    service_date DATE,
    notes TEXT,
    FOREIGN KEY (booking_id) REFERENCES pilgrim_bookings(booking_id),
    FOREIGN KEY (service_id) REFERENCES additional_services(service_id),
    INDEX idx_booking (booking_id)
) ENGINE=InnoDB;

-- Table for storing documents
CREATE TABLE IF NOT EXISTS pilgrim_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    pilgrim_id INT NOT NULL,
    document_type ENUM('Passport', 'Visa', 'Vaccination', 'Other') NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_name VARCHAR(100) NOT NULL,
    expiry_date DATE,
    is_verified BOOLEAN DEFAULT FALSE,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    verified_at TIMESTAMP NULL,
    notes TEXT,
    FOREIGN KEY (pilgrim_id) REFERENCES pilgrims(pilgrim_id),
    INDEX idx_pilgrim (pilgrim_id)
) ENGINE=InnoDB;

-- Table for storing user accounts (system users)
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    role ENUM('Admin', 'Manager', 'Agent', 'Staff') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing system logs
CREATE TABLE IF NOT EXISTS system_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50),
    record_id INT,
    old_values TEXT,
    new_values TEXT,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    INDEX idx_action (action),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB;

-- Insert default pilgrimage types
INSERT
