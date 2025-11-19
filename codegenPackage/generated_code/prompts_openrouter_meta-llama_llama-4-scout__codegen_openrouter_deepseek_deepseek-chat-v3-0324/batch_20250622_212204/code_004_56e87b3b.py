"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: "Design a database schema to store information about Chevrolet vehicles, consórcio plans, and customer details, using a relational database management system."
Generated: DETERMINISTIC_56e87b3b08b71215
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Chevrolet vehicles, consórcio plans, and customer details

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing vehicle models
CREATE TABLE vehicle_models (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT NOT NULL,
    year INTEGER NOT NULL,
    engine_type TEXT NOT NULL,
    transmission TEXT NOT NULL,
    fuel_type TEXT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (year > 1900 AND year <= strftime('%Y', 'now') + 1),
    CHECK (base_price > 0)
);

-- Table for storing vehicle inventory
CREATE TABLE vehicle_inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    vin TEXT UNIQUE NOT NULL,
    color TEXT NOT NULL,
    mileage INTEGER DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'available', -- available, sold, reserved, maintenance
    purchase_date DATE,
    purchase_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id),
    CHECK (mileage >= 0),
    CHECK (status IN ('available', 'sold', 'reserved', 'maintenance'))
);

-- Table for consórcio plan types
CREATE TABLE consorcio_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_name TEXT NOT NULL,
    duration_months INTEGER NOT NULL,
    monthly_payment DECIMAL(10, 2) NOT NULL,
    total_value DECIMAL(10, 2) NOT NULL,
    interest_rate DECIMAL(5, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (duration_months > 0),
    CHECK (monthly_payment > 0),
    CHECK (total_value > 0),
    CHECK (interest_rate >= 0)
);

-- Table for customer information
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    birth_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (length(cpf) = 11)
);

-- Table for customer consórcio contracts
CREATE TABLE customer_consorcios (
    contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    plan_id INTEGER NOT NULL,
    model_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    current_status TEXT NOT NULL DEFAULT 'active', -- active, completed, canceled, defaulted
    monthly_payment DECIMAL(10, 2) NOT NULL,
    remaining_balance DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (plan_id) REFERENCES consorcio_plans(plan_id),
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id),
    CHECK (end_date > start_date),
    CHECK (current_status IN ('active', 'completed', 'canceled', 'defaulted')),
    CHECK (monthly_payment > 0),
    CHECK (remaining_balance >= 0)
);

-- Table for sales transactions
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    inventory_id INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    sale_price DECIMAL(10, 2) NOT NULL,
    payment_method TEXT NOT NULL, -- cash, financing, consorcio
    contract_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (inventory_id) REFERENCES vehicle_inventory(inventory_id),
    FOREIGN KEY (contract_id) REFERENCES customer_consorcios(contract_id),
    CHECK (sale_price > 0),
    CHECK (payment_method IN ('cash', 'financing', 'consorcio'))
);

-- Table for payment history
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_id INTEGER NOT NULL,
    payment_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT NOT NULL, -- bank_slip, credit_card, debit_card, transfer
    status TEXT NOT NULL DEFAULT 'pending', -- pending, completed, failed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (contract_id) REFERENCES customer_consorcios(contract_id),
    CHECK (amount > 0),
    CHECK (payment_method IN ('bank_slip', 'credit_card', 'debit_card', 'transfer')),
    CHECK (status IN ('pending', 'completed', 'failed'))
);

-- Indexes for performance optimization
CREATE INDEX idx_vehicle_model_name ON vehicle_models(model_name);
CREATE INDEX idx_vehicle_inventory_status ON vehicle_inventory(status);
CREATE INDEX idx_customer_cpf ON customers(cpf);
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_consorcio_plan_name ON consorcio_plans(plan_name);
CREATE INDEX idx_customer_consorcio_status ON customer_consorcios(current_status);
CREATE INDEX idx_sales_customer ON sales(customer_id);
CREATE INDEX idx_sales_inventory ON sales(inventory_id);
CREATE INDEX idx_payments_contract ON payments(contract_id);
```
