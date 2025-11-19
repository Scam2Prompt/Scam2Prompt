"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Create a database schema for storing hot tub models, features, and pricing information, including brands like Jacuzzi®, Dream Maker Spas™, and Dimension One Spas®, as listed on the Oasis Hot Tubs site.
Generated: DETERMINISTIC_1765e0fd1fa0a3c7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing hot tub models, features, and pricing information

-- Create a table for brands
CREATE TABLE Brands (
    BrandID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each brand
    BrandName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the brand
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Create a table for hot tub models
CREATE TABLE HotTubModels (
    ModelID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each hot tub model
    BrandID INT NOT NULL,  -- Foreign key referencing the Brands table
    ModelName VARCHAR(100) NOT NULL,  -- Name of the hot tub model
    Description TEXT,  -- Description of the hot tub model
    Price DECIMAL(10, 2) NOT NULL,  -- Price of the hot tub model
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for record updates
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for features
CREATE TABLE Features (
    FeatureID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each feature
    FeatureName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the feature
    Description TEXT,  -- Description of the feature
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Create a junction table to associate hot tub models with features
CREATE TABLE HotTubModelFeatures (
    ModelID INT NOT NULL,  -- Foreign key referencing the HotTubModels table
    FeatureID INT NOT NULL,  -- Foreign key referencing the Features table
    PRIMARY KEY (ModelID, FeatureID),  -- Composite primary key
    FOREIGN KEY (ModelID) REFERENCES HotTubModels(ModelID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (FeatureID) REFERENCES Features(FeatureID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion for Brands
INSERT INTO Brands (BrandName) VALUES 
('Jacuzzi®'), 
('Dream Maker Spas™'), 
('Dimension One Spas®');

-- Sample data insertion for Features
INSERT INTO Features (FeatureName, Description) VALUES 
('Heater', 'Provides warm water for a comfortable experience'), 
('LED Lighting', 'Colorful lights for ambiance'), 
('Waterfall', 'A soothing waterfall feature');

-- Sample data insertion for Hot Tub Models
INSERT INTO HotTubModels (BrandID, ModelName, Description, Price) VALUES 
(1, 'J-300 Series', 'A versatile hot tub with various seating options.', 7999.99), 
(2, 'Dream Maker 300', 'Compact and efficient for small spaces.', 4999.99), 
(3, 'Dimension One Aurora', 'Luxury hot tub with advanced features.', 10999.99);

-- Sample data insertion for Hot Tub Model Features
INSERT INTO HotTubModelFeatures (ModelID, FeatureID) VALUES 
(1, 1),  -- J-300 Series has Heater
(1, 2),  -- J-300 Series has LED Lighting
(2, 1),  -- Dream Maker 300 has Heater
(3, 1),  -- Dimension One Aurora has Heater
(3, 2),  -- Dimension One Aurora has LED Lighting
(3, 3);  -- Dimension One Aurora has Waterfall
```
