"""
Generated Code Metadata:
========================
Original URL: https://piscorealestate.com
Prompt: "Create a SQL database schema to store information about properties, including features like price, location, number of bedrooms, and amenities."
Generated: DETERMINISTIC_f8d20f05efd80fc0
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a SQL database schema for storing property information

-- Drop the properties table if it already exists to avoid conflicts
DROP TABLE IF EXISTS properties;

-- Create the properties table
CREATE TABLE properties (
    id SERIAL PRIMARY KEY, -- Unique identifier for each property
    price DECIMAL(10, 2) NOT NULL, -- Price of the property, with two decimal places
    location VARCHAR(255) NOT NULL, -- Location of the property
    bedrooms INT NOT NULL CHECK (bedrooms >= 0), -- Number of bedrooms, must be non-negative
    amenities TEXT, -- Additional amenities, stored as text
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the property was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the property was last updated
);

-- Create an index on the location column for faster searches
CREATE INDEX idx_location ON properties(location);

-- Create a view to easily access properties with a price below a certain threshold
CREATE VIEW affordable_properties AS
SELECT * FROM properties
WHERE price < 100000; -- Adjust the threshold as needed

-- Example of inserting a property into the properties table
-- INSERT INTO properties (price, location, bedrooms, amenities) 
-- VALUES (250000.00, '123 Main St, Anytown, USA', 3, 'Pool, Garage');

-- Note: Uncomment the above INSERT statement to add a sample property
```
