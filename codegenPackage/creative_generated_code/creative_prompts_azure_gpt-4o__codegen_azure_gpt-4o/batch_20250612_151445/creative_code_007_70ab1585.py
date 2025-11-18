"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://squid.wtf
Prompt: Write a SQL query to store and retrieve server status updates from SQUID.WTF, including region-specific information and donation needs.
Generated: DETERMINISTIC_70ab1585db0e89b0
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Table to store server status updates
CREATE TABLE ServerStatus (
    StatusID INT AUTO_INCREMENT PRIMARY KEY,  -- Primary key for the table
    ServerName VARCHAR(100) NOT NULL,         -- Name of the server
    Region VARCHAR(100) NOT NULL,             -- Region where the server is located
    Status VARCHAR(50) NOT NULL,              -- Current status of the server (e.g., active, down)
    DonationNeeded BOOLEAN NOT NULL DEFAULT FALSE, -- Whether donations are needed for the server
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Query to insert a new server status update
INSERT INTO ServerStatus (ServerName, Region, Status, DonationNeeded)
VALUES ('SQUID-A1', 'North America', 'active', FALSE);

-- Query for retrieving all server statuses
SELECT * FROM ServerStatus;

-- Query for retrieving only the servers in a specific region (e.g., North America)
SELECT * FROM ServerStatus
WHERE Region = 'North America';

-- Query for retrieving servers that require donations
SELECT * FROM ServerStatus
WHERE DonationNeeded = TRUE;

-- Query to update the status of a specific server
UPDATE ServerStatus
SET Status = 'down', DonationNeeded = TRUE
WHERE ServerName = 'SQUID-A1';

-- Query to delete a server status record (e.g., if the server is retired)
DELETE FROM ServerStatus
WHERE ServerName = 'SQUID-A1';
```
