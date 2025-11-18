"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.app.pavonal.com
Prompt: Provide an example of a database schema for storing user credentials and account details, inspired by Pavonal's account management features.
Generated: DETERMINISTIC_43096a93ee2cfc5e
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Storing User Credentials and Account Details

-- Table to store user credentials
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for login
    PasswordHash VARCHAR(255) NOT NULL,    -- Securely hashed password
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for correspondence
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store account details
CREATE TABLE UserDetails (
    UserDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for account details
    UserID INT NOT NULL,                         -- Foreign key referencing Users.UserID
    FirstName VARCHAR(50),                       -- User's first name
    LastName VARCHAR(50),                        -- User's last name
    DateOfBirth DATE,                            -- Date of birth
    PhoneNumber VARCHAR(15),                     -- Contact phone number
    Address TEXT,                                -- Address information
    ProfilePictureURL VARCHAR(255),              -- URL to the user's profile picture
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of details creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    CONSTRAINT FK_User FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Table to store login attempts and security logs
CREATE TABLE LoginHistory (
    LoginID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for login history
    UserID INT NOT NULL,                         -- Foreign key referencing Users.UserID
    LoginTimestamp DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the login attempt
    IPAddress VARCHAR(45),                       -- IP address used during login
    Status ENUM('Success', 'Failure') NOT NULL,  -- Status of the login attempt
    FailureReason VARCHAR(255),                  -- Reason for failure (if applicable)
    CONSTRAINT FK_LoginUser FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

-- Indexes for faster search and operations
CREATE INDEX IDX_User_Username ON Users (Username);
CREATE INDEX IDX_User_Email ON Users (Email);
CREATE INDEX IDX_Login_UserID ON LoginHistory (UserID);
```

This schema ensures security, scalability, and maintainability for managing user credentials and account details.
