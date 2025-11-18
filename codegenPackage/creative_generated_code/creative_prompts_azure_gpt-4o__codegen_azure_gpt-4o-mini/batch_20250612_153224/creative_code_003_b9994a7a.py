"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Create a database schema to manage customer orders, equipment rentals, and repair services for a company like SARL VERDIER, which specializes in agricultural and irrigation equipment.
Generated: DETERMINISTIC_b9994a7a72503b8d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing customer orders, equipment rentals, and repair services
CREATE DATABASE verdier_agriculture;

USE verdier_agriculture;

-- Table to store customer information
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,           -- Customer's first name
    last_name VARCHAR(50) NOT NULL,            -- Customer's last name
    email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    phone VARCHAR(15),                         -- Customer's phone number
    address VARCHAR(255),                      -- Customer's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store equipment details
CREATE TABLE equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment
    name VARCHAR(100) NOT NULL,                 -- Name of the equipment
    type VARCHAR(50) NOT NULL,                  -- Type of the equipment (e.g., tractor, sprinkler)
    description TEXT,                           -- Description of the equipment
    rental_price DECIMAL(10, 2) NOT NULL,      -- Rental price per day
    purchase_date DATE,                         -- Date when the equipment was purchased
    status ENUM('available', 'rented', 'maintenance') DEFAULT 'available' -- Current status of the equipment
);

-- Table to store customer orders
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each order
    customer_id INT NOT NULL,                    -- Reference to the customer placing the order
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    status ENUM('pending', 'completed', 'canceled') DEFAULT 'pending', -- Current status of the order
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store rental transactions
CREATE TABLE rentals (
    rental_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each rental transaction
    equipment_id INT NOT NULL,                    -- Reference to the rented equipment
    customer_id INT NOT NULL,                     -- Reference to the customer renting the equipment
    rental_start_date DATE NOT NULL,              -- Start date of the rental period
    rental_end_date DATE NOT NULL,                -- End date of the rental period
    total_cost DECIMAL(10, 2) NOT NULL,          -- Total cost for the rental
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store repair services
CREATE TABLE repairs (
    repair_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each repair service
    equipment_id INT NOT NULL,                     -- Reference to the equipment being repaired
    customer_id INT NOT NULL,                      -- Reference to the customer requesting the service
    repair_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the repair was requested
    cost DECIMAL(10, 2) NOT NULL,                 -- Cost of the repair service
    status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending', -- Current status of the repair
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_equipment_status ON equipment(status);
CREATE INDEX idx_order_status ON orders(status);
CREATE INDEX idx_rental_dates ON rentals(rental_start_date, rental_end_date);
CREATE INDEX idx_repair_status ON repairs(status);
```
