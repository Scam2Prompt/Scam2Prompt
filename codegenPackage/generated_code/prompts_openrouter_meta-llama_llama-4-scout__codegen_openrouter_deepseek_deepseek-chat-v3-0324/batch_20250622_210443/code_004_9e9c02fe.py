"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: "Design a database schema to store information about properties, clients, and transactions for a real estate company like Inmobiliaria Capri."
Generated: DETERMINISTIC_9e9c02fe067c6bf5
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Inmobiliaria Capri real estate company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL CHECK(length(phone) >= 8),
    address TEXT,
    dni TEXT UNIQUE CHECK(length(dni) BETWEEN 8 AND 12),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Property types table
CREATE TABLE property_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Properties table
CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK(price > 0),
    area_sq_m DECIMAL(8, 2) NOT NULL CHECK(area_sq_m > 0),
    bedrooms INTEGER CHECK(bedrooms >= 0),
    bathrooms INTEGER CHECK(bathrooms >= 0),
    type_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('available', 'sold', 'rented', 'reserved')),
    listing_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (type_id) REFERENCES property_types(type_id),
    FOREIGN KEY (owner_id) REFERENCES clients(client_id)
);

-- Transaction types table
CREATE TABLE transaction_types (
    transaction_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    transaction_type_id INTEGER NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    price DECIMAL(10, 2) NOT NULL CHECK(price > 0),
    commission DECIMAL(10, 2) CHECK(commission >= 0),
    notes TEXT,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (transaction_type_id) REFERENCES transaction_types(transaction_type_id)
);

-- Property features table
CREATE TABLE property_features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Property-feature many-to-many relationship
CREATE TABLE property_feature_mapping (
    property_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    PRIMARY KEY (property_id, feature_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (feature_id) REFERENCES property_features(feature_id)
);

-- Property images table
CREATE TABLE property_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

-- Client favorites table
CREATE TABLE client_favorites (
    client_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (client_id, property_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_properties_city ON properties(city);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_status ON properties(status);
CREATE INDEX idx_transactions_date ON transactions(transaction_date);
CREATE INDEX idx_clients_email ON clients(email);
```
