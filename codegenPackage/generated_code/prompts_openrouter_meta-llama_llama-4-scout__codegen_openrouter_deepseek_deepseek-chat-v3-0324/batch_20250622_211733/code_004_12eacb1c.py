"""
Generated Code Metadata:
========================
Original URL: https://terminaltunja.com
Prompt: Create a SQL database schema to store information about the Terminal Tunja's services, including descriptions, schedules, and contact details.
Generated: DETERMINISTIC_12eacb1c41d14d07
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Terminal Tunja Services Database

-- Create the database
CREATE DATABASE TerminalTunjaServices;
USE TerminalTunjaServices;

-- Table for storing service categories
CREATE TABLE ServiceCategories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_category_name UNIQUE (category_name)
) ENGINE=InnoDB;

-- Table for storing service providers
CREATE TABLE ServiceProviders (
    provider_id INT PRIMARY KEY AUTO_INCREMENT,
    provider_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for storing services
CREATE TABLE Services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    category_id INT NOT NULL,
    provider_id INT NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    standard_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES ServiceCategories(category_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES ServiceProviders(provider_id) ON DELETE CASCADE,
    CONSTRAINT uc_service_name_provider UNIQUE (service_name, provider_id)
) ENGINE=InnoDB;

-- Table for storing service schedules
CREATE TABLE ServiceSchedules (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,
    service_id INT NOT NULL,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE,
    CONSTRAINT chk_time CHECK (start_time < end_time)
) ENGINE=InnoDB;

-- Table for storing contact information
CREATE TABLE ContactDetails (
    contact_id INT PRIMARY KEY AUTO_INCREMENT,
    service_id INT NOT NULL,
    contact_type ENUM('Phone', 'Email', 'WhatsApp', 'Office') NOT NULL,
    contact_value VARCHAR(100) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE,
    CONSTRAINT chk_contact_value CHECK (
        (contact_type = 'Email' AND contact_value LIKE '%@%.%') OR
        (contact_type IN ('Phone', 'WhatsApp') AND contact_value REGEXP '^[0-9]+$') OR
        (contact_type = 'Office')
    )
) ENGINE=InnoDB;

-- Table for storing service reviews
CREATE TABLE ServiceReviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    service_id INT NOT NULL,
    reviewer_name VARCHAR(100) NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_service_category ON Services(category_id);
CREATE INDEX idx_service_provider ON Services(provider_id);
CREATE INDEX idx_schedule_service ON ServiceSchedules(service_id);
CREATE INDEX idx_contact_service ON ContactDetails(service_id);
CREATE INDEX idx_review_service ON ServiceReviews(service_id);
```
