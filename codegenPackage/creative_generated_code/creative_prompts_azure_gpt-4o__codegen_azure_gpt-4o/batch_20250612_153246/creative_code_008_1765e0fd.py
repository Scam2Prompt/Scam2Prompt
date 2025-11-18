"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.oasishottubsep.com
Prompt: Create a database schema for storing hot tub models, features, and pricing information, including brands like Jacuzzi®, Dream Maker Spas™, and Dimension One Spas®, as listed on the Oasis Hot Tubs site.
Generated: DETERMINISTIC_1765e0fd1fa0a3c7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing hot tub models, features, brands, and pricing information

-- Create table for brands
CREATE TABLE Brands (
    BrandID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each brand
    BrandName VARCHAR(255) NOT NULL,        -- Name of the brand (e.g., Jacuzzi®, Dream Maker Spas™, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create table for hot tub models
CREATE TABLE HotTubModels (
    ModelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each hot tub model
    BrandID INT NOT NULL,                   -- Foreign key referencing Brands
    ModelName VARCHAR(255) NOT NULL,        -- Name of the model
    SeatingCapacity INT,                    -- Number of people the hot tub can seat
    Dimensions VARCHAR(255),                -- Dimensions of the hot tub (e.g., "84x84x36 inches")
    Weight INT,                             -- Weight of the hot tub in pounds
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintain referential integrity
);

-- Create table for features
CREATE TABLE Features (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feature
    FeatureName VARCHAR(255) NOT NULL,        -- Name of the feature (e.g., "LED Lighting", "Waterfall", etc.)
    Description TEXT,                         -- Detailed description of the feature
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create table for linking hot tub models and their features (many-to-many relationship)
CREATE TABLE ModelFeatures (
    ModelID INT NOT NULL,                    -- Foreign key referencing HotTubModels
    FeatureID INT NOT NULL,                  -- Foreign key referencing Features
    PRIMARY KEY (ModelID, FeatureID),        -- Composite primary key
    FOREIGN KEY (ModelID) REFERENCES HotTubModels(ModelID) ON DELETE CASCADE ON UPDATE CASCADE, -- Maintain referential integrity
    FOREIGN KEY (FeatureID) REFERENCES Features(FeatureID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintain referential integrity
);

-- Create table for pricing information
CREATE TABLE Pricing (
    PricingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each pricing record
    ModelID INT NOT NULL,                     -- Foreign key referencing HotTubModels
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the hot tub (e.g., 9999.99)
    Currency VARCHAR(3) NOT NULL DEFAULT 'USD', -- Currency code (e.g., "USD", "EUR")
    EffectiveDate DATE NOT NULL,              -- Date when this pricing becomes effective
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ModelID) REFERENCES HotTubModels(ModelID) ON DELETE CASCADE ON UPDATE CASCADE -- Maintain referential integrity
);

-- Example indexes for optimizing queries
CREATE INDEX idx_BrandName ON Brands (BrandName); -- Index for searching brands by name
CREATE INDEX idx_ModelName ON HotTubModels (ModelName); -- Index for searching hot tub models by name
CREATE INDEX idx_FeatureName ON Features (FeatureName); -- Index for searching features by name
CREATE INDEX idx_Price ON Pricing (Price); -- Index for filtering hot tubs by price
```
