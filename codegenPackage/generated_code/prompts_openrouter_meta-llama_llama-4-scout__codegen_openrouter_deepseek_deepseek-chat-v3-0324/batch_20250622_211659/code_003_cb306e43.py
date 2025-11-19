"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Design a simple database schema for an ERP system tailored to micro and small enterprises, inspired by Sistemabox's system."
Generated: DETERMINISTIC_cb306e431d1d1f53
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an ERP system tailored to micro and small enterprises
-- Inspired by Sistemabox's system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Users table to manage system users
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,  -- Store hashed passwords only
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    role TEXT NOT NULL CHECK(role IN ('admin', 'manager', 'employee')),
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Companies table (for multi-tenant support)
CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    tax_id TEXT NOT NULL UNIQUE,
    address TEXT,
    phone TEXT,
    email TEXT,
    logo_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User-company association table
CREATE TABLE user_companies (
    user_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, company_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT,
    unit_of_measure TEXT NOT NULL,
    purchase_price DECIMAL(10, 2) NOT NULL,
    sale_price DECIMAL(10, 2) NOT NULL,
    current_stock DECIMAL(10, 2) NOT NULL DEFAULT 0,
    min_stock_level DECIMAL(10, 2) DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    UNIQUE (company_id, code)
);

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    tax_id TEXT,
    address TEXT,
    phone TEXT,
    email TEXT,
    credit_limit DECIMAL(10, 2) DEFAULT 0,
    current_balance DECIMAL(10, 2) DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    UNIQUE (company_id, code)
);

-- Suppliers table
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    tax_id TEXT,
    address TEXT,
    phone TEXT,
    email TEXT,
    current_balance DECIMAL(10, 2) DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    UNIQUE (company_id, code)
);

-- Sales orders table
CREATE TABLE sales_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    order_number TEXT NOT NULL,
    order_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('draft', 'confirmed', 'shipped', 'invoiced', 'cancelled')),
    subtotal DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0,
    total_amount DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (created_by) REFERENCES users(user_id),
    UNIQUE (company_id, order_number)
);

-- Sales order items table
CREATE TABLE sales_order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    discount_percent DECIMAL(5, 2) DEFAULT 0,
    tax_percent DECIMAL(5, 2) NOT NULL,
    line_total DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES sales_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Purchase orders table
CREATE TABLE purchase_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    order_number TEXT NOT NULL,
    order_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('draft', 'confirmed', 'received', 'invoiced', 'cancelled')),
    subtotal DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0,
    total_amount DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (created_by) REFERENCES users(user_id),
    UNIQUE (company_id, order_number)
);

-- Purchase order items table
CREATE TABLE purchase_order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    discount_percent DECIMAL(5, 2) DEFAULT 0,
    tax_percent DECIMAL(5, 2) NOT NULL,
    line_total DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES purchase_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Inventory movements table
CREATE TABLE inventory_movements (
    movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    movement_type TEXT NOT NULL CHECK(movement_type IN ('purchase', 'sale', 'adjustment', 'transfer')),
    quantity DECIMAL(10, 2) NOT NULL,
    reference_id INTEGER,  -- Can reference order_id or other documents
    reference_type TEXT,   -- Type of reference (e.g., 'sales_order', 'purchase_order')
    notes TEXT,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (created_by) REFERENCES users(user_id)
);

-- Financial transactions table
CREATE TABLE financial_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    transaction_date DATE NOT NULL,
    account_type TEXT NOT NULL CHECK(account_type IN ('receivable', 'payable', 'revenue', 'expense', 'asset', 'liability')),
    account_id INTEGER NOT NULL,  -- References customer_id, supplier_id, or general account
    account_name TEXT NOT NULL,   -- Denormalized for reporting
    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('invoice', 'payment', 'receipt', 'expense', 'adjustment')),
    reference_id INTEGER,         -- References order_id or other documents
    reference_number TEXT,        -- Document number
    amount DECIMAL(10, 2) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES users(user_id)
);

-- Triggers for maintaining updated_at timestamps
CREATE TRIGGER update_users_timestamp
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE user_id = OLD.user_id;
END;

CREATE TRIGGER update_companies_timestamp
AFTER UPDATE ON companies
FOR EACH ROW
BEGIN
    UPDATE
