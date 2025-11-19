"""
Generated Code Metadata:
========================
Original URL: https://equinox.by
Prompt: "Design a basic database schema to store information about Chevrolet Equinox vehicles, including their specifications, auction history, and delivery status."
Generated: DETERMINISTIC_5e6198ed3dd92b5e
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Chevrolet Equinox Vehicle Database

-- Vehicles table stores core vehicle information
CREATE TABLE vehicles (
    vehicle_id VARCHAR(17) PRIMARY KEY, -- VIN number
    model_year INT NOT NULL,
    trim_level VARCHAR(50) NOT NULL,
    exterior_color VARCHAR(50) NOT NULL,
    interior_color VARCHAR(50) NOT NULL,
    engine_type VARCHAR(50) NOT NULL,
    transmission_type VARCHAR(50) NOT NULL,
    drivetrain VARCHAR(20) NOT NULL,
    mileage INT NOT NULL,
    date_manufactured DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (model_year >= 2005) -- First year of Equinox production
);

-- Specifications table for detailed vehicle specs
CREATE TABLE specifications (
    spec_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id VARCHAR(17) NOT NULL,
    fuel_economy_city DECIMAL(4,1),
    fuel_economy_highway DECIMAL(4,1),
    horsepower INT,
    torque INT,
    seating_capacity INT,
    cargo_volume DECIMAL(6,2),
    towing_capacity INT,
    infotainment_system VARCHAR(100),
    safety_features TEXT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    CHECK (horsepower > 0),
    CHECK (torque > 0),
    CHECK (seating_capacity > 0)
);

-- Auction history table
CREATE TABLE auction_history (
    auction_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id VARCHAR(17) NOT NULL,
    auction_date DATE NOT NULL,
    auction_location VARCHAR(100) NOT NULL,
    sale_price DECIMAL(10,2),
    buyer_id VARCHAR(50),
    seller_id VARCHAR(50) NOT NULL,
    auction_notes TEXT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    CHECK (sale_price >= 0)
);

-- Delivery status tracking
CREATE TABLE delivery_status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id VARCHAR(17) NOT NULL,
    current_location VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL, -- e.g., "In Transit", "Delivered", "Pending"
    estimated_delivery_date DATE,
    actual_delivery_date DATE,
    carrier_name VARCHAR(100),
    tracking_number VARCHAR(100),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    CHECK (actual_delivery_date IS NULL OR actual_delivery_date >= estimated_delivery_date)
);

-- Indexes for performance optimization
CREATE INDEX idx_vehicle_model_year ON vehicles(model_year);
CREATE INDEX idx_vehicle_trim ON vehicles(trim_level);
CREATE INDEX idx_auction_date ON auction_history(auction_date);
CREATE INDEX idx_delivery_status ON delivery_status(status);
```
