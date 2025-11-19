"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Create a SQL database schema to manage photography client information, photo shoots, and image metadata for a studio like Officine dell'Immagine.
Generated: DETERMINISTIC_4bfff7088c3059b3
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Photography Studio Database Schema
-- For managing client information, photo shoots, and image metadata

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Photo shoot types
CREATE TABLE shoot_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10,2),
    duration_minutes INTEGER
);

-- Photo shoots
CREATE TABLE shoots (
    shoot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    shoot_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    location TEXT,
    status TEXT CHECK(status IN ('scheduled', 'completed', 'cancelled', 'postponed')),
    price DECIMAL(10,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES shoot_types(type_id)
);

-- Image metadata
CREATE TABLE images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shoot_id INTEGER NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_size INTEGER,
    width INTEGER,
    height INTEGER,
    format TEXT,
    capture_date TIMESTAMP,
    camera_model TEXT,
    lens_model TEXT,
    iso INTEGER,
    aperture TEXT,
    shutter_speed TEXT,
    focal_length TEXT,
    keywords TEXT,
    rating INTEGER CHECK(rating BETWEEN 0 AND 5),
    selected BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shoot_id) REFERENCES shoots(shoot_id) ON DELETE CASCADE
);

-- Invoices
CREATE TABLE invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    shoot_id INTEGER,
    invoice_number TEXT UNIQUE NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status TEXT CHECK(status IN ('draft', 'sent', 'paid', 'overdue', 'cancelled')),
    subtotal DECIMAL(10,2) NOT NULL,
    tax DECIMAL(10,2),
    discount DECIMAL(10,2),
    total DECIMAL(10,2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (shoot_id) REFERENCES shoots(shoot_id)
);

-- Invoice line items
CREATE TABLE invoice_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    quantity INTEGER DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE
);

-- Triggers for timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_shoot_timestamp
AFTER UPDATE ON shoots
FOR EACH ROW
BEGIN
    UPDATE shoots SET updated_at = CURRENT_TIMESTAMP WHERE shoot_id = OLD.shoot_id;
END;

-- Indexes for performance
CREATE INDEX idx_shoots_client ON shoots(client_id);
CREATE INDEX idx_shoots_date ON shoots(shoot_date);
CREATE INDEX idx_images_shoot ON images(shoot_id);
CREATE INDEX idx_invoices_client ON invoices(client_id);
CREATE INDEX idx_invoices_status ON invoices(status);
```
