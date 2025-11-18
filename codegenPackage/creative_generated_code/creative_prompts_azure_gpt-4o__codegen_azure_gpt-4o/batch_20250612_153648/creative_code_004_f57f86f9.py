"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Create a database schema for storing golf grip profiles, including customization details like material type (PU, TPE, rubber), embossing style, and customer preferences, as described on the Longhui Golf website.
Generated: DETERMINISTIC_f57f86f9a440f9f3
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing golf grip profiles
-- This schema includes customization details such as material type, embossing style, and customer preferences.

-- Table: materials
-- Stores information about material types for golf grips
CREATE TABLE materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    material_name VARCHAR(50) NOT NULL,         -- Name of the material (e.g., PU, TPE, rubber)
    description TEXT                            -- Optional description of the material
);

-- Table: embossing_styles
-- Stores information about available embossing styles
CREATE TABLE embossing_styles (
    style_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each embossing style
    style_name VARCHAR(50) NOT NULL,            -- Name of the embossing style
    description TEXT                            -- Optional description of the embossing style
);

-- Table: customers
-- Stores customer information
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,            -- Customer's first name
    last_name VARCHAR(50) NOT NULL,             -- Customer's last name
    email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email address (must be unique)
    phone_number VARCHAR(20)                    -- Optional phone number
);

-- Table: golf_grip_profiles
-- Stores golf grip profile details
CREATE TABLE golf_grip_profiles (
    profile_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each golf grip profile
    customer_id INT NOT NULL,                   -- Foreign key referencing customers table
    material_id INT NOT NULL,                   -- Foreign key referencing materials table
    style_id INT NOT NULL,                      -- Foreign key referencing embossing_styles table
    customization_notes TEXT,                   -- Additional notes or preferences provided by the customer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the profile was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE RESTRICT,
    FOREIGN KEY (style_id) REFERENCES embossing_styles(style_id) ON DELETE RESTRICT
);

-- Insert sample data into materials table
INSERT INTO materials (material_name, description)
VALUES
    ('PU', 'Polyurethane material. Provides a soft yet durable grip.'),
    ('TPE', 'Thermoplastic elastomer. Offers excellent flexibility and comfort.'),
    ('Rubber', 'High-quality rubber. Ensures strong and reliable grip.');

-- Insert sample data into embossing_styles table
INSERT INTO embossing_styles (style_name, description)
VALUES
    ('Classic', 'Traditional embossing style with timeless design.'),
    ('Modern', 'Contemporary embossing style with sleek aesthetics.'),
    ('Custom', 'Unique embossing style tailored to customer preferences.');
```
