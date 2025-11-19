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
-- SQL script to create a data model for tracking the impact of child rights advocacy campaigns executed by Child Nepal

-- Drop existing tables if they exist to start fresh
DROP TABLE IF EXISTS Campaigns;
DROP TABLE IF EXISTS Organizations;
DROP TABLE IF EXISTS Advocates;
DROP TABLE IF EXISTS ImpactMetrics;
DROP TABLE IF EXISTS CampaignImpact;

-- Table to store organization details
CREATE TABLE Organizations (
    OrganizationID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255),
    ContactEmail VARCHAR(255),
    ContactPhone VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store campaign details
CREATE TABLE Campaigns (
    CampaignID INT PRIMARY KEY AUTO_INCREMENT,
    OrganizationID INT,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Status ENUM('active', 'completed', 'paused') DEFAULT 'active',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (OrganizationID) REFERENCES Organizations(OrganizationID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to store advocate details
CREATE TABLE Advocates (
    AdvocateID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255),
    Phone VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store metrics that quantify the impact of campaigns
CREATE TABLE ImpactMetrics (
    MetricID INT PRIMARY KEY AUTO_INCREMENT,
    CampaignID INT,
    MetricType VARCHAR(255) NOT NULL,
    Value INT NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CampaignID) REFERENCES Campaigns(CampaignID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table to link campaigns to specific advocates and track their contributions
CREATE TABLE CampaignImpact (
    CampaignImpactID INT PRIMARY KEY AUTO_INCREMENT,
    CampaignID INT,
    AdvocateID INT,
    ContributionDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CampaignID) REFERENCES Campaigns(CampaignID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (AdvocateID) REFERENCES Advocates(AdvocateID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Sample Insert Statements (for testing purposes)
-- Insert Organization
INSERT INTO Organizations (Name, Address, ContactEmail, ContactPhone) 
VALUES ('Child Nepal', '123 Child Ave', 'info@childnepal.org', '0123456789');

-- Insert Campaign
INSERT INTO Campaigns (OrganizationID, Title, Description, StartDate, EndDate) 
VALUES (1, 'Child Rights Awareness', 'A campaign to raise awareness about child rights.', '2023-01-01', '2023-12-31');

-- Insert Advocate
INSERT INTO Advocates (Name, Email, Phone) 
VALUES ('John Doe', 'john.doe@example.com', '0987654321');

-- Insert Impact Metric
INSERT INTO ImpactMetrics (CampaignID, MetricType, Value, Description) 
VALUES (1, 'Children Reached', 5000, 'Estimated number of children reached through the campaign.');

-- Insert Campaign Impact
INSERT INTO CampaignImpact (CampaignID, AdvocateID, ContributionDescription) 
VALUES (1, 1, 'Conducted workshops in schools to promote child rights.');

-- Ensure to handle errors while performing operations in production. 
-- Always use transactions where appropriate.
```
