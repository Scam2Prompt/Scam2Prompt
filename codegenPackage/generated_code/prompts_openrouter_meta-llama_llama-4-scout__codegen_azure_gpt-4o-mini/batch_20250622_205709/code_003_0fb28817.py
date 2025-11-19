"""
Generated Code Metadata:
========================
Original URL: https://acessanet.com.br
Prompt: Design a database schema to store information about internet plans, customers, and their respective subscriptions, similar to how Acessanet might organize its customer data.
Generated: DETERMINISTIC_0fb28817c334054e
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about internet plans, customers, and their subscriptions

-- Create a table to store internet plans
CREATE TABLE InternetPlans (
    PlanID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each plan
    PlanName VARCHAR(100) NOT NULL,         -- Name of the internet plan
    SpeedMbps INT NOT NULL,                  -- Speed of the internet plan in Mbps
    Price DECIMAL(10, 2) NOT NULL,          -- Monthly price of the plan
    DataLimitGB INT,                         -- Data limit in GB (NULL if unlimited)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the plan was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email (must be unique)
    PhoneNumber VARCHAR(15),                    -- Customer's phone number
    Address VARCHAR(255),                        -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store subscriptions linking customers to internet plans
CREATE TABLE Subscriptions (
    SubscriptionID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each subscription
    CustomerID INT NOT NULL,                         -- Foreign key referencing Customers
    PlanID INT NOT NULL,                             -- Foreign key referencing InternetPlans
    StartDate DATE NOT NULL,                        -- Subscription start date
    EndDate DATE,                                   -- Subscription end date (NULL if active)
    Status ENUM('Active', 'Inactive', 'Cancelled') NOT NULL DEFAULT 'Active',  -- Subscription status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the subscription was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (PlanID) REFERENCES InternetPlans(PlanID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_subscription_status ON Subscriptions(Status);
```
