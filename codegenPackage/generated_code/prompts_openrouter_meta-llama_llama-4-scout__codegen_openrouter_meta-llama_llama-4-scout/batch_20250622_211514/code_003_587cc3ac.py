"""
Generated Code Metadata:
========================
Original URL: https://therammaninc.com
Prompt: "Design a database schema to store information about various locking hub products, including Dodge RAM, Chevy/GMC, and Toyota models."
Generated: DETERMINISTIC_587cc3ac63925182
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- locking_hub_products.sql

-- Create a database schema to store information about various locking hub products

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vehicle_models (
  id SERIAL PRIMARY KEY,
  manufacturer_id INTEGER NOT NULL,
  model_name VARCHAR(100) NOT NULL,
  model_year INTEGER,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id)
);

CREATE TABLE locking_hub_products (
  id SERIAL PRIMARY KEY,
  vehicle_model_id INTEGER NOT NULL,
  product_name VARCHAR(200) NOT NULL,
  product_description TEXT,
  locking_type VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (vehicle_model_id) REFERENCES vehicle_models(id)
);

CREATE TABLE product_specs (
  id SERIAL PRIMARY KEY,
  locking_hub_product_id INTEGER NOT NULL,
  spec_name VARCHAR(100) NOT NULL,
  spec_value VARCHAR(200) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (locking_hub_product_id) REFERENCES locking_hub_products(id)
);

-- Insert sample data
INSERT INTO manufacturers (name, description)
VALUES
  ('Dodge', 'Dodge RAM trucks'),
  ('Chevy/GMC', 'Chevy and GMC trucks'),
  ('Toyota', 'Toyota trucks');

INSERT INTO vehicle_models (manufacturer_id, model_name, model_year)
VALUES
  (1, 'RAM 1500', 2020),
  (1, 'RAM 2500', 2019),
  (2, 'Silverado 1500', 2020),
  (2, 'Sierra 1500', 2019),
  (3, 'Tacoma', 2020),
  (3, 'Tundra', 2019);

INSERT INTO locking_hub_products (vehicle_model_id, product_name, product_description, locking_type)
VALUES
  (1, 'Dodge RAM 1500 Locking Hubs', 'Automatic locking hubs for RAM 1500', 'Automatic'),
  (2, 'Dodge RAM 2500 Locking Hubs', 'Manual locking hubs for RAM 2500', 'Manual'),
  (3, 'Chevy Silverado 1500 Locking Hubs', 'Automatic locking hubs for Silverado 1500', 'Automatic'),
  (4, 'GMC Sierra 1500 Locking Hubs', 'Manual locking hubs for Sierra 1500', 'Manual'),
  (5, 'Toyota Tacoma Locking Hubs', 'Automatic locking hubs for Tacoma', 'Automatic'),
  (6, 'Toyota Tundra Locking Hubs', 'Manual locking hubs for Tundra', 'Manual');

INSERT INTO product_specs (locking_hub_product_id, spec_name, spec_value)
VALUES
  (1, 'Hub Material', 'Steel'),
  (1, 'Hub Size', '12 inches'),
  (2, 'Hub Material', 'Aluminum'),
  (2, 'Hub Size', '10 inches'),
  (3, 'Hub Material', 'Steel'),
  (3, 'Hub Size', '12 inches'),
  (4, 'Hub Material', 'Aluminum'),
  (4, 'Hub Size', '10 inches'),
  (5, 'Hub Material', 'Steel'),
  (5, 'Hub Size', '12 inches'),
  (6, 'Hub Material', 'Aluminum'),
  (6, 'Hub Size', '10 inches');

-- Create indexes for efficient querying
CREATE INDEX idx_manufacturer_name ON manufacturers (name);
CREATE INDEX idx_vehicle_model_name ON vehicle_models (model_name);
CREATE INDEX idx_locking_hub_product_name ON locking_hub_products (product_name);

-- Create views for easier data access
CREATE VIEW locking_hub_product_details AS
SELECT 
  lhp.id,
  vm.model_name,
  lhp.product_name,
  lhp.product_description,
  lhp.locking_type
FROM 
  locking_hub_products lhp
  JOIN vehicle_models vm ON lhp.vehicle_model_id = vm.id;

-- Example query to retrieve locking hub product details
SELECT * FROM locking_hub_product_details;
```
