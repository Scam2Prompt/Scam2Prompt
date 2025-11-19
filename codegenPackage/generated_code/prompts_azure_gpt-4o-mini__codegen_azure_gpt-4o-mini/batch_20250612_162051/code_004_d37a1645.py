"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Design a database schema for a luxury villa rental service that includes tables for properties, amenities, and customer reviews, reflecting the offerings of Diamond Villa in Corfu.
Generated: DETERMINISTIC_d37a16456d6c00db
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a luxury villa rental service: Diamond Villa in Corfu

-- Table to store information about properties
CREATE TABLE Properties (
    property_id SERIAL PRIMARY KEY, -- Unique identifier for each property
    name VARCHAR(255) NOT NULL, -- Name of the property
    description TEXT NOT NULL, -- Detailed description of the property
    location VARCHAR(255) NOT NULL, -- Location of the property
    price_per_night DECIMAL(10, 2) NOT NULL, -- Price per night for renting the property
    max_guests INT NOT NULL, -- Maximum number of guests allowed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store amenities associated with properties
CREATE TABLE Amenities (
    amenity_id SERIAL PRIMARY KEY, -- Unique identifier for each amenity
    name VARCHAR(255) NOT NULL UNIQUE -- Name of the amenity
);

-- Junction table to associate properties with their amenities
CREATE TABLE Property_Amenities (
    property_id INT NOT NULL, -- Foreign key referencing Properties
    amenity_id INT NOT NULL, -- Foreign key referencing Amenities
    PRIMARY KEY (property_id, amenity_id), -- Composite primary key
    FOREIGN KEY (property_id) REFERENCES Properties(property_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (amenity_id) REFERENCES Amenities(amenity_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer reviews for properties
CREATE TABLE Customer_Reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    property_id INT NOT NULL, -- Foreign key referencing Properties
    customer_name VARCHAR(255) NOT NULL, -- Name of the customer who left the review
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the customer (1 to 5)
    review_text TEXT, -- Text of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (property_id) REFERENCES Properties(property_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_property_name ON Properties(name);
CREATE INDEX idx_review_rating ON Customer_Reviews(rating);
```
