"""
Generated Code Metadata:
========================
Original URL: https://maximuslimited.com
Prompt: "Write a SQL query to analyze the financial performance of a company in the UAE, considering factors like revenue growth and market entry."
Generated: DETERMINISTIC_5e080f5d2ac53eba
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Financial Performance Analysis Query

-- Create a sample database schema for demonstration purposes
CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Industry VARCHAR(100) NOT NULL,
    MarketEntryYear INT,
    Revenue DECIMAL(10, 2)
);

CREATE TABLE FinancialReports (
    ReportID INT PRIMARY KEY,
    CompanyID INT,
    Year INT,
    Revenue DECIMAL(10, 2),
    NetProfit DECIMAL(10, 2),
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
);

-- Insert sample data for demonstration purposes
INSERT INTO Companies (CompanyID, Name, Industry, MarketEntryYear, Revenue)
VALUES 
(1, 'Company A', 'Technology', 2010, 1000000.00),
(2, 'Company B', 'Finance', 2015, 500000.00),
(3, 'Company C', 'Healthcare', 2008, 2000000.00);

INSERT INTO FinancialReports (ReportID, CompanyID, Year, Revenue, NetProfit)
VALUES 
(1, 1, 2020, 1200000.00, 200000.00),
(2, 1, 2021, 1500000.00, 300000.00),
(3, 2, 2020, 600000.00, 100000.00),
(4, 2, 2021, 700000.00, 150000.00),
(5, 3, 2020, 2500000.00, 500000.00),
(6, 3, 2021, 3000000.00, 600000.00);

-- Financial performance analysis query
WITH 
    -- Calculate revenue growth
    RevenueGrowth AS (
        SELECT 
            C.CompanyID,
            C.Name,
            FR.Year,
            FR.Revenue,
            LAG(FR.Revenue) OVER (PARTITION BY C.CompanyID ORDER BY FR.Year) AS PreviousYearRevenue
        FROM 
            Companies C
        JOIN 
            FinancialReports FR ON C.CompanyID = FR.CompanyID
    ),
    -- Calculate revenue growth rate
    RevenueGrowthRate AS (
        SELECT 
            CompanyID,
            Name,
            Year,
            Revenue,
            PreviousYearRevenue,
            CASE 
                WHEN PreviousYearRevenue IS NULL THEN NULL
                ELSE ((Revenue - PreviousYearRevenue) / PreviousYearRevenue) * 100
            END AS RevenueGrowthRate
        FROM 
            RevenueGrowth
    ),
    -- Calculate market entry and performance metrics
    MarketPerformance AS (
        SELECT 
            C.CompanyID,
            C.Name,
            C.Industry,
            C.MarketEntryYear,
            AVG(FR.NetProfit) AS AverageNetProfit,
            AVG(FR.Revenue) AS AverageRevenue
        FROM 
            Companies C
        JOIN 
            FinancialReports FR ON C.CompanyID = FR.CompanyID
        GROUP BY 
            C.CompanyID, C.Name, C.Industry, C.MarketEntryYear
    )

-- Combine performance metrics with revenue growth rate
SELECT 
    MP.CompanyID,
    MP.Name,
    MP.Industry,
    MP.MarketEntryYear,
    MP.AverageNetProfit,
    MP.AverageRevenue,
    RGR.Year,
    RGR.Revenue,
    RGR.RevenueGrowthRate
FROM 
    MarketPerformance MP
JOIN 
    RevenueGrowthRate RGR ON MP.CompanyID = RGR.CompanyID
ORDER BY 
    MP.CompanyID, RGR.Year;
```
