"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Create a SQL database schema for storing information about properties, owners, and renters, as used by Inmobiliaria Nueva Ciudad for their property management services.
Generated: DETERMINISTIC_bbb0e7245f33bf0f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Inmobiliaria Nueva Ciudad
CREATE DATABASE inmobiliaria_nueva_ciudad;

-- Use the created database
USE inmobiliaria_nueva_ciudad;

-- Create table for properties
CREATE TABLE properties (
    property_id INT AUTO_INCREMENT,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    property_type ENUM('residential', 'commercial') NOT NULL,
    num_bedrooms INT,
    num_bathrooms INT,
    square_footage DECIMAL(10, 2),
    rent DECIMAL(10, 2),
    sale_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (property_id)
);

-- Create table for owners
CREATE TABLE owners (
    owner_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (owner_id)
);

-- Create table for renters
CREATE TABLE renters (
    renter_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (renter_id)
);

-- Create table for property owners
CREATE TABLE property_owners (
    property_id INT NOT NULL,
    owner_id INT NOT NULL,
    ownership_percentage DECIMAL(5, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (property_id, owner_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE
);

-- Create table for property renters
CREATE TABLE property_renters (
    property_id INT NOT NULL,
    renter_id INT NOT NULL,
    lease_start_date DATE NOT NULL,
    lease_end_date DATE,
    rent DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (property_id, renter_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (renter_id) REFERENCES renters(renter_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    property_id INT NOT NULL,
    renter_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('cash', 'bank_transfer', 'credit_card') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (renter_id) REFERENCES renters(renter_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_properties_address ON properties (address);
CREATE INDEX idx_owners_email ON owners (email);
CREATE INDEX idx_renters_email ON renters (email);
CREATE INDEX idx_property_owners_property_id ON property_owners (property_id);
CREATE INDEX idx_property_renters_property_id ON property_renters (property_id);
CREATE INDEX idx_payments_property_id ON payments (property_id);
```
