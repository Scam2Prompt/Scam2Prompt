"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Construct a SQL query to analyze the performance of the property portfolio managed by Rosebud Holdings Property Income REIT, based on the provided financial metrics.
Generated: DETERMINISTIC_3e2b101385fbfd3d
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Define a stored procedure to analyze the performance of the property portfolio
CREATE PROCEDURE AnalyzePortfolioPerformance
AS
BEGIN
    -- Select relevant financial metrics for analysis
    SELECT 
        -- Property identifier
        p.PropertyID,
        
        -- Financial metrics
        p.PurchasePrice,
        p.CurrentValue,
        p.Rent,
        p.VacancyRate,
        p.OperatingExpenses,
        
        -- Calculate key performance indicators (KPIs)
        (p.CurrentValue - p.PurchasePrice) / p.PurchasePrice AS CapitalAppreciation,
        p.Rent / p.CurrentValue AS RentalYield,
        (p.Rent - p.OperatingExpenses) / p.CurrentValue AS NetOperatingIncome,
        (1 - p.VacancyRate) * p.Rent / p.CurrentValue AS EffectiveRentalYield
    FROM 
        Properties p
    WHERE 
        -- Filter properties managed by Rosebud Holdings Property Income REIT
        p.ManagedBy = 'Rosebud Holdings Property Income REIT'
    ORDER BY 
        -- Sort by capital appreciation in descending order
        CapitalAppreciation DESC;
END
GO

-- Create a function to calculate the portfolio's overall performance
CREATE FUNCTION CalculatePortfolioPerformance
(
    @ManagedBy nvarchar(255)
)
RETURNS @Performance TABLE
(
    Metric nvarchar(50),
    Value decimal(10, 2)
)
AS
BEGIN
    -- Insert overall portfolio metrics into the result table
    INSERT INTO @Performance (Metric, Value)
    SELECT 
        'TotalPurchasePrice', SUM(p.PurchasePrice),
        'TotalCurrentValue', SUM(p.CurrentValue),
        'TotalRent', SUM(p.Rent),
        'TotalOperatingExpenses', SUM(p.OperatingExpenses)
    FROM 
        Properties p
    WHERE 
        p.ManagedBy = @ManagedBy;

    -- Calculate and insert overall portfolio KPIs into the result table
    INSERT INTO @Performance (Metric, Value)
    SELECT 
        'AverageCapitalAppreciation', AVG((p.CurrentValue - p.PurchasePrice) / p.PurchasePrice),
        'AverageRentalYield', AVG(p.Rent / p.CurrentValue),
        'AverageNetOperatingIncome', AVG((p.Rent - p.OperatingExpenses) / p.CurrentValue)
    FROM 
        Properties p
    WHERE 
        p.ManagedBy = @ManagedBy;

    RETURN;
END
GO

-- Example usage:
EXEC AnalyzePortfolioPerformance;

SELECT * FROM CalculatePortfolioPerformance('Rosebud Holdings Property Income REIT');
```

```sql
-- Create table for storing property data
CREATE TABLE Properties
(
    PropertyID int PRIMARY KEY,
    ManagedBy nvarchar(255) NOT NULL,
    PurchasePrice decimal(15, 2) NOT NULL,
    CurrentValue decimal(15, 2) NOT NULL,
    Rent decimal(10, 2) NOT NULL,
    VacancyRate decimal(5, 4) NOT NULL CHECK (VacancyRate BETWEEN 0 AND 1),
    OperatingExpenses decimal(10, 2) NOT NULL
);
GO

-- Insert sample data into the Properties table
INSERT INTO Properties (PropertyID, ManagedBy, PurchasePrice, CurrentValue, Rent, VacancyRate, OperatingExpenses)
VALUES 
(1, 'Rosebud Holdings Property Income REIT', 1000000.00, 1200000.00, 50000.00, 0.05, 20000.00),
(2, 'Rosebud Holdings Property Income REIT', 800000.00, 900000.00, 40000.00, 0.03, 15000.00),
(3, 'Other REIT', 700000.00, 800000.00, 35000.00, 0.04, 12000.00);
GO
```
