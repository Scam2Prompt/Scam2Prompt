"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Develop a database schema for managing customer satisfaction metrics, rental plans, and delivery statistics for a refrigerated transport company, based on the features of RefrigeratorTransport.com.
Generated: DETERMINISTIC_884eeddcbde571ed
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing customer satisfaction metrics, rental plans, and delivery statistics
-- for a refrigerated transport company

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CustomerSatisfactionMetrics;
DROP TABLE IF EXISTS RentalPlans;
DROP TABLE IF EXISTS DeliveryStatistics;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Deliveries;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store rental plans offered by the company
CREATE TABLE RentalPlans (
    PlanID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each rental plan
    PlanName VARCHAR(100) NOT NULL,            -- Name of the rental plan
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the rental plan
    DurationInDays INT NOT NULL,                -- Duration of the rental plan in days
    Features TEXT,                              -- Description of features included in the plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the plan was created
);

-- Table to store customer satisfaction metrics
CREATE TABLE CustomerSatisfactionMetrics (
    MetricID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each metric entry
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    SatisfactionScore INT CHECK (SatisfactionScore BETWEEN 1 AND 10), -- Satisfaction score (1-10)
    Feedback TEXT,                              -- Customer feedback
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the metric was recorded
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store delivery statistics
CREATE TABLE DeliveryStatistics (
    DeliveryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each delivery
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    PlanID INT NOT NULL,                        -- Foreign key referencing RentalPlans
    DeliveryDate DATE NOT NULL,                 -- Date of delivery
    DeliveryStatus ENUM('Pending', 'Completed', 'Cancelled') NOT NULL, -- Status of the delivery
    DeliveryTime TIME,                          -- Time taken for delivery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the delivery was recorded
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (PlanID) REFERENCES RentalPlans(PlanID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_delivery_date ON DeliveryStatistics(DeliveryDate);
CREATE INDEX idx_satisfaction_score ON CustomerSatisfactionMetrics(SatisfactionScore);
```
