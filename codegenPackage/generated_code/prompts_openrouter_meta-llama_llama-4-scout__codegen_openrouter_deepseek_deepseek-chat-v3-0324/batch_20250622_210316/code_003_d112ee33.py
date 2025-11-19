"""
Generated Code Metadata:
========================
Original URL: https://bismillahgems.com
Prompt: Design a database schema to store information about gemstones, including their types, carat weights, prices, and images, for a website like Bismillah Gems.
Generated: DETERMINISTIC_d112ee332b6845db
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Bismillah Gems gemstone inventory system

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Gemstone types/categories table
CREATE TABLE gemstone_types (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    mohs_hardness DECIMAL(3,1),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Color table for gemstones
CREATE TABLE colors (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL UNIQUE,
    hex_code VARCHAR(7),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Gemstones table
CREATE TABLE gemstones (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    type_id UUID NOT NULL REFERENCES gemstone_types(id),
    color_id UUID REFERENCES colors(id),
    carat_weight DECIMAL(8,3) NOT NULL,
    clarity VARCHAR(50),
    cut_quality VARCHAR(50),
    origin VARCHAR(100),
    price DECIMAL(12,2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    stock_quantity INTEGER DEFAULT 1,
    certification VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (carat_weight > 0),
    CHECK (price > 0),
    CHECK (stock_quantity >= 0)
);

-- Images table for gemstones
CREATE TABLE gemstone_images (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    gemstone_id UUID NOT NULL REFERENCES gemstones(id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    caption VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT one_primary_image_per_gemstone UNIQUE (gemstone_id, is_primary) DEFERRABLE INITIALLY DEFERRED
);

-- Price history table
CREATE TABLE price_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    gemstone_id UUID NOT NULL REFERENCES gemstones(id) ON DELETE CASCADE,
    old_price DECIMAL(12,2) NOT NULL,
    new_price DECIMAL(12,2) NOT NULL,
    changed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(100),
    reason TEXT
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger for gemstones table
CREATE TRIGGER update_gemstones_updated_at
BEFORE UPDATE ON gemstones
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Trigger for gemstone_types table
CREATE TRIGGER update_gemstone_types_updated_at
BEFORE UPDATE ON gemstone_types
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Indexes for performance optimization
CREATE INDEX idx_gemstones_type ON gemstones(type_id);
CREATE INDEX idx_gemstones_color ON gemstones(color_id);
CREATE INDEX idx_gemstones_price ON gemstones(price);
CREATE INDEX idx_gemstones_weight ON gemstones(carat_weight);
CREATE INDEX idx_gemstones_availability ON gemstones(is_available);
CREATE INDEX idx_gemstone_images_gemstone ON gemstone_images(gemstone_id);
CREATE INDEX idx_price_history_gemstone ON price_history(gemstone_id);
```
