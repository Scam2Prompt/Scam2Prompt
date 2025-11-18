"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jasmynetwork.org
Prompt: Create a database schema for storing user-submitted web finds and their associated ratings, inspired by the Stumble! ® app.
Generated: DETERMINISTIC_f3eb5616ed93d7f2
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user-submitted web finds and their associated ratings
-- Inspired by the Stumble!® app

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- User's username
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's unique email address
    PasswordHash VARCHAR(255) NOT NULL,    -- Securely hashed password
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store web finds submitted by users
CREATE TABLE WebFinds (
    FindID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each web find
    UserID INT NOT NULL,                   -- Foreign key to the Users table
    URL VARCHAR(2083) NOT NULL,            -- URL of the web find (maximum length for URLs)
    Title VARCHAR(255) NOT NULL,           -- Title of the web find
    Description TEXT,                      -- Optional description of the web find
    Tags VARCHAR(255),                     -- Comma-separated tags for categorization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of submission
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- If user is deleted, delete their finds
);

-- Table to store ratings for each web find
CREATE TABLE Ratings (
    RatingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each rating
    FindID INT NOT NULL,                     -- Foreign key to the WebFinds table
    UserID INT NOT NULL,                     -- Foreign key to the Users table (who rated)
    RatingValue INT CHECK (RatingValue BETWEEN 1 AND 5), -- Rating value (1 to 5 scale)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of rating submission
    FOREIGN KEY (FindID) REFERENCES WebFinds(FindID) ON DELETE CASCADE, -- If web find is deleted, delete ratings
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- If user is deleted, delete ratings
);
```
