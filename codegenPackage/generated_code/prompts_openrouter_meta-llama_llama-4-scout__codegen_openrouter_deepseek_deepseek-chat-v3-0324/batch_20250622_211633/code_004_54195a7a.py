"""
Generated Code Metadata:
========================
Original URL: https://usdevent.com
Prompt: "Create a simple event management system database schema using MySQL."
Generated: DETERMINISTIC_54195a7ac30091d6
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- MySQL Event Management System Database Schema
-- This schema includes tables for events, attendees, event registrations, and organizers.

-- Create the database
DROP DATABASE IF EXISTS event_management_system;
CREATE DATABASE event_management_system;
USE event_management_system;

-- Table for storing event organizers
CREATE TABLE organizers (
    organizer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    organization VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_organizer_email (email)
) ENGINE=InnoDB;

-- Table for storing event categories
CREATE TABLE event_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing events
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    organizer_id INT NOT NULL,
    category_id INT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    location VARCHAR(255) NOT NULL,
    max_attendees INT,
    price DECIMAL(10, 2) DEFAULT 0.00,
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (organizer_id) REFERENCES organizers(organizer_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES event_categories(category_id) ON DELETE SET NULL,
    INDEX idx_event_datetime (start_datetime),
    INDEX idx_event_location (location),
    CONSTRAINT chk_event_times CHECK (start_datetime < end_datetime)
) ENGINE=InnoDB;

-- Table for storing attendees
CREATE TABLE attendees (
    attendee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_attendee_email (email),
    INDEX idx_attendee_name (last_name, first_name)
) ENGINE=InnoDB;

-- Table for event registrations
CREATE TABLE registrations (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    attendee_id INT NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_status ENUM('pending', 'paid', 'cancelled', 'refunded') DEFAULT 'pending',
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME,
    notes TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id) ON DELETE CASCADE,
    INDEX idx_registration_event (event_id),
    INDEX idx_registration_attendee (attendee_id),
    UNIQUE KEY unique_event_attendee (event_id, attendee_id)
) ENGINE=InnoDB;

-- Table for storing event tickets
CREATE TABLE tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    quantity_available INT NOT NULL,
    sales_start DATETIME,
    sales_end DATETIME,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    INDEX idx_ticket_event (event_id),
    CONSTRAINT chk_ticket_sales_times CHECK (sales_start < sales_end)
) ENGINE=InnoDB;

-- Table for storing ticket assignments to registrations
CREATE TABLE registration_tickets (
    registration_ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    registration_id INT NOT NULL,
    ticket_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    price_at_purchase DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (registration_id) REFERENCES registrations(registration_id) ON DELETE CASCADE,
    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id) ON DELETE CASCADE,
    INDEX idx_registration_ticket_reg (registration_id),
    INDEX idx_registration_ticket_ticket (ticket_id)
) ENGINE=InnoDB;

-- Table for storing event feedback
CREATE TABLE feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    attendee_id INT NOT NULL,
    rating TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id) ON DELETE CASCADE,
    INDEX idx_feedback_event (event_id),
    INDEX idx_feedback_attendee (attendee_id)
) ENGINE=InnoDB;
```
