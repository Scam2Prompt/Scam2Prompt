"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proarteasa.com
Prompt: Design a database schema for managing lot reservations and customer information for a real estate project, ensuring it includes fields for payment plans and contact details.
Generated: DETERMINISTIC_5e90bfd8531ccbea
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing lot reservations and customer information

CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,               -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL,            -- Customer's first name
    last_name VARCHAR(100) NOT NULL,             -- Customer's last name
    email VARCHAR(255) UNIQUE NOT NULL,           -- Customer's email address (unique)
    phone_number VARCHAR(15) NOT NULL,            -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp for when the customer record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

CREATE TABLE PaymentPlans (
    payment_plan_id SERIAL PRIMARY KEY,           -- Unique identifier for each payment plan
    plan_name VARCHAR(100) NOT NULL,              -- Name of the payment plan
    amount DECIMAL(10, 2) NOT NULL,               -- Total amount of the payment plan
    duration_months INT NOT NULL,                 -- Duration of the payment plan in months
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp for when the payment plan record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

CREATE TABLE Lots (
    lot_id SERIAL PRIMARY KEY,                     -- Unique identifier for each lot
    lot_number VARCHAR(50) NOT NULL,              -- Lot number or identifier
    size DECIMAL(10, 2) NOT NULL,                 -- Size of the lot in square meters
    price DECIMAL(10, 2) NOT NULL,                -- Price of the lot
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp for when the lot record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

CREATE TABLE Reservations (
    reservation_id SERIAL PRIMARY KEY,             -- Unique identifier for each reservation
    customer_id INT NOT NULL,                      -- Foreign key referencing the Customers table
    lot_id INT NOT NULL,                           -- Foreign key referencing the Lots table
    payment_plan_id INT NOT NULL,                  -- Foreign key referencing the PaymentPlans table
    reservation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of reservation
    status VARCHAR(50) NOT NULL,                   -- Status of the reservation (e.g., 'Pending', 'Confirmed', 'Cancelled')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp for when the reservation record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Cascade delete for customers
    FOREIGN KEY (lot_id) REFERENCES Lots(lot_id) ON DELETE CASCADE,                 -- Cascade delete for lots
    FOREIGN KEY (payment_plan_id) REFERENCES PaymentPlans(payment_plan_id) ON DELETE CASCADE -- Cascade delete for payment plans
);
```
