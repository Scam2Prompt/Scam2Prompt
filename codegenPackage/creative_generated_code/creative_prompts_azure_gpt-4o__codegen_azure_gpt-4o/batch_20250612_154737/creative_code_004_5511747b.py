"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grants-archive-cf.webflow.io
Prompt: Write a SQL query to store and retrieve Gitcoin Grants round data, including fields like round name, funding amount, and grantee count, for analysis.
Generated: DETERMINISTIC_5511747be58c5d67
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store Gitcoin Grants round data
CREATE TABLE GitcoinGrantsRound (
    round_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each round
    round_name VARCHAR(255) NOT NULL,        -- Name of the Gitcoin Grants round
    funding_amount DECIMAL(15, 2) NOT NULL,  -- Total funding amount for the round
    grantee_count INT NOT NULL,              -- Number of grantees in the round
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of entry creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Insert data into the table
INSERT INTO GitcoinGrantsRound (round_name, funding_amount, grantee_count)
VALUES 
    ('Round 1', 100000.00, 50), 
    ('Round 2', 200000.00, 75), 
    ('Round 3', 150000.00, 60);

-- Query to retrieve Gitcoin Grants round data for analysis
SELECT 
    round_id,
    round_name,
    funding_amount,
    grantee_count,
    created_at,
    updated_at
FROM 
    GitcoinGrantsRound
ORDER BY 
    created_at DESC; -- Retrieve data in descending order of creation

-- Query to analyze funding per grantee for each round
SELECT 
    round_id,
    round_name,
    funding_amount,
    grantee_count,
    (funding_amount / grantee_count) AS funding_per_grantee
FROM 
    GitcoinGrantsRound
ORDER BY 
    round_id ASC; -- Retrieve data sorted by round ID for clarity
```
