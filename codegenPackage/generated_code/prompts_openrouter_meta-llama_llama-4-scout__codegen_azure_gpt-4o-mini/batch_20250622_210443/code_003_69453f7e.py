"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: "Design a database schema to store information about plumbing and fire fighting services provided by a company like ERA ENGINEERING."
Generated: DETERMINISTIC_69453f7e3bb13dde
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about plumbing and fire fighting services

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Appointments;

-- Table to store information about services offered
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL, -- Name of the service
    service_description TEXT, -- Description of the service
    service_type VARCHAR(50) NOT NULL CHECK (service_type IN ('Plumbing', 'Fire Fighting')), -- Type of service
    cost DECIMAL(10, 2) NOT NULL, -- Cost of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store customer information
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL, -- Customer's first name
    last_name VARCHAR(50) NOT NULL, -- Customer's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Customer's email address
    phone_number VARCHAR(15), -- Customer's phone number
    address TEXT, -- Customer's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store employee information
CREATE TABLE Employees (
    employee_id SERIAL PRIMARY KEY, -- Unique identifier for each employee
    first_name VARCHAR(50) NOT NULL, -- Employee's first name
    last_name VARCHAR(50) NOT NULL, -- Employee's last name
    position VARCHAR(50) NOT NULL, -- Employee's position (e.g., plumber, technician)
    phone_number VARCHAR(15), -- Employee's phone number
    email VARCHAR(100) UNIQUE NOT NULL, -- Employee's email address
    hire_date DATE NOT NULL, -- Date when the employee was hired
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the employee was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store appointment information
CREATE TABLE Appointments (
    appointment_id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    customer_id INT NOT NULL, -- Reference to the customer
    service_id INT NOT NULL, -- Reference to the service
    employee_id INT NOT NULL, -- Reference to the employee assigned
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    status VARCHAR(20) NOT NULL CHECK (status IN ('Scheduled', 'Completed', 'Cancelled')), -- Status of the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the appointment was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) ON DELETE SET NULL -- Foreign key constraint
);

-- Indexes for faster querying
CREATE INDEX idx_service_name ON Services(service_name);
CREATE INDEX idx_customer_email ON Customers(email);
CREATE INDEX idx_employee_email ON Employees(email);
CREATE INDEX idx_appointment_date ON Appointments(appointment_date);
```
