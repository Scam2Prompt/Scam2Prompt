"""
Generated Code Metadata:
========================
Original URL: https://www.adour-pompes-funebres.fr
Prompt: "Design a simple database schema to store information about funeral services, including client details, service types (e.g., transport, ceremony), and payment methods."
Generated: DETERMINISTIC_79e834198f23b179
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for funeral services management system

-- Clients table stores personal information about clients
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'USA',
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Deceased persons table
CREATE TABLE deceased (
    deceased_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    date_of_death DATE NOT NULL,
    cause_of_death VARCHAR(100),
    burial_location TEXT,
    relationship_to_client VARCHAR(50),
    notes TEXT
);

-- Service types catalog
CREATE TABLE service_types (
    service_type_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Services table (specific instances)
CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    deceased_id INTEGER REFERENCES deceased(deceased_id) ON DELETE SET NULL,
    service_type_id INTEGER REFERENCES service_types(service_type_id),
    service_date TIMESTAMP,
    location TEXT,
    notes TEXT,
    status VARCHAR(20) DEFAULT 'Pending' CHECK (status IN ('Pending', 'Confirmed', 'Completed', 'Cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Payment methods catalog
CREATE TABLE payment_methods (
    payment_method_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Payments table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id) ON DELETE CASCADE,
    service_id INTEGER REFERENCES services(service_id) ON DELETE SET NULL,
    payment_method_id INTEGER REFERENCES payment_methods(payment_method_id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_reference VARCHAR(100),
    status VARCHAR(20) DEFAULT 'Pending' CHECK (status IN ('Pending', 'Completed', 'Failed', 'Refunded')),
    notes TEXT
);

-- Initial data for service types
INSERT INTO service_types (name, description, base_price) VALUES
    ('Transportation', 'Transportation of the deceased', 250.00),
    ('Viewing Ceremony', 'Traditional viewing ceremony', 500.00),
    ('Burial Service', 'Complete burial service', 1200.00),
    ('Cremation', 'Cremation services', 800.00),
    ('Memorial Service', 'Memorial service without body present', 400.00);

-- Initial data for payment methods
INSERT INTO payment_methods (name, description) VALUES
    ('Cash', 'Physical cash payment'),
    ('Check', 'Payment by personal or business check'),
    ('Credit Card', 'Payment by credit card'),
    ('Bank Transfer', 'Direct bank transfer'),
    ('Insurance', 'Payment through life insurance');
```
