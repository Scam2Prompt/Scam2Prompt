"""
Generated Code Metadata:
========================
Original URL: https://tante4dx43.com
Prompt: Create a database schema for storing lottery results (e.g., HK Siang, Singapore, Malaysia) as shown on TANTE4D, including date and result fields.
Generated: DETERMINISTIC_631d56645d7424e6
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing lottery results
CREATE DATABASE IF NOT EXISTS LotteryResults;

USE LotteryResults;

-- Table to store lottery results
CREATE TABLE IF NOT EXISTS Lottery (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each lottery entry
    lottery_name VARCHAR(50) NOT NULL,  -- Name of the lottery (e.g., HK Siang, Singapore, Malaysia)
    draw_date DATE NOT NULL,             -- Date of the lottery draw
    result VARCHAR(255) NOT NULL,        -- Result of the lottery draw (e.g., winning numbers)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the entry was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    UNIQUE KEY unique_lottery (lottery_name, draw_date)  -- Ensure no duplicate entries for the same lottery and date
);

-- Example of inserting a lottery result
INSERT INTO Lottery (lottery_name, draw_date, result) VALUES
('HK Siang', '2023-10-01', '12345'),
('Singapore', '2023-10-01', '67890'),
('Malaysia', '2023-10-01', '54321');

-- Query to retrieve all lottery results
SELECT * FROM Lottery ORDER BY draw_date DESC;

-- Query to retrieve results for a specific lottery
SELECT * FROM Lottery WHERE lottery_name = 'HK Siang' ORDER BY draw_date DESC;

-- Query to delete a specific lottery result by ID
DELETE FROM Lottery WHERE id = ?;  -- Replace ? with the specific ID to delete
```
