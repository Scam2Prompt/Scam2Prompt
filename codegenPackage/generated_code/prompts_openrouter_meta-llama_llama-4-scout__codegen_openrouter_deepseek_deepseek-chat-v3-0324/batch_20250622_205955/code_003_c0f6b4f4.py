"""
Generated Code Metadata:
========================
Original URL: https://biamtechintl.com
Prompt: "Design a database schema to store information about dental instruments, including amalgam condensers, anesthesia instruments, and articulating paper forceps."
Generated: DETERMINISTIC_c0f6b4f43911c71a
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for dental instruments management system

-- Create database
CREATE DATABASE dental_instruments_db;
USE dental_instruments_db;

-- Instrument categories table
CREATE TABLE instrument_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uc_category_name UNIQUE (category_name)
) ENGINE=InnoDB;

-- Instruments table
CREATE TABLE instruments (
    instrument_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    instrument_name VARCHAR(100) NOT NULL,
    description TEXT,
    material VARCHAR(100),
    manufacturer VARCHAR(100),
    model_number VARCHAR(50),
    sterilization_method VARCHAR(100),
    price DECIMAL(10, 2),
    quantity_in_stock INT DEFAULT 0,
    minimum_quantity INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES instrument_categories(category_id) ON DELETE CASCADE,
    CONSTRAINT uc_instrument_model UNIQUE (instrument_name, model_number)
) ENGINE=InnoDB;

-- Instrument images table
CREATE TABLE instrument_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    instrument_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Maintenance records table
CREATE TABLE maintenance_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    instrument_id INT NOT NULL,
    maintenance_date DATE NOT NULL,
    maintenance_type ENUM('cleaning', 'sharpening', 'repair', 'replacement') NOT NULL,
    performed_by VARCHAR(100),
    notes TEXT,
    cost DECIMAL(10, 2),
    next_maintenance_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Usage history table
CREATE TABLE usage_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    instrument_id INT NOT NULL,
    used_by VARCHAR(100) NOT NULL,
    procedure_name VARCHAR(100),
    usage_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Insert initial categories
INSERT INTO instrument_categories (category_name, description) VALUES
('Amalgam Condensers', 'Instruments used for condensing amalgam into prepared cavities'),
('Anesthesia Instruments', 'Tools used for administering local anesthesia'),
('Articulating Paper Forceps', 'Instruments used to hold articulating paper for bite registration');

-- Create indexes for performance
CREATE INDEX idx_instruments_category ON instruments(category_id);
CREATE INDEX idx_instruments_name ON instruments(instrument_name);
CREATE INDEX idx_maintenance_instrument ON maintenance_records(instrument_id);
CREATE INDEX idx_usage_instrument ON usage_history(instrument_id);
```
