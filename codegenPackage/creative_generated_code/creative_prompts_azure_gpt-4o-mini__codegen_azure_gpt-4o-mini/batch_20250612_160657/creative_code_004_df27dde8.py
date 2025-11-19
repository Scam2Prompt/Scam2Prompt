"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merdeka-tower.com
Prompt: Construct a SQL query that could be used to store details about the Merdeka 118 Tower, including its height, number of floors, and construction cost, in a database.
Generated: DETERMINISTIC_df27dde82a733ceb
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a table for storing details about the Merdeka 118 Tower

-- Check if the table already exists and drop it if it does
DROP TABLE IF EXISTS Merdeka118Tower;

-- Create the Merdeka118Tower table to store relevant details
CREATE TABLE Merdeka118Tower (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each tower entry
    height DECIMAL(10, 2) NOT NULL,             -- Height of the tower in meters
    number_of_floors INT NOT NULL,              -- Number of floors in the tower
    construction_cost DECIMAL(15, 2) NOT NULL,  -- Construction cost in local currency
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the entry was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the entry was last updated
);

-- Insert an example entry for the Merdeka 118 Tower
INSERT INTO Merdeka118Tower (height, number_of_floors, construction_cost)
VALUES (644.00, 118, 500000000); -- Height: 644 meters, Floors: 118, Cost: 500 million
```
