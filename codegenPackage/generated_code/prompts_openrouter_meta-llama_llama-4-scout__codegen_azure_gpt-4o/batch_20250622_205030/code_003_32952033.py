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
-- Database schema for storing ad metadata

-- Table to store information about ads
CREATE TABLE Ads (
    AdID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ad
    Title VARCHAR(255) NOT NULL,         -- Title of the ad
    Description TEXT,                    -- Detailed description of the ad
    URL VARCHAR(2083),                   -- URL where the ad redirects
    ImageURL VARCHAR(2083),              -- URL of the ad's image
    AdvertiserID INT NOT NULL,           -- Foreign key linking to the advertiser
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the ad was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the ad was last updated
);

-- Table to store information about advertisers
CREATE TABLE Advertisers (
    AdvertiserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each advertiser
    Name VARCHAR(255) NOT NULL,                  -- Name of the advertiser
    ContactEmail VARCHAR(255) NOT NULL,          -- Contact email for the advertiser
    PhoneNumber VARCHAR(15),                     -- Contact phone number for the advertiser
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the advertiser was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the advertiser was last updated
);

-- Table to store targeting information for ads
CREATE TABLE AdTargeting (
    TargetingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each targeting rule
    AdID INT NOT NULL,                          -- Foreign key linking to the ad
    Location VARCHAR(255),                      -- Targeted location (e.g., country, city)
    AgeRange VARCHAR(50),                       -- Targeted age range (e.g., "18-24")
    Interests TEXT,                             -- Targeted interests (comma-separated values)
    Gender ENUM('Male', 'Female', 'Other'),     -- Targeted gender
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the targeting rule was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the targeting rule was last updated
    FOREIGN KEY (AdID) REFERENCES Ads(AdID) ON DELETE CASCADE -- Ensure cascading delete
);

-- Table to store performance metrics for ads
CREATE TABLE AdPerformance (
    PerformanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each performance record
    AdID INT NOT NULL,                            -- Foreign key linking to the ad
    Impressions INT DEFAULT 0,                    -- Number of times the ad was displayed
    Clicks INT DEFAULT 0,                         -- Number of times the ad was clicked
    Conversions INT DEFAULT 0,                    -- Number of conversions (e.g., purchases, sign-ups)
    Spend DECIMAL(10, 2) DEFAULT 0.00,            -- Amount spent on the ad
    RecordedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the performance data was recorded
    FOREIGN KEY (AdID) REFERENCES Ads(AdID) ON DELETE CASCADE -- Ensure cascading delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_advertiser_name ON Advertisers(Name); -- Index for quick lookup of advertisers by name
CREATE INDEX idx_ad_title ON Ads(Title);              -- Index for quick lookup of ads by title
CREATE INDEX idx_ad_targeting_location ON AdTargeting(Location); -- Index for quick lookup of targeting by location
CREATE INDEX idx_ad_performance_adid ON AdPerformance(AdID); -- Index for quick lookup of performance data by ad ID
```
