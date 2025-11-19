"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: "Design a database schema to store information about YSC's products, including their certifications, quality control measures, and applications, and provide a code example in SQL."
Generated: DETERMINISTIC_5a9546bc75aed84c
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for YSC products management system

-- Create database
CREATE DATABASE IF NOT EXISTS ysc_products;
USE ysc_products;

-- Products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_price CHECK (unit_price >= 0),
    CONSTRAINT chk_quantity CHECK (stock_quantity >= 0)
) ENGINE=InnoDB;

-- Certifications table
CREATE TABLE IF NOT EXISTS certifications (
    certification_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    issuing_authority VARCHAR(100) NOT NULL,
    description TEXT,
    validity_period_months INT
) ENGINE=InnoDB;

-- Product certifications junction table
CREATE TABLE IF NOT EXISTS product_certifications (
    product_id INT NOT NULL,
    certification_id INT NOT NULL,
    certification_date DATE NOT NULL,
    expiry_date DATE,
    PRIMARY KEY (product_id, certification_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (certification_id) REFERENCES certifications(certification_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Quality control measures table
CREATE TABLE IF NOT EXISTS quality_controls (
    control_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    standard VARCHAR(50) NOT NULL,
    frequency VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Product quality controls junction table
CREATE TABLE IF NOT EXISTS product_quality_controls (
    product_id INT NOT NULL,
    control_id INT NOT NULL,
    last_check_date DATE,
    next_check_date DATE,
    status ENUM('Pass', 'Fail', 'Pending') DEFAULT 'Pending',
    notes TEXT,
    PRIMARY KEY (product_id, control_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (control_id) REFERENCES quality_controls(control_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Applications table
CREATE TABLE IF NOT EXISTS applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    industry VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- Product applications junction table
CREATE TABLE IF NOT EXISTS product_applications (
    product_id INT NOT NULL,
    application_id INT NOT NULL,
    suitability_rating INT CHECK (suitability_rating BETWEEN 1 AND 5),
    notes TEXT,
    PRIMARY KEY (product_id, application_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (application_id) REFERENCES applications(application_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Example data insertion
INSERT INTO products (name, description, category, unit_price, stock_quantity) 
VALUES 
('YSC-100', 'High-performance industrial adhesive', 'Adhesives', 45.99, 500),
('YSC-200', 'Food-grade lubricant', 'Lubricants', 32.50, 300);

INSERT INTO certifications (name, issuing_authority, description, validity_period_months)
VALUES 
('ISO 9001', 'International Organization for Standardization', 'Quality management system', 36),
('FDA Approved', 'Food and Drug Administration', 'Safe for food contact applications', 24);

INSERT INTO product_certifications (product_id, certification_id, certification_date, expiry_date)
VALUES 
(1, 1, '2022-01-15', '2025-01-15'),
(2, 1, '2022-03-10', '2025-03-10'),
(2, 2, '2022-04-05', '2024-04-05');

INSERT INTO quality_controls (name, description, standard, frequency)
VALUES 
('Viscosity Test', 'Measures product viscosity at specified temperature', 'ASTM D2196', 'Monthly'),
('Purity Test', 'Checks for contaminants and impurities', 'ISO 8573', 'Quarterly');

INSERT INTO product_quality_controls (product_id, control_id, last_check_date, next_check_date, status)
VALUES 
(1, 1, '2023-05-15', '2023-06-15', 'Pass'),
(2, 2, '2023-04-20', '2023-07-20', 'Pass');

INSERT INTO applications (name, description, industry)
VALUES 
('Automotive Assembly', 'Used in vehicle manufacturing processes', 'Automotive'),
('Food Processing', 'Applications in food production equipment', 'Food Industry');

INSERT INTO product_applications (product_id, application_id, suitability_rating, notes)
VALUES 
(1, 1, 5, 'Excellent bonding for metal parts'),
(2, 2, 4, 'Safe for incidental food contact');
```
