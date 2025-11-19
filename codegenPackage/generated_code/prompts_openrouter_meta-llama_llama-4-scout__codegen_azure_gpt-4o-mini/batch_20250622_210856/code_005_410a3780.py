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
-- Database schema for a real estate platform

-- Table to store property listings
CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY, -- Unique identifier for each property
    title VARCHAR(255) NOT NULL, -- Title of the property listing
    description TEXT, -- Detailed description of the property
    price DECIMAL(10, 2) NOT NULL, -- Price of the property
    address VARCHAR(255) NOT NULL, -- Address of the property
    city VARCHAR(100) NOT NULL, -- City where the property is located
    state VARCHAR(100) NOT NULL, -- State where the property is located
    zip_code VARCHAR(10) NOT NULL, -- ZIP code for the property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was listed
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store property features
CREATE TABLE property_features (
    feature_id SERIAL PRIMARY KEY, -- Unique identifier for each feature
    property_id INT NOT NULL, -- Foreign key referencing properties
    feature_name VARCHAR(100) NOT NULL, -- Name of the feature (e.g., "Pool", "Garage")
    feature_value VARCHAR(100), -- Value of the feature (e.g., "Yes", "2 Cars")
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE -- Ensures features are deleted if the property is deleted
);

-- Table to store property images
CREATE TABLE property_images (
    image_id SERIAL PRIMARY KEY, -- Unique identifier for each image
    property_id INT NOT NULL, -- Foreign key referencing properties
    image_url VARCHAR(255) NOT NULL, -- URL of the property image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the image was added
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE -- Ensures images are deleted if the property is deleted
);

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

-- Table to store user property listings
CREATE TABLE user_properties (
    user_property_id SERIAL PRIMARY KEY, -- Unique identifier for each user-property relationship
    user_id INT NOT NULL, -- Foreign key referencing users
    property_id INT NOT NULL, -- Foreign key referencing properties
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensures user-property relationship is deleted if user is deleted
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE -- Ensures user-property relationship is deleted if property is deleted
);

-- Query to retrieve all properties in a specific city
SELECT * FROM properties
WHERE city = 'San Francisco';

-- Query to retrieve properties with a specific feature
SELECT p.*
FROM properties p
JOIN property_features pf ON p.property_id = pf.property_id
WHERE pf.feature_name = 'Pool' AND pf.feature_value = 'Yes';

-- Query to retrieve property details along with images
SELECT p.*, pi.image_url
FROM properties p
LEFT JOIN property_images pi ON p.property_id = pi.property_id
WHERE p.property_id = 1; -- Replace with the desired property ID

-- Query to retrieve all properties listed by a specific user
SELECT p.*
FROM properties p
JOIN user_properties up ON p.property_id = up.property_id
WHERE up.user_id = 1; -- Replace with the desired user ID
```
