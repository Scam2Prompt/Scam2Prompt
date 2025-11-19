"""
Generated Code Metadata:
========================
Original URL: https://www.curativesurgicalindustry.com
Prompt: "Design a database schema to store information about surgical instruments, including product codes and descriptions, for a company like Curative Surgical Industry."
Generated: DETERMINISTIC_fd7061e437f3ee23
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for surgical instruments inventory
-- Designed for a company like Curative Surgical Industry

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create instrument categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

-- Create manufacturers table
CREATE TABLE IF NOT EXISTS manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

-- Create instruments table
CREATE TABLE IF NOT EXISTS instruments (
    instrument_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_code TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    sterilization_required BOOLEAN DEFAULT TRUE,
    disposable BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id),
    UNIQUE(product_code)
);

-- Create inventory table
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    instrument_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    minimum_stock_level INTEGER DEFAULT 5,
    last_restocked TIMESTAMP,
    location TEXT,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);

-- Create instrument specifications table
CREATE TABLE IF NOT EXISTS specifications (
    specification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    instrument_id INTEGER NOT NULL,
    attribute_name TEXT NOT NULL,
    attribute_value TEXT NOT NULL,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);

-- Create price history table
CREATE TABLE IF NOT EXISTS price_history (
    price_history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    instrument_id INTEGER NOT NULL,
    old_price DECIMAL(10, 2) NOT NULL,
    new_price DECIMAL(10, 2) NOT NULL,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_by TEXT,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);

-- Create trigger to update timestamp on instrument update
CREATE TRIGGER IF NOT EXISTS update_instrument_timestamp
AFTER UPDATE ON instruments
BEGIN
    UPDATE instruments SET updated_at = CURRENT_TIMESTAMP WHERE instrument_id = NEW.instrument_id;
END;

-- Create trigger to log price changes
CREATE TRIGGER IF NOT EXISTS log_price_change
AFTER UPDATE OF unit_price ON instruments
WHEN OLD.unit_price <> NEW.unit_price
BEGIN
    INSERT INTO price_history (instrument_id, old_price, new_price, changed_by)
    VALUES (NEW.instrument_id, OLD.unit_price, NEW.unit_price, 'system');
END;

-- Create index for faster searches
CREATE INDEX IF NOT EXISTS idx_instruments_product_code ON instruments(product_code);
CREATE INDEX IF NOT EXISTS idx_instruments_category ON instruments(category_id);
CREATE INDEX IF NOT EXISTS idx_instruments_manufacturer ON instruments(manufacturer_id);
CREATE INDEX IF NOT EXISTS idx_inventory_instrument ON inventory(instrument_id);
```
