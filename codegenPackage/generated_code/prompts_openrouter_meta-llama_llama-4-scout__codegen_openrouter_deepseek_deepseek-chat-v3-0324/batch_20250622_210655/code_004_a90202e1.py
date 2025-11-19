"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Design a simple database schema for storing information about frozen yogurt flavors, toppings, and store locations for a business like Andias Frozen Yogurt.
Generated: DETERMINISTIC_a90202e1a8e48132
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for frozen yogurt business

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Store locations
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    opening_hours TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (name, address)
);

-- Yogurt flavors
CREATE TABLE flavors (
    flavor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_seasonal BOOLEAN DEFAULT 0,
    is_dairy_free BOOLEAN DEFAULT 0,
    is_sugar_free BOOLEAN DEFAULT 0,
    calories_per_ounce INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Toppings
CREATE TABLE toppings (
    topping_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL CHECK (category IN ('fruit', 'sweet', 'nut', 'sauce', 'other')),
    is_premium BOOLEAN DEFAULT 0,
    has_nuts BOOLEAN DEFAULT 0,
    is_vegan BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for flavors available at locations
CREATE TABLE location_flavors (
    location_id INTEGER NOT NULL,
    flavor_id INTEGER NOT NULL,
    is_available BOOLEAN DEFAULT 1,
    PRIMARY KEY (location_id, flavor_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    FOREIGN KEY (flavor_id) REFERENCES flavors(flavor_id) ON DELETE CASCADE
);

-- Junction table for toppings available at locations
CREATE TABLE location_toppings (
    location_id INTEGER NOT NULL,
    topping_id INTEGER NOT NULL,
    is_available BOOLEAN DEFAULT 1,
    PRIMARY KEY (location_id, topping_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    FOREIGN KEY (topping_id) REFERENCES toppings(topping_id) ON DELETE CASCADE
);

-- Price structure
CREATE TABLE pricing (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    size TEXT NOT NULL CHECK (size IN ('small', 'medium', 'large', 'x-large')),
    base_price DECIMAL(5,2) NOT NULL,
    premium_topping_surcharge DECIMAL(3,2) DEFAULT 0.50,
    effective_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_location_timestamp
AFTER UPDATE ON locations
BEGIN
    UPDATE locations SET updated_at = CURRENT_TIMESTAMP WHERE location_id = NEW.location_id;
END;

CREATE TRIGGER update_flavor_timestamp
AFTER UPDATE ON flavors
BEGIN
    UPDATE flavors SET updated_at = CURRENT_TIMESTAMP WHERE flavor_id = NEW.flavor_id;
END;

CREATE TRIGGER update_topping_timestamp
AFTER UPDATE ON toppings
BEGIN
    UPDATE toppings SET updated_at = CURRENT_TIMESTAMP WHERE topping_id = NEW.topping_id;
END;

-- Create indexes for performance
CREATE INDEX idx_flavor_name ON flavors(name);
CREATE INDEX idx_topping_name ON toppings(name);
CREATE INDEX idx_location_city ON locations(city);
CREATE INDEX idx_location_state ON locations(state);
```
