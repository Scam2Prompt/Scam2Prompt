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
-- Database schema for managing cleaning service plans and customer preferences

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    PhoneNumber VARCHAR(15),                     -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Create a table for cleaning service plans
CREATE TABLE ServicePlans (
    PlanID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each service plan
    PlanType ENUM('Weekly', 'Biweekly', 'Monthly') NOT NULL, -- Type of cleaning plan
    Description TEXT,                            -- Description of the service plan
    Price DECIMAL(10, 2) NOT NULL               -- Price of the service plan
);

-- Create a table to link customers to their chosen service plans
CREATE TABLE CustomerPlans (
    CustomerPlanID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the customer plan link
    CustomerID INT NOT NULL,                      -- Reference to the customer
    PlanID INT NOT NULL,                          -- Reference to the service plan
    StartDate DATE NOT NULL,                     -- Date when the service starts
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Foreign key to Customers
    FOREIGN KEY (PlanID) REFERENCES ServicePlans(PlanID) ON DELETE CASCADE -- Foreign key to ServicePlans
);

-- Create a table for tracking customer cleaning preferences
CREATE TABLE CleaningPreferences (
    PreferenceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each preference
    CustomerID INT NOT NULL,                      -- Reference to the customer
    PreferenceType VARCHAR(100) NOT NULL,        -- Type of preference (e.g., "Dusting", "Vacuuming")
    IsRequired BOOLEAN DEFAULT FALSE,             -- Whether this preference is required
    Notes TEXT,                                   -- Additional notes regarding the preference
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key to Customers
);
```
