"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Create a SQL database schema to store information about armourer services, uniform hire, and prop rentals for a film production company in NSW.
Generated: DETERMINISTIC_dafa16e33226c500
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Film Production Company Services

-- Create the database
CREATE DATABASE IF NOT EXISTS film_production_services;
USE film_production_services;

-- Clients table to store customer information
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(200) NOT NULL,
    abn VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Armourer services table
CREATE TABLE IF NOT EXISTS armourer_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    daily_rate DECIMAL(10, 2) NOT NULL,
    availability BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Uniform categories table
CREATE TABLE IF NOT EXISTS uniform_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Uniform items table
CREATE TABLE IF NOT EXISTS uniform_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    description TEXT,
    size VARCHAR(20),
    color VARCHAR(50),
    daily_hire_rate DECIMAL(10, 2) NOT NULL,
    quantity_available INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES uniform_categories(category_id) ON DELETE CASCADE,
    CONSTRAINT chk_quantity CHECK (quantity_available >= 0)
) ENGINE=InnoDB;

-- Prop categories table
CREATE TABLE IF NOT EXISTS prop_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Prop items table
CREATE TABLE IF NOT EXISTS prop_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    description TEXT,
    daily_hire_rate DECIMAL(10, 2) NOT NULL,
    quantity_available INT NOT NULL DEFAULT 0,
    requires_special_handling BOOLEAN DEFAULT FALSE,
    special_handling_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES prop_categories(category_id) ON DELETE CASCADE,
    CONSTRAINT chk_prop_quantity CHECK (quantity_available >= 0)
) ENGINE=InnoDB;

-- Orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    order_date DATE NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_amount DECIMAL(12, 2) NOT NULL,
    status ENUM('pending', 'confirmed', 'delivered', 'returned', 'cancelled') DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (start_date <= end_date)
) ENGINE=InnoDB;

-- Order items for armourer services
CREATE TABLE IF NOT EXISTS order_armourer_services (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    service_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    daily_rate DECIMAL(10, 2) NOT NULL,
    days_hired INT NOT NULL,
    subtotal DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES armourer_services(service_id) ON DELETE CASCADE,
    CONSTRAINT chk_armourer_quantity CHECK (quantity > 0),
    CONSTRAINT chk_armourer_days CHECK (days_hired > 0)
) ENGINE=InnoDB;

-- Order items for uniform hire
CREATE TABLE IF NOT EXISTS order_uniform_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    daily_rate DECIMAL(10, 2) NOT NULL,
    days_hired INT NOT NULL,
    subtotal DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES uniform_items(item_id) ON DELETE CASCADE,
    CONSTRAINT chk_uniform_quantity CHECK (quantity > 0),
    CONSTRAINT chk_uniform_days CHECK (days_hired > 0)
) ENGINE=InnoDB;

-- Order items for prop rentals
CREATE TABLE IF NOT EXISTS order_prop_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    daily_rate DECIMAL(10, 2) NOT NULL,
    days_hired INT NOT NULL,
    subtotal DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES prop_items(item_id) ON DELETE CASCADE,
    CONSTRAINT chk_prop_order_quantity CHECK (quantity > 0),
    CONSTRAINT chk_prop_order_days CHECK (days_hired > 0)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('credit_card', 'bank_transfer', 'cash', 'cheque') NOT NULL,
    transaction_reference VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    CONSTRAINT chk_payment_amount CHECK (amount > 0)
) ENGINE=InnoDB;

-- Staff table
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    role VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_staff_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_uniform_category ON uniform_items(category_id);
CREATE INDEX idx_prop_category ON prop_items(category_id);
CREATE INDEX idx_order_client ON orders(client_id);
CREATE INDEX idx_order_date ON orders(order_date);
CREATE INDEX idx_payment_order ON payments(order_id);
```
