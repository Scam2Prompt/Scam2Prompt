"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Construct a data model in SQL to track the impact of child rights advocacy campaigns as executed by Child Nepal.
Generated: DETERMINISTIC_a8610d5e4533acc8
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a data model for tracking the impact of child rights advocacy campaigns

-- Table to store information about campaigns
CREATE TABLE Campaigns (
    CampaignID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each campaign
    Name VARCHAR(255) NOT NULL,                -- Name of the campaign
    StartDate DATE NOT NULL,                   -- Start date of the campaign
    EndDate DATE,                              -- End date of the campaign (can be NULL if ongoing)
    Description TEXT,                          -- Detailed description of the campaign
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store details about advocacy activities within campaigns
CREATE TABLE Activities (
    ActivityID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each activity
    CampaignID INT NOT NULL,                   -- Foreign key referencing Campaigns table
    Name VARCHAR(255) NOT NULL,                -- Name of the advocacy activity
    ActivityDate DATE NOT NULL,                -- Date when the activity occurred
    Description TEXT,                          -- Detailed description of the activity
    Reach INT,                                 -- Number of people reached by the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (CampaignID) REFERENCES Campaigns (CampaignID) ON DELETE CASCADE -- Cascade delete if the campaign is deleted
);

-- Table to track indicators of impact for each activity
CREATE TABLE ImpactIndicators (
    IndicatorID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each indicator
    ActivityID INT NOT NULL,                    -- Foreign key referencing Activities table
    IndicatorName VARCHAR(255) NOT NULL,        -- Name of the impact indicator (e.g., "Improved attendance rates")
    IndicatorValue DECIMAL(10, 2),              -- Numeric value of the indicator (e.g., percentage or count)
    Description TEXT,                           -- Detailed explanation of the indicator
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ActivityID) REFERENCES Activities (ActivityID) ON DELETE CASCADE -- Cascade delete if the activity is deleted
);

-- Table to store stakeholders involved in campaigns
CREATE TABLE Stakeholders (
    StakeholderID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each stakeholder
    Name VARCHAR(255) NOT NULL,                   -- Name of the stakeholder (e.g., organization or individual)
    ContactInfo VARCHAR(255),                     -- Contact information
    Role VARCHAR(100),                            -- Role in the campaign (e.g., "Sponsor", "Volunteer")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to associate stakeholders with campaigns
CREATE TABLE CampaignStakeholders (
    CampaignID INT NOT NULL,                      -- Foreign key referencing Campaigns table
    StakeholderID INT NOT NULL,                   -- Foreign key referencing Stakeholders table
    PRIMARY KEY (CampaignID, StakeholderID),      -- Composite primary key to ensure unique associations
    FOREIGN KEY (CampaignID) REFERENCES Campaigns (CampaignID) ON DELETE CASCADE, -- Cascade delete if the campaign is deleted
    FOREIGN KEY (StakeholderID) REFERENCES Stakeholders (StakeholderID) ON DELETE CASCADE -- Cascade delete if the stakeholder is deleted
);
```
