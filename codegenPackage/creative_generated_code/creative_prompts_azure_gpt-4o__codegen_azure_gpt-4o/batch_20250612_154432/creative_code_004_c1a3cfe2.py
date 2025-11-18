"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Develop a SQL database schema for Certified Plumbers Graham, TX to manage customer information, service history, and plumbing service types (e.g., slab leak detection, whole-home repiping).
Generated: DETERMINISTIC_c1a3cfe2ed88022c
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Certified Plumbers Graham, TX

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Email VARCHAR(100),                        -- Customer's email address
    Address TEXT NOT NULL,                     -- Customer's physical address
    City VARCHAR(50) DEFAULT 'Graham',         -- Default city is Graham
    State VARCHAR(50) DEFAULT 'TX'             -- Default state is Texas
);

-- Create a table to store plumbing service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the plumbing service
    ServiceDescription TEXT,                      -- Detailed description of the service
    BaseCost DECIMAL(10, 2) NOT NULL              -- Base cost for the service
);

-- Create a table to store service history for customers
CREATE TABLE ServiceHistory (
    ServiceHistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for service history records
    CustomerID INT NOT NULL,                         -- Foreign key referencing the Customers table
    ServiceTypeID INT NOT NULL,                      -- Foreign key referencing the ServiceTypes table
    ServiceDate DATE NOT NULL,                       -- Date the service was performed
    TechnicianName VARCHAR(50) NOT NULL,            -- Name of the technician who performed the service
    Notes TEXT,                                      -- Additional notes about the service
    TotalCost DECIMAL(10, 2) NOT NULL,               -- Total cost of the service
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete if customer is deleted
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Cascade delete if service type is deleted
);

-- Insert sample data (Optional: for testing purposes)
INSERT INTO ServiceTypes (ServiceName, ServiceDescription, BaseCost)
VALUES
    ('Slab Leak Detection', 'Detect and repair leaks in slab foundations.', 250.00),
    ('Whole-Home Repiping', 'Replace plumbing throughout the entire home.', 4000.00),
    ('Drain Cleaning', 'Clean and unclog drains.', 150.00),
    ('Water Heater Installation', 'Install a new water heater.', 850.00);

-- Add indexes for optimizing queries
CREATE INDEX idx_customer_phone ON Customers (PhoneNumber); -- Index to speed up lookups by phone number
CREATE INDEX idx_service_date ON ServiceHistory (ServiceDate); -- Index to speed up lookups by service date
```
