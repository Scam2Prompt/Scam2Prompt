"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Create a SQL database schema to manage and consolidate shipments for import and export, including tables for air freight, ocean freight, and customs brokerage, inspired by Daimon Logistics' services.
Generated: DETERMINISTIC_a1e9d8b1cc428188
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Shipment Management System
-- Inspired by Daimon Logistics' services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create countries table
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT NOT NULL UNIQUE,
    country_code TEXT NOT NULL UNIQUE CHECK(length(country_code) = 2),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Create ports table
CREATE TABLE ports (
    port_id INTEGER PRIMARY KEY AUTOINCREMENT,
    port_name TEXT NOT NULL,
    port_code TEXT NOT NULL UNIQUE CHECK(length(port_code) >= 3 AND length(port_code) <= 5),
    country_id INTEGER NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- Create airports table
CREATE TABLE airports (
    airport_id INTEGER PRIMARY KEY AUTOINCREMENT,
    airport_name TEXT NOT NULL,
    iata_code TEXT NOT NULL UNIQUE CHECK(length(iata_code) = 3),
    country_id INTEGER NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- Create customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    tax_id TEXT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country_id INTEGER NOT NULL,
    email TEXT CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- Create shipment_types table
CREATE TABLE shipment_types (
    shipment_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create shipment_statuses table
CREATE TABLE shipment_statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create shipments table (parent table for all shipment types)
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    shipment_type_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    tracking_number TEXT UNIQUE,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    estimated_departure TIMESTAMP,
    estimated_arrival TIMESTAMP,
    actual_departure TIMESTAMP,
    actual_arrival TIMESTAMP,
    total_weight DECIMAL(10, 2) CHECK(total_weight > 0),
    total_volume DECIMAL(10, 2) CHECK(total_volume > 0),
    declared_value DECIMAL(12, 2) CHECK(declared_value >= 0),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (shipment_type_id) REFERENCES shipment_types(shipment_type_id),
    FOREIGN KEY (status_id) REFERENCES shipment_statuses(status_id)
);

-- Create air_freight_shipments table
CREATE TABLE air_freight_shipments (
    air_shipment_id INTEGER PRIMARY KEY,
    flight_number TEXT,
    departure_airport_id INTEGER NOT NULL,
    arrival_airport_id INTEGER NOT NULL,
    airline TEXT,
    awb_number TEXT UNIQUE,
    handling_instructions TEXT,
    FOREIGN KEY (air_shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    FOREIGN KEY (departure_airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (arrival_airport_id) REFERENCES airports(airport_id)
);

-- Create ocean_freight_shipments table
CREATE TABLE ocean_freight_shipments (
    ocean_shipment_id INTEGER PRIMARY KEY,
    vessel_name TEXT,
    voyage_number TEXT,
    departure_port_id INTEGER NOT NULL,
    arrival_port_id INTEGER NOT NULL,
    shipping_line TEXT,
    bill_of_lading_number TEXT UNIQUE,
    container_numbers TEXT,
    FOREIGN KEY (ocean_shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    FOREIGN KEY (departure_port_id) REFERENCES ports(port_id),
    FOREIGN KEY (arrival_port_id) REFERENCES ports(port_id)
);

-- Create customs_brokerage table
CREATE TABLE customs_brokerage (
    brokerage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    broker_name TEXT NOT NULL,
    broker_contact TEXT NOT NULL,
    broker_email TEXT CHECK(broker_email LIKE '%@%.%'),
    broker_phone TEXT NOT NULL,
    customs_entry_number TEXT UNIQUE,
    customs_status TEXT,
    duties_fees DECIMAL(12, 2) CHECK(duties_fees >= 0),
    taxes DECIMAL(12, 2) CHECK(taxes >= 0),
    clearance_date TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

-- Create commodities table
CREATE TABLE commodities (
    commodity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hs_code TEXT NOT NULL,
    description TEXT NOT NULL,
    duty_rate DECIMAL(5, 2) CHECK(duty_rate >= 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Create shipment_items table
CREATE TABLE shipment_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    commodity_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    unit_weight DECIMAL(10, 2) CHECK(unit_weight > 0),
    unit_volume DECIMAL(10, 2) CHECK(unit_volume > 0),
    unit_value DECIMAL(10, 2) CHECK(unit_value >= 0),
    description TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    FOREIGN KEY (commodity_id) REFERENCES commodities(commodity_id)
);

-- Create documents table
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    document_type TEXT NOT NULL,
    document_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

-- Create invoices table
CREATE TABLE invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    invoice_number TEXT NOT NULL UNIQUE,
    issue_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    due_date TIMESTAMP NOT NULL,
    amount DECIMAL(12, 2) NOT NULL CHECK(amount > 0),
    tax_amount DECIMAL(12, 2) NOT NULL CHECK(tax_amount >= 0),
    total_amount DECIMAL(12, 2) NOT NULL CHECK(total_amount > 0),
    currency TEXT NOT NULL DEFAULT 'USD',
    status TEXT NOT NULL DEFAULT 'Pending',
    payment_date TIMESTAMP,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

-- Create triggers for update timestamps
CREATE TRIGGER update_shipment_timestamp
AFTER UPDATE ON shipments
FOR EACH ROW
BEGIN
    UPDATE shipments SET updated_at = CURRENT_TIMESTAMP WHERE shipment_id = OLD.shipment_id;
END;
```
