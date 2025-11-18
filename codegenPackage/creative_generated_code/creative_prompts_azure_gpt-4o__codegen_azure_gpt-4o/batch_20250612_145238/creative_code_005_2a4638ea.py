"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Design a database schema to store information about Playland Kenya’s activities, pricing, and operating hours, ensuring it includes fields for activity names, costs, and time slots.
Generated: DETERMINISTIC_2a4638ea75565392
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Playland Kenya

-- Table to store information about activities
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each activity
    ActivityName VARCHAR(100) NOT NULL,         -- Name of the activity
    Description TEXT,                           -- Description of the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last record update
);

-- Table to store pricing information for activities
CREATE TABLE Pricing (
    PricingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each pricing entry
    ActivityID INT NOT NULL,                   -- Foreign key referencing Activities table
    Cost DECIMAL(10, 2) NOT NULL,              -- Cost of the activity (supports up to 2 decimal places)
    Currency VARCHAR(10) DEFAULT 'KES',        -- Currency for the pricing (default to Kenyan Shilling)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last record update
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store operating hours and time slots for activities
CREATE TABLE TimeSlots (
    SlotID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each time slot
    ActivityID INT NOT NULL,                   -- Foreign key referencing Activities table
    DayOfWeek ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL, -- Day of the week
    StartTime TIME NOT NULL,                   -- Start time of the activity
    EndTime TIME NOT NULL,                     -- End time of the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last record update
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexing for performance optimization
CREATE INDEX idx_ActivityID_Pricing ON Pricing(ActivityID);
CREATE INDEX idx_ActivityID_TimeSlots ON TimeSlots(ActivityID);
```
