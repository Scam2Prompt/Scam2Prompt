"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-started.pages.dev
Prompt: Design a database schema for storing Everyworld user activity, including points earned, environmental pledges, and drawing participation.
Generated: DETERMINISTIC_7bf777cb94a187f7
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing Everyworld user activity

-- Create a database for Everyworld
CREATE DATABASE Everyworld;

-- Use the Everyworld database
USE Everyworld;

-- Table to store user information
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for each user
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store points earned by users
CREATE TABLE UserPoints (
    id INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for the points record
    user_id INT NOT NULL,                        -- Reference to the user
    points_earned INT DEFAULT 0,                 -- Points earned by the user
    earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when points were earned
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store environmental pledges made by users
CREATE TABLE EnvironmentalPledges (
    pledge_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each pledge
    user_id INT NOT NULL,                        -- Reference to the user
    pledge_description VARCHAR(255) NOT NULL,   -- Description of the pledge
    pledged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the pledge was made
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store drawing participation by users
CREATE TABLE DrawingParticipation (
    participation_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participation
    user_id INT NOT NULL,                             -- Reference to the user
    drawing_id INT NOT NULL,                          -- Reference to the drawing event
    participated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user participated
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key constraint
    -- Assuming drawings are stored in another table, we will add a foreign key reference for drawing_id
    FOREIGN KEY (drawing_id) REFERENCES Drawings(drawing_id) ON DELETE CASCADE -- Placeholder for drawings table
);

-- Placeholder for the Drawings table (to be defined separately)
CREATE TABLE Drawings (
    drawing_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each drawing
    drawing_title VARCHAR(100) NOT NULL,             -- Title of the drawing event
    drawing_date DATE NOT NULL,                       -- Date of the drawing event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP     -- Record creation timestamp
);

-- Ensure indexing for performance on frequently queried fields
CREATE INDEX idx_user_id ON UserPoints (user_id);
CREATE INDEX idx_user_id_pledge ON EnvironmentalPledges (user_id);
CREATE INDEX idx_user_id_drawing ON DrawingParticipation (user_id);
```
