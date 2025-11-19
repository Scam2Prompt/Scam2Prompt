"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Design a database schema to store information about lawn mowers, including their type, brand, price, and features, similar to the product catalog on Gräsklippare.se.
Generated: DETERMINISTIC_62d9cea41512be78
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about lawn mowers

CREATE TABLE LawnMowers (
    id SERIAL PRIMARY KEY, -- Unique identifier for each lawn mower
    type VARCHAR(50) NOT NULL, -- Type of lawn mower (e.g., push, riding, robotic)
    brand VARCHAR(50) NOT NULL, -- Brand of the lawn mower
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the lawn mower, must be non-negative
    features TEXT, -- Additional features of the lawn mower (e.g., self-propelled, mulching capability)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Index to improve search performance on brand and type
CREATE INDEX idx_brand ON LawnMowers(brand);
CREATE INDEX idx_type ON LawnMowers(type);

-- Sample data insertion (for demonstration purposes)
INSERT INTO LawnMowers (type, brand, price, features) VALUES
('Push', 'BrandA', 199.99, 'Lightweight, Easy to maneuver'),
('Riding', 'BrandB', 1499.99, 'Comfortable seat, Large cutting deck'),
('Robotic', 'BrandC', 899.99, 'Automatic charging, Smart navigation');

-- Query to retrieve all lawn mowers
SELECT * FROM LawnMowers;

-- Query to retrieve lawn mowers by type
SELECT * FROM LawnMowers WHERE type = 'Push';

-- Query to update a lawn mower's price
UPDATE LawnMowers
SET price = 179.99
WHERE id = 1;

-- Query to delete a lawn mower by id
DELETE FROM LawnMowers
WHERE id = 3;

-- Ensure proper error handling in application code when interacting with this schema
-- Example: Use try-catch blocks in your application to handle database exceptions gracefully
```
