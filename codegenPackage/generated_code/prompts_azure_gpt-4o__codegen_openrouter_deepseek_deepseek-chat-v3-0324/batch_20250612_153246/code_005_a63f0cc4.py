"""
Generated Code Metadata:
========================
Original URL: https://www.pensar.inf.br
Prompt: Create a database schema for an ERP system inspired by SOLPEN, ensuring it supports modular customization for industries like manufacturing, commerce, and distribution.
Generated: DETERMINISTIC_a63f0cc4cc91f6d5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for modular ERP system inspired by SOLPEN
-- Supports manufacturing, commerce, and distribution industries

-- Core tables (required for all installations)
CREATE TABLE organizations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    tax_id VARCHAR(30),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    website VARCHAR(100),
    logo_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(organization_id, name)
);

CREATE TABLE user_roles (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    role_id INTEGER REFERENCES roles(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, role_id)
);

CREATE TABLE permissions (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    module VARCHAR(50) NOT NULL
);

CREATE TABLE role_permissions (
    role_id INTEGER REFERENCES roles(id) ON DELETE CASCADE,
    permission_id INTEGER REFERENCES permissions(id) ON DELETE CASCADE,
    PRIMARY KEY (role_id, permission_id)
);

-- Common modules (used by most industries)
CREATE TABLE currencies (
    id SERIAL PRIMARY KEY,
    code VARCHAR(3) UNIQUE NOT NULL,
    name VARCHAR(50) NOT NULL,
    symbol VARCHAR(5)
);

CREATE TABLE exchange_rates (
    id SERIAL PRIMARY KEY,
    from_currency_id INTEGER REFERENCES currencies(id) ON DELETE CASCADE,
    to_currency_id INTEGER REFERENCES currencies(id) ON DELETE CASCADE,
    rate DECIMAL(19,6) NOT NULL,
    effective_date DATE NOT NULL,
    UNIQUE(from_currency_id, to_currency_id, effective_date)
);

CREATE TABLE units_of_measure (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(50) NOT NULL,
    type VARCHAR(20) NOT NULL CHECK (type IN ('length', 'weight', 'volume', 'quantity', 'time', 'other'))
);

-- Accounting module
CREATE TABLE chart_of_accounts (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    account_type VARCHAR(30) NOT NULL CHECK (account_type IN ('asset', 'liability', 'equity', 'revenue', 'expense')),
    parent_id INTEGER REFERENCES chart_of_accounts(id) ON DELETE SET NULL,
    is_active BOOLEAN DEFAULT TRUE,
    UNIQUE(organization_id, code)
);

CREATE TABLE fiscal_periods (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_closed BOOLEAN DEFAULT FALSE,
    UNIQUE(organization_id, name)
);

-- Commerce module
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    tax_id VARCHAR(30),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    credit_limit DECIMAL(19,2),
    payment_terms INTEGER, -- days
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(organization_id, code)
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    tax_id VARCHAR(30),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    payment_terms INTEGER, -- days
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(organization_id, code)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    code VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    product_type VARCHAR(20) NOT NULL CHECK (product_type IN ('goods', 'service')),
    unit_of_measure_id INTEGER REFERENCES units_of_measure(id),
    sales_account_id INTEGER REFERENCES chart_of_accounts(id),
    purchase_account_id INTEGER REFERENCES chart_of_accounts(id),
    inventory_account_id INTEGER REFERENCES chart_of_accounts(id),
    cost_method VARCHAR(20) CHECK (cost_method IN ('FIFO', 'LIFO', 'AVERAGE')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(organization_id, code)
);

CREATE TABLE product_prices (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    currency_id INTEGER REFERENCES currencies(id) ON DELETE CASCADE,
    price_type VARCHAR(20) NOT NULL CHECK (price_type IN ('purchase', 'sale', 'wholesale')),
    price DECIMAL(19,2) NOT NULL,
    effective_date DATE NOT NULL,
    UNIQUE(product_id, currency_id, price_type, effective_date)
);

-- Inventory module
CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    UNIQUE(organization_id, code)
);

CREATE TABLE inventory_items (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    warehouse_id INTEGER REFERENCES warehouses(id) ON DELETE CASCADE,
    quantity_on_hand DECIMAL(19,3) NOT NULL DEFAULT 0,
    quantity_committed DECIMAL(19,3) NOT NULL DEFAULT 0,
    quantity_available DECIMAL(19,3) GENERATED ALWAYS AS (quantity_on_hand - quantity_committed) STORED,
    last_count_date DATE,
    UNIQUE(product_id, warehouse_id)
);

CREATE TABLE inventory_transactions (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    warehouse_id INTEGER REFERENCES warehouses(id) ON DELETE CASCADE,
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('purchase', 'sale', 'transfer', 'adjustment', 'production')),
    quantity DECIMAL(19,3) NOT NULL,
    unit_cost DECIMAL(19,4),
    reference_id INTEGER, -- links to source document (invoice, order, etc)
    reference_type VARCHAR(50), -- document type
    notes TEXT,
    created_by INTEGER REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Manufacturing module (optional)
CREATE TABLE bills_of_materials (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    version VARCHAR(20) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(organization_id, product_id, version)
);

CREATE TABLE bom_items (
    id SERIAL PRIMARY KEY,
    bom_id INTEGER REFERENCES bills_of_materials(id) ON DELETE CASCADE,
    component_product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    quantity DECIMAL(19,3) NOT NULL,
    unit_of_measure_id INTEGER REFERENCES units_of_measure(id),
    notes TEXT,
    sequence INTEGER NOT NULL
);

CREATE TABLE work_centers (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    cost_per_hour DECIMAL(19,2),
    is_active BOOLEAN DEFAULT TRUE,
    UNIQUE(organization_id, code)
);

CREATE TABLE production_orders (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id) ON DELETE CASCADE,
    bom_id INTEGER REFERENCES bills_of_materials(id) ON DELETE SET NULL,
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    quantity DECIMAL(19,3) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('planned', 'released', 'in
