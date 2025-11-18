"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Develop a SQL database schema to store information about health insurance plans, including provider details, benefits, and pricing, similar to the comparison service offered by Health Insurance Shop.
Generated: DETERMINISTIC_4a66081104a09e57
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Schema for storing health insurance plans
-- This schema includes tables for providers, plans, benefits, and pricing.

-- Table to store health insurance providers information
CREATE TABLE Providers (
    ProviderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each provider
    Name VARCHAR(255) NOT NULL, -- Name of the provider
    ContactEmail VARCHAR(255) NOT NULL, -- Contact email for the provider
    PhoneNumber VARCHAR(15), -- Contact phone number
    Address TEXT, -- Physical address of the provider
    WebsiteURL VARCHAR(255) -- Website URL of the provider
);

-- Table to store health insurance plans information
CREATE TABLE Plans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each plan
    ProviderID INT NOT NULL, -- Foreign key to link to the Providers table
    Name VARCHAR(255) NOT NULL, -- Name of the insurance plan
    CoverageType ENUM('Individual', 'Family') NOT NULL, -- Type of coverage
    Description TEXT, -- Detailed description of the plan
    CreatedDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the plan was created
    FOREIGN KEY (ProviderID) REFERENCES Providers(ProviderID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store benefits associated with each plan
CREATE TABLE Benefits (
    BenefitID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each benefit
    PlanID INT NOT NULL, -- Foreign key to link to the Plans table
    BenefitName VARCHAR(255) NOT NULL, -- Name of the benefit
    BenefitDescription TEXT, -- Detailed description of the benefit
    FOREIGN KEY (PlanID) REFERENCES Plans(PlanID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store pricing information for each plan
CREATE TABLE Pricing (
    PricingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for pricing entries
    PlanID INT NOT NULL, -- Foreign key to link to the Plans table
    MonthlyPremium DECIMAL(10, 2) NOT NULL, -- Monthly premium cost
    Deductible DECIMAL(10, 2) NOT NULL, -- Deductible amount
    OutOfPocketMax DECIMAL(10, 2) NOT NULL, -- Maximum out-of-pocket cost
    FOREIGN KEY (PlanID) REFERENCES Plans(PlanID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Optional: Table to store user reviews for providers or plans
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for reviews
    PlanID INT NOT NULL, -- Foreign key to link reviews to plans
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 (worst) and 5 (best)
    Comment TEXT, -- User comments about the plan
    ReviewDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (PlanID) REFERENCES Plans(PlanID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexing and constraints for better performance and data integrity
CREATE INDEX idx_provider_name ON Providers(Name); -- Index for quick provider name searches
CREATE INDEX idx_plan_name ON Plans(Name); -- Index for quick plan name searches
CREATE INDEX idx_benefit_name ON Benefits(BenefitName); -- Index for quick benefit name searches
CREATE INDEX idx_pricing_monthly_premium ON Pricing(MonthlyPremium); -- Index for quick pricing searches
```
