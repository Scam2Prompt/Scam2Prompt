"""
Generated Code Metadata:
========================
Original URL: https://portal-crypto-io.com
Prompt: Create a SQL database schema to store information about Gould Barbers' shops, barbers, and clients.
Generated: DETERMINISTIC_b163c5d39c6ff16b
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Gould Barbers' Shops, Barbers, and Clients

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS shops (
    shop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    opening_hours TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_shop UNIQUE (name, address)
);

CREATE TABLE IF NOT EXISTS barbers (
    barber_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shop_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    hire_date DATE NOT NULL,
    specialization TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shop_id) REFERENCES shops(shop_id) ON DELETE CASCADE,
    CONSTRAINT unique_barber UNIQUE (shop_id, first_name, last_name, phone)
);

CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    preferred_barber_id INTEGER,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (preferred_barber_id) REFERENCES barbers(barber_id) ON DELETE SET NULL,
    CONSTRAINT unique_client UNIQUE (first_name, last_name, phone)
);

CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_service UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS barber_services (
    barber_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (barber_id, service_id),
    FOREIGN KEY (barber_id) REFERENCES barbers(barber_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    barber_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    shop_id INTEGER NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT DEFAULT 'scheduled' CHECK(status IN ('scheduled', 'completed', 'cancelled', 'no-show')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (barber_id) REFERENCES barbers(barber_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (shop_id) REFERENCES shops(shop_id) ON DELETE CASCADE,
    CONSTRAINT unique_appointment UNIQUE (barber_id, appointment_date, start_time)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_barber_shop ON barbers(shop_id);
CREATE INDEX IF NOT EXISTS idx_client_preferred_barber ON clients(preferred_barber_id);
CREATE INDEX IF NOT EXISTS idx_appointment_client ON appointments(client_id);
CREATE INDEX IF NOT EXISTS idx_appointment_barber ON appointments(barber_id);
CREATE INDEX IF NOT EXISTS idx_appointment_date ON appointments(appointment_date);
CREATE INDEX IF NOT EXISTS idx_appointment_status ON appointments(status);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_shop_timestamp
AFTER UPDATE ON shops
FOR EACH ROW
BEGIN
    UPDATE shops SET updated_at = CURRENT_TIMESTAMP WHERE shop_id = OLD.shop_id;
END;

CREATE TRIGGER IF NOT EXISTS update_barber_timestamp
AFTER UPDATE ON barbers
FOR EACH ROW
BEGIN
    UPDATE barbers SET updated_at = CURRENT_TIMESTAMP WHERE barber_id = OLD.barber_id;
END;

CREATE TRIGGER IF NOT EXISTS update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER IF NOT EXISTS update_appointment_timestamp
AFTER UPDATE ON appointments
FOR EACH ROW
BEGIN
    UPDATE appointments SET updated_at = CURRENT_TIMESTAMP WHERE appointment_id = OLD.appointment_id;
END;
```
