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
-- Creating a database schema for storing fishing reel details
-- This schema includes tables for reels with their models, price, and line class information.

-- Table to store fishing reel details
CREATE TABLE FishingReels (
    ReelID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each reel
    ModelName VARCHAR(255) NOT NULL,                 -- Name of the reel model (e.g., "Old School 1", "Trout 1 Large")
    Price DECIMAL(10, 2) NOT NULL,                   -- Price of the reel (stored as monetary value)
    LineClass VARCHAR(255) NOT NULL,                 -- Line class information for the reel
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the entry is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the entry is last updated
);

-- Adding an index to optimize searches based on the ModelName
CREATE INDEX idx_model_name ON FishingReels (ModelName);

-- Example of inserting a record into the FishingReels table
-- INSERT INTO FishingReels (ModelName, Price, LineClass)
-- VALUES ('Old School 1', 299.99, '10-20 lb'), ('Trout 1 Large', 149.99, '5-10 lb');
```
