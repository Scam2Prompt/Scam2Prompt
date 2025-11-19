"""
Generated Code Metadata:
========================
Original URL: https://pepesco.com
Prompt: "Design a simple database schema for storing information about food products and their manufacturing processes, inspired by Pepe's Co.'s services."
Generated: DETERMINISTIC_689324c173a1537e
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for food products and manufacturing processes

-- Table for storing product categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing manufacturers
CREATE TABLE manufacturers (
    manufacturer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    certification_details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing food products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INTEGER REFERENCES categories(category_id),
    manufacturer_id INTEGER REFERENCES manufacturers(manufacturer_id),
    ingredients TEXT,
    nutritional_info TEXT,
    shelf_life_days INTEGER,
    is_organic BOOLEAN DEFAULT FALSE,
    is_gluten_free BOOLEAN DEFAULT FALSE,
    is_vegan BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing manufacturing processes
CREATE TABLE manufacturing_processes (
    process_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_minutes INTEGER,
    temperature_celsius DECIMAL(5,2),
    required_equipment TEXT,
    safety_precautions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for product-process relationships
CREATE TABLE product_processes (
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    process_id INTEGER REFERENCES manufacturing_processes(process_id) ON DELETE CASCADE,
    step_order INTEGER NOT NULL,
    notes TEXT,
    PRIMARY KEY (product_id, process_id)
);

-- Table for quality control checks
CREATE TABLE quality_checks (
    check_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    standard VARCHAR(100),
    frequency_days INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for process-quality check relationships
CREATE TABLE process_quality_checks (
    process_id INTEGER REFERENCES manufacturing_processes(process_id) ON DELETE CASCADE,
    check_id INTEGER REFERENCES quality_checks(check_id) ON DELETE CASCADE,
    is_mandatory BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (process_id, check_id)
);

-- Table for batch production records
CREATE TABLE production_batches (
    batch_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    production_date DATE NOT NULL,
    expiry_date DATE,
    quantity_produced INTEGER NOT NULL,
    operator_name VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for batch quality test results
CREATE TABLE batch_quality_results (
    result_id SERIAL PRIMARY KEY,
    batch_id INTEGER REFERENCES production_batches(batch_id) ON DELETE CASCADE,
    check_id INTEGER REFERENCES quality_checks(check_id),
    test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    passed BOOLEAN NOT NULL,
    test_value DECIMAL(10,2),
    notes TEXT,
    tester_name VARCHAR(100)
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_categories_timestamp
BEFORE UPDATE ON categories
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_manufacturers_timestamp
BEFORE UPDATE ON manufacturers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_processes_timestamp
BEFORE UPDATE ON manufacturing_processes
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_quality_checks_timestamp
BEFORE UPDATE ON quality_checks
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_batches_timestamp
BEFORE UPDATE ON production_batches
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
