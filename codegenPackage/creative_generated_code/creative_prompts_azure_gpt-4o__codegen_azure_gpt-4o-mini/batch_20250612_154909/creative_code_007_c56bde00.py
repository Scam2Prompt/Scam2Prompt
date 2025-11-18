"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Create a database schema for managing merchant acquisition and activation data, inspired by Paradigm Group's MTN Momo projects in South Africa.
Generated: DETERMINISTIC_c56bde002fbc6d67
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing merchant acquisition and activation data
-- Inspired by Paradigm Group's MTN Momo projects in South Africa

CREATE DATABASE merchant_acquisition;

USE merchant_acquisition;

-- Table to store merchant information
CREATE TABLE merchants (
    merchant_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each merchant
    name VARCHAR(255) NOT NULL,                       -- Merchant's name
    contact_person VARCHAR(255) NULL,                 -- Contact person's name
    email VARCHAR(255) NULL,                           -- Contact email
    phone_number VARCHAR(15) NULL,                     -- Contact phone number
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    status ENUM('active', 'inactive', 'pending') DEFAULT 'pending' -- Status of the merchant
);

-- Table to store merchant activation data
CREATE TABLE merchant_activation (
    activation_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each activation
    merchant_id INT NOT NULL,                          -- Foreign key to merchants table
    activation_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date of activation
    activation_status ENUM('success', 'failed') NOT NULL, -- Status of activation
    failure_reason VARCHAR(255) NULL,                 -- Reason for failure (if applicable)
    FOREIGN KEY (merchant_id) REFERENCES merchants(merchant_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store acquisition campaigns information
CREATE TABLE acquisition_campaigns (
    campaign_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each campaign
    campaign_name VARCHAR(255) NOT NULL,              -- Name of the campaign
    start_date DATE NOT NULL,                          -- Start date of the campaign
    end_date DATE NOT NULL,                            -- End date of the campaign
    budget DECIMAL(10, 2) NOT NULL,                   -- Budget allocated for the campaign
    status ENUM('active', 'inactive') DEFAULT 'active' -- Status of the campaign
);

-- Table to track which merchants are linked to which acquisition campaigns
CREATE TABLE campaign_merchants (
    campaign_merchant_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the link
    campaign_id INT NOT NULL,                           -- Foreign key to acquisition campaigns table
    merchant_id INT NOT NULL,                          -- Foreign key to merchants table
    FOREIGN KEY (campaign_id) REFERENCES acquisition_campaigns(campaign_id) ON DELETE CASCADE, -- Campaign reference
    FOREIGN KEY (merchant_id) REFERENCES merchants(merchant_id) ON DELETE CASCADE -- Merchant reference
);

-- Table to log errors related to merchant activation
CREATE TABLE activation_error_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each error log
    merchant_id INT NOT NULL,                           -- Foreign key to merchants table
    activation_date DATETIME NOT NULL,                  -- Date of the activation attempt
    error_message TEXT NOT NULL,                        -- Description of the error
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- Timestamp of when the log was created
    FOREIGN KEY (merchant_id) REFERENCES merchants(merchant_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for improved performance
CREATE INDEX idx_merchant_status ON merchants(status);
CREATE INDEX idx_activation_status ON merchant_activation(activation_status);
CREATE INDEX idx_campaign_status ON acquisition_campaigns(status);
```
