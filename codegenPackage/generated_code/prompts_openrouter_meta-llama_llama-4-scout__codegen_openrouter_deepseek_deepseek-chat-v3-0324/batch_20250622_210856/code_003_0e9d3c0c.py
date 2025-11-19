"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Design a database schema to store information about staged homes, clients, and services offered by a home staging company like Unique Home Staging & Redesign by Dee.
Generated: DETERMINISTIC_0e9d3c0cac30dcea
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Unique Home Staging & Redesign by Dee

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
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
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Properties table
CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    property_type TEXT NOT NULL,
    square_footage INTEGER,
    bedrooms INTEGER,
    bathrooms INTEGER,
    listing_price REAL,
    listing_date DATE,
    target_sale_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price REAL NOT NULL,
    duration_hours INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (base_price >= 0)
);

-- Inventory items table
CREATE TABLE inventory_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    purchase_price REAL,
    rental_price_per_day REAL,
    condition TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (quantity >= 0),
    CHECK (rental_price_per_day >= 0)
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    start_date DATE NOT NULL,
    completion_date DATE,
    budget REAL,
    status TEXT NOT NULL DEFAULT 'planned',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    CHECK (status IN ('planned', 'in_progress', 'completed', 'cancelled'))
);

-- Project services junction table
CREATE TABLE project_services (
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    custom_price REAL,
    notes TEXT,
    PRIMARY KEY (project_id, service_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    CHECK (quantity > 0)
);

-- Project inventory junction table
CREATE TABLE project_inventory (
    project_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    start_date DATE NOT NULL,
    end_date DATE,
    notes TEXT,
    PRIMARY KEY (project_id, item_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES inventory_items(item_id) ON DELETE CASCADE,
    CHECK (quantity > 0)
);

-- Before/after photos table
CREATE TABLE property_photos (
    photo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    project_id INTEGER,
    photo_url TEXT NOT NULL,
    caption TEXT,
    is_before BOOLEAN NOT NULL DEFAULT FALSE,
    taken_date DATE,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_property_timestamp
AFTER UPDATE ON properties
FOR EACH ROW
BEGIN
    UPDATE properties SET updated_at = CURRENT_TIMESTAMP WHERE property_id = OLD.property_id;
END;

CREATE TRIGGER update_service_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER update_inventory_timestamp
AFTER UPDATE ON inventory_items
FOR EACH ROW
BEGIN
    UPDATE inventory_items SET updated_at = CURRENT_TIMESTAMP WHERE item_id = OLD.item_id;
END;

CREATE TRIGGER update_project_timestamp
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

-- Indexes for performance
CREATE INDEX idx_properties_client ON properties(client_id);
CREATE INDEX idx_projects_property ON projects(property_id);
CREATE INDEX idx_project_services ON project_services(project_id);
CREATE INDEX idx_project_inventory ON project_inventory(project_id);
CREATE INDEX idx_property_photos_property ON property_photos(property_id);
CREATE INDEX idx_property_photos_project ON property_photos(project_id);
```
