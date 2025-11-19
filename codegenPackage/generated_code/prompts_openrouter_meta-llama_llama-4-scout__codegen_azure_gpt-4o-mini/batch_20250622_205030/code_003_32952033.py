"""
Generated Code Metadata:
========================
Original URL: https://adstar.network
Prompt: "Design a simple database schema for storing ad metadata, inspired by AdStar's data needs."
Generated: DETERMINISTIC_3295203316cb8720
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a simple database schema for storing ad metadata

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Ad;
DROP TABLE IF EXISTS Advertiser;
DROP TABLE IF EXISTS Campaign;

-- Table to store Advertiser information
CREATE TABLE Advertiser (
    advertiser_id SERIAL PRIMARY KEY, -- Unique identifier for each advertiser
    name VARCHAR(255) NOT NULL,       -- Name of the advertiser
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Contact email for the advertiser
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the advertiser was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store Campaign information
CREATE TABLE Campaign (
    campaign_id SERIAL PRIMARY KEY, -- Unique identifier for each campaign
    advertiser_id INT NOT NULL,      -- Foreign key referencing the Advertiser
    name VARCHAR(255) NOT NULL,      -- Name of the campaign
    start_date DATE NOT NULL,        -- Start date of the campaign
    end_date DATE NOT NULL,          -- End date of the campaign
    budget DECIMAL(10, 2) NOT NULL,  -- Budget allocated for the campaign
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the campaign was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (advertiser_id) REFERENCES Advertiser(advertiser_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store Ad information
CREATE TABLE Ad (
    ad_id SERIAL PRIMARY KEY,        -- Unique identifier for each ad
    campaign_id INT NOT NULL,        -- Foreign key referencing the Campaign
    title VARCHAR(255) NOT NULL,     -- Title of the ad
    description TEXT NOT NULL,        -- Description of the ad
    image_url VARCHAR(255),           -- URL of the ad image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the ad was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (campaign_id) REFERENCES Campaign(campaign_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_advertiser_name ON Advertiser(name);
CREATE INDEX idx_campaign_name ON Campaign(name);
CREATE INDEX idx_ad_title ON Ad(title);
```
