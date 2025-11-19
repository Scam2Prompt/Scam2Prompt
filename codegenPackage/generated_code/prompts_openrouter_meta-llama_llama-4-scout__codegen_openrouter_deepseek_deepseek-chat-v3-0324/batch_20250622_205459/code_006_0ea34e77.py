"""
Generated Code Metadata:
========================
Original URL: https://aaaverify.claimsdetective.com
Prompt: Design a database schema to store client information and verification results for a company using AAAVerify's services, and provide SQL code to populate the schema with sample data.
Generated: DETERMINISTIC_0ea34e7708674a8f
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for AAAVerify client information and verification results

-- Create the database
CREATE DATABASE IF NOT EXISTS aaav_verification_db;
USE aaav_verification_db;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL UNIQUE,
    contact_phone VARCHAR(20) NOT NULL,
    company_address TEXT NOT NULL,
    registration_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    account_status ENUM('active', 'suspended', 'terminated') NOT NULL DEFAULT 'active',
    api_key VARCHAR(64) UNIQUE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Verification services table
CREATE TABLE IF NOT EXISTS verification_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    base_cost DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE=InnoDB;

-- Client subscriptions table
CREATE TABLE IF NOT EXISTS client_subscriptions (
    subscription_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    start_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_date DATETIME,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    custom_rate DECIMAL(10, 2),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES verification_services(service_id) ON DELETE CASCADE,
    UNIQUE KEY unique_client_service (client_id, service_id)
) ENGINE=InnoDB;

-- Verification requests table
CREATE TABLE IF NOT EXISTS verification_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    request_timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    request_data JSON NOT NULL,
    status ENUM('pending', 'processing', 'completed', 'failed') NOT NULL DEFAULT 'pending',
    completion_timestamp DATETIME,
    cost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES verification_services(service_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Verification results table
CREATE TABLE IF NOT EXISTS verification_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    verification_score DECIMAL(5, 2),
    verification_status ENUM('verified', 'unverified', 'fraudulent', 'inconclusive') NOT NULL,
    result_details JSON NOT NULL,
    notes TEXT,
    FOREIGN KEY (request_id) REFERENCES verification_requests(request_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Billing records table
CREATE TABLE IF NOT EXISTS billing_records (
    billing_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    billing_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'paid', 'overdue', 'disputed') NOT NULL DEFAULT 'pending',
    payment_date DATETIME,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Insert sample verification services
INSERT INTO verification_services (service_name, description, base_cost) VALUES
('Email Verification', 'Verify email address validity and deliverability', 0.05),
('Phone Verification', 'Verify phone number validity and carrier information', 0.10),
('Identity Verification', 'Verify personal identity documents', 1.50),
('Business Verification', 'Verify business registration and legitimacy', 2.00),
('Document Verification', 'Verify authenticity of uploaded documents', 1.25);

-- Insert sample clients
INSERT INTO clients (company_name, contact_name, contact_email, contact_phone, company_address, api_key) VALUES
('Acme Corp', 'John Smith', 'john@acmecorp.com', '+15551234567', '123 Main St, Anytown, USA', 'acme_apikey_1234567890'),
('Globex Inc', 'Sarah Johnson', 'sarah@globex.com', '+15559876543', '456 Oak Ave, Somewhere City', 'globex_apikey_9876543210'),
('Initech LLC', 'Michael Scott', 'michael@initech.com', '+15555555555', '789 Park Blvd, Scranton, PA', 'initech_apikey_5555555555');

-- Insert sample subscriptions
INSERT INTO client_subscriptions (client_id, service_id, custom_rate) VALUES
(1, 1, 0.04),  -- Acme Corp gets discount on email verification
(1, 2, NULL),  -- Acme Corp standard rate for phone verification
(2, 1, NULL),  -- Globex standard rate for email verification
(2, 3, 1.25),  -- Globex gets discount on identity verification
(3, 4, NULL),  -- Initech standard rate for business verification
(3, 5, 1.00);  -- Initech gets discount on document verification

-- Insert sample verification requests
INSERT INTO verification_requests (client_id, service_id, request_data, status, completion_timestamp, cost) VALUES
(1, 1, '{"email": "user1@example.com"}', 'completed', NOW() - INTERVAL 1 DAY, 0.04),
(1, 2, '{"phone": "+15551231234", "country": "US"}', 'completed', NOW() - INTERVAL 2 HOUR, 0.10),
(2, 1, '{"email": "user2@example.com"}', 'processing', NULL, 0.05),
(2, 3, '{"name": "Alice Johnson", "dob": "1985-05-15", "id_number": "ID12345678"}', 'completed', NOW() - INTERVAL 3 DAY, 1.25),
(3, 4, '{"business_name": "Dunder Mifflin", "registration_number": "BUS987654"}', 'completed', NOW() - INTERVAL 1 HOUR, 2.00);

-- Insert sample verification results
INSERT INTO verification_results (request_id, verification_score, verification_status, result_details) VALUES
(1, 95.00, 'verified', '{"valid": true, "disposable": false, "catch_all": false, "mx_records": true}'),
(2, 80.00, 'verified', '{"valid": true, "carrier": "Verizon Wireless", "line_type": "mobile"}'),
(4, 100.00, 'verified', '{"name_match": true, "dob_match": true, "id_valid": true, "fraud_risk": "low"}'),
(5, 65.00, 'unverified', '{"registered": true, "active": false, "address_match": false}');

-- Insert sample billing records
INSERT INTO billing_records (client_id, period_start, period_end, total_amount, tax_amount, status, payment_date) VALUES
(1, '2023-01-01', '2023-01-31', 150.75, 12.06, 'paid', '2023-02-05'),
(2, '2023-01-01', '2023-01-31', 225.50, 18.04, 'paid', '2023-02-07'),
(3, '2023-01-01', '2023-01-31', 180.25, 14.42, 'pending', NULL),
(1, '2023-02-01', '2023-02-28', 135.20, 10.82, 'pending', NULL);
```
