"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Create a database schema to store Meowgon NFT data, including anatomy parts, elements, rarity, and unique identifiers, based on the structure described on the Realis website.
Generated: DETERMINISTIC_4e2e88c5e84e9c50
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Meowgon NFT data
CREATE DATABASE meowgon_nft;

-- Use the meowgon_nft database
USE meowgon_nft;

-- Create a table for anatomy parts
CREATE TABLE anatomy_parts (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for elements
CREATE TABLE elements (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for rarity levels
CREATE TABLE rarity_levels (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for Meowgon NFTs
CREATE TABLE meowgon_nfts (
  id INT AUTO_INCREMENT,
  unique_identifier VARCHAR(255) NOT NULL UNIQUE,
  anatomy_part_id INT,
  element_id INT,
  rarity_level_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (anatomy_part_id) REFERENCES anatomy_parts(id),
  FOREIGN KEY (element_id) REFERENCES elements(id),
  FOREIGN KEY (rarity_level_id) REFERENCES rarity_levels(id)
);

-- Create a table for Meowgon NFT metadata
CREATE TABLE meowgon_nft_metadata (
  id INT AUTO_INCREMENT,
  meowgon_nft_id INT,
  key VARCHAR(255) NOT NULL,
  value TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (meowgon_nft_id) REFERENCES meowgon_nfts(id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_meowgon_nfts_anatomy_part_id ON meowgon_nfts (anatomy_part_id);
CREATE INDEX idx_meowgon_nfts_element_id ON meowgon_nfts (element_id);
CREATE INDEX idx_meowgon_nfts_rarity_level_id ON meowgon_nfts (rarity_level_id);
CREATE INDEX idx_meowgon_nft_metadata_meowgon_nft_id ON meowgon_nft_metadata (meowgon_nft_id);

-- Insert sample data for testing
INSERT INTO anatomy_parts (name, description) 
VALUES 
('Head', 'Meowgon head'),
('Body', 'Meowgon body'),
('Tail', 'Meowgon tail');

INSERT INTO elements (name, description) 
VALUES 
('Fire', 'Fire element'),
('Water', 'Water element'),
('Earth', 'Earth element');

INSERT INTO rarity_levels (name, description) 
VALUES 
('Common', 'Common rarity'),
('Uncommon', 'Uncommon rarity'),
('Rare', 'Rare rarity');

INSERT INTO meowgon_nfts (unique_identifier, anatomy_part_id, element_id, rarity_level_id) 
VALUES 
('MEOWGON-001', 1, 1, 1),
('MEOWGON-002', 2, 2, 2),
('MEOWGON-003', 3, 3, 3);

INSERT INTO meowgon_nft_metadata (meowgon_nft_id, key, value) 
VALUES 
(1, 'color', 'red'),
(2, 'pattern', 'stripes'),
(3, 'size', 'large');
```
