"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Design a database schema to store information about beers, including name, style, price, and quantity in stock, suitable for an online beer store like Barbudo Growler.
Generated: DETERMINISTIC_4d0235337122580b
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Barbudo Growler online beer store

CREATE TABLE beer_styles (
    style_id SERIAL PRIMARY KEY,
    style_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE breweries (
    brewery_id SERIAL PRIMARY KEY,
    brewery_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    website VARCHAR(255),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE beers (
    beer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    style_id INTEGER REFERENCES beer_styles(style_id),
    brewery_id INTEGER REFERENCES breweries(brewery_id),
    abv DECIMAL(3,1),
    ibu INTEGER,
    description TEXT,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    beer_id INTEGER REFERENCES beers(beer_id) ON DELETE CASCADE,
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    quantity INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    size_oz DECIMAL(5,2) NOT NULL CHECK (size_oz > 0),
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_beer_style ON beers(style_id);
CREATE INDEX idx_beer_brewery ON beers(brewery_id);
CREATE INDEX idx_inventory_beer ON inventory(beer_id);
CREATE INDEX idx_inventory_availability ON inventory(is_available);

-- Trigger to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_beer_styles_timestamp
BEFORE UPDATE ON beer_styles
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_breweries_timestamp
BEFORE UPDATE ON breweries
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_beers_timestamp
BEFORE UPDATE ON beers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_inventory_timestamp
BEFORE UPDATE ON inventory
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
