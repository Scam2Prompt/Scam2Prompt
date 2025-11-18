"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rubberflooringindonesia.com
Prompt: Create a database schema to store information about various rubber flooring products (e.g., Eva Mats, EPDM) and their applications in areas like parking lots and sports fields, based on Rubber Flooring Indonesia's offerings.
Generated: DETERMINISTIC_36c2d77a4679e445
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about rubber flooring products and their applications

-- Create a table to store information about different rubber flooring products
CREATE TABLE RubberFlooringProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,       -- Name of the rubber flooring product
    MaterialType VARCHAR(50) NOT NULL,       -- Type of material used (e.g., EVA, EPDM)
    Thickness DECIMAL(5,2) NOT NULL,         -- Thickness of the flooring in mm
    Color VARCHAR(50),                       -- Color options available for the product
    Weight DECIMAL(6,2),                     -- Weight of the flooring per square meter
    Price DECIMAL(10,2) NOT NULL,            -- Price per square meter of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store information about applications for rubber flooring products
CREATE TABLE Applications (
    ApplicationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each application
    ApplicationName VARCHAR(100) NOT NULL,        -- Name of the application (e.g., Parking Lot, Sports Field)
    Description TEXT,                              -- Description of the application
    SuitableProducts VARCHAR(255),                -- Comma-separated list of ProductIDs suitable for this application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to establish a many-to-many relationship between products and applications
CREATE TABLE ProductApplications (
    ProductID INT,                                -- Foreign key linking to RubberFlooringProducts
    ApplicationID INT,                            -- Foreign key linking to Applications
    PRIMARY KEY (ProductID, ApplicationID),      -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES RubberFlooringProducts(ProductID) ON DELETE CASCADE, -- Ensures product deletion cascades
    FOREIGN KEY (ApplicationID) REFERENCES Applications(ApplicationID) ON DELETE CASCADE -- Ensures application deletion cascades
);

-- Sample queries to insert data into the tables
-- Insert example rubber flooring products
INSERT INTO RubberFlooringProducts (ProductName, MaterialType, Thickness, Color, Weight, Price)
VALUES 
    ('Eva Mats', 'EVA', 10.00, 'Black', 2.5, 30.00),
    ('EPDM Rubber', 'EPDM', 15.00, 'Green', 3.0, 50.00);

-- Insert example applications
INSERT INTO Applications (ApplicationName, Description, SuitableProducts)
VALUES 
    ('Parking Lot', 'Durable flooring suitable for vehicle traffic', '1,2'),
    ('Sports Field', 'High-performance flooring for sports activities', '2');

-- Example query to retrieve all products and their applications
SELECT p.ProductName, a.ApplicationName
FROM RubberFlooringProducts p
JOIN ProductApplications pa ON p.ProductID = pa.ProductID
JOIN Applications a ON pa.ApplicationID = a.ApplicationID;
```
