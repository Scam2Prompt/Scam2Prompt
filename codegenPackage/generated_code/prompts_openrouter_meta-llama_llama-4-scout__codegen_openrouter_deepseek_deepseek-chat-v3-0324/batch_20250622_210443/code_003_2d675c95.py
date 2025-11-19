"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Design a database schema for storing event-related data, including information about venues, event staff, and audio-visual equipment.
Generated: DETERMINISTIC_2d675c95768b5c8b
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for event management system

-- Create the database
CREATE DATABASE event_management_system;
USE event_management_system;

-- Venue table
CREATE TABLE venues (
    venue_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    capacity INT NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    contact_email VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_capacity CHECK (capacity > 0),
    CONSTRAINT uniq_venue_email UNIQUE (contact_email)
) ENGINE=InnoDB;

-- Event staff table
CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    role VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uniq_staff_email UNIQUE (email)
) ENGINE=InnoDB;

-- Equipment types table
CREATE TABLE equipment_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uniq_equipment_type UNIQUE (name)
) ENGINE=InnoDB;

-- Equipment table
CREATE TABLE equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    type_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    model VARCHAR(100),
    serial_number VARCHAR(100),
    purchase_date DATE,
    purchase_price DECIMAL(10,2),
    current_value DECIMAL(10,2),
    condition_status ENUM('excellent', 'good', 'fair', 'poor', 'needs_repair') NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES equipment_types(type_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Events table
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    venue_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    expected_attendance INT,
    is_private BOOLEAN DEFAULT FALSE,
    status ENUM('planned', 'confirmed', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (venue_id) REFERENCES venues(venue_id) ON DELETE RESTRICT,
    CONSTRAINT chk_event_dates CHECK (end_datetime > start_datetime),
    CONSTRAINT chk_attendance CHECK (expected_attendance IS NULL OR expected_attendance > 0)
) ENGINE=InnoDB;

-- Event staff assignments
CREATE TABLE event_staff (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    staff_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    CONSTRAINT uniq_staff_assignment UNIQUE (event_id, staff_id)
) ENGINE=InnoDB;

-- Event equipment assignments
CREATE TABLE event_equipment (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    equipment_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    notes TEXT,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    returned_at TIMESTAMP NULL,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE RESTRICT,
    CONSTRAINT chk_quantity CHECK (quantity > 0)
) ENGINE=InnoDB;

-- Maintenance records for equipment
CREATE TABLE equipment_maintenance (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_id INT NOT NULL,
    maintenance_date DATE NOT NULL,
    maintenance_type ENUM('routine', 'repair', 'inspection', 'upgrade') NOT NULL,
    description TEXT NOT NULL,
    cost DECIMAL(10,2),
    performed_by VARCHAR(100),
    next_maintenance_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_events_venue ON events(venue_id);
CREATE INDEX idx_events_dates ON events(start_datetime, end_datetime);
CREATE INDEX idx_event_staff_event ON event_staff(event_id);
CREATE INDEX idx_event_staff_staff ON event_staff(staff_id);
CREATE INDEX idx_event_equipment_event ON event_equipment(event_id);
CREATE INDEX idx_event_equipment_equipment ON event_equipment(equipment_id);
CREATE INDEX idx_equipment_type ON equipment(type_id);
CREATE INDEX idx_maintenance_equipment ON equipment_maintenance(equipment_id);
```
