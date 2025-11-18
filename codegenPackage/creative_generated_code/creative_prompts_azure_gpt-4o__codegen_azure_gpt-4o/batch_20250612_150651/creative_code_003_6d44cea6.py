"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Provide an example of a database schema for tracking charitable grants awarded by the Armourers & Brasiers' Gauntlet Trust, including fields for recipient details, grant purpose, and funding amount.
Generated: DETERMINISTIC_6d44cea6f84fd7c7
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for tracking charitable grants awarded by the Armourers & Brasiers' Gauntlet Trust

-- Table to store information about grant recipients
CREATE TABLE Recipients (
    RecipientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each recipient
    Name VARCHAR(255) NOT NULL,                -- Full name of the recipient
    Email VARCHAR(255) NOT NULL,               -- Email address of the recipient
    PhoneNumber VARCHAR(20),                   -- Phone number of the recipient
    Address TEXT,                              -- Physical address of the recipient
    OrganizationName VARCHAR(255),             -- Name of the organization (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store details about the grants
CREATE TABLE Grants (
    GrantID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each grant
    RecipientID INT NOT NULL,                  -- Foreign key referencing Recipients table
    GrantPurpose TEXT NOT NULL,                -- Purpose or description of the grant
    FundingAmount DECIMAL(10, 2) NOT NULL,     -- Amount of funding awarded
    AwardDate DATE NOT NULL,                   -- Date the grant was awarded
    Notes TEXT,                                -- Additional notes or comments about the grant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (RecipientID) REFERENCES Recipients(RecipientID) 
        ON DELETE CASCADE ON UPDATE CASCADE    -- Ensure integrity between tables
);

-- Indexes for optimized queries
CREATE INDEX idx_recipient_email ON Recipients(Email); -- Index on recipient email for faster lookups
CREATE INDEX idx_grant_recipient ON Grants(RecipientID); -- Index on grant recipient foreign key

-- Example constraints
ALTER TABLE Grants
ADD CONSTRAINT chk_funding_amount CHECK (FundingAmount > 0); -- Ensure funding amounts are positive
```
