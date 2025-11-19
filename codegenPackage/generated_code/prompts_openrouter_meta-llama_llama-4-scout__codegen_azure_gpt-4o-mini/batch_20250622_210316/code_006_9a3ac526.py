"""
Generated Code Metadata:
========================
Original URL: https://germanierpropiedades.com
Prompt: "Design a database schema for storing real estate property listings, including details like location, price, property type, and contact information for the agency."
Generated: DETERMINISTIC_9a3ac5267714dfb4
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing real estate property listings

CREATE TABLE Agencies (
    agency_id SERIAL PRIMARY KEY, -- Unique identifier for each agency
    name VARCHAR(255) NOT NULL, -- Name of the agency
    phone VARCHAR(15), -- Contact phone number for the agency
    email VARCHAR(255) UNIQUE NOT NULL, -- Contact email for the agency
    address VARCHAR(255), -- Physical address of the agency
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the agency was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

CREATE TABLE Properties (
    property_id SERIAL PRIMARY KEY, -- Unique identifier for each property
    agency_id INT NOT NULL, -- Foreign key referencing the agency
    location VARCHAR(255) NOT NULL, -- Location of the property
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the property
    property_type VARCHAR(50) NOT NULL, -- Type of property (e.g., house, apartment)
    description TEXT, -- Description of the property
    bedrooms INT CHECK (bedrooms >= 0), -- Number of bedrooms
    bathrooms INT CHECK (bathrooms >= 0), -- Number of bathrooms
    square_feet INT CHECK (square_feet >= 0), -- Size of the property in square feet
    listing_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the property was listed
    status VARCHAR(20) NOT NULL DEFAULT 'available', -- Status of the property (e.g., available, sold)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (agency_id) REFERENCES Agencies(agency_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_property_location ON Properties(location);
CREATE INDEX idx_property_price ON Properties(price);
CREATE INDEX idx_property_type ON Properties(property_type);
```
