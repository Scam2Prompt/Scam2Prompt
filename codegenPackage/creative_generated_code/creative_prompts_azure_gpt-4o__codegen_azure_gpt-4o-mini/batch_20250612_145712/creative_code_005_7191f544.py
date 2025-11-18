"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: Create a database schema in SQL for storing user credentials and account details for a platform like MicroLab, including fields for username, password, and account recovery options.
Generated: DETERMINISTIC_7191f544181e5d55
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Schema for User Credentials and Account Details

-- Create a table to store user accounts
CREATE TABLE UserAccounts (
    UserID SERIAL PRIMARY KEY,                -- Unique identifier for each user
    Username VARCHAR(50) UNIQUE NOT NULL,    -- Unique username for account login
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    Email VARCHAR(100) UNIQUE NOT NULL,      -- User's email address for recovery
    PhoneNumber VARCHAR(15),                  -- Optional phone number for recovery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    LastLogin TIMESTAMP,                      -- Timestamp of the last login
    IsActive BOOLEAN DEFAULT TRUE,            -- Status of the account (active/inactive)
    CONSTRAINT chk_phone CHECK (PhoneNumber ~ '^\+?[1-9]\d{1,14}$') -- Check for valid phone number format
);

-- Create a table for password recovery options
CREATE TABLE PasswordRecovery (
    RecoveryID SERIAL PRIMARY KEY,            -- Unique identifier for each recovery option
    UserID INT REFERENCES UserAccounts(UserID) ON DELETE CASCADE, -- Link to user account
    RecoveryOptionType VARCHAR(50) NOT NULL,  -- Type of recovery option (e.g., email, phone)
    RecoveryValue VARCHAR(255) NOT NULL,      -- Value of the recovery option (e.g., email address, phone number)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of recovery option creation
    UNIQUE(UserID, RecoveryOptionType)       -- Ensure each user has unique recovery options
);

-- Create an index for faster lookups on the Username field
CREATE INDEX idx_user_username ON UserAccounts(Username);

-- Create an index for faster lookups on the Email field
CREATE INDEX idx_user_email ON UserAccounts(Email);
```
