"""
Generated Code Metadata:
========================
Original URL: https://immediate-vortex.com
Prompt: Design a basic database schema for storing user information and investment education firm details, inspired by Immediate Vortex's approach to connecting learners with educators.
Generated: DETERMINISTIC_6d02491f31bcbef8
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user information and investment education firm details

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for security
    PhoneNumber VARCHAR(15),              -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store investment education firm details
CREATE TABLE EducationFirms (
    FirmID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each firm
    FirmName VARCHAR(100) NOT NULL,        -- Name of the firm
    Description TEXT,                      -- Description of the firm
    WebsiteURL VARCHAR(255),              -- Firm's website URL
    ContactEmail VARCHAR(100) NOT NULL,   -- Contact email for the firm
    PhoneNumber VARCHAR(15),              -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the firm was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store connections between users and education firms
CREATE TABLE UserFirmConnections (
    ConnectionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each connection
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    FirmID INT NOT NULL,                         -- Foreign key referencing EducationFirms table
    ConnectionStatus ENUM('Pending', 'Active', 'Inactive') DEFAULT 'Pending', -- Status of the connection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the connection was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (FirmID) REFERENCES EducationFirms(FirmID) ON DELETE CASCADE -- Cascade delete if firm is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users (Email); -- Index for quick lookup by email
CREATE INDEX idx_firm_name ON EducationFirms (FirmName); -- Index for quick lookup by firm name
CREATE INDEX idx_connection_user_firm ON UserFirmConnections (UserID, FirmID); -- Composite index for user-firm connections
```
