"""
Generated Code Metadata:
========================
Original URL: https://loyal.credit
Prompt: "Design a database schema for a loyalty program using credit points."
Generated: DETERMINISTIC_620f32acfd73cd89
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a loyalty program using credit points

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email address (must be unique)
    PhoneNumber VARCHAR(15),               -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store loyalty program details
CREATE TABLE LoyaltyPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each loyalty program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the loyalty program
    Description TEXT,                         -- Optional description of the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store user enrollment in loyalty programs
CREATE TABLE UserEnrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    ProgramID INT NOT NULL,                      -- Foreign key referencing LoyaltyPrograms table
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the user enrolled
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (ProgramID) REFERENCES LoyaltyPrograms(ProgramID) ON DELETE CASCADE -- Cascade delete if program is removed
);

-- Table to store credit points transactions
CREATE TABLE CreditTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    ProgramID INT NOT NULL,                       -- Foreign key referencing LoyaltyPrograms table
    Points INT NOT NULL,                          -- Number of points added or deducted
    TransactionType ENUM('Earned', 'Redeemed') NOT NULL, -- Type of transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (ProgramID) REFERENCES LoyaltyPrograms(ProgramID) ON DELETE CASCADE -- Cascade delete if program is removed
);

-- Table to store the current balance of credit points for each user in each program
CREATE TABLE UserPointBalances (
    BalanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each balance record
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    ProgramID INT NOT NULL,                   -- Foreign key referencing LoyaltyPrograms table
    CurrentPoints INT DEFAULT 0,              -- Current balance of points
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (ProgramID) REFERENCES LoyaltyPrograms(ProgramID) ON DELETE CASCADE -- Cascade delete if program is removed
);

-- Indexes for optimization
CREATE INDEX idx_user_email ON Users(Email); -- Index for quick lookup by email
CREATE INDEX idx_user_program ON UserEnrollments(UserID, ProgramID); -- Composite index for user-program lookup
CREATE INDEX idx_transaction_user_program ON CreditTransactions(UserID, ProgramID); -- Composite index for transaction lookup
CREATE INDEX idx_balance_user_program ON UserPointBalances(UserID, ProgramID); -- Composite index for balance lookup
```
