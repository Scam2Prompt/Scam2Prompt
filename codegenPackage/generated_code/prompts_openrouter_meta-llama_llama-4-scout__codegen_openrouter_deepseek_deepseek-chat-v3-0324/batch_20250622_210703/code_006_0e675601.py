"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Develop a simple database schema to manage refrigerated vehicle rentals, customer information, and delivery records for a company like Refrigerator Transport in Dubai.
Generated: DETERMINISTIC_0e675601d1fd6e27
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Refrigerated Vehicle Rentals Management System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL CHECK(length(phone) >= 8),
    address TEXT NOT NULL,
    company_name TEXT,
    tax_id TEXT,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive', 'suspended'))
);

-- Vehicle types table
CREATE TABLE IF NOT EXISTS vehicle_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    capacity_cubic_meters REAL NOT NULL CHECK(capacity_cubic_meters > 0),
    temperature_range TEXT NOT NULL,
    daily_rate REAL NOT NULL CHECK(daily_rate > 0),
    weekly_rate REAL NOT NULL CHECK(weekly_rate > 0),
    monthly_rate REAL NOT NULL CHECK(monthly_rate > 0)
);

-- Vehicles table
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration_number TEXT NOT NULL UNIQUE,
    type_id INTEGER NOT NULL,
    manufacture_year INTEGER NOT NULL CHECK(manufacture_year > 2000),
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    status TEXT NOT NULL DEFAULT 'available' CHECK(status IN ('available', 'rented', 'maintenance')),
    current_mileage REAL DEFAULT 0 CHECK(current_mileage >= 0),
    FOREIGN KEY (type_id) REFERENCES vehicle_types(type_id) ON DELETE RESTRICT
);

-- Rental agreements table
CREATE TABLE IF NOT EXISTS rental_agreements (
    agreement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    vehicle_id INTEGER NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL CHECK(end_date > start_date),
    rental_type TEXT NOT NULL CHECK(rental_type IN ('daily', 'weekly', 'monthly')),
    rate REAL NOT NULL CHECK(rate > 0),
    deposit_amount REAL DEFAULT 0 CHECK(deposit_amount >= 0),
    status TEXT NOT NULL DEFAULT 'active' CHECK(status IN ('active', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE RESTRICT
);

-- Delivery records table
CREATE TABLE IF NOT EXISTS delivery_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agreement_id INTEGER NOT NULL,
    driver_name TEXT NOT NULL,
    pickup_location TEXT NOT NULL,
    delivery_location TEXT NOT NULL,
    pickup_time TIMESTAMP NOT NULL,
    delivery_time TIMESTAMP,
    cargo_description TEXT NOT NULL,
    temperature_maintained REAL NOT NULL,
    mileage_start REAL NOT NULL CHECK(mileage_start >= 0),
    mileage_end REAL CHECK(mileage_end >= mileage_start),
    notes TEXT,
    status TEXT NOT NULL DEFAULT 'in_transit' CHECK(status IN ('in_transit', 'delivered', 'cancelled')),
    FOREIGN KEY (agreement_id) REFERENCES rental_agreements(agreement_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agreement_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK(amount > 0),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('cash', 'credit_card', 'bank_transfer', 'check')),
    transaction_reference TEXT,
    status TEXT NOT NULL DEFAULT 'completed' CHECK(status IN ('completed', 'pending', 'failed', 'refunded')),
    FOREIGN KEY (agreement_id) REFERENCES rental_agreements(agreement_id) ON DELETE CASCADE
);

-- Maintenance records table
CREATE TABLE IF NOT EXISTS maintenance_records (
    maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER NOT NULL,
    maintenance_type TEXT NOT NULL CHECK(maintenance_type IN ('routine', 'repair', 'inspection')),
    description TEXT NOT NULL,
    cost REAL NOT NULL CHECK(cost >= 0),
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    service_provider TEXT,
    status TEXT NOT NULL DEFAULT 'scheduled' CHECK(status IN ('scheduled', 'in_progress', 'completed')),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_customers_email ON customers(email);
CREATE INDEX IF NOT EXISTS idx_vehicles_status ON vehicles(status);
CREATE INDEX IF NOT EXISTS idx_rental_agreements_customer ON rental_agreements(customer_id);
CREATE INDEX IF NOT EXISTS idx_rental_agreements_vehicle ON rental_agreements(vehicle_id);
CREATE INDEX IF NOT EXISTS idx_rental_agreements_dates ON rental_agreements(start_date, end_date);
CREATE INDEX IF NOT EXISTS idx_delivery_records_agreement ON delivery_records(agreement_id);
CREATE INDEX IF NOT EXISTS idx_payments_agreement ON payments(agreement_id);
CREATE INDEX IF NOT EXISTS idx_maintenance_records_vehicle ON maintenance_records(vehicle_id);
```
