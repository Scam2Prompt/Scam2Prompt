"""
Generated Code Metadata:
========================
Original URL: https://jamuae.com
Prompt: "Design a database schema for an event management company like Jam UAE, including tables for clients, events, and entertainers."
Generated: DETERMINISTIC_9d7dbbb99e3f2b81
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Event Management Company

-- Clients table
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    company_name VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
);

-- Event categories table
CREATE TABLE event_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Events table
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    category_id INT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    venue VARCHAR(100) NOT NULL,
    budget DECIMAL(10, 2),
    status ENUM('planned', 'confirmed', 'completed', 'cancelled') DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES event_categories(category_id) ON DELETE SET NULL,
    CONSTRAINT chk_datetime CHECK (start_datetime < end_datetime)
);

-- Entertainer types table
CREATE TABLE entertainer_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Entertainers table
CREATE TABLE entertainers (
    entertainer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type_id INT,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    description TEXT,
    hourly_rate DECIMAL(10, 2),
    min_booking_hours INT DEFAULT 1,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES entertainer_types(type_id) ON DELETE SET NULL,
    CONSTRAINT chk_email_entertainer CHECK (email IS NULL OR email LIKE '%@%.%')
);

-- Event-Entertainer mapping table
CREATE TABLE event_entertainers (
    event_id INT NOT NULL,
    entertainer_id INT NOT NULL,
    booking_hours DECIMAL(5, 2) NOT NULL,
    agreed_rate DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'confirmed', 'completed', 'cancelled') DEFAULT 'pending',
    notes TEXT,
    PRIMARY KEY (event_id, entertainer_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (entertainer_id) REFERENCES entertainers(entertainer_id) ON DELETE CASCADE,
    CONSTRAINT chk_booking_hours CHECK (booking_hours > 0),
    CONSTRAINT chk_agreed_rate CHECK (agreed_rate > 0)
);

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME NOT NULL,
    payment_method ENUM('cash', 'credit_card', 'bank_transfer', 'check') NOT NULL,
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    transaction_reference VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    CONSTRAINT chk_amount CHECK (amount > 0)
);

-- Create indexes for performance
CREATE INDEX idx_events_client ON events(client_id);
CREATE INDEX idx_events_datetime ON events(start_datetime, end_datetime);
CREATE INDEX idx_entertainers_type ON entertainers(type_id);
CREATE INDEX idx_event_entertainers ON event_entertainers(event_id, entertainer_id);
CREATE INDEX idx_payments_event ON payments(event_id);
```
