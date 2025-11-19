"""
Generated Code Metadata:
========================
Original URL: https://enfock.com
Prompt: Develop a database schema for managing assets, fiscal data, and distribution center operations for a fuel station ERP system, as outlined by Enfock.
Generated: DETERMINISTIC_ede50d28eb2b2865
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for fuel station ERP system
CREATE DATABASE fuel_station_erp;

-- Use the database
USE fuel_station_erp;

-- Create table for assets
CREATE TABLE assets (
    asset_id INT AUTO_INCREMENT,
    asset_type ENUM('pump', 'tank', 'generator') NOT NULL,
    asset_name VARCHAR(255) NOT NULL,
    asset_description TEXT,
    purchase_date DATE,
    purchase_price DECIMAL(10, 2),
    PRIMARY KEY (asset_id)
);

-- Create table for fiscal data
CREATE TABLE fiscal_data (
    fiscal_id INT AUTO_INCREMENT,
    fiscal_year INT NOT NULL,
    fiscal_period ENUM('monthly', 'quarterly', 'annually') NOT NULL,
    revenue DECIMAL(10, 2),
    expenses DECIMAL(10, 2),
    profit DECIMAL(10, 2),
    PRIMARY KEY (fiscal_id)
);

-- Create table for distribution center operations
CREATE TABLE distribution_centers (
    center_id INT AUTO_INCREMENT,
    center_name VARCHAR(255) NOT NULL,
    center_address VARCHAR(255) NOT NULL,
    PRIMARY KEY (center_id)
);

-- Create table for fuel inventory
CREATE TABLE fuel_inventory (
    inventory_id INT AUTO_INCREMENT,
    center_id INT NOT NULL,
    fuel_type ENUM('gasoline', 'diesel', 'ethanol') NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (inventory_id),
    FOREIGN KEY (center_id) REFERENCES distribution_centers(center_id)
);

-- Create table for fuel sales
CREATE TABLE fuel_sales (
    sale_id INT AUTO_INCREMENT,
    center_id INT NOT NULL,
    fuel_type ENUM('gasoline', 'diesel', 'ethanol') NOT NULL,
    sale_date DATE NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    sale_price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (sale_id),
    FOREIGN KEY (center_id) REFERENCES distribution_centers(center_id)
);

-- Create table for employees
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role ENUM('manager', 'clerk', 'mechanic') NOT NULL,
    PRIMARY KEY (employee_id)
);

-- Create table for maintenance records
CREATE TABLE maintenance_records (
    record_id INT AUTO_INCREMENT,
    asset_id INT NOT NULL,
    employee_id INT NOT NULL,
    maintenance_date DATE NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (record_id),
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Create table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    fiscal_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('cash', 'credit', 'bank transfer') NOT NULL,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (fiscal_id) REFERENCES fiscal_data(fiscal_id)
);

-- Create indexes for faster queries
CREATE INDEX idx_assets_asset_type ON assets(asset_type);
CREATE INDEX idx_fiscal_data_fiscal_year ON fiscal_data(fiscal_year);
CREATE INDEX idx_fuel_inventory_center_id ON fuel_inventory(center_id);
CREATE INDEX idx_fuel_sales_center_id ON fuel_sales(center_id);
CREATE INDEX idx_maintenance_records_asset_id ON maintenance_records(asset_id);
CREATE INDEX idx_maintenance_records_employee_id ON maintenance_records(employee_id);
```

```sql
-- Example stored procedure to add new fuel sale
DELIMITER //
CREATE PROCEDURE add_fuel_sale(
    IN p_center_id INT,
    IN p_fuel_type ENUM('gasoline', 'diesel', 'ethanol'),
    IN p_sale_date DATE,
    IN p_quantity DECIMAL(10, 2),
    IN p_sale_price DECIMAL(10, 2)
)
BEGIN
    INSERT INTO fuel_sales (center_id, fuel_type, sale_date, quantity, sale_price)
    VALUES (p_center_id, p_fuel_type, p_sale_date, p_quantity, p_sale_price);
END//
DELIMITER ;

-- Example stored procedure to get fuel sales by center
DELIMITER //
CREATE PROCEDURE get_fuel_sales_by_center(
    IN p_center_id INT
)
BEGIN
    SELECT * FROM fuel_sales
    WHERE center_id = p_center_id;
END//
DELIMITER ;
```

```sql
-- Example trigger to update asset maintenance records
DELIMITER //
CREATE TRIGGER update_asset_maintenance
AFTER INSERT ON maintenance_records
FOR EACH ROW
BEGIN
    UPDATE assets
    SET asset_description = CONCAT(asset_description, '\nMaintenance performed on ', NEW.maintenance_date)
    WHERE asset_id = NEW.asset_id;
END//
DELIMITER ;
```
