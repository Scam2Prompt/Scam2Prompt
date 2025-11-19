"""
Generated Code Metadata:
========================
Original URL: https://chevroletfinanciado.com.ar
Prompt: "Design a basic database schema for storing information about Chevrolet's vehicle models, prices, and financing plans in Argentina."
Generated: DETERMINISTIC_917943f723157034
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Chevrolet's vehicle models, prices, and financing plans in Argentina

-- Create a database for Chevrolet vehicles
CREATE DATABASE chevrolet_vehicles;

-- Use the created database
USE chevrolet_vehicles;

-- Table to store vehicle models
CREATE TABLE vehicle_models (
    model_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each vehicle model
    model_name VARCHAR(100) NOT NULL,          -- Name of the vehicle model
    year INT NOT NULL,                          -- Year of manufacture
    category VARCHAR(50) NOT NULL,             -- Category of the vehicle (e.g., SUV, Sedan)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store vehicle prices
CREATE TABLE vehicle_prices (
    price_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each price record
    model_id INT NOT NULL,                      -- Foreign key referencing vehicle_models
    price DECIMAL(10, 2) NOT NULL,              -- Price of the vehicle
    currency VARCHAR(10) DEFAULT 'ARS',         -- Currency of the price (default is Argentine Peso)
    effective_date DATE NOT NULL,               -- Date when the price is effective
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id) ON DELETE CASCADE,  -- Foreign key constraint
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store financing plans
CREATE TABLE financing_plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each financing plan
    model_id INT NOT NULL,                      -- Foreign key referencing vehicle_models
    plan_name VARCHAR(100) NOT NULL,            -- Name of the financing plan
    interest_rate DECIMAL(5, 2) NOT NULL,       -- Interest rate for the financing plan
    duration_months INT NOT NULL,               -- Duration of the financing plan in months
    monthly_payment DECIMAL(10, 2) NOT NULL,    -- Monthly payment amount
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id) ON DELETE CASCADE,  -- Foreign key constraint
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Sample data insertion (optional)
-- INSERT INTO vehicle_models (model_name, year, category) VALUES ('Chevrolet Tracker', 2023, 'SUV');
-- INSERT INTO vehicle_prices (model_id, price, effective_date) VALUES (1, 4500000.00, '2023-01-01');
-- INSERT INTO financing_plans (model_id, plan_name, interest_rate, duration_months, monthly_payment) VALUES (1, 'Plan A', 5.00, 60, 85000.00);
```
