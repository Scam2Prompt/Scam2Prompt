"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: Design a database schema using SQL for storing customer reviews and service requests for a roofing company, focusing on fields like customer name, service type, and satisfaction rating.
Generated: DETERMINISTIC_bb34b21a6b88fed9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a roofing company's customer reviews and service requests

-- Create the database
CREATE DATABASE roofing_company;
USE roofing_company;

-- Customers table to store customer information
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(2) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_customer_name (last_name, first_name)
) ENGINE=InnoDB;

-- Service types table
CREATE TABLE service_types (
    service_type_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    average_cost DECIMAL(10, 2),
    estimated_duration_hours INT
) ENGINE=InnoDB;

-- Service requests table
CREATE TABLE service_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    service_type_id INT NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    scheduled_date TIMESTAMP NULL,
    completed_date TIMESTAMP NULL,
    status ENUM('pending', 'scheduled', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    priority ENUM('low', 'medium', 'high', 'emergency') DEFAULT 'medium',
    description TEXT,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id),
    INDEX idx_request_status (status),
    INDEX idx_request_dates (request_date, scheduled_date, completed_date)
) ENGINE=InnoDB;

-- Reviews table
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    request_id INT,
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(100),
    comment TEXT,
    would_recommend BOOLEAN,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE SET NULL,
    INDEX idx_review_rating (rating),
    INDEX idx_review_date (review_date)
) ENGINE=InnoDB;

-- Attachments table for service requests and reviews
CREATE TABLE attachments (
    attachment_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT,
    review_id INT,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size INT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (review_id) REFERENCES reviews(review_id) ON DELETE CASCADE,
    CONSTRAINT chk_reference CHECK (request_id IS NOT NULL OR review_id IS NOT NULL)
) ENGINE=InnoDB;

-- Initial data for service types
INSERT INTO service_types (service_name, description, average_cost, estimated_duration_hours)
VALUES 
    ('Roof Inspection', 'Comprehensive roof inspection and assessment', 150.00, 2),
    ('Roof Repair', 'Repair of damaged or leaking roof sections', 500.00, 8),
    ('Roof Replacement', 'Complete roof replacement with new materials', 10000.00, 40),
    ('Emergency Repair', 'Urgent repairs for storm or accident damage', 750.00, 6),
    ('Gutter Installation', 'Installation of new gutter system', 1200.00, 12),
    ('Roof Cleaning', 'Professional cleaning and moss removal', 300.00, 4);
```
