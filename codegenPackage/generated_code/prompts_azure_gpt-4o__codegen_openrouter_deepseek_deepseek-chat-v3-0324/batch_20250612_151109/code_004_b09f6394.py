"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Develop a database schema to manage advertising projects, including details for billboards, banners, and videotrons, based on SIGMA Advertising's catalog.
Generated: DETERMINISTIC_b09f6394ca8e8efb
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SIGMA Advertising project management

-- Create the database
CREATE DATABASE IF NOT EXISTS sigma_advertising;
USE sigma_advertising;

-- Table for storing client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    tax_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (company_name),
    INDEX (email)
) ENGINE=InnoDB;

-- Table for advertising locations
CREATE TABLE IF NOT EXISTS locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'Mexico',
    coordinates POINT,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    SPATIAL INDEX (coordinates),
    INDEX (city),
    INDEX (state)
) ENGINE=InnoDB;

-- Table for advertising media types
CREATE TABLE IF NOT EXISTS media_types (
    media_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for advertising formats
CREATE TABLE IF NOT EXISTS formats (
    format_id INT AUTO_INCREMENT PRIMARY KEY,
    media_type_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    standard_size VARCHAR(50),
    max_duration_seconds INT,
    file_types VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (media_type_id) REFERENCES media_types(media_type_id) ON DELETE CASCADE,
    UNIQUE KEY (media_type_id, name)
) ENGINE=InnoDB;

-- Table for advertising units (billboards, banners, videotrons)
CREATE TABLE IF NOT EXISTS advertising_units (
    unit_id INT AUTO_INCREMENT PRIMARY KEY,
    location_id INT NOT NULL,
    format_id INT NOT NULL,
    code VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    daily_rate DECIMAL(10,2) NOT NULL,
    is_illuminated BOOLEAN NOT NULL DEFAULT FALSE,
    is_digital BOOLEAN NOT NULL DEFAULT FALSE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    FOREIGN KEY (format_id) REFERENCES formats(format_id) ON DELETE CASCADE,
    INDEX (code),
    INDEX (is_active)
) ENGINE=InnoDB;

-- Table for advertising campaigns
CREATE TABLE IF NOT EXISTS campaigns (
    campaign_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    budget DECIMAL(12,2) NOT NULL,
    status ENUM('planned', 'active', 'paused', 'completed', 'cancelled') NOT NULL DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX (status),
    INDEX (start_date),
    INDEX (end_date),
    CHECK (end_date >= start_date)
) ENGINE=InnoDB;

-- Table for campaign items (specific ads in specific units)
CREATE TABLE IF NOT EXISTS campaign_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    campaign_id INT NOT NULL,
    unit_id INT NOT NULL,
    creative_name VARCHAR(100) NOT NULL,
    creative_description TEXT,
    creative_file_path VARCHAR(255),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    rotation_schedule VARCHAR(100),
    actual_cost DECIMAL(10,2) NOT NULL,
    status ENUM('planned', 'active', 'paused', 'completed', 'cancelled') NOT NULL DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    FOREIGN KEY (unit_id) REFERENCES advertising_units(unit_id) ON DELETE CASCADE,
    INDEX (status),
    INDEX (start_date),
    INDEX (end_date),
    CHECK (end_date >= start_date)
) ENGINE=InnoDB;

-- Table for invoices
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    campaign_id INT NOT NULL,
    invoice_number VARCHAR(50) NOT NULL UNIQUE,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    tax_amount DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(12,2) NOT NULL,
    status ENUM('draft', 'sent', 'paid', 'overdue', 'cancelled') NOT NULL DEFAULT 'draft',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    INDEX (invoice_number),
    INDEX (status),
    INDEX (due_date),
    CHECK (due_date >= issue_date)
) ENGINE=InnoDB;

-- Table for invoice items
CREATE TABLE IF NOT EXISTS invoice_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_id INT NOT NULL,
    campaign_item_id INT NOT NULL,
    description VARCHAR(255) NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (campaign_item_id) REFERENCES campaign_items(item_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for media assets
CREATE TABLE IF NOT EXISTS media_assets (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    campaign_item_id INT NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    file_size BIGINT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN NOT NULL DEFAULT FALSE,
    approval_date TIMESTAMP NULL,
    notes TEXT,
    FOREIGN KEY (campaign_item_id) REFERENCES campaign_items(item_id) ON DELETE CASCADE,
    INDEX (is_approved)
) ENGINE=InnoDB;

-- Table for maintenance records
CREATE TABLE IF NOT EXISTS maintenance_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    unit_id INT NOT NULL,
    maintenance_date DATE NOT NULL,
    maintenance_type ENUM('routine', 'repair', 'upgrade', 'cleaning') NOT NULL,
    description TEXT NOT NULL,
    cost DECIMAL(10,2),
    performed_by VARCHAR(100),
    next_maintenance_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES advertising_units(unit_id) ON DELETE CASCADE,
    INDEX (maintenance_date),
    INDEX (next_maintenance_date)
) ENGINE=InnoDB;

-- Initial data for media types
INSERT IGNORE INTO media_types (name, description) VALUES
    ('Billboard', 'Large outdoor advertising structure'),
    ('Banner', 'Flexible advertising material'),
    ('Videotron', 'Digital screen for video advertising');

-- Initial data for formats (example data)
INSERT IGNORE INTO formats (media_type_id, name, description, standard_size, max_duration_seconds, file_types) VALUES
    (1, 'Classic', 'Traditional static billboard', '14x48 ft', NULL, 'jpg,png'),
    (1, 'Digital', 'Digital LED billboard', '10x20 ft', 15, 'mp4,jpg,png,gif'),
    (2, 'Street Banner', 'Banners hung across streets', '3x20 ft', NULL, 'jpg,png'),
    (2, 'Building Banner', 'Large banners on buildings', '10x30 ft', NULL, 'jpg,png'),
    (3, 'HD Screen', 'High-definition digital screen', '16:9 ratio', 30, 'mp4,jpg,png,gif'),
    (3, 'Megatron', 'Extra-large digital screen', '32:9 ratio', 60, 'mp4,jpg,png,gif');
```
