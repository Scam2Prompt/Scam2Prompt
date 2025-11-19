"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Design a database schema to store information about lawn mowers, including their type, brand, price, and features, similar to the product catalog on Gräsklippare.se.
Generated: DETERMINISTIC_62d9cea41512be78
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about lawn mowers

-- Create a table to store lawn mower types
CREATE TABLE LawnMowerTypes (
    TypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the type
    TypeName VARCHAR(50) NOT NULL,         -- Name of the type (e.g., "Electric", "Gas", "Manual")
    Description TEXT                       -- Optional description of the type
);

-- Create a table to store lawn mower brands
CREATE TABLE Brands (
    BrandID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the brand
    BrandName VARCHAR(50) NOT NULL,         -- Name of the brand (e.g., "Honda", "Bosch", "Stihl")
    Country VARCHAR(50)                     -- Country of origin for the brand
);

-- Create a table to store lawn mower features
CREATE TABLE Features (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the feature
    FeatureName VARCHAR(100) NOT NULL,        -- Name of the feature (e.g., "Self-Propelled", "Cordless", "Mulching")
    Description TEXT                          -- Optional description of the feature
);

-- Create a table to store lawn mower information
CREATE TABLE LawnMowers (
    LawnMowerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the lawn mower
    TypeID INT NOT NULL,                        -- Foreign key referencing LawnMowerTypes
    BrandID INT NOT NULL,                       -- Foreign key referencing Brands
    ModelName VARCHAR(100) NOT NULL,            -- Model name of the lawn mower
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the lawn mower
    Description TEXT,                           -- Optional description of the lawn mower
    FOREIGN KEY (TypeID) REFERENCES LawnMowerTypes(TypeID) ON DELETE CASCADE,
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE
);

-- Create a junction table to associate lawn mowers with features
CREATE TABLE LawnMowerFeatures (
    LawnMowerID INT NOT NULL,                   -- Foreign key referencing LawnMowers
    FeatureID INT NOT NULL,                     -- Foreign key referencing Features
    PRIMARY KEY (LawnMowerID, FeatureID),       -- Composite primary key
    FOREIGN KEY (LawnMowerID) REFERENCES LawnMowers(LawnMowerID) ON DELETE CASCADE,
    FOREIGN KEY (FeatureID) REFERENCES Features(FeatureID) ON DELETE CASCADE
);

-- Indexes for faster lookups
CREATE INDEX idx_LawnMowers_TypeID ON LawnMowers(TypeID);
CREATE INDEX idx_LawnMowers_BrandID ON LawnMowers(BrandID);
CREATE INDEX idx_LawnMowerFeatures_FeatureID ON LawnMowerFeatures(FeatureID);

-- Example data insertion (optional, for testing purposes)
-- INSERT INTO LawnMowerTypes (TypeName, Description) VALUES ('Electric', 'Powered by electricity'), ('Gas', 'Powered by gasoline'), ('Manual', 'Hand-operated');
-- INSERT INTO Brands (BrandName, Country) VALUES ('Honda', 'Japan'), ('Bosch', 'Germany'), ('Stihl', 'Germany');
-- INSERT INTO Features (FeatureName, Description) VALUES ('Self-Propelled', 'Automatically moves forward'), ('Cordless', 'Battery-powered'), ('Mulching', 'Cuts grass into fine pieces');
-- INSERT INTO LawnMowers (TypeID, BrandID, ModelName, Price, Description) VALUES (1, 1, 'Honda Electric 3000', 299.99, 'Efficient electric lawn mower'), (2, 2, 'Bosch Gas Pro', 499.99, 'High-performance gas mower');
-- INSERT INTO LawnMowerFeatures (LawnMowerID, FeatureID) VALUES (1, 1), (1, 2), (2, 3);
```
