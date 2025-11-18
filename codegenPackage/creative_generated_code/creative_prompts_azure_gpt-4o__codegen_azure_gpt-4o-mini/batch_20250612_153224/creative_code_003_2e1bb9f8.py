"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Create a database schema for storing fishing reel details, including models like "Old School 1" and "Trout 1 Large," along with their price and line class information as listed on Emanuelson Reels.
Generated: DETERMINISTIC_2e1bb9f88309ae36
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing fishing reel details

CREATE DATABASE FishingReelsDB;

USE FishingReelsDB;

-- Table to store details of fishing reels
CREATE TABLE FishingReels (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reel
    model VARCHAR(100) NOT NULL,       -- Model name of the reel
    price DECIMAL(10, 2) NOT NULL,     -- Price of the reel, with two decimals
    line_class VARCHAR(50) NOT NULL,   -- Line class information (e.g., 4-8 lb, 10-15 lb)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    CONSTRAINT unique_model UNIQUE (model) -- Ensures each model name is unique
);

-- Example entry for "Old School 1" and "Trout 1 Large"
INSERT INTO FishingReels (model, price, line_class) VALUES
('Old School 1', 49.99, '6-10 lb'),
('Trout 1 Large', 89.99, '8-12 lb');

-- Select statement to view all fishing reels
SELECT * FROM FishingReels;

-- Error handling and best practices:
-- Always use prepared statements for any dynamic queries to avoid SQL injection.
-- Implement application-level validation to ensure that prices and line classes conform to expected formats.
-- Regularly backup the database to prevent data loss.
-- Monitor and optimize database performance as needed.
```
