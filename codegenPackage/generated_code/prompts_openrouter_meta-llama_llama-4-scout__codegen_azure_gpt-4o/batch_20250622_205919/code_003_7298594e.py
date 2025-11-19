"""
Generated Code Metadata:
========================
Original URL: https://claim-bits.com
Prompt: "Design a database schema to store user information, ad clicks, and payment records for a platform that pays users for viewing ads and completing tasks."
Generated: DETERMINISTIC_7298594ea6703f90
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a platform that pays users for viewing ads and completing tasks

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store ad information
CREATE TABLE Ads (
    AdID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each ad
    AdTitle VARCHAR(100) NOT NULL,         -- Title of the ad
    AdDescription TEXT,                    -- Description of the ad
    AdURL VARCHAR(255) NOT NULL,           -- URL of the ad
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the ad was created
);

-- Table to store ad clicks by users
CREATE TABLE AdClicks (
    ClickID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each click
    UserID INT NOT NULL,                    -- Foreign key referencing Users table
    AdID INT NOT NULL,                      -- Foreign key referencing Ads table
    ClickedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the ad was clicked
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (AdID) REFERENCES Ads(AdID) ON DELETE CASCADE -- Cascade delete if ad is deleted
);

-- Table to store payment records
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    Amount DECIMAL(10, 2) NOT NULL,           -- Payment amount
    PaymentMethod VARCHAR(50) NOT NULL,       -- Payment method (e.g., PayPal, Bank Transfer)
    PaymentStatus ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the payment record was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store tasks completed by users
CREATE TABLE Tasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each task
    TaskName VARCHAR(100) NOT NULL,          -- Name of the task
    TaskDescription TEXT,                    -- Description of the task
    Reward DECIMAL(10, 2) NOT NULL,          -- Reward amount for completing the task
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the task was created
);

-- Table to store task completions by users
CREATE TABLE TaskCompletions (
    CompletionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each task completion
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    TaskID INT NOT NULL,                         -- Foreign key referencing Tasks table
    CompletedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the task was completed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID) ON DELETE CASCADE -- Cascade delete if task is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users (Email);
CREATE INDEX idx_ad_url ON Ads (AdURL);
CREATE INDEX idx_click_user_ad ON AdClicks (UserID, AdID);
CREATE INDEX idx_payment_user ON Payments (UserID);
CREATE INDEX idx_task_user ON TaskCompletions (UserID, TaskID);
```
