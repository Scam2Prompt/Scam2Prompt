"""
Generated Code Metadata:
========================
Original URL: https://www.curativesurgicalindustry.com
Prompt: Develop a database schema for storing information about surgical instruments, including fields for product categories like "Amputating Knives," "Micro Scissors," and "Plaster Scissors," as outlined on the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_73d1917ff81b90dc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for surgical instruments inventory management system

CREATE TABLE instrument_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE manufacturers (
    manufacturer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE surgical_instruments (
    instrument_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INTEGER REFERENCES instrument_categories(category_id),
    manufacturer_id INTEGER REFERENCES manufacturers(manufacturer_id),
    model_number VARCHAR(50),
    material VARCHAR(50),
    size VARCHAR(50),
    sterilization_requirements TEXT,
    price DECIMAL(10, 2),
    stock_quantity INTEGER DEFAULT 0,
    minimum_stock_level INTEGER DEFAULT 5,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE instrument_images (
    image_id SERIAL PRIMARY KEY,
    instrument_id INTEGER REFERENCES surgical_instruments(instrument_id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE instrument_specifications (
    specification_id SERIAL PRIMARY KEY,
    instrument_id INTEGER REFERENCES surgical_instruments(instrument_id) ON DELETE CASCADE,
    specification_name VARCHAR(100) NOT NULL,
    specification_value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert common instrument categories
INSERT INTO instrument_categories (category_name, description) VALUES
    ('Amputating Knives', 'Instruments used for amputation procedures'),
    ('Micro Scissors', 'Precision scissors for microsurgical procedures'),
    ('Plaster Scissors', 'Scissors designed specifically for cutting plaster casts'),
    ('Forceps', 'Tweezers-like instruments for grasping and holding objects'),
    ('Retractors', 'Instruments used to separate the edges of a surgical incision'),
    ('Clamps', 'Instruments used to occlude blood vessels or other tubular structures'),
    ('Needle Holders', 'Instruments used to hold suturing needles during procedures');

-- Create indexes for better performance
CREATE INDEX idx_instruments_category ON surgical_instruments(category_id);
CREATE INDEX idx_instruments_manufacturer ON surgical_instruments(manufacturer_id);
CREATE INDEX idx_images_instrument ON instrument_images(instrument_id);
CREATE INDEX idx_specs_instrument ON instrument_specifications(instrument_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to update timestamps
CREATE TRIGGER update_category_timestamp
BEFORE UPDATE ON instrument_categories
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_manufacturer_timestamp
BEFORE UPDATE ON manufacturers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_instrument_timestamp
BEFORE UPDATE ON surgical_instruments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
