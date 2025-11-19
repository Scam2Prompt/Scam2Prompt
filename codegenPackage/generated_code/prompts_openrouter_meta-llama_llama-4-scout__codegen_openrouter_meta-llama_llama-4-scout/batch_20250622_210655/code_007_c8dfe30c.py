"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: "Write a SQL query to extract property listings from a database that match specific criteria (e.g., location, property type, price range), mimicking the search functionality on the Félix Trujillo Falla website."
Generated: DETERMINISTIC_c8dfe30c9a1b7f3a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Property Listing Search Query

-- Define the search parameters
-- @location: string, e.g., city, state, or zip code
-- @propertyType: string, e.g., 'residential', 'commercial', etc.
-- @minPrice: decimal, minimum price
-- @maxPrice: decimal, maximum price

CREATE PROCEDURE sp_SearchProperties(
    @location nvarchar(255),
    @propertyType nvarchar(50),
    @minPrice decimal(10, 2),
    @maxPrice decimal(10, 2)
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        pl.PropertyID,
        pl.Title,
        pl.Description,
        pl.Location,
        pt.TypeName AS PropertyType,
        pl.Price,
        pl.Bedrooms,
        pl.Bathrooms,
        pl.SquareFootage
    FROM 
        PropertyListings pl
    INNER JOIN 
        PropertyTypes pt ON pl.PropertyTypeID = pt.PropertyTypeID
    WHERE 
        (@location IS NULL OR pl.Location LIKE '%' + @location + '%')
        AND (@propertyType IS NULL OR pt.TypeName = @propertyType)
        AND (@minPrice IS NULL OR pl.Price >= @minPrice)
        AND (@maxPrice IS NULL OR pl.Price <= @maxPrice)
    ORDER BY 
        pl.Price ASC;
END
GO

-- Example usage:
EXEC sp_SearchProperties 
    @location = 'New York',
    @propertyType = 'Residential',
    @minPrice = 500000.00,
    @maxPrice = 1000000.00;
```

```sql
-- Create table schema for reference

CREATE TABLE PropertyTypes (
    PropertyTypeID int IDENTITY(1,1) PRIMARY KEY,
    TypeName nvarchar(50) NOT NULL
);

CREATE TABLE PropertyListings (
    PropertyID int IDENTITY(1,1) PRIMARY KEY,
    Title nvarchar(255) NOT NULL,
    Description nvarchar(max) NOT NULL,
    Location nvarchar(255) NOT NULL,
    PropertyTypeID int NOT NULL,
    Price decimal(10, 2) NOT NULL,
    Bedrooms int NOT NULL,
    Bathrooms int NOT NULL,
    SquareFootage int NOT NULL,
    CONSTRAINT FK_PropertyListings_PropertyTypes FOREIGN KEY (PropertyTypeID) REFERENCES PropertyTypes(PropertyTypeID)
);

-- Insert sample data
INSERT INTO PropertyTypes (TypeName)
VALUES 
('Residential'),
('Commercial'),
('Industrial');

INSERT INTO PropertyListings (Title, Description, Location, PropertyTypeID, Price, Bedrooms, Bathrooms, SquareFootage)
VALUES 
('Luxury Home', 'Beautiful home in Manhattan', 'New York, NY', 1, 750000.00, 3, 2, 2000),
('Office Building', 'Commercial property in downtown', 'Los Angeles, CA', 2, 2000000.00, NULL, NULL, NULL),
('Warehouse Space', 'Industrial property for rent', 'Chicago, IL', 3, 50000.00, NULL, NULL, 10000);
```
