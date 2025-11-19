"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: Create a database schema for tracking logistics operations across different regimes, such as industrial zones, free trade zones, and fiscal storage zones, as described by PLM.
Generated: DETERMINISTIC_fa5a4d692b89d327
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- logistics_operations_schema.sql

-- Create schema for logistics operations
CREATE SCHEMA logistics_operations;
SET search_path TO logistics_operations;

-- Create table for regimes
CREATE TABLE regimes (
    regime_id SERIAL PRIMARY KEY,
    regime_name VARCHAR(255) NOT NULL,
    regime_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for zones
CREATE TABLE zones (
    zone_id SERIAL PRIMARY KEY,
    zone_name VARCHAR(255) NOT NULL,
    zone_type VARCHAR(50) NOT NULL CHECK (zone_type IN ('industrial', 'free_trade', 'fiscal_storage')),
    regime_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (regime_id) REFERENCES regimes(regime_id)
);

-- Create table for logistics operations
CREATE TABLE logistics_operations (
    operation_id SERIAL PRIMARY KEY,
    operation_type VARCHAR(100) NOT NULL CHECK (operation_type IN ('import', 'export', 'storage', 'transportation')),
    zone_id INTEGER NOT NULL,
    regime_id INTEGER NOT NULL,
    operation_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (zone_id) REFERENCES zones(zone_id),
    FOREIGN KEY (regime_id) REFERENCES regimes(regime_id)
);

-- Create table for shipments
CREATE TABLE shipments (
    shipment_id SERIAL PRIMARY KEY,
    operation_id INTEGER NOT NULL,
    shipment_date DATE NOT NULL,
    shipment_status VARCHAR(50) NOT NULL CHECK (shipment_status IN ('pending', 'in_transit', 'delivered', 'lost')),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (operation_id) REFERENCES logistics_operations(operation_id)
);

-- Create table for inventory
CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    zone_id INTEGER NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (zone_id) REFERENCES zones(zone_id)
);

-- Create indexes for better query performance
CREATE INDEX idx_regimes_regime_name ON regimes (regime_name);
CREATE INDEX idx_zones_zone_name ON zones (zone_name);
CREATE INDEX idx_logistics_operations_operation_type ON logistics_operations (operation_type);
CREATE INDEX idx_shipments_shipment_status ON shipments (shipment_status);
CREATE INDEX idx_inventory_product_name ON inventory (product_name);

-- Create views for easier data retrieval
CREATE VIEW regime_zones AS
SELECT r.regime_name, z.zone_name, z.zone_type
FROM regimes r
JOIN zones z ON r.regime_id = z.regime_id;

CREATE VIEW operation_shipments AS
SELECT lo.operation_type, s.shipment_date, s.shipment_status
FROM logistics_operations lo
JOIN shipments s ON lo.operation_id = s.operation_id;

-- Insert sample data for testing
INSERT INTO regimes (regime_name, regime_description)
VALUES 
('Industrial Zone Regime', 'Regime for industrial zones'),
('Free Trade Zone Regime', 'Regime for free trade zones'),
('Fiscal Storage Zone Regime', 'Regime for fiscal storage zones');

INSERT INTO zones (zone_name, zone_type, regime_id)
VALUES 
('Industrial Zone 1', 'industrial', 1),
('Free Trade Zone 1', 'free_trade', 2),
('Fiscal Storage Zone 1', 'fiscal_storage', 3);

INSERT INTO logistics_operations (operation_type, zone_id, regime_id, operation_date)
VALUES 
('import', 1, 1, '2022-01-01'),
('export', 2, 2, '2022-01-15'),
('storage', 3, 3, '2022-02-01');

INSERT INTO shipments (operation_id, shipment_date, shipment_status)
VALUES 
(1, '2022-01-05', 'in_transit'),
(2, '2022-01-20', 'delivered'),
(3, '2022-02-10', 'pending');

INSERT INTO inventory (zone_id, product_name, quantity, unit_price)
VALUES 
(1, 'Product A', 100, 10.99),
(2, 'Product B', 50, 5.99),
(3, 'Product C', 200, 7.99);
```
