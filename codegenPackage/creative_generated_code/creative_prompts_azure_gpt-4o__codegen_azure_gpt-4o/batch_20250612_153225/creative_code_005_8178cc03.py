"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Create a database schema for managing cleaning service plans (weekly, biweekly, monthly) and tracking customer preferences for specific cleaning details.
Generated: DETERMINISTIC_8178cc03e562e8b9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing cleaning service plans and tracking customer preferences

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record creation/update
);

-- Table to define cleaning service plans
CREATE TABLE ServicePlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each service plan
    PlanName ENUM('Weekly', 'Biweekly', 'Monthly') NOT NULL, -- Type of plan
    Price DECIMAL(10, 2) NOT NULL,             -- Price for the service plan
    Description TEXT,                          -- Optional description for the plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record creation/update
);

-- Table to store customer subscriptions to service plans
CREATE TABLE CustomerSubscriptions (
    SubscriptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subscription
    CustomerID INT NOT NULL,                        -- Foreign key referencing Customers table
    PlanID INT NOT NULL,                            -- Foreign key referencing ServicePlans table
    StartDate DATE NOT NULL,                        -- Start date of the subscription
    EndDate DATE,                                   -- Optional end date for the subscription
    Active BOOLEAN DEFAULT TRUE,                   -- Indicates if the subscription is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record creation/update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is deleted
    FOREIGN KEY (PlanID) REFERENCES ServicePlans(PlanID) ON DELETE CASCADE -- Cascade delete if service plan is deleted
);

-- Table to track customer preferences for cleaning details
CREATE TABLE CustomerPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each preference
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers table
    PreferenceKey VARCHAR(100) NOT NULL,         -- Key/Name for the preference (e.g., "Vacuum", "Dusting")
    PreferenceValue VARCHAR(255),                -- Value associated with the preference (e.g., "Yes", "No", "Specific instructions")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record creation/update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table to log cleaning service visits (for tracking purposes)
CREATE TABLE CleaningVisits (
    VisitID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each cleaning visit
    CustomerID INT NOT NULL,                         -- Foreign key referencing Customers table
    PlanID INT NOT NULL,                             -- Foreign key referencing ServicePlans table
    VisitDate DATE NOT NULL,                         -- Date of the cleaning visit
    Notes TEXT,                                      -- Any additional notes about the visit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record creation/update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is deleted
    FOREIGN KEY (PlanID) REFERENCES ServicePlans(PlanID) ON DELETE CASCADE -- Cascade delete if service plan is deleted
);

-- Add indexes for faster querying
CREATE INDEX idx_customer_email ON Customers (Email); -- Index for customer email
CREATE INDEX idx_subscription_active ON CustomerSubscriptions (Active); -- Index for active subscriptions
CREATE INDEX idx_visit_date ON CleaningVisits (VisitDate); -- Index for visit dates
```
