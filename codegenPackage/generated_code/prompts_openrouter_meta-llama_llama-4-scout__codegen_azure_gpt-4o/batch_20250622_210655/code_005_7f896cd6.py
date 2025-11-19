"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Write a SQL query to design a database schema for storing information about various spices, their nutritional content, and pricing, similar to Ratnaraj Foods' product range.
Generated: DETERMINISTIC_7f896cd691dbc375
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing information about spices, their nutritional content, and pricing

-- Create a table to store information about spices
CREATE TABLE Spices (
    SpiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each spice
    Name VARCHAR(100) NOT NULL,             -- Name of the spice
    Description TEXT,                       -- Description of the spice
    Origin VARCHAR(100),                    -- Country or region of origin
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store nutritional content for each spice
CREATE TABLE NutritionalContent (
    NutritionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each nutritional record
    SpiceID INT NOT NULL,                       -- Foreign key referencing Spices table
    Calories DECIMAL(10, 2),                    -- Calories per serving
    Protein DECIMAL(10, 2),                     -- Protein content per serving (grams)
    Fat DECIMAL(10, 2),                         -- Fat content per serving (grams)
    Carbohydrates DECIMAL(10, 2),               -- Carbohydrates per serving (grams)
    Fiber DECIMAL(10, 2),                       -- Fiber content per serving (grams)
    Sodium DECIMAL(10, 2),                      -- Sodium content per serving (milligrams)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (SpiceID) REFERENCES Spices(SpiceID) ON DELETE CASCADE -- Ensure data integrity
);

-- Create a table to store pricing information for each spice
CREATE TABLE Pricing (
    PriceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each pricing record
    SpiceID INT NOT NULL,                   -- Foreign key referencing Spices table
    Price DECIMAL(10, 2) NOT NULL,          -- Price per unit (e.g., per kilogram)
    Currency VARCHAR(10) NOT NULL,          -- Currency of the price (e.g., USD, EUR)
    EffectiveDate DATE NOT NULL,            -- Date when the price becomes effective
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (SpiceID) REFERENCES Spices(SpiceID) ON DELETE CASCADE -- Ensure data integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_spices_name ON Spices(Name); -- Index for quick lookup by spice name
CREATE INDEX idx_pricing_effective_date ON Pricing(EffectiveDate); -- Index for quick lookup by effective date

-- Error handling and constraints
-- Ensure that the price is always positive
ALTER TABLE Pricing ADD CONSTRAINT chk_price_positive CHECK (Price > 0);

-- Ensure that nutritional values are non-negative
ALTER TABLE NutritionalContent ADD CONSTRAINT chk_nutrition_non_negative CHECK (
    Calories >= 0 AND Protein >= 0 AND Fat >= 0 AND Carbohydrates >= 0 AND Fiber >= 0 AND Sodium >= 0
);
```
