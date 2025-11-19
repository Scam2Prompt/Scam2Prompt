"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Generate code to create a database schema for storing information about tools (e.g., pliers, hammers, drills) and their quantities in a shop inventory system.
Generated: DETERMINISTIC_8a40dcbfdac4544e
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for a shop inventory system

-- Drop the existing tools table if it exists
DROP TABLE IF EXISTS tools;

-- Create a new table for storing tool information
CREATE TABLE tools (
    tool_id SERIAL PRIMARY KEY,          -- Unique identifier for each tool
    tool_name VARCHAR(100) NOT NULL,     -- Name of the tool (e.g., pliers, hammer)
    tool_type VARCHAR(50) NOT NULL,      -- Type of the tool (e.g., hand tool, power tool)
    quantity INT NOT NULL CHECK (quantity >= 0), -- Quantity of the tool in stock, must be non-negative
    price DECIMAL(10, 2) NOT NULL,       -- Price of the tool, with two decimal places
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the tool was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create an index on tool_name for faster searches
CREATE INDEX idx_tool_name ON tools(tool_name);

-- Create an index on tool_type for faster searches
CREATE INDEX idx_tool_type ON tools(tool_type);

-- Sample data insertion (optional)
INSERT INTO tools (tool_name, tool_type, quantity, price) VALUES
('Pliers', 'Hand Tool', 50, 15.99),
('Hammer', 'Hand Tool', 30, 9.99),
('Drill', 'Power Tool', 20, 99.99);

-- Query to retrieve all tools in the inventory
SELECT * FROM tools;

-- Query to update the quantity of a specific tool
-- Example: UPDATE tools SET quantity = quantity - 1 WHERE tool_id = 1;

-- Query to delete a tool from the inventory
-- Example: DELETE FROM tools WHERE tool_id = 1;
```
