"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.oasishottubsep.com
Prompt: Create a database schema for storing hot tub models, features, and pricing information, including brands like Jacuzzi®, Dream Maker Spas™, and Dimension One Spas®, as listed on the Oasis Hot Tubs site.
Generated: DETERMINISTIC_1765e0fd1fa0a3c7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing hot tub models, features, and pricing information

-- Create a database named hot_tub_store
CREATE DATABASE hot_tub_store;

-- Use the created database
USE hot_tub_store;

-- Table to store information about different hot tub brands
CREATE TABLE brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each brand
    brand_name VARCHAR(255) NOT NULL UNIQUE, -- Name of the brand
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the brand was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store hot tub models
CREATE TABLE hot_tubs (
    hot_tub_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each hot tub model
    brand_id INT, -- Foreign key referencing brands table
    model_name VARCHAR(255) NOT NULL UNIQUE, -- Name of the hot tub model
    description TEXT, -- Description of the hot tub model
    base_price DECIMAL(10, 2) NOT NULL, -- Base price of the hot tub model
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the hot tub was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update

    -- Foreign key constraint to ensure the brand exists
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE
);

-- Table to store features associated with each hot tub model
CREATE TABLE features (
    feature_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feature
    feature_name VARCHAR(255) NOT NULL UNIQUE, -- Name of the feature
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the feature was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to associate hot tubs with their features (Many-to-Many relationship)
CREATE TABLE hot_tub_features (
    hot_tub_id INT, -- Foreign key referencing hot tubs table
    feature_id INT, -- Foreign key referencing features table
    PRIMARY KEY (hot_tub_id, feature_id), -- Composite primary key
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the association was created

    -- Foreign key constraints to ensure the hot tub and feature exist
    FOREIGN KEY (hot_tub_id) REFERENCES hot_tubs(hot_tub_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES features(feature_id) ON DELETE CASCADE
);

-- Insert initial data into brands table
INSERT INTO brands (brand_name) VALUES
('Jacuzzi®'),
('Dream Maker Spas™'),
('Dimension One Spas®');

-- Insert initial data into features table
INSERT INTO features (feature_name) VALUES
('Heater'),
('LED Lighting'),
('Massage Jets'),
('Waterfall'),
('Bluetooth Audio');

-- Example insertion of a hot tub model
INSERT INTO hot_tubs (brand_id, model_name, description, base_price) VALUES
(1, 'J-300 Series', 'A versatile hot tub with a variety of features and styles.', 7499.99);

-- Example association of features with a hot tub model
INSERT INTO hot_tub_features (hot_tub_id, feature_id) VALUES
(1, 1), -- Heater
(1, 2), -- LED Lighting
(1, 3); -- Massage Jets

-- Ensure to handle potential errors during insertions and other operations accordingly
-- In a production environment, proper error handling mechanisms should be implemented in the application logic that interacts with this database.
```
