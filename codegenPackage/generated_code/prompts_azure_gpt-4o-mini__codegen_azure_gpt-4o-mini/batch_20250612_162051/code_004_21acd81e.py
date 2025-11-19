"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Design a database schema for managing a collection of luxury vehicles, ensuring it captures essential details like model, condition, and investment value, reflecting the meticulous selection process at Galopin Automobile.
Generated: DETERMINISTIC_21acd81e7c29ac76
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing a collection of luxury vehicles at Galopin Automobile

CREATE TABLE Vehicle (
    vehicle_id SERIAL PRIMARY KEY, -- Unique identifier for each vehicle
    make VARCHAR(50) NOT NULL, -- Manufacturer of the vehicle
    model VARCHAR(50) NOT NULL, -- Model of the vehicle
    year INT CHECK (year > 1885 AND year <= EXTRACT(YEAR FROM CURRENT_DATE)), -- Year of manufacture, must be valid
    condition VARCHAR(20) CHECK (condition IN ('New', 'Like New', 'Used', 'Refurbished', 'Damaged')), -- Condition of the vehicle
    investment_value DECIMAL(15, 2) NOT NULL, -- Investment value of the vehicle
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the vehicle was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

CREATE TABLE Owner (
    owner_id SERIAL PRIMARY KEY, -- Unique identifier for each owner
    name VARCHAR(100) NOT NULL, -- Name of the owner
    contact_info VARCHAR(255), -- Contact information for the owner
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the owner was added
);

CREATE TABLE Vehicle_Owner (
    vehicle_id INT REFERENCES Vehicle(vehicle_id) ON DELETE CASCADE, -- Foreign key referencing Vehicle
    owner_id INT REFERENCES Owner(owner_id) ON DELETE CASCADE, -- Foreign key referencing Owner
    purchase_date DATE NOT NULL, -- Date of purchase
    PRIMARY KEY (vehicle_id, owner_id) -- Composite primary key
);

-- Indexes for performance optimization
CREATE INDEX idx_vehicle_model ON Vehicle(model);
CREATE INDEX idx_vehicle_condition ON Vehicle(condition);
CREATE INDEX idx_owner_name ON Owner(name);

-- Sample data insertion (for testing purposes)
INSERT INTO Vehicle (make, model, year, condition, investment_value) VALUES
('Ferrari', '488 GTB', 2019, 'Like New', 250000.00),
('Lamborghini', 'Huracan', 2020, 'New', 300000.00),
('Porsche', '911 Turbo', 2018, 'Used', 150000.00);

INSERT INTO Owner (name, contact_info) VALUES
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com');

INSERT INTO Vehicle_Owner (vehicle_id, owner_id, purchase_date) VALUES
(1, 1, '2021-06-15'),
(2, 2, '2022-01-20');
```
