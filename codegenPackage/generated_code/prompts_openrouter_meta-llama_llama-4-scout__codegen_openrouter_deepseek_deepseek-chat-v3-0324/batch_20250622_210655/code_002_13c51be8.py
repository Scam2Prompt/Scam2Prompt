"""
Generated Code Metadata:
========================
Original URL: https://hsrenterprises.co.in
Prompt: Generate a sample database schema for storing information about Royal Enfield vehicles, including pre-owned vehicles, at a dealership like HSR Enterprises.
Generated: DETERMINISTIC_13c51be887814686
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Royal Enfield dealership management system

-- Create the database
CREATE DATABASE IF NOT EXISTS royal_enfield_dealership;
USE royal_enfield_dealership;

-- Table for storing vehicle models
CREATE TABLE IF NOT EXISTS vehicle_models (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    engine_cc INT NOT NULL,
    fuel_type ENUM('Petrol', 'Diesel', 'Electric') NOT NULL,
    launch_year YEAR NOT NULL,
    current_price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    is_discontinued BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_engine_cc CHECK (engine_cc > 0),
    CONSTRAINT chk_price CHECK (current_price > 0)
) ENGINE=InnoDB;

-- Table for storing color options
CREATE TABLE IF NOT EXISTS colors (
    color_id INT AUTO_INCREMENT PRIMARY KEY,
    color_name VARCHAR(50) NOT NULL,
    color_code VARCHAR(7) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Junction table for model-color combinations
CREATE TABLE IF NOT EXISTS model_colors (
    model_id INT NOT NULL,
    color_id INT NOT NULL,
    PRIMARY KEY (model_id, color_id),
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id) ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES colors(color_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing inventory (new vehicles)
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    model_id INT NOT NULL,
    color_id INT NOT NULL,
    vin VARCHAR(17) UNIQUE NOT NULL,
    manufacturing_date DATE NOT NULL,
    purchase_date DATE NOT NULL,
    purchase_price DECIMAL(10, 2) NOT NULL,
    selling_price DECIMAL(10, 2) NOT NULL,
    is_sold BOOLEAN DEFAULT FALSE,
    sold_date DATE,
    sold_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id),
    FOREIGN KEY (color_id) REFERENCES colors(color_id),
    CONSTRAINT chk_purchase_price CHECK (purchase_price > 0),
    CONSTRAINT chk_selling_price CHECK (selling_price > 0),
    CONSTRAINT chk_sold_price CHECK (sold_price > 0 OR sold_price IS NULL)
) ENGINE=InnoDB;

-- Table for storing pre-owned vehicles
CREATE TABLE IF NOT EXISTS pre_owned_vehicles (
    pre_owned_id INT AUTO_INCREMENT PRIMARY KEY,
    model_id INT NOT NULL,
    color_id INT NOT NULL,
    vin VARCHAR(17) UNIQUE NOT NULL,
    manufacturing_date DATE NOT NULL,
    previous_owner_name VARCHAR(100) NOT NULL,
    previous_owner_contact VARCHAR(15) NOT NULL,
    km_driven INT NOT NULL,
    purchase_date DATE NOT NULL,
    purchase_price DECIMAL(10, 2) NOT NULL,
    selling_price DECIMAL(10, 2) NOT NULL,
    is_sold BOOLEAN DEFAULT FALSE,
    sold_date DATE,
    sold_price DECIMAL(10, 2),
    condition_notes TEXT,
    service_history TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id),
    FOREIGN KEY (color_id) REFERENCES colors(color_id),
    CONSTRAINT chk_km_driven CHECK (km_driven >= 0),
    CONSTRAINT chk_purchase_price_preowned CHECK (purchase_price > 0),
    CONSTRAINT chk_selling_price_preowned CHECK (selling_price > 0),
    CONSTRAINT chk_sold_price_preowned CHECK (sold_price > 0 OR sold_price IS NULL)
) ENGINE=InnoDB;

-- Table for storing accessories
CREATE TABLE IF NOT EXISTS accessories (
    accessory_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_accessory_price CHECK (price > 0)
) ENGINE=InnoDB;

-- Table for storing customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing sales transactions
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    vehicle_type ENUM('New', 'Pre-owned') NOT NULL,
    vehicle_id INT NOT NULL, -- references either inventory_id or pre_owned_id
    sale_date DATE NOT NULL,
    sale_price DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Cash', 'Loan', 'Credit Card', 'Debit Card', 'Bank Transfer') NOT NULL,
    sales_person VARCHAR(100) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT chk_sale_price CHECK (sale_price > 0),
    CONSTRAINT chk_tax_amount CHECK (tax_amount >= 0),
    CONSTRAINT chk_total_amount CHECK (total_amount > 0)
) ENGINE=InnoDB;

-- Junction table for sales-accessories (many-to-many relationship)
CREATE TABLE IF NOT EXISTS sale_accessories (
    sale_id INT NOT NULL,
    accessory_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    price_per_unit DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (sale_id, accessory_id),
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id) ON DELETE CASCADE,
    FOREIGN KEY (accessory_id) REFERENCES accessories(accessory_id),
    CONSTRAINT chk_quantity CHECK (quantity > 0),
    CONSTRAINT chk_accessory_price_sale CHECK (price_per_unit > 0)
) ENGINE=InnoDB;

-- Table for storing service appointments
CREATE TABLE IF NOT EXISTS service_appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    vehicle_id INT NOT NULL, -- references either inventory_id or pre_owned_id
    vehicle_type ENUM('New', 'Pre-owned') NOT NULL,
    appointment_date DATETIME NOT NULL,
    service_type ENUM('Regular Maintenance', 'Repair', 'Customization', 'Inspection') NOT NULL,
    estimated_cost DECIMAL(10, 2),
    actual_cost DECIMAL(10, 2),
    status ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT chk_estimated_cost CHECK (estimated_cost > 0 OR estimated_cost IS NULL),
    CONSTRAINT chk_actual_cost CHECK (actual_cost > 0 OR actual_cost IS NULL)
) ENGINE=InnoDB;

-- Table for storing service history
CREATE TABLE IF NOT EXISTS service_history (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    service_details TEXT NOT NULL,
    parts_used TEXT,
    technician_name VARCHAR(100) NOT NULL,
    service_date DATE NOT NULL,
    next_service_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (appointment_id) REFERENCES service_appointments(appointment_id)
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_inventory_model ON inventory(model_id);
CREATE INDEX idx_inventory_color ON inventory(color_id);
CREATE INDEX idx_preowned_model ON pre_owned_vehicles(model_id);
CREATE INDEX idx_preowned_color ON pre_owned_vehicles(color_id);
CREATE INDEX idx_sales_customer ON sales(customer_id);
CREATE INDEX idx_sales_vehicle ON sales(vehicle_id);
CREATE INDEX idx_appointments_customer ON service_appointments(customer_id);
CREATE INDEX idx_appointments_vehicle ON service_appointments(vehicle_id);
```
