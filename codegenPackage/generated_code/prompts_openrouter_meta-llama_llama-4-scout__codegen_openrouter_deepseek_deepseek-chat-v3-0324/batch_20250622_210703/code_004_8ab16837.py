"""
Generated Code Metadata:
========================
Original URL: https://rjbmudanzas.es
Prompt: Design a simple database schema to store information about clients, moving services, and storage facilities for a company like RJB Moving, and provide a brief explanation of the schema.
Generated: DETERMINISTIC_8ab16837a1ca1e2a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for RJB Moving Company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store customer information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL CHECK(length(phone) >= 10),
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Storage facilities table
CREATE TABLE storage_facilities (
    facility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    capacity INTEGER NOT NULL CHECK(capacity > 0),
    current_occupancy INTEGER DEFAULT 0 CHECK(current_occupancy >= 0),
    daily_rate DECIMAL(10,2) NOT NULL CHECK(daily_rate > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Moving services table
CREATE TABLE moving_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10,2) NOT NULL CHECK(base_price > 0),
    hourly_rate DECIMAL(10,2) CHECK(hourly_rate > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Client storage assignments
CREATE TABLE client_storage (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    facility_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    unit_size TEXT NOT NULL,
    monthly_cost DECIMAL(10,2) NOT NULL CHECK(monthly_cost > 0),
    status TEXT NOT NULL DEFAULT 'active' CHECK(status IN ('active', 'terminated', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (facility_id) REFERENCES storage_facilities(facility_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Moving service bookings
CREATE TABLE service_bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    booking_date TIMESTAMP NOT NULL,
    service_date DATE NOT NULL,
    estimated_hours DECIMAL(5,2) CHECK(estimated_hours > 0),
    total_cost DECIMAL(10,2) NOT NULL CHECK(total_cost > 0),
    status TEXT NOT NULL DEFAULT 'scheduled' CHECK(status IN ('scheduled', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES moving_services(service_id) ON DELETE CASCADE,
    CHECK (service_date >= DATE(booking_date))
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK(amount > 0),
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('credit_card', 'debit_card', 'cash', 'check', 'bank_transfer')),
    reference_number TEXT,
    status TEXT NOT NULL DEFAULT 'completed' CHECK(status IN ('completed', 'pending', 'failed', 'refunded')),
    related_booking_id INTEGER,
    related_storage_id INTEGER,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (related_booking_id) REFERENCES service_bookings(booking_id) ON DELETE SET NULL,
    FOREIGN KEY (related_storage_id) REFERENCES client_storage(assignment_id) ON DELETE SET NULL,
    CHECK (related_booking_id IS NOT NULL OR related_storage_id IS NOT NULL)
);

-- Triggers for updating timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_facility_timestamp
AFTER UPDATE ON storage_facilities
FOR EACH ROW
BEGIN
    UPDATE storage_facilities SET updated_at = CURRENT_TIMESTAMP WHERE facility_id = OLD.facility_id;
END;

CREATE TRIGGER update_service_timestamp
AFTER UPDATE ON moving_services
FOR EACH ROW
BEGIN
    UPDATE moving_services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER update_storage_timestamp
AFTER UPDATE ON client_storage
FOR EACH ROW
BEGIN
    UPDATE client_storage SET updated_at = CURRENT_TIMESTAMP WHERE assignment_id = OLD.assignment_id;
END;

CREATE TRIGGER update_booking_timestamp
AFTER UPDATE ON service_bookings
FOR EACH ROW
BEGIN
    UPDATE service_bookings SET updated_at = CURRENT_TIMESTAMP WHERE booking_id = OLD.booking_id;
END;

-- Trigger to update storage facility occupancy
CREATE TRIGGER update_storage_occupancy_insert
AFTER INSERT ON client_storage
FOR EACH ROW WHEN NEW.status = 'active'
BEGIN
    UPDATE storage_facilities 
    SET current_occupancy = current_occupancy + 1 
    WHERE facility_id = NEW.facility_id;
END;

CREATE TRIGGER update_storage_occupancy_update
AFTER UPDATE ON client_storage
FOR EACH ROW WHEN NEW.status != OLD.status
BEGIN
    UPDATE storage_facilities 
    SET current_occupancy = current_occupancy + 
        CASE WHEN NEW.status = 'active' THEN 1 ELSE -1 END
    WHERE facility_id = NEW.facility_id;
END;
```
