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
CREATE TABLE gitcoin_grants_rounds (
    id SERIAL PRIMARY KEY,          -- Unique identifier for each round
    round_name VARCHAR(255) NOT NULL,  -- Name of the round
    funding_amount DECIMAL(15, 2) NOT NULL,  -- Total funding amount for the round
    grantee_count INT NOT NULL,     -- Number of grantees in the round
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    UNIQUE (round_name)             -- Ensure round names are unique
);

-- Function to insert a new Gitcoin Grants round
CREATE OR REPLACE FUNCTION insert_grants_round(
    p_round_name VARCHAR,
    p_funding_amount DECIMAL,
    p_grantee_count INT
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO gitcoin_grants_rounds (round_name, funding_amount, grantee_count)
    VALUES (p_round_name, p_funding_amount, p_grantee_count);
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Round with name "%" already exists. Please use a unique name.', p_round_name;
    WHEN others THEN
        RAISE EXCEPTION 'An error occurred while inserting the round: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Function to retrieve all Gitcoin Grants rounds
CREATE OR REPLACE FUNCTION get_grants_rounds()
RETURNS TABLE (
    id INT,
    round_name VARCHAR,
    funding_amount DECIMAL,
    grantee_count INT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
) AS $$
BEGIN
    RETURN QUERY
    SELECT id, round_name, funding_amount, grantee_count, created_at, updated_at
    FROM gitcoin_grants_rounds;
END;
$$ LANGUAGE plpgsql;

-- Example usage
-- Inserting a new round (ensure the round name is unique)
SELECT insert_grants_round('Round 1', 100000.00, 5);

-- Retrieving all rounds for analysis
SELECT * FROM get_grants_rounds();
```
