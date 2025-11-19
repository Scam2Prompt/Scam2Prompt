"""
Generated Code Metadata:
========================
Original URL: https://grupoinmobiliariocrecer.com.co
Prompt: Design a database schema for storing information about properties, clients, and transactions for a real estate company like Grupo Crecer.
Generated: DETERMINISTIC_b41e00ee634ba77e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Grupo Crecer Real Estate Management System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL CHECK(length(phone) >= 10),
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Property types lookup table
CREATE TABLE IF NOT EXISTS property_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT UNIQUE NOT NULL,
    description TEXT
);

-- Properties table
CREATE TABLE IF NOT EXISTS properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    price DECIMAL(12, 2) NOT NULL CHECK(price > 0),
    bedrooms INTEGER CHECK(bedrooms >= 0),
    bathrooms INTEGER CHECK(bathrooms >= 0),
    square_feet INTEGER CHECK(square_feet > 0),
    year_built INTEGER,
    property_type_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('available', 'pending', 'sold', 'rented')),
    listing_date DATE DEFAULT CURRENT_DATE,
    owner_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_type_id) REFERENCES property_types(type_id),
    FOREIGN KEY (owner_id) REFERENCES clients(client_id)
);

-- Agents table
CREATE TABLE IF NOT EXISTS agents (
    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL CHECK(length(phone) >= 10),
    license_number TEXT UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    commission_rate DECIMAL(5, 2) CHECK(commission_rate BETWEEN 0 AND 100),
    active BOOLEAN DEFAULT 1
);

-- Transactions table
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    buyer_id INTEGER NOT NULL,
    seller_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('sale', 'rental')),
    transaction_date DATE NOT NULL,
    amount DECIMAL(12, 2) NOT NULL CHECK(amount > 0),
    commission_amount DECIMAL(12, 2) CHECK(commission_amount >= 0),
    status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (buyer_id) REFERENCES clients(client_id),
    FOREIGN KEY (seller_id) REFERENCES clients(client_id),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

-- Property images table
CREATE TABLE IF NOT EXISTS property_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT 0,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
);

-- Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    appointment_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER NOT NULL CHECK(duration_minutes > 0),
    status TEXT NOT NULL CHECK(status IN ('scheduled', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_properties_city ON properties(city);
CREATE INDEX IF NOT EXISTS idx_properties_price ON properties(price);
CREATE INDEX IF NOT EXISTS idx_properties_status ON properties(status);
CREATE INDEX IF NOT EXISTS idx_transactions_date ON transactions(transaction_date);
CREATE INDEX IF NOT EXISTS idx_clients_email ON clients(email);
```
