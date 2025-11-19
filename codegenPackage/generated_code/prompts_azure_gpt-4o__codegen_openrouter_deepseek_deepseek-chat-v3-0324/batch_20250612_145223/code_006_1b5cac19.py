"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Provide an example of how to structure a database for storing employee registration details and brand-specific offers in a corporate benefits portal.
Generated: DETERMINISTIC_1b5cac19333363e5
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for corporate benefits portal

-- Create database
CREATE DATABASE corporate_benefits_portal;
USE corporate_benefits_portal;

-- Employees table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    department VARCHAR(50) NOT NULL,
    position VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_department (department)
) ENGINE=InnoDB;

-- Brands table
CREATE TABLE brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_name VARCHAR(100) NOT NULL,
    description TEXT,
    website_url VARCHAR(255),
    logo_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_brand_name (brand_name)
) ENGINE=InnoDB;

-- Offers table
CREATE TABLE offers (
    offer_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    discount_details TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE,
    INDEX idx_brand_id (brand_id),
    INDEX idx_dates (start_date, end_date)
) ENGINE=InnoDB;

-- Employee favorites table
CREATE TABLE employee_favorites (
    favorite_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    offer_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (offer_id) REFERENCES offers(offer_id) ON DELETE CASCADE,
    UNIQUE KEY unique_favorite (employee_id, offer_id)
) ENGINE=InnoDB;

-- Offer categories table
CREATE TABLE offer_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_category_name (category_name)
) ENGINE=InnoDB;

-- Offer-category mapping table
CREATE TABLE offer_category_mapping (
    mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    offer_id INT NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (offer_id) REFERENCES offers(offer_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES offer_categories(category_id) ON DELETE CASCADE,
    UNIQUE KEY unique_mapping (offer_id, category_id)
) ENGINE=InnoDB;

-- Employee offer redemptions table
CREATE TABLE employee_redemptions (
    redemption_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    offer_id INT NOT NULL,
    redemption_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    redemption_code VARCHAR(50),
    status ENUM('pending', 'completed', 'expired', 'cancelled') DEFAULT 'pending',
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (offer_id) REFERENCES offers(offer_id) ON DELETE CASCADE,
    INDEX idx_employee_id (employee_id),
    INDEX idx_offer_id (offer_id),
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Audit log table
CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    action_type VARCHAR(20) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT NOT NULL,
    employee_id INT,
    action_details TEXT,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_action_type (action_type),
    INDEX idx_table_name (table_name),
    INDEX idx_action_timestamp (action_timestamp)
) ENGINE=InnoDB;
```
