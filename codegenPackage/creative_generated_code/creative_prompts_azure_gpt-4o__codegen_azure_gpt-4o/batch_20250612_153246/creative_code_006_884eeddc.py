"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Develop a database schema for managing customer satisfaction metrics, rental plans, and delivery statistics for a refrigerated transport company, based on the features of RefrigeratorTransport.com.
Generated: DETERMINISTIC_884eeddcbde571ed
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing customer satisfaction metrics, rental plans, and delivery statistics
-- This schema is designed for RefrigeratorTransport.com and includes tables to store data related
-- to customers, rental plans, deliveries, and satisfaction metrics.

-- Table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer was created
);

-- Table for managing rental plans
CREATE TABLE RentalPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each rental plan
    PlanName VARCHAR(50) NOT NULL,             -- Name of the rental plan
    Description TEXT,                          -- Description of the rental plan
    MonthlyCost DECIMAL(10, 2) NOT NULL,       -- Monthly cost of the plan
    MaxCapacityKg INT NOT NULL,                -- Maximum weight capacity in kilograms
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the rental plan was created
);

-- Table for storing delivery statistics
CREATE TABLE Deliveries (
    DeliveryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each delivery
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    PlanID INT NOT NULL,                       -- Foreign key referencing RentalPlans table
    DeliveryDate DATE NOT NULL,                -- Date of the delivery
    WeightKg INT NOT NULL,                     -- Weight of the goods in kilograms
    DistanceKm DECIMAL(10, 2) NOT NULL,        -- Distance covered during the delivery in kilometers
    DeliveryStatus ENUM('Pending', 'In Transit', 'Delivered', 'Failed') NOT NULL, -- Status of the delivery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the delivery record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete behavior
    FOREIGN KEY (PlanID) REFERENCES RentalPlans(PlanID) ON DELETE CASCADE
);

-- Table for storing customer satisfaction metrics
CREATE TABLE SatisfactionMetrics (
    SatisfactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each satisfaction metric
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers table
    DeliveryID INT NOT NULL,                       -- Foreign key referencing Deliveries table
    Rating INT CHECK (Rating BETWEEN 1 AND 5) NOT NULL, -- Customer's rating (1-5 scale)
    Feedback TEXT,                                 -- Optional textual feedback from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the satisfaction metric was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete behavior
    FOREIGN KEY (DeliveryID) REFERENCES Deliveries(DeliveryID) ON DELETE CASCADE
);

-- Index for optimizing query performance on delivery date
CREATE INDEX idx_delivery_date ON Deliveries (DeliveryDate);

-- Index for optimizing query performance on satisfaction ratings
CREATE INDEX idx_satisfaction_rating ON SatisfactionMetrics (Rating);
```
