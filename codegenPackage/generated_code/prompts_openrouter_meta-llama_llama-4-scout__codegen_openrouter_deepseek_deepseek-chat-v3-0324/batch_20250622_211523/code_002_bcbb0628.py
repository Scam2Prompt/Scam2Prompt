"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: "Generate a sample database schema for storing information about property associations, including contact details, services offered, and client testimonials, inspired by BlocPrest's services."
Generated: DETERMINISTIC_bcbb062811f2d35d
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for property associations management
-- Inspired by BlocPrest's services

-- Create database
CREATE DATABASE IF NOT EXISTS property_associations;
USE property_associations;

-- Table for storing association information
CREATE TABLE IF NOT EXISTS associations (
    association_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    year_founded YEAR,
    logo_url VARCHAR(255),
    website_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_year CHECK (year_founded <= YEAR(CURRENT_DATE))
) ENGINE=InnoDB;

-- Table for storing contact details
CREATE TABLE IF NOT EXISTS contact_details (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    association_id INT NOT NULL,
    address_line1 VARCHAR(100) NOT NULL,
    address_line2 VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50),
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (association_id) REFERENCES associations(association_id) ON DELETE CASCADE,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for storing services offered
CREATE TABLE IF NOT EXISTS services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    association_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (association_id) REFERENCES associations(association_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing service pricing tiers
CREATE TABLE IF NOT EXISTS service_pricing (
    pricing_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    tier_name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'EUR',
    features TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    CONSTRAINT chk_price CHECK (price >= 0)
) ENGINE=InnoDB;

-- Table for storing client testimonials
CREATE TABLE IF NOT EXISTS testimonials (
    testimonial_id INT AUTO_INCREMENT PRIMARY KEY,
    association_id INT NOT NULL,
    client_name VARCHAR(100) NOT NULL,
    client_title VARCHAR(100),
    client_company VARCHAR(100),
    content TEXT NOT NULL,
    rating TINYINT NOT NULL,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (association_id) REFERENCES associations(association_id) ON DELETE CASCADE,
    CONSTRAINT chk_rating CHECK (rating BETWEEN 1 AND 5)
) ENGINE=InnoDB;

-- Table for storing association team members
CREATE TABLE IF NOT EXISTS team_members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    association_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    position VARCHAR(100) NOT NULL,
    bio TEXT,
    email VARCHAR(100),
    phone VARCHAR(20),
    photo_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (association_id) REFERENCES associations(association_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing documents related to associations
CREATE TABLE IF NOT EXISTS documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    association_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    file_url VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size INT NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (association_id) REFERENCES associations(association_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing association events
CREATE TABLE IF NOT EXISTS events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    association_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    location VARCHAR(255),
    is_public BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (association_id) REFERENCES associations(association_id) ON DELETE CASCADE,
    CONSTRAINT chk_datetime CHECK (end_datetime > start_datetime)
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_association_name ON associations(name);
CREATE INDEX idx_service_category ON services(category);
CREATE INDEX idx_testimonial_rating ON testimonials(rating);
CREATE INDEX idx_event_datetime ON events(start_datetime, end_datetime);
```
