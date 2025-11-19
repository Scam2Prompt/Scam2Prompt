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
-- Create a database for Child Nepal's advocacy campaigns
CREATE DATABASE ChildNepalCampaigns;

-- Switch to the newly created database
USE ChildNepalCampaigns;

-- Table to store information about campaigns
CREATE TABLE Campaigns (
    CampaignID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each campaign
    Name VARCHAR(255) NOT NULL,                -- Name of the campaign
    StartDate DATE NOT NULL,                   -- Start date of the campaign
    EndDate DATE,                              -- End date of the campaign (nullable for ongoing campaigns)
    Description TEXT,                          -- Detailed description of the campaign
    Budget DECIMAL(15, 2),                     -- Budget allocated for the campaign
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the campaign record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store target groups for each campaign
CREATE TABLE TargetGroups (
    TargetGroupID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each target group
    CampaignID INT NOT NULL,                      -- Foreign key linking to the Campaigns table
    GroupName VARCHAR(255) NOT NULL,              -- Name of the target group (e.g., "Children under 12", "Parents")
    Description TEXT,                             -- Description of the target group
    FOREIGN KEY (CampaignID) REFERENCES Campaigns(CampaignID) ON DELETE CASCADE -- Cascade delete if campaign is deleted
);

-- Table to store advocacy activities within campaigns
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity
    CampaignID INT NOT NULL,                   -- Foreign key linking to the Campaigns table
    Name VARCHAR(255) NOT NULL,                -- Name of the activity
    ActivityDate DATE NOT NULL,                -- Date the activity was conducted
    Description TEXT,                          -- Detailed description of the activity
    ImpactScore INT CHECK (ImpactScore BETWEEN 0 AND 100), -- Impact score (0-100) to measure effectiveness
    FOREIGN KEY (CampaignID) REFERENCES Campaigns(CampaignID) ON DELETE CASCADE -- Cascade delete if campaign is deleted
);

-- Table to store feedback from participants
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    ActivityID INT NOT NULL,                   -- Foreign key linking to the Activities table
    ParticipantName VARCHAR(255),              -- Name of the participant providing feedback
    FeedbackText TEXT NOT NULL,                -- Feedback provided by the participant
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating (1-5) provided by the participant
    SubmittedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the feedback was submitted
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE -- Cascade delete if activity is deleted
);

-- Table to store metrics for campaign impact
CREATE TABLE ImpactMetrics (
    MetricID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each metric
    CampaignID INT NOT NULL,                 -- Foreign key linking to the Campaigns table
    MetricName VARCHAR(255) NOT NULL,        -- Name of the metric (e.g., "Children Reached", "Awareness Level")
    MetricValue DECIMAL(15, 2) NOT NULL,     -- Value of the metric
    RecordedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the metric was recorded
    FOREIGN KEY (CampaignID) REFERENCES Campaigns(CampaignID) ON DELETE CASCADE -- Cascade delete if campaign is deleted
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_campaign_start_date ON Campaigns(StartDate);
CREATE INDEX idx_activity_date ON Activities(ActivityDate);
CREATE INDEX idx_feedback_rating ON Feedback(Rating);
```
