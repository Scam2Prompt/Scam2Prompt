"""
Generated Code Metadata:
========================
Original URL: https://starklinical.com.br
Prompt: "Design a database schema to store information about different types of furniture products, including hospital, school, and auditorium furniture, for a company like Starklinical."
Generated: DETERMINISTIC_4af8ff05ce5ce451
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about different types of furniture products
-- for a company like Starklinical.

-- Table to store general product information
CREATE TABLE FurnitureProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the furniture product
    Description TEXT,                         -- Detailed description of the product
    Category ENUM('Hospital', 'School', 'Auditorium') NOT NULL, -- Category of furniture
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store dimensions of furniture products
CREATE TABLE FurnitureDimensions (
    DimensionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for dimensions
    ProductID INT NOT NULL,                     -- Foreign key referencing FurnitureProducts
    Length DECIMAL(10, 2) NOT NULL,             -- Length of the furniture in cm
    Width DECIMAL(10, 2) NOT NULL,              -- Width of the furniture in cm
    Height DECIMAL(10, 2) NOT NULL,             -- Height of the furniture in cm
    Weight DECIMAL(10, 2),                      -- Weight of the furniture in kg
    FOREIGN KEY (ProductID) REFERENCES FurnitureProducts(ProductID) ON DELETE CASCADE
);

-- Table to store materials used in furniture products
CREATE TABLE FurnitureMaterials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for materials
    ProductID INT NOT NULL,                    -- Foreign key referencing FurnitureProducts
    MaterialName VARCHAR(255) NOT NULL,        -- Name of the material (e.g., wood, metal, plastic)
    Quantity DECIMAL(10, 2),                   -- Quantity of the material used
    FOREIGN KEY (ProductID) REFERENCES FurnitureProducts(ProductID) ON DELETE CASCADE
);

-- Table to store additional attributes specific to furniture categories
CREATE TABLE FurnitureAttributes (
    AttributeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for attributes
    ProductID INT NOT NULL,                     -- Foreign key referencing FurnitureProducts
    AttributeName VARCHAR(255) NOT NULL,        -- Name of the attribute (e.g., "Number of Seats")
    AttributeValue VARCHAR(255) NOT NULL,       -- Value of the attribute (e.g., "4")
    FOREIGN KEY (ProductID) REFERENCES FurnitureProducts(ProductID) ON DELETE CASCADE
);

-- Table to store images of furniture products
CREATE TABLE FurnitureImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for images
    ProductID INT NOT NULL,                 -- Foreign key referencing FurnitureProducts
    ImageURL VARCHAR(2083) NOT NULL,        -- URL of the image
    AltText VARCHAR(255),                   -- Alternative text for the image
    FOREIGN KEY (ProductID) REFERENCES FurnitureProducts(ProductID) ON DELETE CASCADE
);

-- Table to store reviews for furniture products
CREATE TABLE FurnitureReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for reviews
    ProductID INT NOT NULL,                  -- Foreign key referencing FurnitureProducts
    ReviewerName VARCHAR(255) NOT NULL,      -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the reviewer (1 to 5)
    ReviewText TEXT,                         -- Review text
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (ProductID) REFERENCES FurnitureProducts(ProductID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_category ON FurnitureProducts(Category); -- Index for category filtering
CREATE INDEX idx_price ON FurnitureProducts(Price);       -- Index for price filtering
CREATE INDEX idx_stock ON FurnitureProducts(Stock);       -- Index for stock filtering
```
