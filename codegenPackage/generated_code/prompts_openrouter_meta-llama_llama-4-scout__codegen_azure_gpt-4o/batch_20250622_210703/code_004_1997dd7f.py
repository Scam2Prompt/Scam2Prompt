"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: "Design a database schema for an art studio that stores information about artists, sculptures, paintings, and other creative products, and provide a sample query to retrieve product details."
Generated: DETERMINISTIC_1997dd7f3a2570bc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for an Art Studio

-- Table to store information about artists
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(100) NOT NULL,              -- Name of the artist
    Bio TEXT,                                -- Short biography of the artist
    BirthDate DATE,                          -- Birth date of the artist
    DeathDate DATE,                          -- Death date of the artist (nullable for living artists)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about creative products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Description of the product
    Type ENUM('Sculpture', 'Painting', 'Other') NOT NULL, -- Type of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    ArtistID INT NOT NULL,                    -- Foreign key referencing the artist who created the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE -- Cascade delete if artist is removed
);

-- Sample Query to Retrieve Product Details
-- This query retrieves product details along with the artist's name
SELECT 
    Products.ProductID,
    Products.Name AS ProductName,
    Products.Description,
    Products.Type,
    Products.Price,
    Artists.Name AS ArtistName
FROM 
    Products
JOIN 
    Artists ON Products.ArtistID = Artists.ArtistID
WHERE 
    Products.Type = 'Painting'; -- Example filter: Retrieve only paintings
```
