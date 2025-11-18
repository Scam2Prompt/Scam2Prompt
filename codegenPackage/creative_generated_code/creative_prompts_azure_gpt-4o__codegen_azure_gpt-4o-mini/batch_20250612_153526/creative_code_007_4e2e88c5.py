"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realis.pages.dev
Prompt: Create a database schema to store Meowgon NFT data, including anatomy parts, elements, rarity, and unique identifiers, based on the structure described on the Realis website.
Generated: DETERMINISTIC_4e2e88c5e84e9c50
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the database schema for storing Meowgon NFT data

-- Drop the existing database if it exists (for development purposes)
DROP DATABASE IF EXISTS meowgon_nft;

-- Create a new database for Meowgon NFT
CREATE DATABASE meowgon_nft;

-- Use the newly created database
USE meowgon_nft;

-- Table for storing unique identifiers for each Meowgon
CREATE TABLE meowgons (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each Meowgon
    name VARCHAR(255) NOT NULL,                 -- Name of the Meowgon
    unique_identifier VARCHAR(255) UNIQUE NOT NULL, -- Unique NFT identifier
    rarity_id INT NOT NULL,                      -- Foreign key linked to rarity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the creation of the NFT
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Updated timestamp
    FOREIGN KEY (rarity_id) REFERENCES rarity(id) -- Ensure referential integrity
);

-- Table for storing different anatomy parts of Meowgons
CREATE TABLE anatomy_parts (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for anatomy parts
    part_name VARCHAR(255) NOT NULL,            -- Name of the anatomy part (e.g., Tail, Ears)
    description TEXT,                            -- Description of the anatomy part
    meowgon_id INT NOT NULL,                     -- Foreign key linked to Meowgon
    FOREIGN KEY (meowgon_id) REFERENCES meowgons(id) -- Ensure referential integrity
);

-- Table for storing elements associated with Meowgons
CREATE TABLE elements (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for elements
    element_name VARCHAR(255) NOT NULL,         -- Name of the element (e.g., Fire, Water)
    meowgon_id INT NOT NULL,                     -- Foreign key linked to Meowgon
    FOREIGN KEY (meowgon_id) REFERENCES meowgons(id) -- Ensure referential integrity
);

-- Table for defining rarity categories
CREATE TABLE rarity (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for rarity
    rarity_name VARCHAR(255) NOT NULL UNIQUE,   -- Name of the rarity (e.g., Common, Rare)
    description TEXT                             -- Description of the rarity
);

-- Table for associating Meowgons with their respective elements
CREATE TABLE meowgon_elements (
    meowgon_id INT NOT NULL,                    -- Foreign key linked to Meowgon
    element_id INT NOT NULL,                    -- Foreign key linked to elements
    PRIMARY KEY (meowgon_id, element_id),      -- Composite primary key to avoid duplicates
    FOREIGN KEY (meowgon_id) REFERENCES meowgons(id), -- Ensure referential integrity
    FOREIGN KEY (element_id) REFERENCES elements(id) -- Ensure referential integrity
);

-- Insert sample data (for demonstration purposes)
INSERT INTO rarity (rarity_name, description) VALUES
('Common', 'A frequently found Meowgon.'),
('Rare', 'A Meowgon that is less commonly found.'),
('Legendary', 'An exceptionally rare Meowgon.');

INSERT INTO meowgons (name, unique_identifier, rarity_id) VALUES
('Meowgon One', 'M001', 1),
('Meowgon Two', 'M002', 2),
('Meowgon Three', 'M003', 3);

INSERT INTO anatomy_parts (part_name, description, meowgon_id) VALUES
('Tail', 'A long and fluffy tail.', 1),
('Ears', 'Pointy ears that can hear high frequencies.', 2),
('Fur', 'Soft and silky fur that shines.', 3);

INSERT INTO elements (element_name, meowgon_id) VALUES
('Fire', 1),
('Water', 2),
('Earth', 3);

-- Create indexes for better performance on searches
CREATE INDEX idx_meowgon_unique_id ON meowgons(unique_identifier);
CREATE INDEX idx_anatomy_meowgon ON anatomy_parts(meowgon_id);
CREATE INDEX idx_elements_meowgon ON elements(meowgon_id);

-- All tables and relationships are set up and ready for data manipulation and retrieval.
```
