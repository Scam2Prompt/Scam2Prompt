"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Design a database schema to store and manage educational resources and activities for children, inspired by the "Vivir es Convivir" program's approach to teaching values.
Generated: DETERMINISTIC_b2348565ff64e1d8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Educational Resources and Activities Management
-- Inspired by the "Vivir es Convivir" program's approach to teaching values

-- Create a table to store information about values being taught
CREATE TABLE Values (
    ValueID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each value
    Name VARCHAR(100) NOT NULL,             -- Name of the value (e.g., Respect, Empathy)
    Description TEXT NOT NULL,              -- Detailed description of the value
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store educational resources
CREATE TABLE Resources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resource
    Title VARCHAR(255) NOT NULL,               -- Title of the resource
    Description TEXT NOT NULL,                 -- Detailed description of the resource
    URL VARCHAR(2083),                         -- Link to the resource (e.g., PDF, video)
    Type ENUM('Video', 'Document', 'Activity', 'Other') NOT NULL, -- Type of resource
    ValueID INT,                               -- Foreign key linking to the Values table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ValueID) REFERENCES Values(ValueID) ON DELETE SET NULL -- Handle deletion gracefully
);

-- Create a table to store activities for children
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity
    Name VARCHAR(255) NOT NULL,                -- Name of the activity
    Description TEXT NOT NULL,                 -- Detailed description of the activity
    AgeGroup ENUM('3-5', '6-8', '9-12', '13-15') NOT NULL, -- Target age group
    Duration INT NOT NULL,                     -- Duration of the activity in minutes
    ValueID INT,                               -- Foreign key linking to the Values table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ValueID) REFERENCES Values(ValueID) ON DELETE SET NULL -- Handle deletion gracefully
);

-- Create a table to store feedback or reviews for resources and activities
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    ResourceID INT,                            -- Foreign key linking to the Resources table
    ActivityID INT,                            -- Foreign key linking to the Activities table
    UserName VARCHAR(100) NOT NULL,            -- Name of the user providing feedback
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating (1 to 5 stars)
    Comments TEXT,                             -- Optional comments from the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ResourceID) REFERENCES Resources(ResourceID) ON DELETE CASCADE, -- Cascade deletion
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE -- Cascade deletion
);

-- Create a table to store users (e.g., educators, parents, administrators)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Name VARCHAR(100) NOT NULL,            -- Name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,    -- Email address (must be unique)
    Role ENUM('Educator', 'Parent', 'Admin') NOT NULL, -- Role of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for authentication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to log user interactions with resources and activities
CREATE TABLE UserInteractions (
    InteractionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each interaction
    UserID INT NOT NULL,                          -- Foreign key linking to the Users table
    ResourceID INT,                               -- Foreign key linking to the Resources table
    ActivityID INT,                               -- Foreign key linking to the Activities table
    InteractionType ENUM('Viewed', 'Completed', 'Shared') NOT NULL, -- Type of interaction
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the interaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade deletion
    FOREIGN KEY (ResourceID) REFERENCES Resources(ResourceID) ON DELETE SET NULL, -- Handle deletion gracefully
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE SET NULL -- Handle deletion gracefully
);

-- Ensure the database is optimized for production use
-- Add indexes for faster querying
CREATE INDEX idx_values_name ON Values(Name);
CREATE INDEX idx_resources_title ON Resources(Title);
CREATE INDEX idx_activities_name ON Activities(Name);
CREATE INDEX idx_users_email ON Users(Email);
CREATE INDEX idx_feedback_resource_activity ON Feedback(ResourceID, ActivityID);
CREATE INDEX idx_user_interactions_user ON UserInteractions(UserID);
```
