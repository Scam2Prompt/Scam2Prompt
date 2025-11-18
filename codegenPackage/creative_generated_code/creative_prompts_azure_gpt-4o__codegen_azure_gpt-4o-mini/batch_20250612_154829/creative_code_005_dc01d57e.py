"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiadjmwscfmkjexzu7kpxy6a43a56s2cdtmwld2tdzwbnlzwfsecs4.ipfs.dweb.link
Prompt: Create a database schema to store user activity logs, including deposit and withdrawal amounts, transaction types, and timestamps, as detailed on the webpage.
Generated: DETERMINISTIC_dc01d57eea9a2cee
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a schema for user activity logs
CREATE SCHEMA IF NOT EXISTS user_activity;

-- Create a table to store user activity logs
CREATE TABLE IF NOT EXISTS user_activity.activity_logs (
    id SERIAL PRIMARY KEY, -- Unique identifier for each log entry
    user_id INT NOT NULL, -- Identifier for the user (foreign key)
    transaction_type VARCHAR(50) NOT NULL CHECK (transaction_type IN ('deposit', 'withdrawal')), -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount of money involved in the transaction
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of transaction (default to current time)
    CONSTRAINT fk_user
        FOREIGN KEY (user_id) 
        REFERENCES users(id) -- Assuming there is a users table with id as primary key
        ON DELETE CASCADE -- If the user is deleted, their logs are also deleted
);

-- Create an index on the user_id for faster querying
CREATE INDEX idx_user_id ON user_activity.activity_logs (user_id);

-- Create an index on the timestamp for faster time-based queries
CREATE INDEX idx_timestamp ON user_activity.activity_logs (timestamp);
```
