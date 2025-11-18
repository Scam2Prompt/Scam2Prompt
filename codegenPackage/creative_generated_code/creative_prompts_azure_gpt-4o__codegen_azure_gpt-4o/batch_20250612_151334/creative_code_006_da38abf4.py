"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Develop a SQL query to store and retrieve tire product data, including width, height, rim size, and price, as structured on the "Dal Cortivo Pneus" website.
Generated: DETERMINISTIC_da38abf496379e02
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store tire product data
CREATE TABLE IF NOT EXISTS TireProducts (
    id INT AUTO_INCREMENT PRIMARY KEY,                -- Unique identifier for each tire product
    width INT NOT NULL,                               -- Tire width (e.g., 205)
    height INT NOT NULL,                              -- Tire height (e.g., 55)
    rim_size INT NOT NULL,                            -- Rim size (e.g., 16)
    price DECIMAL(10, 2) NOT NULL,                    -- Price of the tire (e.g., 120.50)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP    -- Timestamp to track when the record was created
);

-- Insert sample tire product data
INSERT INTO TireProducts (width, height, rim_size, price)
VALUES 
    (205, 55, 16, 120.50),
    (225, 45, 17, 150.75),
    (195, 60, 15, 100.00),
    (215, 50, 16, 130.99);

-- Retrieve tire product data with filtering and sorting
-- Example: Retrieve tires with width >= 200, ordered by price in ascending order
SELECT 
    id,
    width,
    height,
    rim_size,
    price
FROM 
    TireProducts
WHERE 
    width >= 200                                      -- Filter for tire width greater than or equal to 200
ORDER BY 
    price ASC;                                        -- Sort results by price in ascending order

-- Error handling should be implemented at the application level when interacting with this query
-- Ensure proper validation and sanitization of user inputs to prevent SQL injection vulnerabilities.
```
