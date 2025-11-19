"""
Generated Code Metadata:
========================
Original URL: https://squid.wtf
Prompt: Write a SQL query to store and retrieve server status updates from SQUID.WTF, including region-specific information and donation needs.
Generated: DETERMINISTIC_70ab1585db0e89b0
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store server status updates
CREATE TABLE ServerStatusUpdates (
    id SERIAL PRIMARY KEY, -- Unique identifier for each status update
    region VARCHAR(100) NOT NULL, -- Region of the server
    status_update TEXT NOT NULL, -- Status message
    donation_needs TEXT, -- Description of donation needs
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the update was created
);

-- Function to insert a new server status update
CREATE OR REPLACE FUNCTION insert_server_status(
    p_region VARCHAR,
    p_status_update TEXT,
    p_donation_needs TEXT
) RETURNS VOID AS $$
BEGIN
    INSERT INTO ServerStatusUpdates (region, status_update, donation_needs)
    VALUES (p_region, p_status_update, p_donation_needs);
EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Error inserting server status: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Function to retrieve all server status updates
CREATE OR REPLACE FUNCTION get_server_status_updates()
RETURNS TABLE(id INT, region VARCHAR, status_update TEXT, donation_needs TEXT, created_at TIMESTAMP) AS $$
BEGIN
    RETURN QUERY
    SELECT id, region, status_update, donation_needs, created_at
    FROM ServerStatusUpdates
    ORDER BY created_at DESC; -- Order by the most recent updates
END;
$$ LANGUAGE plpgsql;

-- Example usage of the insert function
-- SELECT insert_server_status('North America', 'Server is running smoothly.', 'Need donations for server upgrades.');

-- Example usage of the retrieval function
-- SELECT * FROM get_server_status_updates();
```
