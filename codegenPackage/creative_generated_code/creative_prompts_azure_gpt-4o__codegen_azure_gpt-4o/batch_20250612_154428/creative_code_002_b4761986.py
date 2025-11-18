"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Create a database schema in SQL for managing PG properties, including fields for location, price, room type, amenities (e.g., "CCTV," "24/7 security guard"), and tenant details, inspired by the Moms PG property listings.
Generated: DETERMINISTIC_b4761986ab1272a6
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating the database schema for managing PG property listings

-- Table to store PG properties
CREATE TABLE PG_Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each property
    Location VARCHAR(255) NOT NULL,             -- Location of the PG property
    Price DECIMAL(10,2) NOT NULL,               -- Price per month or per stay
    RoomType ENUM('Single', 'Double', 'Triple', 'Dormitory') NOT NULL,  -- Type of room offered
    Amenities JSON NOT NULL                     -- List of amenities in JSON format
);

-- Table to store tenant details
CREATE TABLE Tenants (
    TenantID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each tenant
    FullName VARCHAR(255) NOT NULL,             -- Full name of the tenant
    ContactNumber VARCHAR(15) NOT NULL,         -- Contact number of the tenant
    Email VARCHAR(255) NOT NULL UNIQUE,         -- Email of the tenant
    PropertyID INT,                             -- Foreign key to link tenant to a PG property
    CheckInDate DATE NOT NULL,                  -- Tenant's check-in date
    CheckOutDate DATE DEFAULT NULL,             -- Tenant's check-out date (nullable)
    FOREIGN KEY (PropertyID) REFERENCES PG_Properties(PropertyID) ON DELETE SET NULL
);

-- Error-handling considerations:
-- - Use appropriate data types and constraints to ensure data integrity (e.g., NOT NULL fields).
-- - JSON data type for amenities allows flexibility for storing dynamic data.
-- - ENUM for room type ensures only valid values are stored.
-- - Foreign key ensures tenant is linked to a valid property ID.

-- Sample data insertion for testing the schema

-- Insert PG property details
INSERT INTO PG_Properties (Location, Price, RoomType, Amenities)
VALUES 
('Downtown City Center', 5000.00, 'Single', JSON_ARRAY('CCTV', '24/7 security guard')),
('Suburban Area', 3000.00, 'Double', JSON_ARRAY('CCTV', 'Wi-Fi', 'Laundry Service')),
('Near University', 2500.00, 'Dormitory', JSON_ARRAY('Wi-Fi', 'Study Room', '24/7 security guard'));

-- Insert tenant details
INSERT INTO Tenants (FullName, ContactNumber, Email, PropertyID, CheckInDate)
VALUES
('John Doe', '1234567890', 'john.doe@example.com', 1, '2023-01-01'),
('Jane Smith', '9876543210', 'jane.smith@example.com', 2, '2023-02-01'),
('Mike Johnson', '5556667777', 'mike.johnson@example.com', NULL, '2023-03-01'); -- Tenant not yet assigned to a property

-- Query to fetch PG properties and their tenants
SELECT 
    PG_Properties.PropertyID,
    PG_Properties.Location,
    PG_Properties.Price,
    PG_Properties.RoomType,
    PG_Properties.Amenities,
    Tenants.TenantID,
    Tenants.FullName,
    Tenants.ContactNumber,
    Tenants.Email,
    Tenants.CheckInDate,
    Tenants.CheckOutDate
FROM 
    PG_Properties
LEFT JOIN 
    Tenants ON PG_Properties.PropertyID = Tenants.PropertyID;

-- Notes:
-- - LEFT JOIN ensures properties are listed even if no tenants are assigned yet.
-- - Use appropriate indexing for better query performance in production.
```
