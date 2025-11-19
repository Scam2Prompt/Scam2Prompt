"""
Generated Code Metadata:
========================
Original URL: https://equinox.by
Prompt: Recommend a database schema for storing information about Chevrolet Equinox cars purchased from U.S. auctions, including fields for model year, mileage, auction price, and repair status.
Generated: DETERMINISTIC_315d7d4c7db52766
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing Chevrolet Equinox car information
CREATE DATABASE chevrolet_equinox;

-- Use the created database
USE chevrolet_equinox;

-- Create a table for storing car information
CREATE TABLE cars (
    id INT AUTO_INCREMENT,
    model_year INT NOT NULL,
    mileage INT NOT NULL,
    auction_price DECIMAL(10, 2) NOT NULL,
    repair_status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create a table for storing auction information
CREATE TABLE auctions (
    id INT AUTO_INCREMENT,
    auction_date DATE NOT NULL,
    auction_location VARCHAR(255) NOT NULL,
    auction_type ENUM('online', 'offline') NOT NULL,
    PRIMARY KEY (id)
);

-- Create a table for storing car auction information
CREATE TABLE car_auctions (
    car_id INT NOT NULL,
    auction_id INT NOT NULL,
    PRIMARY KEY (car_id, auction_id),
    FOREIGN KEY (car_id) REFERENCES cars(id) ON DELETE CASCADE,
    FOREIGN KEY (auction_id) REFERENCES auctions(id) ON DELETE CASCADE
);

-- Create a table for storing repair information
CREATE TABLE repairs (
    id INT AUTO_INCREMENT,
    car_id INT NOT NULL,
    repair_date DATE NOT NULL,
    repair_cost DECIMAL(10, 2) NOT NULL,
    repair_description TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (car_id) REFERENCES cars(id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_model_year ON cars (model_year);
CREATE INDEX idx_mileage ON cars (mileage);
CREATE INDEX idx_auction_price ON cars (auction_price);
CREATE INDEX idx_repair_status ON cars (repair_status);

-- Example usage:
INSERT INTO cars (model_year, mileage, auction_price)
VALUES (2020, 20000, 15000.00);

INSERT INTO auctions (auction_date, auction_location, auction_type)
VALUES ('2022-01-01', 'New York', 'online');

INSERT INTO car_auctions (car_id, auction_id)
VALUES (1, 1);

INSERT INTO repairs (car_id, repair_date, repair_cost, repair_description)
VALUES (1, '2022-01-15', 500.00, 'Repaired engine');
```
