"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: Generate code for a database schema to manage event details, including social and corporate event types, client preferences, and design specifications.
Generated: DETERMINISTIC_b742922b09a8bbf2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Event Management System

-- Create the database
CREATE DATABASE IF NOT EXISTS event_management;
USE event_management;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    company_name VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Event types table
CREATE TABLE IF NOT EXISTS event_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_corporate BOOLEAN DEFAULT FALSE
) ENGINE=InnoDB;

-- Events table
CREATE TABLE IF NOT EXISTS events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    type_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    location VARCHAR(255) NOT NULL,
    budget DECIMAL(10, 2),
    status ENUM('planned', 'confirmed', 'completed', 'cancelled') DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES event_types(type_id),
    CONSTRAINT chk_datetime CHECK (start_datetime < end_datetime)
) ENGINE=InnoDB;

-- Client preferences table
CREATE TABLE IF NOT EXISTS client_preferences (
    preference_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    preferred_colors VARCHAR(255),
    preferred_themes VARCHAR(255),
    dietary_restrictions TEXT,
    additional_notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Design specifications table
CREATE TABLE IF NOT EXISTS design_specifications (
    design_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    theme VARCHAR(100),
    color_scheme VARCHAR(255),
    layout_plan TEXT,
    decorations TEXT,
    special_requirements TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Vendors table
CREATE TABLE IF NOT EXISTS vendors (
    vendor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    service_type VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20) NOT NULL,
    rating DECIMAL(3, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Event vendors mapping table
CREATE TABLE IF NOT EXISTS event_vendors (
    event_id INT NOT NULL,
    vendor_id INT NOT NULL,
    service_description TEXT,
    cost DECIMAL(10, 2),
    PRIMARY KEY (event_id, vendor_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (vendor_id) REFERENCES vendors(vendor_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Event checklist table
CREATE TABLE IF NOT EXISTS event_checklist (
    checklist_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    task_description VARCHAR(255) NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    due_date DATE,
    assigned_to VARCHAR(100),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Insert default event types
INSERT IGNORE INTO event_types (type_name, description, is_corporate) VALUES
('Wedding', 'Wedding ceremony and reception', FALSE),
('Corporate Meeting', 'Business meetings and conferences', TRUE),
('Birthday Party', 'Personal birthday celebrations', FALSE),
('Product Launch', 'Corporate product launch events', TRUE),
('Charity Gala', 'Fundraising and charity events', FALSE),
('Conference', 'Professional conferences', TRUE),
('Anniversary', 'Personal anniversary celebrations', FALSE),
('Team Building', 'Corporate team building activities', TRUE);
```
