"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Design a database schema for storing property listings and their associated details, suitable for a real estate platform like Presval, and write SQL queries to retrieve specific data.
Generated: DETERMINISTIC_410a37801a5b242a
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for real estate property listings
CREATE TABLE property_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8)
);

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    property_type_id INTEGER REFERENCES property_types(id),
    location_id INTEGER REFERENCES locations(id),
    price DECIMAL(15, 2) NOT NULL,
    area_sqft DECIMAL(10, 2),
    bedrooms INTEGER,
    bathrooms INTEGER,
    year_built INTEGER,
    is_featured BOOLEAN DEFAULT FALSE,
    is_sold BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE property_features (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    feature_name VARCHAR(100) NOT NULL,
    feature_value VARCHAR(255)
);

CREATE TABLE property_images (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    caption VARCHAR(255),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE agents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    license_number VARCHAR(50),
    profile_picture_url TEXT
);

CREATE TABLE property_agents (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    agent_id INTEGER REFERENCES agents(id) ON DELETE CASCADE,
    is_primary BOOLEAN DEFAULT FALSE
);

-- Indexes for better performance
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_location ON properties(location_id);
CREATE INDEX idx_properties_type ON properties(property_type_id);
CREATE INDEX idx_properties_bedrooms ON properties(bedrooms);
CREATE INDEX idx_properties_bathrooms ON properties(bathrooms);
CREATE INDEX idx_property_features ON property_features(property_id);
CREATE INDEX idx_property_images ON property_images(property_id);

-- Example SQL queries

-- Get all properties with their details
SELECT 
    p.id, p.title, p.description, p.price, p.area_sqft, p.bedrooms, p.bathrooms,
    pt.name AS property_type,
    l.city, l.state, l.country,
    STRING_AGG(DISTINCT pf.feature_name || ': ' || pf.feature_value, ', ') AS features,
    pi.image_url AS primary_image
FROM 
    properties p
JOIN 
    property_types pt ON p.property_type_id = pt.id
JOIN 
    locations l ON p.location_id = l.id
LEFT JOIN 
    property_features pf ON p.id = pf.property_id
LEFT JOIN 
    property_images pi ON p.id = pi.property_id AND pi.is_primary = TRUE
GROUP BY 
    p.id, pt.name, l.city, l.state, l.country, pi.image_url;

-- Get featured properties in a specific city
SELECT 
    p.id, p.title, p.price, p.bedrooms, p.bathrooms, p.area_sqft,
    pi.image_url AS primary_image
FROM 
    properties p
JOIN 
    locations l ON p.location_id = l.id
LEFT JOIN 
    property_images pi ON p.id = pi.property_id AND pi.is_primary = TRUE
WHERE 
    p.is_featured = TRUE 
    AND l.city = 'New York'
ORDER BY 
    p.price DESC;

-- Get properties within a price range and with specific features
SELECT 
    p.id, p.title, p.price, p.bedrooms, p.bathrooms,
    pt.name AS property_type,
    l.city, l.state
FROM 
    properties p
JOIN 
    property_types pt ON p.property_type_id = pt.id
JOIN 
    locations l ON p.location_id = l.id
WHERE 
    p.price BETWEEN 200000 AND 500000
    AND p.bedrooms >= 2
    AND p.bathrooms >= 2
    AND EXISTS (
        SELECT 1 FROM property_features pf 
        WHERE pf.property_id = p.id 
        AND pf.feature_name = 'Swimming Pool' 
        AND pf.feature_value = 'Yes'
    )
ORDER BY 
    p.price ASC;

-- Get agent details for a specific property
SELECT 
    a.id, a.name, a.email, a.phone, a.license_number, a.profile_picture_url
FROM 
    agents a
JOIN 
    property_agents pa ON a.id = pa.agent_id
WHERE 
    pa.property_id = 123;

-- Get all images for a property
SELECT 
    image_url, caption
FROM 
    property_images
WHERE 
    property_id = 123
ORDER BY 
    is_primary DESC, uploaded_at ASC;

-- Update property price
UPDATE properties
SET price = 450000, updated_at = CURRENT_TIMESTAMP
WHERE id = 123;

-- Mark property as sold
UPDATE properties
SET is_sold = TRUE, updated_at = CURRENT_TIMESTAMP
WHERE id = 123;

-- Add a new property
INSERT INTO properties (
    title, description, property_type_id, location_id, 
    price, area_sqft, bedrooms, bathrooms, year_built
) VALUES (
    'Modern Downtown Apartment', 'Spacious 2-bedroom apartment with great views', 
    1, 5, 350000, 1200, 2, 2, 2015
) RETURNING id;

-- Add features to a property
INSERT INTO property_features (property_id, feature_name, feature_value)
VALUES 
    (123, 'Swimming Pool', 'Yes'),
    (123, 'Gym', 'Yes'),
    (123, 'Parking', 'Garage');
```
