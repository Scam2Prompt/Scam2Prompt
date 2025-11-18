"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.punpuntoy.com
Prompt: Create a database schema for managing playground equipment inventory, including fields for product types like mini gyms, pet playgrounds, and soft flooring, as described on the Pun Pun Toy website.
Generated: DETERMINISTIC_00f10b04c71ca650
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing playground equipment inventory

-- Drop the existing table if it exists
DROP TABLE IF EXISTS PlaygroundEquipment;

-- Create a table to store playground equipment inventory
CREATE TABLE PlaygroundEquipment (
    EquipmentID SERIAL PRIMARY KEY,         -- Unique identifier for each equipment
    ProductType VARCHAR(50) NOT NULL,      -- Type of playground equipment (e.g., mini gyms, pet playgrounds, soft flooring)
    Description TEXT,                       -- Detailed description of the equipment
    Quantity INT NOT NULL CHECK (Quantity >= 0),  -- Number of items available in inventory, cannot be negative
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price per item, cannot be negative
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the equipment was added to the inventory
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Date when the equipment details were last updated
);

-- Create index for faster searches on ProductType
CREATE INDEX idx_product_type ON PlaygroundEquipment(ProductType);

-- Sample data insertion for initial setup
INSERT INTO PlaygroundEquipment (ProductType, Description, Quantity, Price)
VALUES
    ('Mini Gym', 'A fun and safe mini gym for toddlers.', 10, 299.99),
    ('Pet Playground', 'A playground designed specifically for pets.', 5, 399.99),
    ('Soft Flooring', 'Soft flooring mats for safe play areas.', 20, 49.99);

-- Function to retrieve all playground equipment from the inventory
CREATE OR REPLACE FUNCTION GetAllEquipment()
RETURNS TABLE (EquipmentID INT, ProductType VARCHAR, Description TEXT, Quantity INT, Price DECIMAL, DateAdded TIMESTAMP, LastUpdated TIMESTAMP) AS $$
BEGIN
    RETURN QUERY SELECT * FROM PlaygroundEquipment;
END;
$$ LANGUAGE plpgsql;

-- Error handling for data insertion
CREATE OR REPLACE FUNCTION AddEquipment(
    p_ProductType VARCHAR,
    p_Description TEXT,
    p_Quantity INT,
    p_Price DECIMAL
) RETURNS VOID AS $$
BEGIN
    INSERT INTO PlaygroundEquipment (ProductType, Description, Quantity, Price)
    VALUES (p_ProductType, p_Description, p_Quantity, p_Price);
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Equipment with the product type "%" already exists.', p_ProductType;
    WHEN others THEN
        RAISE EXCEPTION 'An error occurred while adding equipment: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Function to update existing equipment details
CREATE OR REPLACE FUNCTION UpdateEquipment(
    p_EquipmentID INT,
    p_ProductType VARCHAR,
    p_Description TEXT,
    p_Quantity INT,
    p_Price DECIMAL
) RETURNS VOID AS $$
BEGIN
    UPDATE PlaygroundEquipment
    SET ProductType = p_ProductType,
        Description = p_Description,
        Quantity = p_Quantity,
        Price = p_Price
    WHERE EquipmentID = p_EquipmentID;
EXCEPTION
    WHEN no_data_found THEN
        RAISE NOTICE 'No equipment found with ID %.', p_EquipmentID;
    WHEN others THEN
        RAISE EXCEPTION 'An error occurred while updating equipment: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Function to delete equipment from inventory
CREATE OR REPLACE FUNCTION DeleteEquipment(p_EquipmentID INT)
RETURNS VOID AS $$
BEGIN
    DELETE FROM PlaygroundEquipment WHERE EquipmentID = p_EquipmentID;
EXCEPTION
    WHEN no_data_found THEN
        RAISE NOTICE 'No equipment found with ID % for deletion.', p_EquipmentID;
    WHEN others THEN
        RAISE EXCEPTION 'An error occurred while deleting equipment: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;
```
