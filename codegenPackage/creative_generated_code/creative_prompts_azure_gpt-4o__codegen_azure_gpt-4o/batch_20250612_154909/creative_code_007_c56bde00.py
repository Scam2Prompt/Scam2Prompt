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

-- Create a table for merchants
CREATE TABLE Merchants (
    MerchantID BIGINT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each merchant
    Name VARCHAR(255) NOT NULL,                   -- Merchant's name
    Email VARCHAR(255) UNIQUE NOT NULL,           -- Merchant's email address (must be unique)
    PhoneNumber VARCHAR(20) NOT NULL,             -- Merchant's phone number
    BusinessName VARCHAR(255),                    -- Name of the merchant's business
    RegistrationDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date and time of registration
    Status ENUM('Pending', 'Activated', 'Suspended', 'Deactivated') NOT NULL DEFAULT 'Pending', -- Activation status
    Country VARCHAR(50) NOT NULL,                 -- Country where the merchant operates
    City VARCHAR(50),                             -- City where the merchant operates
    Address TEXT,                                 -- Full address of the merchant
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for merchant activation logs
CREATE TABLE MerchantActivationLogs (
    LogID BIGINT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each log entry
    MerchantID BIGINT NOT NULL,                   -- Reference to the Merchants table
    ActivationDate DATETIME NOT NULL,             -- Activation date and time
    ActivatedBy VARCHAR(255) NOT NULL,            -- Name or ID of the person/system activating the merchant
    Status ENUM('Activated', 'Suspended', 'Deactivated') NOT NULL, -- Activation status
    Reason TEXT,                                  -- Reason for status change
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (MerchantID) REFERENCES Merchants(MerchantID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key to link to Merchants
);

-- Create a table for merchant acquisition campaigns
CREATE TABLE AcquisitionCampaigns (
    CampaignID BIGINT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each campaign
    Name VARCHAR(255) NOT NULL,                   -- Name of the campaign
    Description TEXT,                             -- Detailed description of the campaign
    StartDate DATETIME NOT NULL,                  -- Campaign start date
    EndDate DATETIME,                             -- Campaign end date (NULL if ongoing)
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to track merchant participation in campaigns
CREATE TABLE MerchantCampaigns (
    MerchantCampaignID BIGINT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each record
    MerchantID BIGINT NOT NULL,                           -- Reference to the Merchants table
    CampaignID BIGINT NOT NULL,                           -- Reference to the AcquisitionCampaigns table
    ParticipationDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Date of participation
    FOREIGN KEY (MerchantID) REFERENCES Merchants(MerchantID) ON DELETE CASCADE ON UPDATE CASCADE, -- Foreign key to link to Merchants
    FOREIGN KEY (CampaignID) REFERENCES AcquisitionCampaigns(CampaignID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key to link to AcquisitionCampaigns
);

-- Create an index to optimize queries on MerchantActivationLogs
CREATE INDEX idx_merchant_activation_logs_merchant_id ON MerchantActivationLogs (MerchantID);

-- Create an index to optimize queries on MerchantCampaigns
CREATE INDEX idx_merchant_campaigns_merchant_id_campaign_id ON MerchantCampaigns (MerchantID, CampaignID);

-- Ensure the database uses the InnoDB storage engine for foreign key support
SET default_storage_engine = InnoDB;
```
