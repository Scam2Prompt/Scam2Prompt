"""
Generated Code Metadata:
========================
Original URL: https://www.propertyshare.net
Prompt: "Design a database schema to store property information for a real estate marketing platform similar to Property Share in Egypt."
Generated: DETERMINISTIC_6d37964722d5781f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a real estate marketing platform

-- Create a table to store property types (e.g., apartment, villa, commercial)
CREATE TABLE PropertyTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each property type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the property type
    description TEXT -- Description of the property type
);

-- Create a table to store locations (e.g., city, neighborhood)
CREATE TABLE Locations (
    id SERIAL PRIMARY KEY, -- Unique identifier for each location
    city VARCHAR(100) NOT NULL, -- City name
    neighborhood VARCHAR(100), -- Neighborhood name (optional)
    latitude DECIMAL(9, 6), -- Latitude for geolocation
    longitude DECIMAL(9, 6) -- Longitude for geolocation
);

-- Create a table to store properties
CREATE TABLE Properties (
    id SERIAL PRIMARY KEY, -- Unique identifier for each property
    title VARCHAR(255) NOT NULL, -- Title of the property listing
    description TEXT NOT NULL, -- Detailed description of the property
    price DECIMAL(10, 2) NOT NULL, -- Price of the property
    area DECIMAL(10, 2) NOT NULL, -- Area of the property in square meters
    property_type_id INT NOT NULL, -- Foreign key referencing PropertyTypes
    location_id INT NOT NULL, -- Foreign key referencing Locations
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    is_active BOOLEAN DEFAULT TRUE, -- Status of the property listing
    FOREIGN KEY (property_type_id) REFERENCES PropertyTypes(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (location_id) REFERENCES Locations(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store property images
CREATE TABLE PropertyImages (
    id SERIAL PRIMARY KEY, -- Unique identifier for each image
    property_id INT NOT NULL, -- Foreign key referencing Properties
    image_url VARCHAR(255) NOT NULL, -- URL of the image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the image was added
    FOREIGN KEY (property_id) REFERENCES Properties(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store user information
CREATE TABLE Users (
    id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store user roles (e.g., admin, agent, buyer)
CREATE TABLE UserRoles (
    id SERIAL PRIMARY KEY, -- Unique identifier for each role
    role_name VARCHAR(50) NOT NULL UNIQUE -- Name of the user role
);

-- Create a junction table to associate users with roles
CREATE TABLE UserRoleAssignments (
    user_id INT NOT NULL, -- Foreign key referencing Users
    role_id INT NOT NULL, -- Foreign key referencing UserRoles
    PRIMARY KEY (user_id, role_id), -- Composite primary key
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (role_id) REFERENCES UserRoles(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store inquiries about properties
CREATE TABLE Inquiries (
    id SERIAL PRIMARY KEY, -- Unique identifier for each inquiry
    property_id INT NOT NULL, -- Foreign key referencing Properties
    user_id INT NOT NULL, -- Foreign key referencing Users
    message TEXT NOT NULL, -- Inquiry message
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the inquiry was made
    FOREIGN KEY (property_id) REFERENCES Properties(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE -- Ensure referential integrity
);
```
