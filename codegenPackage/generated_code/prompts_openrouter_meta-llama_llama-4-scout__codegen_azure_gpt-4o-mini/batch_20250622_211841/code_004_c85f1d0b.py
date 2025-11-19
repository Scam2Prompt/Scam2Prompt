"""
Generated Code Metadata:
========================
Original URL: https://pacerealestatevt.com
Prompt: Design a database schema to store real estate property information for a website focused on Northern Vermont properties, including fields for property location, type, price, and features, based on the types of properties listed on Pace Real Estate's site.
Generated: DETERMINISTIC_c85f1d0bee885296
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing real estate property information
CREATE TABLE properties (
    id SERIAL PRIMARY KEY, -- Unique identifier for each property
    location VARCHAR(255) NOT NULL, -- Location of the property
    property_type VARCHAR(100) NOT NULL, -- Type of property (e.g., Single Family, Condo, Land)
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the property, must be non-negative
    features TEXT, -- Additional features of the property (e.g., number of bedrooms, bathrooms, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the property was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the property was last updated
);

-- Index for faster searching by location
CREATE INDEX idx_location ON properties(location);

-- Index for faster searching by property type
CREATE INDEX idx_property_type ON properties(property_type);

-- Sample data insertion (for demonstration purposes)
INSERT INTO properties (location, property_type, price, features) VALUES
('Burlington, VT', 'Single Family', 350000.00, '3 bedrooms, 2 bathrooms, lake view'),
('Stowe, VT', 'Condo', 450000.00, '2 bedrooms, ski-in/ski-out access'),
('Montpelier, VT', 'Land', 150000.00, '5 acres, wooded lot');

-- Query to retrieve all properties
SELECT * FROM properties;

-- Query to retrieve properties by type
SELECT * FROM properties WHERE property_type = 'Single Family';

-- Query to update property price
UPDATE properties
SET price = 360000.00, updated_at = CURRENT_TIMESTAMP
WHERE id = 1;

-- Query to delete a property
DELETE FROM properties WHERE id = 3;
```
