"""
Generated Code Metadata:
========================
Original URL: https://2ms.pt
Prompt: "Design a simple database schema for storing property information similar to what is presented on 2ms.pt, including fields for address, city, and contact details."
Generated: DETERMINISTIC_ad9e8fad320d7684
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a simple database schema for storing property information

-- Drop the table if it already exists to avoid conflicts during creation
DROP TABLE IF EXISTS properties;

-- Create a table named 'properties' to store property information
CREATE TABLE properties (
    id SERIAL PRIMARY KEY, -- Unique identifier for each property
    address VARCHAR(255) NOT NULL, -- Address of the property
    city VARCHAR(100) NOT NULL, -- City where the property is located
    contact_name VARCHAR(100) NOT NULL, -- Name of the contact person
    contact_phone VARCHAR(15) NOT NULL, -- Phone number of the contact person
    contact_email VARCHAR(100), -- Email address of the contact person
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Add an index on the city field for faster queries
CREATE INDEX idx_city ON properties(city);

-- Sample insert statement to demonstrate how to add a property
INSERT INTO properties (address, city, contact_name, contact_phone, contact_email)
VALUES ('123 Main St', 'Lisbon', 'John Doe', '+351912345678', 'john.doe@example.com');

-- Sample select statement to retrieve all properties
SELECT * FROM properties;

-- Note: Ensure to handle errors in your application code when executing these SQL statements.
```
