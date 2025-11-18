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
-- SQL script to create a database schema for storing tool information

-- Drop the table if it already exists for re-creation
DROP TABLE IF EXISTS Tools;

-- Create the Tools table to store information about various tools
CREATE TABLE Tools (
    ToolID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each tool
    Brand VARCHAR(100) NOT NULL,               -- Brand name of the tool
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the tool, must be non-negative
    Category VARCHAR(100) NOT NULL,            -- Category of the tool (e.g., Hand tools, Power tools)
    Availability BOOLEAN NOT NULL DEFAULT TRUE, -- Availability status (TRUE = available, FALSE = out of stock)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Sample insert statements for testing purposes
INSERT INTO Tools (Brand, Price, Category, Availability) VALUES
('Bosch', 99.99, 'Power Tools', TRUE),
('Makita', 79.49, 'Hand Tools', TRUE),
('DeWalt', 120.00, 'Power Tools', FALSE),
('Stanley', 25.75, 'Hand Tools', TRUE);

-- Query to check inserted data
SELECT * FROM Tools;
```
