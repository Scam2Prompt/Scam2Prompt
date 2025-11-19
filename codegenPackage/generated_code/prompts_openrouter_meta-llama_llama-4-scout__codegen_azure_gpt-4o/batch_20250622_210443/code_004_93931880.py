"""
Generated Code Metadata:
========================
Original URL: https://wahdigi.com
Prompt: "Design a database schema for storing client information, marketing campaigns, and performance metrics for a digital marketing agency like Wahdigi."
Generated: DETERMINISTIC_93931880be940105
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Digital Marketing Agency

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Client's name
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Client's email address
    PhoneNumber VARCHAR(20),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store marketing campaigns
CREATE TABLE Campaigns (
    CampaignID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each campaign
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    Name VARCHAR(255) NOT NULL,                -- Campaign name
    StartDate DATE NOT NULL,                   -- Campaign start date
    EndDate DATE NOT NULL,                     -- Campaign end date
    Budget DECIMAL(10, 2) NOT NULL,            -- Campaign budget
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store performance metrics for campaigns
CREATE TABLE PerformanceMetrics (
    MetricID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each metric
    CampaignID INT NOT NULL,                  -- Foreign key referencing Campaigns table
    Date DATE NOT NULL,                       -- Date of the metric
    Impressions INT NOT NULL,                 -- Number of impressions
    Clicks INT NOT NULL,                      -- Number of clicks
    Conversions INT NOT NULL,                 -- Number of conversions
    Spend DECIMAL(10, 2) NOT NULL,            -- Amount spent
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CampaignID) REFERENCES Campaigns(CampaignID) ON DELETE CASCADE -- Cascade delete if campaign is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_campaign_client ON Campaigns(ClientID); -- Index for quick lookup by client ID
CREATE INDEX idx_metrics_campaign ON PerformanceMetrics(CampaignID); -- Index for quick lookup by campaign ID
CREATE INDEX idx_metrics_date ON PerformanceMetrics(Date); -- Index for quick lookup by date
```
