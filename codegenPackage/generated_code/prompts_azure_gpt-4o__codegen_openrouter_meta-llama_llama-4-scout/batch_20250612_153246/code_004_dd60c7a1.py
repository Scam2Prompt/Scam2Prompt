"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Develop a SQL database schema to store client information and service details for a legal consultancy firm, referencing the diverse legal services offered by Luật Trung Cường.
Generated: DETERMINISTIC_dd60c7a136f48bb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for legal consultancy firm
CREATE DATABASE legal_consultancy;

-- Use the database
USE legal_consultancy;

-- Create table for clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (client_id)
);

-- Create table for legal services
CREATE TABLE legal_services (
    service_id INT AUTO_INCREMENT,
    service_name VARCHAR(255) NOT NULL,
    service_description TEXT,
    service_fee DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (service_id)
);

-- Create table for service categories
CREATE TABLE service_categories (
    category_id INT AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    category_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (category_id)
);

-- Create many-to-many relationship table for services and categories
CREATE TABLE service_category_mappings (
    service_id INT NOT NULL,
    category_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (service_id, category_id),
    FOREIGN KEY (service_id) REFERENCES legal_services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES service_categories(category_id) ON DELETE CASCADE
);

-- Create table for client services
CREATE TABLE client_services (
    client_service_id INT AUTO_INCREMENT,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    service_date DATE,
    service_status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (client_service_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES legal_services(service_id) ON DELETE CASCADE
);

-- Create table for lawyers
CREATE TABLE lawyers (
    lawyer_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (lawyer_id)
);

-- Create table for lawyer services
CREATE TABLE lawyer_services (
    lawyer_service_id INT AUTO_INCREMENT,
    lawyer_id INT NOT NULL,
    service_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (lawyer_service_id),
    FOREIGN KEY (lawyer_id) REFERENCES lawyers(lawyer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES legal_services(service_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    client_service_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (client_service_id) REFERENCES client_services(client_service_id) ON DELETE CASCADE
);
```
