"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Create a database schema to store computer specifications similar to the Londritech models, including fields for processor type, memory size, storage capacity, graphics card, and price.
Generated: DETERMINISTIC_1edbc59ce2885f3f
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing computer specifications

CREATE TABLE processors (
    processor_id SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    cores INTEGER NOT NULL,
    threads INTEGER NOT NULL,
    base_clock DECIMAL(5,2) NOT NULL, -- GHz
    boost_clock DECIMAL(5,2), -- GHz
    cache_size INTEGER, -- MB
    tdp INTEGER, -- Watts
    UNIQUE(brand, model)
);

CREATE TABLE memory_types (
    memory_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE, -- e.g., DDR4, DDR5
    speed INTEGER NOT NULL -- MHz
);

CREATE TABLE storage_types (
    storage_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE, -- e.g., SSD, HDD, NVMe
    interface VARCHAR(50) -- e.g., SATA, PCIe
);

CREATE TABLE graphics_cards (
    graphics_card_id SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    vram_size INTEGER NOT NULL, -- GB
    memory_type VARCHAR(50), -- e.g., GDDR6
    base_clock INTEGER, -- MHz
    boost_clock INTEGER, -- MHz
    tdp INTEGER, -- Watts
    UNIQUE(brand, model)
);

CREATE TABLE operating_systems (
    os_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE, -- e.g., Windows 11 Pro
    version VARCHAR(50),
    architecture VARCHAR(20) -- e.g., 64-bit
);

CREATE TABLE computers (
    computer_id SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL UNIQUE,
    processor_id INTEGER REFERENCES processors(processor_id) NOT NULL,
    memory_size INTEGER NOT NULL, -- GB
    memory_type_id INTEGER REFERENCES memory_types(memory_type_id) NOT NULL,
    storage_capacity INTEGER NOT NULL, -- GB
    storage_type_id INTEGER REFERENCES storage_types(storage_type_id) NOT NULL,
    graphics_card_id INTEGER REFERENCES graphics_cards(graphics_card_id),
    os_id INTEGER REFERENCES operating_systems(os_id),
    price DECIMAL(10,2) NOT NULL,
    release_date DATE,
    weight DECIMAL(5,2), -- kg
    dimensions VARCHAR(50), -- e.g., "350 x 250 x 50 mm"
    warranty_months INTEGER,
    stock_quantity INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better query performance
CREATE INDEX idx_computers_model ON computers(model_name);
CREATE INDEX idx_computers_processor ON computers(processor_id);
CREATE INDEX idx_computers_price ON computers(price);
CREATE INDEX idx_computers_memory ON computers(memory_size);
CREATE INDEX idx_computers_storage ON computers(storage_capacity);

-- Trigger to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_computers_timestamp
BEFORE UPDATE ON computers
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();
```
