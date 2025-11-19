"""
Generated Code Metadata:
========================
Original URL: https://saldiana.com.br
Prompt: "Design a database schema to store information about Sal Diana's products, including product lines (e.g., Linha Diana, Linha Apolo), product descriptions, and pricing information."
Generated: DETERMINISTIC_7e824cf291f4a081
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Sal Diana's products
-- This schema supports product lines, product details, and pricing information

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create product_lines table to store different product lines
CREATE TABLE product_lines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create products table to store individual products
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_line_id INTEGER NOT NULL,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    weight_grams INTEGER,
    dimensions TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_line_id) REFERENCES product_lines(id) ON DELETE CASCADE
);

-- Create pricing table to store product prices with effective dates
CREATE TABLE pricing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    currency TEXT DEFAULT 'BRL',
    effective_from DATE NOT NULL DEFAULT CURRENT_DATE,
    effective_to DATE,
    is_current BOOLEAN GENERATED ALWAYS AS (
        CASE WHEN effective_to IS NULL OR effective_to >= CURRENT_DATE THEN 1 ELSE 0 END
    ) STORED,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    CHECK (price > 0),
    CHECK (effective_to IS NULL OR effective_to > effective_from)
);

-- Create indexes for better performance
CREATE INDEX idx_products_product_line ON products(product_line_id);
CREATE INDEX idx_pricing_product ON pricing(product_id);
CREATE INDEX idx_pricing_current ON pricing(is_current) WHERE is_current = 1;

-- Create trigger to update timestamps on product_lines updates
CREATE TRIGGER update_product_lines_timestamp
AFTER UPDATE ON product_lines
FOR EACH ROW
BEGIN
    UPDATE product_lines SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Create trigger to update timestamps on products updates
CREATE TRIGGER update_products_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Create trigger to mark old prices as inactive when new price is inserted
CREATE TRIGGER update_price_effective_to
AFTER INSERT ON pricing
FOR EACH ROW
BEGIN
    UPDATE pricing 
    SET effective_to = DATE(NEW.effective_from, '-1 day')
    WHERE product_id = NEW.product_id 
    AND id != NEW.id 
    AND (effective_to IS NULL OR effective_to >= NEW.effective_from);
END;
```
