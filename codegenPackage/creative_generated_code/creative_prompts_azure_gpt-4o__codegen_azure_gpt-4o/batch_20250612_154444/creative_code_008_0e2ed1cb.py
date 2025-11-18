"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bsc-scan.net
Prompt: Write a SQL query to store and retrieve data for BSC Scan's investment plans, including contract duration, profit percentages, and user contributions.
Generated: DETERMINISTIC_0e2ed1cbdfd7b626
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the table to store investment plans
CREATE TABLE InvestmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each plan
    PlanName VARCHAR(255) NOT NULL,                 -- Name of the investment plan
    ContractDuration INT NOT NULL,                  -- Duration of the contract (in days)
    ProfitPercentage DECIMAL(5, 2) NOT NULL,        -- Profit percentage offered by the plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp of when the plan was created
);

-- Create the table to store user contributions
CREATE TABLE UserContributions (
    ContributionID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each contribution
    UserID INT NOT NULL,                            -- ID of the user making the contribution
    PlanID INT NOT NULL,                            -- ID of the associated investment plan
    ContributionAmount DECIMAL(10, 2) NOT NULL,     -- Amount contributed by the user
    ContributionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the contribution
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE CASCADE -- Foreign key linking to InvestmentPlans
);

-- Insert example data into InvestmentPlans
INSERT INTO InvestmentPlans (PlanName, ContractDuration, ProfitPercentage)
VALUES 
('Short-Term Plan', 30, 5.00),
('Medium-Term Plan', 90, 15.00),
('Long-Term Plan', 180, 30.00);

-- Insert example data into UserContributions
INSERT INTO UserContributions (UserID, PlanID, ContributionAmount)
VALUES 
(1, 1, 1000.00),
(2, 2, 500.00),
(1, 3, 2000.00);

-- Query to retrieve all investment plans
SELECT * FROM InvestmentPlans;

-- Query to retrieve all contributions made by a specific user (example UserID = 1)
SELECT 
    UC.ContributionID,
    UC.UserID,
    IP.PlanName,
    UC.ContributionAmount,
    UC.ContributionDate,
    IP.ProfitPercentage
FROM 
    UserContributions UC
JOIN 
    InvestmentPlans IP ON UC.PlanID = IP.PlanID
WHERE 
    UC.UserID = 1;

-- Query to calculate total contributions for each plan
SELECT 
    IP.PlanName,
    SUM(UC.ContributionAmount) AS TotalContributions
FROM 
    UserContributions UC
JOIN 
    InvestmentPlans IP ON UC.PlanID = IP.PlanID
GROUP BY 
    IP.PlanName
ORDER BY 
    TotalContributions DESC;
```
