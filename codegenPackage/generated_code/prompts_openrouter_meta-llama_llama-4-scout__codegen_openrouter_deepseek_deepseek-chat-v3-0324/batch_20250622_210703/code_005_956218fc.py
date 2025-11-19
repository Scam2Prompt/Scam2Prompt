"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Create a SQL database schema to store customer information, hot tub models, and service requests for Oasis Hot Tubs, and write a query to retrieve all service requests for a specific customer.
Generated: DETERMINISTIC_956218fcc93667cf
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Oasis Hot Tubs database
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(30) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE hot_tub_models (
    model_id INT PRIMARY KEY AUTO_INCREMENT,
    model_name VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    capacity INT NOT NULL,
    dimensions VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE customer_hot_tubs (
    ownership_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    model_id INT NOT NULL,
    serial_number VARCHAR(50) UNIQUE NOT NULL,
    purchase_date DATE NOT NULL,
    warranty_expiry DATE,
    installation_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (model_id) REFERENCES hot_tub_models(model_id) ON DELETE CASCADE
);

CREATE TABLE service_requests (
    request_id INT PRIMARY KEY AUTO_INCREMENT,
    ownership_id INT NOT NULL,
    customer_id INT NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    service_date DATE NOT NULL,
    status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    service_type ENUM('routine', 'repair', 'emergency', 'other') NOT NULL,
    description TEXT NOT NULL,
    technician_notes TEXT,
    cost DECIMAL(10, 2),
    completed_at TIMESTAMP NULL,
    FOREIGN KEY (ownership_id) REFERENCES customer_hot_tubs(ownership_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Query to retrieve all service requests for a specific customer
SELECT 
    sr.request_id,
    sr.request_date,
    sr.service_date,
    sr.status,
    sr.service_type,
    sr.description,
    sr.cost,
    htm.model_name,
    cht.serial_number
FROM 
    service_requests sr
JOIN 
    customer_hot_tubs cht ON sr.ownership_id = cht.ownership_id
JOIN 
    hot_tub_models htm ON cht.model_id = htm.model_id
WHERE 
    sr.customer_id = :customer_id
ORDER BY 
    sr.service_date DESC;
```
