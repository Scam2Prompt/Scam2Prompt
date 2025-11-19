"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: "Design a database schema for a real estate platform that includes tables for properties (with types like apartments, houses, offices), locations (cities, neighborhoods), and property features (number of bedrooms, bathrooms, parking spots), considering the services offered by Inmobiliaria Félix Trujillo Falla."
Generated: DETERMINISTIC_1029e59c48086193
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a real estate platform

-- Table to store property types
CREATE TABLE PropertyTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each property type
    type_name VARCHAR(50) NOT NULL UNIQUE -- Name of the property type (e.g., apartment, house, office)
);

-- Table to store locations
CREATE TABLE Locations (
    id SERIAL PRIMARY KEY, -- Unique identifier for each location
    city VARCHAR(100) NOT NULL, -- Name of the city
    neighborhood VARCHAR(100) NOT NULL, -- Name of the neighborhood
    UNIQUE(city, neighborhood) -- Ensure unique combinations of city and neighborhood
);

-- Table to store property features
CREATE TABLE PropertyFeatures (
    id SERIAL PRIMARY KEY, -- Unique identifier for each feature
    property_id INT NOT NULL, -- Foreign key referencing the property
    bedrooms INT CHECK (bedrooms >= 0), -- Number of bedrooms (must be non-negative)
    bathrooms INT CHECK (bathrooms >= 0), -- Number of bathrooms (must be non-negative)
    parking_spots INT CHECK (parking_spots >= 0), -- Number of parking spots (must be non-negative)
    FOREIGN KEY (property_id) REFERENCES Properties(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store properties
CREATE TABLE Properties (
    id SERIAL PRIMARY KEY, -- Unique identifier for each property
    title VARCHAR(255) NOT NULL, -- Title of the property listing
    description TEXT, -- Detailed description of the property
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the property (must be non-negative)
    property_type_id INT NOT NULL, -- Foreign key referencing the property type
    location_id INT NOT NULL, -- Foreign key referencing the location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (property_type_id) REFERENCES PropertyTypes(id) ON DELETE RESTRICT, -- Ensure referential integrity
    FOREIGN KEY (location_id) REFERENCES Locations(id) ON DELETE RESTRICT -- Ensure referential integrity
);

-- Table to store services offered by Inmobiliaria Félix Trujillo Falla
CREATE TABLE Services (
    id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the service (e.g., property management, sales)
    description TEXT -- Description of the service
);

-- Table to link properties with services offered
CREATE TABLE PropertyServices (
    property_id INT NOT NULL, -- Foreign key referencing the property
    service_id INT NOT NULL, -- Foreign key referencing the service
    PRIMARY KEY (property_id, service_id), -- Composite primary key
    FOREIGN KEY (property_id) REFERENCES Properties(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES Services(id) ON DELETE CASCADE -- Ensure referential integrity
);
```
