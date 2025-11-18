"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Create a database schema in SQL for storing tool information, including fields for "brand," "price," "category," and "availability," inspired by the Anhanguera Ferramentas catalog.
Generated: DETERMINISTIC_b7873237fd7f1ef8
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the database schema for storing tool information
CREATE TABLE Tools (
    -- Unique identifier for each tool
    ToolID INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Name of the brand/manufacturer of the tool
    Brand VARCHAR(100) NOT NULL,
    
    -- Price of the tool
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Ensures non-negative values for price
    
    -- Category of the tool (e.g., drill, saw, etc.)
    Category VARCHAR(100) NOT NULL,
    
    -- Availability status (e.g., 'In Stock', 'Out of Stock')
    Availability ENUM('In Stock', 'Out of Stock') NOT NULL,
    
    -- Timestamp for when the tool record was created
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Timestamp for the last update to the tool record
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create an index on the 'Category' field for faster searches
CREATE INDEX idx_category ON Tools (Category);

-- Create an index on the 'Brand' field for faster searches
CREATE INDEX idx_brand ON Tools (Brand);

-- Example error handling: Ensure the table is not created if it already exists
-- To safely create the table only if it doesn't exist
-- (Uncomment the following and remove the CREATE TABLE block above if applicable)
-- CREATE TABLE IF NOT EXISTS Tools (
--     ... [same schema as above]
-- );
```
