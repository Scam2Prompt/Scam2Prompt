"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Create a database schema for managing merchant acquisition and activation data, inspired by Paradigm Group's MTN Momo projects in South Africa.
Generated: DETERMINISTIC_c56bde002fbc6d67
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing merchant acquisition and activation data

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS merchants CASCADE;
DROP TABLE IF EXISTS activations CASCADE;
DROP TABLE IF EXISTS acquisition_sources CASCADE;

-- Table to store merchant information
CREATE TABLE merchants (
    merchant_id SERIAL PRIMARY KEY, -- Unique identifier for each merchant
    name VARCHAR(255) NOT NULL, -- Merchant's name
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Merchant's contact email
    phone_number VARCHAR(15) UNIQUE NOT NULL, -- Merchant's contact phone number
    address TEXT NOT NULL, -- Merchant's physical address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store activation data for merchants
CREATE TABLE activations (
    activation_id SERIAL PRIMARY KEY, -- Unique identifier for each activation
    merchant_id INT NOT NULL REFERENCES merchants(merchant_id) ON DELETE CASCADE, -- Foreign key to merchants table
    activation_date TIMESTAMP NOT NULL, -- Date of activation
    status VARCHAR(50) NOT NULL CHECK (status IN ('active', 'inactive', 'pending')), -- Activation status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store acquisition sources for merchants
CREATE TABLE acquisition_sources (
    source_id SERIAL PRIMARY KEY, -- Unique identifier for each acquisition source
    source_name VARCHAR(255) NOT NULL, -- Name of the acquisition source
    description TEXT, -- Description of the acquisition source
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to link merchants with their acquisition sources
CREATE TABLE merchant_acquisition (
    merchant_id INT NOT NULL REFERENCES merchants(merchant_id) ON DELETE CASCADE, -- Foreign key to merchants table
    source_id INT NOT NULL REFERENCES acquisition_sources(source_id) ON DELETE CASCADE, -- Foreign key to acquisition sources table
    acquisition_date TIMESTAMP NOT NULL, -- Date of acquisition
    PRIMARY KEY (merchant_id, source_id) -- Composite primary key
);

-- Indexes for performance optimization
CREATE INDEX idx_merchant_name ON merchants(name);
CREATE INDEX idx_activation_status ON activations(status);
CREATE INDEX idx_acquisition_date ON merchant_acquisition(acquisition_date);

-- Sample data insertion (for testing purposes)
INSERT INTO acquisition_sources (source_name, description) VALUES
('Online Marketing', 'Acquisition through online advertisements'),
('Referral Program', 'Acquisition through referrals from existing merchants');

INSERT INTO merchants (name, contact_email, phone_number, address) VALUES
('Merchant A', 'contact@merchanta.com', '1234567890', '123 Merchant St, City, Country'),
('Merchant B', 'contact@merchantb.com', '0987654321', '456 Merchant Ave, City, Country');

INSERT INTO activations (merchant_id, activation_date, status) VALUES
(1, NOW(), 'active'),
(2, NOW(), 'pending');

INSERT INTO merchant_acquisition (merchant_id, source_id, acquisition_date) VALUES
(1, 1, NOW()),
(2, 2, NOW());
```
