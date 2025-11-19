"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Design a database schema for storing hotel operations data, including sales, reservations, and customer information, using a hospitality management system.
Generated: DETERMINISTIC_6807f1020bc1622e
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Hotel Management System

-- Create the database
CREATE DATABASE hotel_management_system;
USE hotel_management_system;

-- Customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    id_proof_type VARCHAR(50),
    id_proof_number VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_phone (phone)
) ENGINE=InnoDB;

-- Rooms table
CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) UNIQUE NOT NULL,
    room_type_id INT NOT NULL,
    floor_number INT NOT NULL,
    status ENUM('available', 'occupied', 'maintenance', 'reserved') DEFAULT 'available',
    max_occupancy INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (room_type_id) REFERENCES room_types(room_type_id),
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Room types table
CREATE TABLE room_types (
    room_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    amenities TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_name (name)
) ENGINE=InnoDB;

-- Reservations table
CREATE TABLE reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    adults INT NOT NULL DEFAULT 1,
    children INT NOT NULL DEFAULT 0,
    status ENUM('confirmed', 'cancelled', 'checked-in', 'checked-out', 'no-show') DEFAULT 'confirmed',
    total_amount DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    INDEX idx_dates (check_in_date, check_out_date),
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('cash', 'credit_card', 'debit_card', 'bank_transfer', 'other') NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_id VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'completed',
    notes TEXT,
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id),
    INDEX idx_payment_date (payment_date),
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Services table
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_name (name)
) ENGINE=InnoDB;

-- Room service orders
CREATE TABLE room_service_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    service_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'delivered', 'cancelled') DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    INDEX idx_order_time (order_time),
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Staff table
CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    position VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_department (department)
) ENGINE=InnoDB;

-- Room cleaning log
CREATE TABLE room_cleaning_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT NOT NULL,
    staff_id INT NOT NULL,
    cleaning_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('clean', 'dirty', 'in-progress') DEFAULT 'clean',
    notes TEXT,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    INDEX idx_cleaning_date (cleaning_date),
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Audit log for important operations
CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT,
    old_values TEXT,
    new_values TEXT,
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_action_time (action_time),
    INDEX idx_action (action)
) ENGINE=InnoDB;
```
