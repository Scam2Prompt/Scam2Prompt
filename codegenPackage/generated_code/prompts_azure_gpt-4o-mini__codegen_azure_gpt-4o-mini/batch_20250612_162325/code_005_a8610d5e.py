"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Construct a data model in SQL to track the impact of child rights advocacy campaigns as executed by Child Nepal.
Generated: DETERMINISTIC_a8610d5e4533acc8
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a data model for tracking the impact of child rights advocacy campaigns by Child Nepal

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Campaigns;
DROP TABLE IF EXISTS Advocates;
DROP TABLE IF EXISTS Beneficiaries;
DROP TABLE IF EXISTS CampaignImpactReports;

-- Table to store information about advocacy campaigns
CREATE TABLE Campaigns (
    campaign_id SERIAL PRIMARY KEY, -- Unique identifier for each campaign
    campaign_name VARCHAR(255) NOT NULL, -- Name of the campaign
    start_date DATE NOT NULL, -- Start date of the campaign
    end_date DATE NOT NULL, -- End date of the campaign
    description TEXT, -- Description of the campaign
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the campaign was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store information about advocates involved in campaigns
CREATE TABLE Advocates (
    advocate_id SERIAL PRIMARY KEY, -- Unique identifier for each advocate
    name VARCHAR(255) NOT NULL, -- Name of the advocate
    email VARCHAR(255) UNIQUE NOT NULL, -- Email of the advocate
    phone VARCHAR(20), -- Phone number of the advocate
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the advocate was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store information about beneficiaries of the campaigns
CREATE TABLE Beneficiaries (
    beneficiary_id SERIAL PRIMARY KEY, -- Unique identifier for each beneficiary
    name VARCHAR(255) NOT NULL, -- Name of the beneficiary
    age INT CHECK (age >= 0), -- Age of the beneficiary
    gender VARCHAR(10), -- Gender of the beneficiary
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the beneficiary was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to track the impact reports of each campaign
CREATE TABLE CampaignImpactReports (
    report_id SERIAL PRIMARY KEY, -- Unique identifier for each report
    campaign_id INT NOT NULL, -- Foreign key referencing the Campaigns table
    advocate_id INT NOT NULL, -- Foreign key referencing the Advocates table
    beneficiary_id INT NOT NULL, -- Foreign key referencing the Beneficiaries table
    impact_description TEXT, -- Description of the impact observed
    report_date DATE NOT NULL, -- Date of the report
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the report was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (campaign_id) REFERENCES Campaigns(campaign_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (advocate_id) REFERENCES Advocates(advocate_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (beneficiary_id) REFERENCES Beneficiaries(beneficiary_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_campaign_name ON Campaigns(campaign_name);
CREATE INDEX idx_advocate_email ON Advocates(email);
CREATE INDEX idx_beneficiary_name ON Beneficiaries(name);
CREATE INDEX idx_report_date ON CampaignImpactReports(report_date);
```
