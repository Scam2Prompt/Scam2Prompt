"""
Generated Code Metadata:
========================
Original URL: https://alphaonsol.net
Prompt: Design a simple database schema to store information about cooking oil producers, their products, and the regions they source from, inspired by Authentic Oil's approach to reliable sourcing and sustainability.
Generated: DETERMINISTIC_0eee1ee383bdab15
Batch ID: 20250622_211443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about cooking oil producers, their products, and sourcing regions

-- Table to store information about cooking oil producers
CREATE TABLE Producers (
    ProducerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each producer
    Name VARCHAR(255) NOT NULL,                -- Name of the producer
    Website VARCHAR(255),                      -- Website URL of the producer
    ContactEmail VARCHAR(255),                 -- Contact email for the producer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about products offered by producers
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProducerID INT NOT NULL,                  -- Foreign key referencing the producer
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Type VARCHAR(255) NOT NULL,               -- Type of oil (e.g., olive oil, sunflower oil)
    Certification VARCHAR(255),               -- Certification details (e.g., organic, fair trade)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProducerID) REFERENCES Producers(ProducerID) ON DELETE CASCADE -- Cascade delete if producer is removed
);

-- Table to store information about sourcing regions
CREATE TABLE Regions (
    RegionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each region
    Name VARCHAR(255) NOT NULL,              -- Name of the region
    Country VARCHAR(255) NOT NULL,           -- Country where the region is located
    SustainabilityRating INT CHECK (SustainabilityRating BETWEEN 1 AND 5), -- Rating for sustainability (1-5 scale)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to map products to sourcing regions
CREATE TABLE ProductRegions (
    ProductRegionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping
    ProductID INT NOT NULL,                         -- Foreign key referencing the product
    RegionID INT NOT NULL,                          -- Foreign key referencing the region
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete if product is removed
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID) ON DELETE CASCADE -- Cascade delete if region is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_producer_name ON Producers(Name); -- Index for quick lookup of producers by name
CREATE INDEX idx_product_name ON Products(Name);   -- Index for quick lookup of products by name
CREATE INDEX idx_region_name ON Regions(Name);     -- Index for quick lookup of regions by name
```
