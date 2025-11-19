"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Design a database schema for storing information about tennis club members, their membership types, and contributions, and provide SQL code to create the schema.
Generated: DETERMINISTIC_34c8936850902a5e
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Tennis Club Management System

-- Members table stores core information about club members
CREATE TABLE members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    active_status BOOLEAN NOT NULL DEFAULT TRUE,
    address_line1 VARCHAR(100),
    address_line2 VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
);

-- Membership types table defines different membership levels
CREATE TABLE membership_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    annual_fee DECIMAL(10, 2) NOT NULL,
    court_access_level INT NOT NULL DEFAULT 1,
    max_guests INT NOT NULL DEFAULT 0,
    is_renewable BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Member memberships table tracks current and historical memberships
CREATE TABLE member_memberships (
    membership_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT NOT NULL,
    type_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    auto_renew BOOLEAN NOT NULL DEFAULT FALSE,
    payment_method VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES membership_types(type_id),
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Payments table records all financial transactions
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    membership_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    payment_type ENUM('annual_fee', 'contribution', 'donation', 'other') NOT NULL,
    payment_method ENUM('cash', 'credit_card', 'bank_transfer', 'check', 'online') NOT NULL,
    transaction_reference VARCHAR(100),
    recorded_by INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (membership_id) REFERENCES member_memberships(membership_id) ON DELETE CASCADE
);

-- Court bookings table manages reservations
CREATE TABLE court_bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT NOT NULL,
    court_number INT NOT NULL,
    booking_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    guest_count INT DEFAULT 0,
    booking_status ENUM('confirmed', 'cancelled', 'completed') DEFAULT 'confirmed',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    CONSTRAINT chk_time CHECK (end_time > start_time),
    CONSTRAINT chk_guest_count CHECK (guest_count >= 0)
);

-- Create indexes for performance optimization
CREATE INDEX idx_member_name ON members(last_name, first_name);
CREATE INDEX idx_membership_active ON member_memberships(is_active);
CREATE INDEX idx_membership_dates ON member_memberships(start_date, end_date);
CREATE INDEX idx_booking_dates ON court_bookings(booking_date, start_time);
CREATE INDEX idx_payment_dates ON payments(payment_date);
```
