"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: "Design a database schema to store information about Chevrolet vehicles, consórcio plans, and customer details, using a relational database management system."
Generated: DETERMINISTIC_56e87b3b08b71215
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Chevrolet vehicles, consórcio plans, and customer details

-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                     -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Create a table to store Chevrolet vehicle details
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each vehicle
    Model VARCHAR(50) NOT NULL,                  -- Vehicle model
    Year INT NOT NULL CHECK (Year >= 1886),      -- Year of manufacture (must be valid)
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the vehicle
    CustomerID INT,                               -- Foreign key referencing the customer
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE SET NULL -- Relationship to Customers
);

-- Create a table to store consórcio plans
CREATE TABLE Consorcios (
    ConsorcioID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each consórcio plan
    PlanName VARCHAR(100) NOT NULL,               -- Name of the consórcio plan
    MonthlyPayment DECIMAL(10, 2) NOT NULL,       -- Monthly payment amount
    DurationMonths INT NOT NULL CHECK (DurationMonths > 0), -- Duration of the plan in months
    VehicleID INT,                                 -- Foreign key referencing the vehicle
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE -- Relationship to Vehicles
);

-- Create a table to store consórcio subscriptions
CREATE TABLE ConsorcioSubscriptions (
    SubscriptionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each subscription
    CustomerID INT NOT NULL,                        -- Foreign key referencing the customer
    ConsorcioID INT NOT NULL,                       -- Foreign key referencing the consórcio plan
    SubscriptionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of subscription
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Relationship to Customers
    FOREIGN KEY (ConsorcioID) REFERENCES Consorcios(ConsorcioID) ON DELETE CASCADE -- Relationship to Consorcios
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_vehicle_model ON Vehicles(Model);
CREATE INDEX idx_consorcio_plan_name ON Consorcios(PlanName);
```
