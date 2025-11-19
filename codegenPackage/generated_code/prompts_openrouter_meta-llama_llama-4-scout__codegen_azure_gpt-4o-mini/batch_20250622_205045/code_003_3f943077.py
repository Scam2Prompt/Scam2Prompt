"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Create a simple database schema to store information about business clients, including their business type (e.g. sole proprietorship, LLC, corporation), tax ID numbers, and services used.
Generated: DETERMINISTIC_3f94307788f36c74
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing business client information

-- Create a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS BusinessClientsDB;

-- Use the created database
USE BusinessClientsDB;

-- Create a table to store information about business clients
CREATE TABLE IF NOT EXISTS Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    BusinessName VARCHAR(255) NOT NULL,       -- Name of the business
    BusinessType ENUM('Sole Proprietorship', 'LLC', 'Corporation') NOT NULL,  -- Type of business
    TaxID VARCHAR(50) NOT NULL UNIQUE,        -- Unique tax identification number
    ServicesUsed TEXT,                        -- Description of services used by the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create an index on the TaxID for faster lookups
CREATE INDEX idx_taxid ON Clients (TaxID);

-- Example of inserting a new client into the Clients table
-- INSERT INTO Clients (BusinessName, BusinessType, TaxID, ServicesUsed)
-- VALUES ('Example Corp', 'Corporation', '123-45-6789', 'Consulting, Development');

-- Note: Uncomment the above INSERT statement to add a sample client
```
