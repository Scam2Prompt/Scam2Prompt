"""
Generated Code Metadata:
========================
Original URL: https://celestia.homes
Prompt: Design a database schema to store information about properties for sale on the Costa del Sol, inspired by the types of properties and features listed on Celestia Homes.
Generated: DETERMINISTIC_f052e1b9f299da67
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about properties for sale on the Costa del Sol

-- Create a table to store property types
CREATE TABLE PropertyTypes (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each property type
    type_name VARCHAR(100) NOT NULL,    -- Name of the property type (e.g., Villa, Apartment)
    description TEXT                     -- Description of the property type
);

-- Create a table to store features of properties
CREATE TABLE PropertyFeatures (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each feature
    feature_name VARCHAR(100) NOT NULL, -- Name of the feature (e.g., Pool, Garden)
    description TEXT                     -- Description of the feature
);

-- Create a table to store properties
CREATE TABLE Properties (
    id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each property
    title VARCHAR(255) NOT NULL,         -- Title of the property listing
    description TEXT NOT NULL,            -- Detailed description of the property
    price DECIMAL(10, 2) NOT NULL,       -- Price of the property
    location VARCHAR(255) NOT NULL,      -- Location of the property
    property_type_id INT NOT NULL,       -- Foreign key referencing PropertyTypes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was listed
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (property_type_id) REFERENCES PropertyTypes(id) -- Ensures referential integrity
);

-- Create a junction table to associate properties with their features
CREATE TABLE PropertyFeatureAssociations (
    property_id INT NOT NULL,            -- Foreign key referencing Properties
    feature_id INT NOT NULL,             -- Foreign key referencing PropertyFeatures
    PRIMARY KEY (property_id, feature_id), -- Composite primary key
    FOREIGN KEY (property_id) REFERENCES Properties(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (feature_id) REFERENCES PropertyFeatures(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store user information for potential buyers
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of user registration
);

-- Create a table to store inquiries about properties
CREATE TABLE Inquiries (
    id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each inquiry
    user_id INT NOT NULL,                  -- Foreign key referencing Users
    property_id INT NOT NULL,               -- Foreign key referencing Properties
    message TEXT NOT NULL,                  -- Message from the user regarding the property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the inquiry
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (property_id) REFERENCES Properties(id) ON DELETE CASCADE -- Ensures referential integrity
);
```
