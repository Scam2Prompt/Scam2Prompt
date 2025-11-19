"""
Generated Code Metadata:
========================
Original URL: https://sala-events.co.il
Prompt: Create a database schema for managing event bookings at DCITY Events, including tables for customer details, event types, menu selections, and technology requirements.
Generated: DETERMINISTIC_35569a6a79c4fd66
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for DCITY Events
CREATE DATABASE dcity_events;

-- Use the database
USE dcity_events;

-- Create table for customer details
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (customer_id)
);

-- Create table for event types
CREATE TABLE event_types (
    event_type_id INT AUTO_INCREMENT,
    event_type_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_type_id)
);

-- Create table for events
CREATE TABLE events (
    event_id INT AUTO_INCREMENT,
    customer_id INT NOT NULL,
    event_type_id INT NOT NULL,
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    event_location VARCHAR(255) NOT NULL,
    guest_count INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (event_type_id) REFERENCES event_types(event_type_id)
);

-- Create table for menu selections
CREATE TABLE menu_selections (
    menu_selection_id INT AUTO_INCREMENT,
    menu_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (menu_selection_id)
);

-- Create table for event menu selections
CREATE TABLE event_menu_selections (
    event_id INT NOT NULL,
    menu_selection_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id, menu_selection_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (menu_selection_id) REFERENCES menu_selections(menu_selection_id)
);

-- Create table for technology requirements
CREATE TABLE technology_requirements (
    technology_requirement_id INT AUTO_INCREMENT,
    technology_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (technology_requirement_id)
);

-- Create table for event technology requirements
CREATE TABLE event_technology_requirements (
    event_id INT NOT NULL,
    technology_requirement_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id, technology_requirement_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (technology_requirement_id) REFERENCES technology_requirements(technology_requirement_id)
);

-- Create table for event bookings
CREATE TABLE event_bookings (
    event_booking_id INT AUTO_INCREMENT,
    event_id INT NOT NULL,
    booking_date DATE NOT NULL,
    booking_status VARCHAR(50) NOT NULL CHECK (booking_status IN ('pending', 'confirmed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_booking_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);

-- Create table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    event_booking_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_status VARCHAR(50) NOT NULL CHECK (payment_status IN ('pending', 'paid', 'refunded')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (event_booking_id) REFERENCES event_bookings(event_booking_id)
);
```
