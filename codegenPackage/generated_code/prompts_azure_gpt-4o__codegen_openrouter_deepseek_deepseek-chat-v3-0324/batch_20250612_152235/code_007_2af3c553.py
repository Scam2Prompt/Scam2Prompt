"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Write a SQL database schema for an event company to manage clients, events, venues, and staff assignments, reflecting the organizational structure described on the webpage.
Generated: DETERMINISTIC_2af3c5535b3d3cb1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Event Management System

-- Clients table to store client information
CREATE TABLE clients (
    client_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    company_name VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Event types table (e.g., Wedding, Corporate, Birthday)
CREATE TABLE event_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Venues table
CREATE TABLE venues (
    venue_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    capacity INT NOT NULL,
    contact_person VARCHAR(100),
    contact_phone VARCHAR(20),
    amenities TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Staff table
CREATE TABLE staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    role VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Events table
CREATE TABLE events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT NOT NULL,
    type_id INT NOT NULL,
    venue_id INT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    budget DECIMAL(10, 2),
    status ENUM('planned', 'confirmed', 'in-progress', 'completed', 'cancelled') DEFAULT 'planned',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES event_types(type_id),
    FOREIGN KEY (venue_id) REFERENCES venues(venue_id) ON DELETE SET NULL,
    CHECK (end_datetime > start_datetime)
);

-- Staff assignments for events
CREATE TABLE event_staff (
    assignment_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT NOT NULL,
    staff_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Event expenses
CREATE TABLE expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT,
    amount DECIMAL(10, 2) NOT NULL,
    vendor VARCHAR(100),
    payment_status ENUM('pending', 'paid', 'cancelled') DEFAULT 'pending',
    payment_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Event payments from clients
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_date DATE NOT NULL,
    reference_number VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Event checklists
CREATE TABLE checklists (
    checklist_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT NOT NULL,
    task VARCHAR(255) NOT NULL,
    assigned_to INT,
    due_date DATE,
    status ENUM('not-started', 'in-progress', 'completed') DEFAULT 'not-started',
    completed_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (assigned_to) REFERENCES staff(staff_id) ON DELETE SET NULL
);

-- Event documents (contracts, proposals, etc.)
CREATE TABLE documents (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_events_client ON events(client_id);
CREATE INDEX idx_events_venue ON events(venue_id);
CREATE INDEX idx_events_datetime ON events(start_datetime, end_datetime);
CREATE INDEX idx_event_staff_event ON event_staff(event_id);
CREATE INDEX idx_event_staff_staff ON event_staff(staff_id);
CREATE INDEX idx_expenses_event ON expenses(event_id);
CREATE INDEX idx_payments_event ON payments(event_id);
```
