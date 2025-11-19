"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Develop a sample database schema for a Professional Kitchen Management system that includes tables for food pricing, menu design, and chef responsibilities, as outlined in the courses at Hampton's.
Generated: DETERMINISTIC_040a2f3380345c75
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Professional Kitchen Management System Database Schema

-- Table: FoodPricing
-- Stores information about food items and their pricing
CREATE TABLE FoodPricing (
    FoodID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each food item
    FoodName VARCHAR(255) NOT NULL,         -- Name of the food item
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the food item
    Category VARCHAR(100),                  -- Category (e.g., Appetizer, Main Course, Dessert)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: MenuDesign
-- Stores menu information including the chef's recommendation and food items
CREATE TABLE MenuDesign (
    MenuID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the menu
    MenuName VARCHAR(255) NOT NULL,        -- Name of the menu
    Description TEXT,                      -- Description of the menu
    ChefRecommendation VARCHAR(255),      -- Recommended by chef (optional)
    FoodID INT NOT NULL,                   -- Foreign key referring to FoodPricing table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (FoodID) REFERENCES FoodPricing(FoodID) ON DELETE CASCADE
);

-- Table: ChefResponsibilities
-- Stores information about chefs and their assigned responsibilities
CREATE TABLE ChefResponsibilities (
    ChefID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each chef
    ChefName VARCHAR(255) NOT NULL,        -- Name of the chef
    Specialty VARCHAR(100),                -- Area of expertise or specialty
    AssignedMenuID INT,                    -- Foreign key referring to MenuDesign table
    ShiftTime ENUM('Morning', 'Afternoon', 'Evening', 'Night') NOT NULL, -- Working shift
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AssignedMenuID) REFERENCES MenuDesign(MenuID) ON DELETE SET NULL
);

-- Example Error Handling:
-- Ensure the FoodID entered in MenuDesign exists in FoodPricing table
DELIMITER //
CREATE TRIGGER ValidateFoodID
BEFORE INSERT ON MenuDesign
FOR EACH ROW
BEGIN
    DECLARE food_exists INT;
    SELECT COUNT(*) INTO food_exists FROM FoodPricing WHERE FoodID = NEW.FoodID;
    IF food_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'FoodID does not exist in FoodPricing table';
    END IF;
END;
//
DELIMITER ;

-- Additional Best Practices: Indexing
-- Create indexes for faster lookups on commonly queried fields
CREATE INDEX idx_food_category ON FoodPricing(Category);
CREATE INDEX idx_menu_name ON MenuDesign(MenuName);
CREATE INDEX idx_chef_specialty ON ChefResponsibilities(Specialty);
```
