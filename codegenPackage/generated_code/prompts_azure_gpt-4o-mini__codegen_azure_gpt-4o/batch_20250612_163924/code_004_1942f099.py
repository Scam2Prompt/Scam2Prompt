"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Design a database schema for storing information about commercial properties for sale, including fields for type of business, location, and price, inspired by the lighting store listing.
Generated: DETERMINISTIC_1942f099297cb395
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about commercial properties for sale

-- Table: commercial_properties
CREATE TABLE commercial_properties (
    property_id SERIAL PRIMARY KEY, -- Unique identifier for each property
    business_type VARCHAR(255) NOT NULL, -- Type of business (e.g., lighting store, restaurant, etc.)
    location TEXT NOT NULL, -- Location of the property (address, city, state, etc.)
    price DECIMAL(15, 2) NOT NULL, -- Price of the property in USD
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Indexes for faster querying
CREATE INDEX idx_business_type ON commercial_properties (business_type); -- Index for business type
CREATE INDEX idx_location ON commercial_properties (location); -- Index for location
CREATE INDEX idx_price ON commercial_properties (price); -- Index for price

-- Example of inserting data into the table
-- INSERT INTO commercial_properties (business_type, location, price)
-- VALUES ('Lighting Store', '123 Main St, Springfield, IL', 250000.00);

-- Example of querying data
-- SELECT * FROM commercial_properties WHERE business_type = 'Lighting Store';
```
