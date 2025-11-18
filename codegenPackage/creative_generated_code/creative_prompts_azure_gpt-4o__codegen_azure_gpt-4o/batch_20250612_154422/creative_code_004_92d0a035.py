"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Develop a database schema for a "五级三阶制直销软件" (five-level, three-stage direct selling system) that supports membership levels like E, D, C, B, and A, as detailed on JieyaSoft.
Generated: DETERMINISTIC_92d0a0355c0c3e4b
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for a five-level, three-stage direct selling system.

-- Create a table for storing member information
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    Name VARCHAR(100) NOT NULL,              -- Name of the member
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Email address (unique for contact purposes)
    PhoneNumber VARCHAR(15),                 -- Phone number of the member
    Level ENUM('E', 'D', 'C', 'B', 'A') NOT NULL, -- Membership level (E, D, C, B, A)
    SponsorID INT,                           -- ID of the sponsoring member (supports the hierarchy)
    JoinedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the member joined the system
    FOREIGN KEY (SponsorID) REFERENCES Members(MemberID) -- Self-referencing foreign key for sponsor
);

-- Create a table for tracking sales transactions
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sale
    MemberID INT NOT NULL,                 -- ID of the member responsible for the sale
    Amount DECIMAL(10, 2) NOT NULL,        -- Amount of the sale
    Stage TINYINT NOT NULL CHECK (Stage BETWEEN 1 AND 3), -- Stage (1, 2, or 3)
    SaleDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,        -- Date when the sale occurred
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)  -- Foreign key linking to the member
);

-- Create a table for storing commission details
CREATE TABLE Commissions (
    CommissionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each commission record
    MemberID INT NOT NULL,                       -- ID of the member receiving the commission
    SaleID INT NOT NULL,                         -- ID of the related sale
    CommissionAmount DECIMAL(10, 2) NOT NULL,   -- Amount of commission earned
    EarnedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the commission was earned
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID), -- Foreign key linking to the member
    FOREIGN KEY (SaleID) REFERENCES Sales(SaleID)        -- Foreign key linking to the sale
);

-- Create a table for storing level-specific benefits and thresholds
CREATE TABLE MembershipLevels (
    Level ENUM('E', 'D', 'C', 'B', 'A') PRIMARY KEY, -- Membership level
    RequiredSales DECIMAL(10, 2) NOT NULL,          -- Minimum sales required to achieve the level
    Benefits TEXT NOT NULL                          -- Description of benefits for the level
);

-- Create indexes to optimize queries for hierarchical lookups and sales performance
CREATE INDEX idx_sponsor ON Members(SponsorID); -- Index for sponsor relationships
CREATE INDEX idx_member_sales ON Sales(MemberID); -- Index for member sales queries
CREATE INDEX idx_member_commissions ON Commissions(MemberID); -- Index for member commission queries

-- Error handling: Ensure database constraints prevent invalid data
-- Example: Prevent circular sponsorships (handled via application logic)

-- This schema provides a solid foundation for the five-level, three-stage direct selling system.
-- Future enhancements can include additional features such as audit logs, performance metrics, and reporting tables.
```
