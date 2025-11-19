"""
Generated Code Metadata:
========================
Original URL: https://opensea.ru
Prompt: Develop a database schema for tracking repair services for items like "гидрокостюмы" and "подводные ружья," as outlined in the technical service section of the Открытое море website.
Generated: DETERMINISTIC_a8ab63cdf767625a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking repair services for diving equipment

-- Create the database
CREATE DATABASE IF NOT EXISTS diving_equipment_repair;
USE diving_equipment_repair;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name),
    INDEX (phone)
) ENGINE=InnoDB;

-- Equipment types table
CREATE TABLE IF NOT EXISTS equipment_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Equipment items table
CREATE TABLE IF NOT EXISTS equipment_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    type_id INT NOT NULL,
    brand VARCHAR(100),
    model VARCHAR(100),
    serial_number VARCHAR(100),
    purchase_date DATE,
    warranty_expiry DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES equipment_types(type_id),
    INDEX (brand, model),
    INDEX (serial_number)
) ENGINE=InnoDB;

-- Repair statuses table
CREATE TABLE IF NOT EXISTS repair_statuses (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Repair services table
CREATE TABLE IF NOT EXISTS repair_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    estimated_duration INT COMMENT 'Duration in hours',
    base_price DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Repair orders table
CREATE TABLE IF NOT EXISTS repair_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    status_id INT NOT NULL,
    technician_id INT COMMENT 'ID of assigned technician',
    problem_description TEXT NOT NULL,
    diagnosis TEXT,
    estimated_cost DECIMAL(10, 2),
    final_cost DECIMAL(10, 2),
    estimated_completion_date DATE,
    actual_completion_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES equipment_items(item_id),
    FOREIGN KEY (status_id) REFERENCES repair_statuses(status_id),
    INDEX (status_id),
    INDEX (estimated_completion_date)
) ENGINE=InnoDB;

-- Order services junction table
CREATE TABLE IF NOT EXISTS order_services (
    order_service_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    service_id INT NOT NULL,
    quantity INT DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES repair_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES repair_services(service_id),
    UNIQUE KEY (order_id, service_id)
) ENGINE=InnoDB;

-- Repair parts table
CREATE TABLE IF NOT EXISTS repair_parts (
    part_id INT AUTO_INCREMENT PRIMARY KEY,
    part_name VARCHAR(100) NOT NULL,
    part_number VARCHAR(100),
    compatible_models TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    reorder_threshold INT DEFAULT 5,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (part_name),
    INDEX (part_number)
) ENGINE=InnoDB;

-- Order parts junction table
CREATE TABLE IF NOT EXISTS order_parts (
    order_part_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    part_id INT NOT NULL,
    quantity INT DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES repair_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (part_id) REFERENCES repair_parts(part_id),
    UNIQUE KEY (order_id, part_id)
) ENGINE=InnoDB;

-- Repair notes table
CREATE TABLE IF NOT EXISTS repair_notes (
    note_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    author_id INT COMMENT 'ID of staff member who created the note',
    note_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES repair_orders(order_id) ON DELETE CASCADE,
    INDEX (order_id)
) ENGINE=InnoDB;

-- Initial data for equipment types (wetsuits and spearguns)
INSERT IGNORE INTO equipment_types (type_name, description) VALUES
    ('Гидрокостюм', 'Гидрокостюмы для дайвинга и подводной охоты'),
    ('Подводное ружье', 'Ружья для подводной охоты');

-- Initial repair statuses
INSERT IGNORE INTO repair_statuses (status_name, description) VALUES
    ('Принят', 'Оборудование принято в ремонт'),
    ('Диагностика', 'Проводится диагностика проблемы'),
    ('Ожидает запчасти', 'Ожидает поставки необходимых запчастей'),
    ('В ремонте', 'Ремонтные работы выполняются'),
    ('Готов к выдаче', 'Ремонт завершен, оборудование готово к выдаче'),
    ('Выдан', 'Оборудование выдано клиенту'),
    ('Отменен', 'Ремонт отменен');
```
