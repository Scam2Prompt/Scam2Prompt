"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Design a simple database schema to store information about fishing reels, including models like Old School 1, Trout 2, and Salmon, with their respective line classes and prices."
Generated: DETERMINISTIC_e669ead2cc872023
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about fishing reels

-- Create a table to store fishing reel information
CREATE TABLE FishingReels (
    ReelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reel
    ModelName VARCHAR(100) NOT NULL,       -- Name of the reel model (e.g., Old School 1, Trout 2, Salmon)
    LineClass VARCHAR(50) NOT NULL,        -- Line class associated with the reel (e.g., light, medium, heavy)
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the reel in decimal format (e.g., 99.99)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Insert sample data into the FishingReels table
INSERT INTO FishingReels (ModelName, LineClass, Price)
VALUES 
    ('Old School 1', 'Light', 49.99),
    ('Trout 2', 'Medium', 79.99),
    ('Salmon', 'Heavy', 129.99);

-- Query to retrieve all fishing reels
SELECT * FROM FishingReels;

-- Query to retrieve fishing reels within a specific price range
SELECT * FROM FishingReels
WHERE Price BETWEEN 50 AND 100;

-- Query to update the price of a specific reel
UPDATE FishingReels
SET Price = 89.99
WHERE ModelName = 'Trout 2';

-- Query to delete a reel by its ID
DELETE FROM FishingReels
WHERE ReelID = 3;

-- Ensure proper indexing for faster queries
CREATE INDEX idx_model_name ON FishingReels (ModelName);
CREATE INDEX idx_price ON FishingReels (Price);
```
