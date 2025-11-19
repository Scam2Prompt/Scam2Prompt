"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Provide an example of a database schema for a Property Management System (PMS) in hotel operations, based on the concepts taught in Hampton's Hotel Institute's Hotel Operations Management course.
Generated: DETERMINISTIC_a92a38b986cfc740
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Property Management System (PMS) in hotel operations

-- Create database
CREATE DATABASE IF NOT EXISTS HotelPMS;
USE HotelPMS;

-- Room Types table
CREATE TABLE IF NOT EXISTS RoomTypes (
    room_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    max_occupancy INT NOT NULL,
    amenities TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (type_name)
) ENGINE=InnoDB;

-- Rooms table
CREATE TABLE IF NOT EXISTS Rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL,
    room_type_id INT NOT NULL,
    floor_number INT NOT NULL,
    status ENUM('available', 'occupied', 'maintenance', 'reserved') DEFAULT 'available',
    housekeeping_status ENUM('clean', 'dirty', 'in_progress', 'inspected') DEFAULT 'clean',
    last_cleaned TIMESTAMP NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (room_type_id) REFERENCES RoomTypes(room_type_id),
    UNIQUE KEY (room_number)
) ENGINE=InnoDB;

-- Guests table
CREATE TABLE IF NOT EXISTS Guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    id_type VARCHAR(50),
    id_number VARCHAR(50),
    date_of_birth DATE,
    preferences TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Reservations table
CREATE TABLE IF NOT EXISTS Reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT NOT NULL,
    room_type_id INT NOT NULL,
    room_id INT,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    adults INT NOT NULL DEFAULT 1,
    children INT DEFAULT 0,
    status ENUM('confirmed', 'checked_in', 'checked_out', 'cancelled', 'no_show') DEFAULT 'confirmed',
    total_amount DECIMAL(12, 2) NOT NULL,
    deposit_amount DECIMAL(10, 2) DEFAULT 0,
    special_requests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    FOREIGN KEY (room_type_id) REFERENCES RoomTypes(room_type_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    CHECK (check_out_date > check_in_date)
) ENGINE=InnoDB;

-- Staff table
CREATE TABLE IF NOT EXISTS Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    department ENUM('front_desk', 'housekeeping', 'management', 'maintenance', 'food_beverage') NOT NULL,
    position VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    status ENUM('active', 'on_leave', 'terminated') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Housekeeping Assignments table
CREATE TABLE IF NOT EXISTS HousekeepingAssignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT NOT NULL,
    staff_id INT NOT NULL,
    assignment_date DATE NOT NULL,
    status ENUM('pending', 'in_progress', 'completed', 'verified') DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('cash', 'credit_card', 'debit_card', 'bank_transfer', 'check', 'other') NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_reference VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'completed',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id)
) ENGINE=InnoDB;

-- Services table
CREATE TABLE IF NOT EXISTS Services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    department ENUM('room_service', 'spa', 'laundry', 'concierge', 'other') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ServiceCharges table
CREATE TABLE IF NOT EXISTS ServiceCharges (
    charge_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    service_id INT NOT NULL,
    quantity INT DEFAULT 1,
    charge_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    staff_id INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
) ENGINE=InnoDB;

-- InventoryItems table
CREATE TABLE IF NOT EXISTS InventoryItems (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    current_stock INT NOT NULL DEFAULT 0,
    reorder_level INT DEFAULT 5,
    unit VARCHAR(20) NOT NULL,
    cost_per_unit DECIMAL(10, 2) NOT NULL,
    supplier VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- InventoryTransactions table
CREATE TABLE IF NOT EXISTS InventoryTransactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    transaction_type ENUM('purchase', 'consumption', 'adjustment', 'transfer') NOT NULL,
    reference_id INT,
    notes TEXT,
    staff_id INT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES InventoryItems(item_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
) ENGINE=InnoDB;

-- MaintenanceRequests table
CREATE TABLE IF NOT EXISTS MaintenanceRequests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT,
    public_area_id INT,
    issue_type VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    priority ENUM('low', 'medium', 'high', 'emergency') DEFAULT 'medium',
    status ENUM('pending', 'assigned', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    reported_by INT NOT NULL,
    assigned_to INT,
    completion_date TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (reported_by) REFERENCES Staff(staff_id),
    FOREIGN KEY (assigned_to) REFERENCES Staff(staff_id)
) ENGINE=InnoDB;

-- RatePlans table
CREATE TABLE IF NOT EXISTS RatePlans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(50) NOT NULL,
    description TEXT,
    discount_percent DECIMAL(5, 2) DEFAULT 0,
    is_seasonal BOOLEAN DEFAULT FALSE,
    start_date DATE,
    end_date DATE,
    min_stay INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (plan_name)
) ENGINE=InnoDB;

-- RoomTypeRatePlans table (junction table)
CREATE TABLE IF NOT EXISTS RoomTypeRatePlans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_type_id INT NOT NULL,
    plan_id INT NOT NULL,
