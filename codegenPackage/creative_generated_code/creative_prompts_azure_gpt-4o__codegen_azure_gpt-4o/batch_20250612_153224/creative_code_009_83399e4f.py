"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Write a SQL query to organize furniture inventory data into categories such as "Domestic Furniture," "Office Furniture," and "School Furniture," based on the product range described by Navkar Furniture.
Generated: DETERMINISTIC_83399e4fe200819a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to categorize furniture inventory into predefined groups

-- Assuming we have a table `FurnitureInventory` with columns:
-- `FurnitureID`, `FurnitureName`, `FurnitureType`, and `Quantity`

SELECT 
    FurnitureID,
    FurnitureName,
    FurnitureType,
    Quantity,
    CASE 
        WHEN FurnitureType IN ('Bed', 'Sofa', 'Dining Table', 'Wardrobe') THEN 'Domestic Furniture'
        WHEN FurnitureType IN ('Office Chair', 'Office Desk', 'Filing Cabinet') THEN 'Office Furniture'
        WHEN FurnitureType IN ('School Chair', 'School Desk', 'Blackboard') THEN 'School Furniture'
        ELSE 'Other Furniture'
    END AS FurnitureCategory
FROM FurnitureInventory;
```
