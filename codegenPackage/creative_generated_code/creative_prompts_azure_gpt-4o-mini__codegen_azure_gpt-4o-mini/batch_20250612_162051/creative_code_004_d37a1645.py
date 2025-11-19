"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Design a database schema for a luxury villa rental service that includes tables for properties, amenities, and customer reviews, reflecting the offerings of Diamond Villa in Corfu.
Generated: DETERMINISTIC_d37a16456d6c00db
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Luxury Villa Rental Service

-- Table for storing property details
CREATE TABLE Properties (
    property_id SERIAL PRIMARY KEY,               -- Unique identifier for each property
    name VARCHAR(255) NOT NULL,                   -- Name of the property
    description TEXT NOT NULL,                     -- Detailed description of the property
    location VARCHAR(255) NOT NULL,                -- Location of the property (e.g., Corfu)
    price_per_night DECIMAL(10, 2) NOT NULL,      -- Price per night for renting the property
    number_of_bedrooms INT NOT NULL,               -- Number of bedrooms in the property
    number_of_bathrooms INT NOT NULL,              -- Number of bathrooms in the property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table for storing amenities available in the properties
CREATE TABLE Amenities (
    amenity_id SERIAL PRIMARY KEY,                 -- Unique identifier for each amenity
    name VARCHAR(255) NOT NULL UNIQUE               -- Name of the amenity (e.g., Pool, WiFi)
);

-- Table for mapping properties to their amenities (Many-to-Many relationship)
CREATE TABLE Property_Amenities (
    property_id INT REFERENCES Properties(property_id) ON DELETE CASCADE, -- Foreign key to Properties
    amenity_id INT REFERENCES Amenities(amenity_id) ON DELETE CASCADE,   -- Foreign key to Amenities
    PRIMARY KEY (property_id, amenity_id)                                  -- Composite primary key
);

-- Table for storing customer reviews
CREATE TABLE Customer_Reviews (
    review_id SERIAL PRIMARY KEY,                -- Unique identifier for each review
    property_id INT REFERENCES Properties(property_id) ON DELETE CASCADE, -- Foreign key to Properties
    customer_name VARCHAR(255) NOT NULL,        -- Name of the customer who wrote the review
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the customer (1 to 5)
    review_text TEXT,                            -- Text content of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was submitted
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Optional: Index for faster searchability on property name
CREATE INDEX idx_property_name ON Properties(name);

-- Optional: Index for faster lookup of reviews by property
CREATE INDEX idx_property_reviews ON Customer_Reviews(property_id);
```
