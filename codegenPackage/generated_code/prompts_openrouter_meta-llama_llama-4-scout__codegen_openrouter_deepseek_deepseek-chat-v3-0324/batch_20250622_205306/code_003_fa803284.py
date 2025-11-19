"""
Generated Code Metadata:
========================
Original URL: https://michelledoylegoldsmith.com
Prompt: Design a database schema to store information about unique jewelry pieces, including details about gemstones, metals, and certifications like GIA and HRD.
Generated: DETERMINISTIC_fa803284b5af9318
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for jewelry inventory system

-- Create database
CREATE DATABASE jewelry_inventory;
USE jewelry_inventory;

-- Metals table
CREATE TABLE metals (
    metal_id INT AUTO_INCREMENT PRIMARY KEY,
    metal_name VARCHAR(50) NOT NULL,
    purity VARCHAR(20) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (metal_name, purity)
);

-- Gemstone types table
CREATE TABLE gemstone_types (
    gemstone_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    mohs_hardness DECIMAL(3,1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Certification authorities table
CREATE TABLE certification_authorities (
    authority_id INT AUTO_INCREMENT PRIMARY KEY,
    authority_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Gemstones table
CREATE TABLE gemstones (
    gemstone_id INT AUTO_INCREMENT PRIMARY KEY,
    gemstone_type_id INT NOT NULL,
    carat_weight DECIMAL(6,2) NOT NULL,
    color VARCHAR(50),
    clarity VARCHAR(50),
    cut_grade VARCHAR(50),
    origin VARCHAR(100),
    treatment VARCHAR(100),
    is_lab_created BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (gemstone_type_id) REFERENCES gemstone_types(gemstone_type_id)
);

-- Certifications table
CREATE TABLE certifications (
    certification_id INT AUTO_INCREMENT PRIMARY KEY,
    gemstone_id INT NOT NULL,
    authority_id INT NOT NULL,
    certificate_number VARCHAR(100) NOT NULL,
    issue_date DATE,
    report_url VARCHAR(255),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (gemstone_id) REFERENCES gemstones(gemstone_id),
    FOREIGN KEY (authority_id) REFERENCES certification_authorities(authority_id),
    UNIQUE KEY (authority_id, certificate_number)
);

-- Jewelry pieces table
CREATE TABLE jewelry_pieces (
    piece_id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    jewelry_type VARCHAR(50) NOT NULL,
    primary_metal_id INT NOT NULL,
    metal_weight_grams DECIMAL(8,2),
    retail_price DECIMAL(10,2),
    cost_price DECIMAL(10,2),
    date_acquired DATE,
    is_sold BOOLEAN DEFAULT FALSE,
    sold_date DATE,
    sold_price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (primary_metal_id) REFERENCES metals(metal_id)
);

-- Junction table for jewelry pieces and gemstones
CREATE TABLE jewelry_gemstones (
    jewelry_gemstone_id INT AUTO_INCREMENT PRIMARY KEY,
    piece_id INT NOT NULL,
    gemstone_id INT NOT NULL,
    setting_type VARCHAR(50),
    position_description VARCHAR(100),
    is_center_stone BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (piece_id) REFERENCES jewelry_pieces(piece_id),
    FOREIGN KEY (gemstone_id) REFERENCES gemstones(gemstone_id),
    UNIQUE KEY (piece_id, gemstone_id)
);

-- Images table
CREATE TABLE images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    piece_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    caption VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (piece_id) REFERENCES jewelry_pieces(piece_id)
);

-- Create indexes for better performance
CREATE INDEX idx_gemstones_type ON gemstones(gemstone_type_id);
CREATE INDEX idx_certifications_gemstone ON certifications(gemstone_id);
CREATE INDEX idx_jewelry_gemstones_piece ON jewelry_gemstones(piece_id);
CREATE INDEX idx_jewelry_gemstones_gemstone ON jewelry_gemstones(gemstone_id);
CREATE INDEX idx_images_piece ON images(piece_id);
```
