"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Write a SQL query to analyze customer visit patterns and service preferences for a car repair shop like Pneus ML, helping to identify trends and popular services.
Generated: DETERMINISTIC_605bae4eb5bee321
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a sample database schema for the car repair shop
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL
);

CREATE TABLE Services (
    ServiceID INT PRIMARY KEY,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Visits (
    VisitID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    VisitDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE VisitServices (
    VisitID INT NOT NULL,
    ServiceID INT NOT NULL,
    PRIMARY KEY (VisitID, ServiceID),
    FOREIGN KEY (VisitID) REFERENCES Visits(VisitID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Analyze customer visit patterns and service preferences
WITH 
-- Calculate total visits per customer
TotalVisits AS (
    SELECT 
        c.CustomerID, 
        c.Name, 
        COUNT(v.VisitID) AS TotalVisits
    FROM 
        Customers c
    JOIN 
        Visits v ON c.CustomerID = v.CustomerID
    GROUP BY 
        c.CustomerID, 
        c.Name
),

-- Calculate service frequency
ServiceFrequency AS (
    SELECT 
        s.ServiceName, 
        COUNT(vs.ServiceID) AS Frequency
    FROM 
        Services s
    JOIN 
        VisitServices vs ON s.ServiceID = vs.ServiceID
    GROUP BY 
        s.ServiceName
),

-- Calculate customer service preferences
CustomerPreferences AS (
    SELECT 
        c.CustomerID, 
        c.Name, 
        s.ServiceName, 
        COUNT(vs.ServiceID) AS ServiceCount
    FROM 
        Customers c
    JOIN 
        Visits v ON c.CustomerID = v.CustomerID
    JOIN 
        VisitServices vs ON v.VisitID = vs.VisitID
    JOIN 
        Services s ON vs.ServiceID = s.ServiceID
    GROUP BY 
        c.CustomerID, 
        c.Name, 
        s.ServiceName
)

-- Combine the results to analyze trends and popular services
SELECT 
    'Total Visits' AS Category,
    tv.Name, 
    tv.TotalVisits
FROM 
    TotalVisits tv

UNION ALL

SELECT 
    'Service Frequency' AS Category,
    sf.ServiceName, 
    sf.Frequency
FROM 
    ServiceFrequency sf

UNION ALL

SELECT 
    'Customer Preferences' AS Category,
    cp.Name, 
    cp.ServiceName
FROM 
    CustomerPreferences cp

ORDER BY 
    Category, 
    Name;
```

```sql
-- Stored procedure to analyze customer visit patterns and service preferences
DELIMITER //
CREATE PROCEDURE AnalyzeCustomerVisits()
BEGIN
    -- Calculate total visits per customer
    SELECT 
        c.CustomerID, 
        c.Name, 
        COUNT(v.VisitID) AS TotalVisits
    FROM 
        Customers c
    JOIN 
        Visits v ON c.CustomerID = v.CustomerID
    GROUP BY 
        c.CustomerID, 
        c.Name;

    -- Calculate service frequency
    SELECT 
        s.ServiceName, 
        COUNT(vs.ServiceID) AS Frequency
    FROM 
        Services s
    JOIN 
        VisitServices vs ON s.ServiceID = vs.ServiceID
    GROUP BY 
        s.ServiceName;

    -- Calculate customer service preferences
    SELECT 
        c.CustomerID, 
        c.Name, 
        s.ServiceName, 
        COUNT(vs.ServiceID) AS ServiceCount
    FROM 
        Customers c
    JOIN 
        Visits v ON c.CustomerID = v.CustomerID
    JOIN 
        VisitServices vs ON v.VisitID = vs.VisitID
    JOIN 
        Services s ON vs.ServiceID = s.ServiceID
    GROUP BY 
        c.CustomerID, 
        c.Name, 
        s.ServiceName;
END//
DELIMITER ;
```

```sql
-- Indexing for performance optimization
CREATE INDEX idx_Customers_CustomerID ON Customers(CustomerID);
CREATE INDEX idx_Visits_CustomerID ON Visits(CustomerID);
CREATE INDEX idx_Visits_VisitID ON Visits(VisitID);
CREATE INDEX idx_Services_ServiceID ON Services(ServiceID);
CREATE INDEX idx_VisitServices_VisitID ON VisitServices(VisitID);
CREATE INDEX idx_VisitServices_ServiceID ON VisitServices(ServiceID);
```
