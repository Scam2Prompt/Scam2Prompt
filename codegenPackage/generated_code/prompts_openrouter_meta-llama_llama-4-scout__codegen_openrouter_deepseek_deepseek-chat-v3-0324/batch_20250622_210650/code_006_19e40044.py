"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: "Suggest an efficient database schema for managing vehicle inventory, customer information, and renting agreements for a company like Innova Renting, including relationships between entities and potential queries for reporting."
Generated: DETERMINISTIC_19e40044d9de1592
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Innova Renting vehicle rental management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Vehicle Types table
CREATE TABLE vehicle_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL,
    daily_rate REAL NOT NULL CHECK(daily_rate > 0),
    weekly_rate REAL NOT NULL CHECK(weekly_rate > 0),
    monthly_rate REAL NOT NULL CHECK(monthly_rate > 0),
    over_mileage_fee REAL NOT NULL CHECK(over_mileage_fee >= 0),
    description TEXT
);

-- Vehicles table
CREATE TABLE vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER NOT NULL,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL CHECK(year > 1900),
    vin TEXT UNIQUE NOT NULL,
    license_plate TEXT UNIQUE NOT NULL,
    color TEXT,
    current_mileage REAL NOT NULL CHECK(current_mileage >= 0),
    last_service_date DATE,
    next_service_due DATE,
    status TEXT NOT NULL CHECK(status IN ('available', 'rented', 'maintenance', 'out_of_service')),
    FOREIGN KEY (type_id) REFERENCES vehicle_types(type_id)
);

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    driver_license_number TEXT UNIQUE NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Employees table
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    position TEXT NOT NULL,
    hire_date DATE NOT NULL DEFAULT CURRENT_DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Rental Agreements table
CREATE TABLE rental_agreements (
    agreement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    vehicle_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL CHECK(end_date > start_date),
    actual_return_date DATE,
    start_mileage REAL NOT NULL CHECK(start_mileage >= 0),
    end_mileage REAL CHECK(end_mileage >= start_mileage OR end_mileage IS NULL),
    daily_rate REAL NOT NULL CHECK(daily_rate > 0),
    total_charge REAL CHECK(total_charge >= 0 OR total_charge IS NULL),
    payment_status TEXT CHECK(payment_status IN ('pending', 'paid', 'partially_paid', 'refunded') OR payment_status IS NULL),
    agreement_status TEXT NOT NULL CHECK(agreement_status IN ('reserved', 'active', 'completed', 'cancelled')),
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agreement_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK(amount > 0),
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('cash', 'credit_card', 'debit_card', 'bank_transfer')),
    transaction_reference TEXT,
    FOREIGN KEY (agreement_id) REFERENCES rental_agreements(agreement_id)
);

-- Maintenance Records table
CREATE TABLE maintenance_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    service_date DATE NOT NULL,
    service_type TEXT NOT NULL,
    description TEXT,
    cost REAL CHECK(cost >= 0),
    mileage_at_service REAL NOT NULL CHECK(mileage_at_service >= 0),
    next_service_due DATE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_vehicles_status ON vehicles(status);
CREATE INDEX idx_rental_agreements_customer ON rental_agreements(customer_id);
CREATE INDEX idx_rental_agreements_vehicle ON rental_agreements(vehicle_id);
CREATE INDEX idx_rental_agreements_dates ON rental_agreements(start_date, end_date);
CREATE INDEX idx_payments_agreement ON payments(agreement_id);

-- Common reporting queries

-- Query 1: Currently rented vehicles
SELECT v.vehicle_id, v.make, v.model, v.year, c.first_name, c.last_name, 
       ra.start_date, ra.end_date, ra.agreement_status
FROM vehicles v
JOIN rental_agreements ra ON v.vehicle_id = ra.vehicle_id
JOIN customers c ON ra.customer_id = c.customer_id
WHERE ra.agreement_status = 'active'
AND ra.actual_return_date IS NULL;

-- Query 2: Revenue by vehicle type
SELECT vt.type_name, 
       COUNT(ra.agreement_id) AS rental_count,
       SUM(ra.total_charge) AS total_revenue,
       AVG(ra.total_charge) AS avg_revenue_per_rental
FROM rental_agreements ra
JOIN vehicles v ON ra.vehicle_id = v.vehicle_id
JOIN vehicle_types vt ON v.type_id = vt.type_id
WHERE ra.agreement_status = 'completed'
GROUP BY vt.type_name
ORDER BY total_revenue DESC;

-- Query 3: Vehicles due for maintenance
SELECT v.vehicle_id, v.make, v.model, v.year, v.current_mileage,
       v.next_service_due, mr.mileage_at_service AS last_service_mileage,
       mr.service_date AS last_service_date
FROM vehicles v
JOIN maintenance_records mr ON v.vehicle_id = mr.vehicle_id
WHERE v.next_service_due <= DATE('now', '+7 days') 
   OR v.current_mileage >= mr.mileage_at_service + 5000
ORDER BY v.next_service_due;

-- Query 4: Customer rental history
SELECT c.customer_id, c.first_name, c.last_name, c.email,
       COUNT(ra.agreement_id) AS total_rentals,
       SUM(ra.total_charge) AS total_spent,
       MAX(ra.end_date) AS last_rental_date
FROM customers c
LEFT JOIN rental_agreements ra ON c.customer_id = ra.customer_id
WHERE ra.agreement_status IN ('completed', 'active')
GROUP BY c.customer_id, c.first_name, c.last_name, c.email
ORDER BY total_spent DESC;

-- Query 5: Monthly revenue report
SELECT strftime('%Y-%m', ra.start_date) AS month,
       COUNT(ra.agreement_id) AS rental_count,
       SUM(ra.total_charge) AS total_revenue,
       SUM(p.amount) AS total_payments_received
FROM rental_agreements ra
LEFT JOIN payments p ON ra.agreement_id = p.agreement_id
WHERE ra.agreement_status = 'completed'
GROUP BY strftime('%Y-%m', ra.start_date)
ORDER BY month DESC;
```
