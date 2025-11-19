"""
Generated Code Metadata:
========================
Original URL: https://celestia.events
Prompt: Design a database schema for storing information about events, performers, artists, and vendors for a festival like Celestia, and write a brief explanation of the schema.
Generated: DETERMINISTIC_bbd61c9732f18fd4
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Celestia Festival

-- Create the database
CREATE DATABASE IF NOT EXISTS celestia_festival;
USE celestia_festival;

-- Table for storing event information
CREATE TABLE IF NOT EXISTS events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    location VARCHAR(100) NOT NULL,
    capacity INT,
    ticket_price DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (end_datetime > start_datetime)
) ENGINE=InnoDB;

-- Table for storing performer/artist information
CREATE TABLE IF NOT EXISTS performers (
    performer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    bio TEXT,
    performer_type ENUM('Musician', 'Dancer', 'Actor', 'Other') NOT NULL,
    genre VARCHAR(50),
    website_url VARCHAR(255),
    social_media_links JSON,
    is_headliner BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing vendor information
CREATE TABLE IF NOT EXISTS vendors (
    vendor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    vendor_type ENUM('Food', 'Merchandise', 'Art', 'Service', 'Other') NOT NULL,
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    website_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Junction table for events and performers (many-to-many relationship)
CREATE TABLE IF NOT EXISTS event_performers (
    event_id INT NOT NULL,
    performer_id INT NOT NULL,
    performance_order INT,
    performance_duration_minutes INT,
    PRIMARY KEY (event_id, performer_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (performer_id) REFERENCES performers(performer_id) ON DELETE CASCADE,
    INDEX (event_id),
    INDEX (performer_id)
) ENGINE=InnoDB;

-- Junction table for events and vendors (many-to-many relationship)
CREATE TABLE IF NOT EXISTS event_vendors (
    event_id INT NOT NULL,
    vendor_id INT NOT NULL,
    booth_location VARCHAR(50),
    PRIMARY KEY (event_id, vendor_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (vendor_id) REFERENCES vendors(vendor_id) ON DELETE CASCADE,
    INDEX (event_id),
    INDEX (vendor_id)
) ENGINE=InnoDB;

-- Table for storing festival attendees
CREATE TABLE IF NOT EXISTS attendees (
    attendee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_volunteer BOOLEAN DEFAULT FALSE,
    is_vip BOOLEAN DEFAULT FALSE,
    notes TEXT
) ENGINE=InnoDB;

-- Table for storing ticket purchases
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    attendee_id INT NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quantity INT NOT NULL DEFAULT 1,
    total_price DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('Pending', 'Completed', 'Refunded', 'Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id),
    INDEX (event_id),
    INDEX (attendee_id)
) ENGINE=InnoDB;

-- Table for storing schedules
CREATE TABLE IF NOT EXISTS schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    day_number INT NOT NULL,
    date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    INDEX (event_id)
) ENGINE=InnoDB;

-- Table for storing schedule items
CREATE TABLE IF NOT EXISTS schedule_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    schedule_id INT NOT NULL,
    performer_id INT,
    vendor_id INT,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    description TEXT,
    location VARCHAR(100),
    is_important BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (schedule_id) REFERENCES schedules(schedule_id) ON DELETE CASCADE,
    FOREIGN KEY (performer_id) REFERENCES performers(performer_id) ON DELETE SET NULL,
    FOREIGN KEY (vendor_id) REFERENCES vendors(vendor_id) ON DELETE SET NULL,
    CHECK (end_time > start_time),
    INDEX (schedule_id)
) ENGINE=InnoDB;
```
