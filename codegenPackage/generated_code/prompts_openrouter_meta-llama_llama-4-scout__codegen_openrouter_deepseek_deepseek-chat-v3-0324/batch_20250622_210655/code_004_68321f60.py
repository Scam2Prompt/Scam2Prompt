"""
Generated Code Metadata:
========================
Original URL: https://salonlapista.com.ar
Prompt: Design a basic database schema for storing party reservations, client information, and services offered by a children's party salon.
Generated: DETERMINISTIC_68321f6098fc0bc7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a children's party salon

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table stores customer information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Services table stores available party packages/services
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10,2) NOT NULL,
    duration_minutes INTEGER NOT NULL,
    max_children INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (base_price >= 0),
    CHECK (duration_minutes > 0),
    CHECK (max_children > 0)
);

-- Add-ons table for additional services/options
CREATE TABLE add_ons (
    add_on_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (price >= 0)
);

-- Party reservations table
CREATE TABLE reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    party_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    number_of_children INTEGER NOT NULL,
    special_requests TEXT,
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    total_price DECIMAL(10,2) NOT NULL,
    deposit_paid DECIMAL(10,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    CHECK (number_of_children > 0),
    CHECK (total_price >= 0),
    CHECK (deposit_paid >= 0),
    CHECK (end_time > start_time)
);

-- Junction table for reservation add-ons
CREATE TABLE reservation_add_ons (
    reservation_id INTEGER NOT NULL,
    add_on_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    price_at_booking DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (reservation_id, add_on_id),
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE,
    FOREIGN KEY (add_on_id) REFERENCES add_ons(add_on_id),
    CHECK (quantity > 0),
    CHECK (price_at_booking >= 0)
);

-- Staff members table
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    role TEXT NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Staff assignments for reservations
CREATE TABLE reservation_staff (
    reservation_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    PRIMARY KEY (reservation_id, staff_id),
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

-- Create indexes for performance
CREATE INDEX idx_reservations_date ON reservations(party_date);
CREATE INDEX idx_reservations_client ON reservations(client_id);
CREATE INDEX idx_reservations_service ON reservations(service_id);
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_clients_phone ON clients(phone);

-- Triggers to update timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_service_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER update_add_on_timestamp
AFTER UPDATE ON add_ons
FOR EACH ROW
BEGIN
    UPDATE add_ons SET updated_at = CURRENT_TIMESTAMP WHERE add_on_id = OLD.add_on_id;
END;

CREATE TRIGGER update_reservation_timestamp
AFTER UPDATE ON reservations
FOR EACH ROW
BEGIN
    UPDATE reservations SET updated_at = CURRENT_TIMESTAMP WHERE reservation_id = OLD.reservation_id;
END;

CREATE TRIGGER update_staff_timestamp
AFTER UPDATE ON staff
FOR EACH ROW
BEGIN
    UPDATE staff SET updated_at = CURRENT_TIMESTAMP WHERE staff_id = OLD.staff_id;
END;
```
