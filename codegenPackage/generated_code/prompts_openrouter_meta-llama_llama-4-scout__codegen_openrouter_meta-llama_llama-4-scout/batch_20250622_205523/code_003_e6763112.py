"""
Generated Code Metadata:
========================
Original URL: https://enjin.pro
Prompt: "Create a SQL query to retrieve a list of cars from an inventory database that match specific criteria such as model, price range, and location, as 縁陣 might do for customer inquiries."
Generated: DETERMINISTIC_e676311230dbb4e2
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve a list of cars from the inventory database based on specific criteria

-- Define the stored procedure
CREATE PROCEDURE sp_GetCarsByCriteria
    @Model nvarchar(50) = NULL,
    @MinPrice decimal(10, 2) = NULL,
    @MaxPrice decimal(10, 2) = NULL,
    @Location nvarchar(50) = NULL
AS
BEGIN
    -- Validate input parameters
    IF @MinPrice IS NOT NULL AND @MaxPrice IS NOT NULL AND @MinPrice > @MaxPrice
    BEGIN
        RAISERROR('Invalid price range', 16, 1);
        RETURN;
    END

    -- Retrieve the list of cars based on the specified criteria
    SELECT 
        c.CarId,
        c.Model,
        c.Price,
        c.Location,
        c.Year,
        c.Make
    FROM 
        dbo.Cars c
    WHERE 
        (@Model IS NULL OR c.Model = @Model)
        AND (@MinPrice IS NULL OR c.Price >= @MinPrice)
        AND (@MaxPrice IS NULL OR c.Price <= @MaxPrice)
        AND (@Location IS NULL OR c.Location = @Location);
END
GO

-- Example usage
EXEC sp_GetCarsByCriteria 
    @Model = 'Toyota Camry',
    @MinPrice = 20000.00,
    @MaxPrice = 30000.00,
    @Location = 'New York';

-- Alternatively, you can use a SELECT statement directly
SELECT 
    c.CarId,
    c.Model,
    c.Price,
    c.Location,
    c.Year,
    c.Make
FROM 
    dbo.Cars c
WHERE 
    (c.Model = 'Toyota Camry' OR 'Toyota Camry' IS NULL)
    AND (c.Price >= 20000.00 OR 20000.00 IS NULL)
    AND (c.Price <= 30000.00 OR 30000.00 IS NULL)
    AND (c.Location = 'New York' OR 'New York' IS NULL);
```

```sql
-- Create table if it does not exist
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Cars')
BEGIN
    CREATE TABLE dbo.Cars
    (
        CarId int IDENTITY(1,1) PRIMARY KEY,
        Model nvarchar(50) NOT NULL,
        Price decimal(10, 2) NOT NULL,
        Location nvarchar(50) NOT NULL,
        Year int NOT NULL,
        Make nvarchar(50) NOT NULL
    );
END
GO

-- Insert sample data
IF NOT EXISTS (SELECT * FROM dbo.Cars)
BEGIN
    INSERT INTO dbo.Cars (Model, Price, Location, Year, Make)
    VALUES 
        ('Toyota Camry', 25000.00, 'New York', 2020, 'Toyota'),
        ('Honda Civic', 22000.00, 'Los Angeles', 2019, 'Honda'),
        ('Toyota Camry', 28000.00, 'New York', 2021, 'Toyota'),
        ('Ford Mustang', 30000.00, 'Chicago', 2020, 'Ford');
END
GO
```
