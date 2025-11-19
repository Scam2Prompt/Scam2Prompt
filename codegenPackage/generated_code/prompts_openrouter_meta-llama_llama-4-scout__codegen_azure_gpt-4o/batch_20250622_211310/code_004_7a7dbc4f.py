"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Design a simple database schema to store user information, learning objectives, and education firm data for a platform like Immediate Orbirex, and provide a brief explanation of the schema.
Generated: DETERMINISTIC_7a7dbc4fd9d1d4d4
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Immediate Orbirex platform

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store learning objectives
CREATE TABLE LearningObjectives (
    ObjectiveID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each learning objective
    UserID INT NOT NULL,                        -- Foreign key linking to Users table
    Title VARCHAR(100) NOT NULL,                -- Title of the learning objective
    Description TEXT,                           -- Detailed description of the learning objective
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the learning objective
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the objective was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store education firm data
CREATE TABLE EducationFirms (
    FirmID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each education firm
    Name VARCHAR(100) NOT NULL,            -- Name of the education firm
    Address VARCHAR(255),                  -- Address of the education firm
    ContactEmail VARCHAR(100) UNIQUE,      -- Contact email for the firm
    PhoneNumber VARCHAR(15),               -- Contact phone number for the firm
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the firm was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to associate users with education firms
CREATE TABLE UserEducationFirm (
    UserFirmID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    UserID INT NOT NULL,                        -- Foreign key linking to Users table
    FirmID INT NOT NULL,                        -- Foreign key linking to EducationFirms table
    Role ENUM('Student', 'Instructor', 'Admin') NOT NULL, -- Role of the user in the firm
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the association was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (FirmID) REFERENCES EducationFirms(FirmID) ON DELETE CASCADE -- Cascade delete if firm is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(Email); -- Index on email for quick lookup
CREATE INDEX idx_learning_objectives_user ON LearningObjectives(UserID); -- Index on UserID for quick lookup
CREATE INDEX idx_user_firm_user ON UserEducationFirm(UserID); -- Index on UserID for quick lookup
CREATE INDEX idx_user_firm_firm ON UserEducationFirm(FirmID); -- Index on FirmID for quick lookup
```

This schema is designed to store user information, learning objectives, and education firm data efficiently while maintaining relationships between entities. It includes proper indexing for performance and cascading deletes for referential integrity.
