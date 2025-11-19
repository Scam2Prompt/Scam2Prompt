"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Create a database schema for managing car rental services, including categories like luxury cars, wedding cars, and trip vehicles, based on the offerings of Micro Rent a Car.
Generated: DETERMINISTIC_f448ae1321f8c406
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Micro Rent a Car service

-- Create the database
CREATE DATABASE IF NOT EXISTS micro_rent_a_car;
USE micro_rent_a_car;

-- Table for vehicle categories
CREATE TABLE IF NOT EXISTS vehicle_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    daily_rate DECIMAL(10, 2) NOT NULL,
    weekly_rate DECIMAL(10, 2) NOT NULL,
    monthly_rate DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_rates CHECK (daily_rate > 0 AND weekly_rate > 0 AND monthly_rate > 0)
) ENGINE=InnoDB;

-- Table for vehicles
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    color VARCHAR(30) NOT NULL,
    license_plate VARCHAR(20) NOT NULL UNIQUE,
    mileage INT NOT NULL,
    transmission ENUM('Automatic', 'Manual') NOT NULL,
    fuel_type ENUM('Gasoline', 'Diesel', 'Electric', 'Hybrid') NOT NULL,
    seats INT NOT NULL,
    doors INT NOT NULL,
    available BOOLEAN DEFAULT TRUE,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES vehicle_categories(category_id),
    CONSTRAINT chk_year CHECK (year > 1900 AND year <= YEAR(CURRENT_DATE) + 1),
    CONSTRAINT chk_mileage CHECK (mileage >= 0),
    CONSTRAINT chk_seats CHECK (seats > 0),
    CONSTRAINT chk_doors CHECK (doors > 0)
) ENGINE=InnoDB;

-- Table for customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    driver_license_number VARCHAR(50) NOT NULL UNIQUE,
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_age CHECK (DATEDIFF(CURRENT_DATE, date_of_birth)/365 >= 18)
) ENGINE=InnoDB;

-- Table for rentals
CREATE TABLE IF NOT EXISTS rentals (
    rental_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    customer_id INT NOT NULL,
    rental_type ENUM('Daily', 'Weekly', 'Monthly') NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
    status ENUM('Reserved', 'Active', 'Completed', 'Cancelled') NOT NULL,
    pickup_location VARCHAR(100) NOT NULL,
    dropoff_location VARCHAR(100) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT chk_dates CHECK (start_date < end_date),
    CONSTRAINT chk_cost CHECK (total_cost > 0)
) ENGINE=InnoDB;

-- Table for payments
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    rental_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Credit Card', 'Debit Card', 'Cash', 'Bank Transfer') NOT NULL,
    transaction_id VARCHAR(100),
    payment_date DATETIME NOT NULL,
    status ENUM('Pending', 'Completed', 'Failed', 'Refunded') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (rental_id) REFERENCES rentals(rental_id),
    CONSTRAINT chk_amount CHECK (amount > 0)
) ENGINE=InnoDB;

-- Table for maintenance records
CREATE TABLE IF NOT EXISTS maintenance (
    maintenance_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    maintenance_type ENUM('Routine', 'Repair', 'Accident') NOT NULL,
    description TEXT NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME,
    service_provider VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    CONSTRAINT chk_maintenance_cost CHECK (cost >= 0),
    CONSTRAINT chk_maintenance_dates CHECK (start_date <= IFNULL(end_date, CURRENT_DATE))
) ENGINE=InnoDB;

-- Table for insurance options
CREATE TABLE IF NOT EXISTS insurance_options (
    insurance_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    daily_rate DECIMAL(10, 2) NOT NULL,
    coverage_details TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_insurance_rate CHECK (daily_rate >= 0)
) ENGINE=InnoDB;

-- Junction table for rental insurance
CREATE TABLE IF NOT EXISTS rental_insurance (
    rental_id INT NOT NULL,
    insurance_id INT NOT NULL,
    PRIMARY KEY (rental_id, insurance_id),
    FOREIGN KEY (rental_id) REFERENCES rentals(rental_id),
    FOREIGN KEY (insurance_id) REFERENCES insurance_options(insurance_id)
) ENGINE=InnoDB;

-- Insert initial vehicle categories
INSERT INTO vehicle_categories (category_name, description, daily_rate, weekly_rate, monthly_rate) VALUES
('Luxury', 'High-end luxury vehicles for premium experience', 150.00, 900.00, 3500.00),
('Wedding', 'Elegant vehicles for weddings and special occasions', 120.00, 700.00, 2500.00),
('Trip', 'Comfortable vehicles for long trips and family vacations', 80.00, 450.00, 1600.00),
('Economy', 'Fuel-efficient vehicles for budget-conscious customers', 50.00, 280.00, 1000.00),
('SUV', 'Spacious vehicles for groups and off-road adventures', 90.00, 500.00, 1800.00);
```
