"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Write a SQL query to analyze customer data and cleaning service usage for an industrial ultrasonic cleaning company, identifying trends and areas for improvement."
Generated: DETERMINISTIC_0dc5517c1ac1b4c4
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Analyze customer data and cleaning service usage

-- Create a sample database schema for demonstration purposes
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CompanyName VARCHAR(255) NOT NULL,
    Industry VARCHAR(100) NOT NULL,
    ContactPerson VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL
);

CREATE TABLE CleaningServices (
    ServiceID INT PRIMARY KEY,
    ServiceName VARCHAR(255) NOT NULL,
    Description VARCHAR(500) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE CustomerServices (
    CustomerID INT NOT NULL,
    ServiceID INT NOT NULL,
    ServiceDate DATE NOT NULL,
    Frequency VARCHAR(50) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ServiceID) REFERENCES CleaningServices(ServiceID),
    PRIMARY KEY (CustomerID, ServiceID, ServiceDate)
);

-- Insert sample data for demonstration purposes
INSERT INTO Customers (CustomerID, CompanyName, Industry, ContactPerson, Email, Phone)
VALUES
(1, 'ABC Inc.', 'Manufacturing', 'John Doe', 'john.doe@example.com', '123-456-7890'),
(2, 'XYZ Corp.', 'Automotive', 'Jane Smith', 'jane.smith@example.com', '987-654-3210'),
(3, ' DEF Ltd.', 'Aerospace', 'Bob Johnson', 'bob.johnson@example.com', '555-123-4567');

INSERT INTO CleaningServices (ServiceID, ServiceName, Description, Price)
VALUES
(1, 'Ultrasonic Cleaning', 'Cleaning of parts and equipment using ultrasonic technology', 100.00),
(2, 'High-Pressure Cleaning', 'Cleaning of surfaces using high-pressure water jets', 150.00),
(3, 'Precision Cleaning', 'Cleaning of delicate equipment and parts', 200.00);

INSERT INTO CustomerServices (CustomerID, ServiceID, ServiceDate, Frequency)
VALUES
(1, 1, '2022-01-01', 'Monthly'),
(1, 2, '2022-02-01', 'Quarterly'),
(2, 1, '2022-03-01', 'Bi-Monthly'),
(3, 3, '2022-04-01', 'Annually');

-- SQL query to analyze customer data and cleaning service usage
WITH 
-- Calculate total services used by each customer
CustomerServiceUsage AS (
    SELECT 
        c.CustomerID,
        c.CompanyName,
        COUNT(cs.ServiceID) AS TotalServices,
        SUM(cs2.Price) AS TotalRevenue
    FROM 
        Customers c
    JOIN 
        CustomerServices cs ON c.CustomerID = cs.CustomerID
    JOIN 
        CleaningServices cs2 ON cs.ServiceID = cs2.ServiceID
    GROUP BY 
        c.CustomerID, c.CompanyName
),
-- Calculate service usage by industry
IndustryServiceUsage AS (
    SELECT 
        c.Industry,
        COUNT(cs.ServiceID) AS TotalServices,
        SUM(cs2.Price) AS TotalRevenue
    FROM 
        Customers c
    JOIN 
        CustomerServices cs ON c.CustomerID = cs.CustomerID
    JOIN 
        CleaningServices cs2 ON cs.ServiceID = cs2.ServiceID
    GROUP BY 
        c.Industry
),
-- Calculate service usage by frequency
FrequencyServiceUsage AS (
    SELECT 
        cs.Frequency,
        COUNT(cs.ServiceID) AS TotalServices,
        SUM(cs2.Price) AS TotalRevenue
    FROM 
        CustomerServices cs
    JOIN 
        CleaningServices cs2 ON cs.ServiceID = cs2.ServiceID
    GROUP BY 
        cs.Frequency
)
-- Analyze customer data and cleaning service usage
SELECT 
    'Customer Service Usage' AS AnalysisType,
    CustomerID,
    CompanyName,
    TotalServices,
    TotalRevenue
FROM 
    CustomerServiceUsage
UNION ALL
SELECT 
    'Industry Service Usage' AS AnalysisType,
    Industry AS CustomerID,
    Industry AS CompanyName,
    TotalServices,
    TotalRevenue
FROM 
    IndustryServiceUsage
UNION ALL
SELECT 
    'Frequency Service Usage' AS AnalysisType,
    Frequency AS CustomerID,
    Frequency AS CompanyName,
    TotalServices,
    TotalRevenue
FROM 
    FrequencyServiceUsage
ORDER BY 
    AnalysisType, CustomerID;

-- Drop sample database schema
DROP TABLE CustomerServices;
DROP TABLE CleaningServices;
DROP TABLE Customers;
```
