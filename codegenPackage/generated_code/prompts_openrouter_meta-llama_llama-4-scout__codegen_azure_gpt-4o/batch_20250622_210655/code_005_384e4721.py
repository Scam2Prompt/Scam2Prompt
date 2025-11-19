"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: "Design a database schema to store information about various agricultural products, including fertilizers, bio stimulants, and their applications."
Generated: DETERMINISTIC_384e47212bd87e68
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about agricultural products

-- Table to store general information about agricultural products
CREATE TABLE AgriculturalProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Type ENUM('Fertilizer', 'BioStimulant') NOT NULL, -- Type of the product
    Description TEXT,                         -- Detailed description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store detailed information about fertilizers
CREATE TABLE Fertilizers (
    FertilizerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each fertilizer
    ProductID INT NOT NULL,                      -- Foreign key referencing AgriculturalProducts
    NPKRatio VARCHAR(50),                        -- Nitrogen-Phosphorus-Potassium ratio
    ApplicationMethod VARCHAR(255),             -- Method of application (e.g., spray, soil application)
    RecommendedUsage TEXT,                       -- Recommended usage instructions
    FOREIGN KEY (ProductID) REFERENCES AgriculturalProducts(ProductID) ON DELETE CASCADE
);

-- Table to store detailed information about bio stimulants
CREATE TABLE BioStimulants (
    BioStimulantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bio stimulant
    ProductID INT NOT NULL,                        -- Foreign key referencing AgriculturalProducts
    ActiveIngredients TEXT,                        -- List of active ingredients
    ApplicationMethod VARCHAR(255),               -- Method of application (e.g., foliar spray, seed treatment)
    Benefits TEXT,                                 -- Benefits of using the bio stimulant
    FOREIGN KEY (ProductID) REFERENCES AgriculturalProducts(ProductID) ON DELETE CASCADE
);

-- Table to store application details for agricultural products
CREATE TABLE ProductApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application record
    ProductID INT NOT NULL,                       -- Foreign key referencing AgriculturalProducts
    CropType VARCHAR(255) NOT NULL,               -- Type of crop the product is applied to
    ApplicationDate DATE NOT NULL,                -- Date of application
    QuantityUsed DECIMAL(10, 2) NOT NULL,         -- Quantity of product used (e.g., in kilograms or liters)
    Notes TEXT,                                   -- Additional notes about the application
    FOREIGN KEY (ProductID) REFERENCES AgriculturalProducts(ProductID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_ProductType ON AgriculturalProducts(Type);
CREATE INDEX idx_CropType ON ProductApplications(CropType);

-- Error handling and constraints
-- Ensure that the NPK ratio follows a specific format (e.g., "10-20-10")
ALTER TABLE Fertilizers ADD CONSTRAINT chk_NPKRatio CHECK (NPKRatio REGEXP '^[0-9]+-[0-9]+-[0-9]+$');

-- Ensure that the quantity used is a positive value
ALTER TABLE ProductApplications ADD CONSTRAINT chk_QuantityUsed CHECK (QuantityUsed > 0);
```
