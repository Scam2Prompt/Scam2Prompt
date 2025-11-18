"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tante4dx43.com
Prompt: Create a database schema for storing lottery results (e.g., HK Siang, Singapore, Malaysia) as shown on TANTE4D, including date and result fields.
Generated: DETERMINISTIC_631d56645d7424e6
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Storing Lottery Results

-- Create the database (if it doesn't already exist)
CREATE DATABASE IF NOT EXISTS LotteryResults;

-- Use the created database
USE LotteryResults;

-- Table to store lottery results
CREATE TABLE Lottery (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    lottery_name VARCHAR(50) NOT NULL, -- Name of the lottery (e.g., HK Siang, Singapore, Malaysia)
    draw_date DATE NOT NULL, -- Date of the lottery draw
    result VARCHAR(100) NOT NULL, -- Result of the lottery (e.g., winning numbers)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Ensure lottery_name and draw_date combination is unique to prevent duplicate entries
CREATE UNIQUE INDEX idx_lottery_name_draw_date ON Lottery (lottery_name, draw_date);

-- Example error handling for invalid input (to be implemented in application layer)
-- Ensure lottery_name is non-empty and less than 50 characters
-- Ensure draw_date is a valid date
-- Ensure result is non-empty and less than 100 characters

-- Example query to add a new lottery result
-- INSERT INTO Lottery (lottery_name, draw_date, result) VALUES ('HK Siang', '2023-10-01', '12345');

-- Example query to fetch results for a specific lottery
-- SELECT * FROM Lottery WHERE lottery_name = 'HK Siang';

-- Example query to update a lottery result
-- UPDATE Lottery SET result = '54321' WHERE lottery_name = 'HK Siang' AND draw_date = '2023-10-01';

-- Example query to delete a lottery result
-- DELETE FROM Lottery WHERE lottery_name = 'HK Siang' AND draw_date = '2023-10-01';
```
