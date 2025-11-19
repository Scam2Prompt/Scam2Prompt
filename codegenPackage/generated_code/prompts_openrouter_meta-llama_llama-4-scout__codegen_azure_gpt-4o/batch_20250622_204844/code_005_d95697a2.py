"""
Generated Code Metadata:
========================
Original URL: https://thechampionsshop.com
Prompt: Design a database schema to store information about wrestling belts, including title names, promotions, materials, and prices, similar to The Champions Shop catalog.
Generated: DETERMINISTIC_d95697a2d40fcacd
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about wrestling belts

-- Table to store promotions (e.g., WWE, AEW, NJPW)
CREATE TABLE Promotions (
    PromotionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each promotion
    Name VARCHAR(255) NOT NULL,                 -- Name of the promotion
    Country VARCHAR(100),                       -- Country of origin for the promotion
    EstablishedYear INT,                        -- Year the promotion was established
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store wrestling belt titles
CREATE TABLE WrestlingBelts (
    BeltID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each belt
    TitleName VARCHAR(255) NOT NULL,            -- Name of the wrestling belt title
    PromotionID INT NOT NULL,                   -- Foreign key linking to Promotions table
    Material VARCHAR(255),                      -- Material used for the belt (e.g., leather, gold)
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the belt
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (PromotionID) REFERENCES Promotions(PromotionID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store additional details about belt materials
CREATE TABLE BeltMaterials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each material
    MaterialName VARCHAR(255) NOT NULL,         -- Name of the material (e.g., leather, gold, silver)
    Description TEXT,                           -- Description of the material
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to associate belts with multiple materials (many-to-many relationship)
CREATE TABLE BeltMaterialMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each mapping
    BeltID INT NOT NULL,                        -- Foreign key linking to WrestlingBelts table
    MaterialID INT NOT NULL,                    -- Foreign key linking to BeltMaterials table
    Quantity INT DEFAULT 1,                     -- Quantity of the material used in the belt
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (BeltID) REFERENCES WrestlingBelts(BeltID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (MaterialID) REFERENCES BeltMaterials(MaterialID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_promotion_name ON Promotions(Name);
CREATE INDEX idx_belt_title_name ON WrestlingBelts(TitleName);
CREATE INDEX idx_material_name ON BeltMaterials(MaterialName);
```
