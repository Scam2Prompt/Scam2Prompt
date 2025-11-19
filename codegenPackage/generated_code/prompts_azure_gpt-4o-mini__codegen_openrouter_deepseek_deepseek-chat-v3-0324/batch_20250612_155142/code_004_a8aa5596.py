"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Design a database schema for an NDIS provider that tracks client goals, support services, and community engagement, reflecting the tailored services provided by Shareth Homecare.
Generated: DETERMINISTIC_a8aa5596c86a478d
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Shareth Homecare NDIS provider

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    ndis_number TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT NOT NULL,
    suburb TEXT NOT NULL,
    state TEXT NOT NULL,
    postcode TEXT NOT NULL,
    emergency_contact_name TEXT NOT NULL,
    emergency_contact_phone TEXT NOT NULL,
    date_joined DATE NOT NULL,
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (active IN (0, 1))
);

-- Client goals table
CREATE TABLE client_goals (
    goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    goal_description TEXT NOT NULL,
    target_date DATE,
    is_achieved BOOLEAN DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (is_achieved IN (0, 1))
);

-- Support categories table
CREATE TABLE support_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Support workers table
CREATE TABLE support_workers (
    worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    qualifications TEXT,
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (active IN (0, 1))
);

-- Support services table
CREATE TABLE support_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    description TEXT,
    ndis_code TEXT,
    rate DECIMAL(10, 2) NOT NULL,
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES support_categories(category_id),
    CHECK (active IN (0, 1))
);

-- Client services table (junction between clients and services)
CREATE TABLE client_services (
    client_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    frequency TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES support_services(service_id)
);

-- Service delivery table (records actual service delivery)
CREATE TABLE service_delivery (
    delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_service_id INTEGER NOT NULL,
    worker_id INTEGER NOT NULL,
    delivery_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    notes TEXT,
    kilometers DECIMAL(5, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_service_id) REFERENCES client_services(client_service_id),
    FOREIGN KEY (worker_id) REFERENCES support_workers(worker_id)
);

-- Community activities table
CREATE TABLE community_activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity_name TEXT NOT NULL,
    description TEXT,
    location TEXT NOT NULL,
    cost DECIMAL(10, 2),
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (active IN (0, 1))
);

-- Client community engagement table
CREATE TABLE client_community_engagement (
    engagement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    activity_id INTEGER NOT NULL,
    engagement_date DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (activity_id) REFERENCES community_activities(activity_id)
);

-- Goal progress notes table
CREATE TABLE goal_progress_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    goal_id INTEGER NOT NULL,
    worker_id INTEGER NOT NULL,
    note_date DATE NOT NULL,
    progress TEXT NOT NULL,
    next_steps TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (goal_id) REFERENCES client_goals(goal_id) ON DELETE CASCADE,
    FOREIGN KEY (worker_id) REFERENCES support_workers(worker_id)
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_goal_timestamp
AFTER UPDATE ON client_goals
FOR EACH ROW
BEGIN
    UPDATE client_goals SET updated_at = CURRENT_TIMESTAMP WHERE goal_id = OLD.goal_id;
END;

CREATE TRIGGER update_service_timestamp
AFTER UPDATE ON support_services
FOR EACH ROW
BEGIN
    UPDATE support_services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER update_worker_timestamp
AFTER UPDATE ON support_workers
FOR EACH ROW
BEGIN
    UPDATE support_workers SET updated_at = CURRENT_TIMESTAMP WHERE worker_id = OLD.worker_id;
END;

CREATE TRIGGER update_client_service_timestamp
AFTER UPDATE ON client_services
FOR EACH ROW
BEGIN
    UPDATE client_services SET updated_at = CURRENT_TIMESTAMP WHERE client_service_id = OLD.client_service_id;
END;

CREATE TRIGGER update_delivery_timestamp
AFTER UPDATE ON service_delivery
FOR EACH ROW
BEGIN
    UPDATE service_delivery SET updated_at = CURRENT_TIMESTAMP WHERE delivery_id = OLD.delivery_id;
END;

CREATE TRIGGER update_activity_timestamp
AFTER UPDATE ON community_activities
FOR EACH ROW
BEGIN
    UPDATE community_activities SET updated_at = CURRENT_TIMESTAMP WHERE activity_id = OLD.activity_id;
END;

CREATE TRIGGER update_engagement_timestamp
AFTER UPDATE ON client_community_engagement
FOR EACH ROW
BEGIN
    UPDATE client_community_engagement SET updated_at = CURRENT_TIMESTAMP WHERE engagement_id = OLD.engagement_id;
END;

CREATE TRIGGER update_progress_note_timestamp
AFTER UPDATE ON goal_progress_notes
FOR EACH ROW
BEGIN
    UPDATE goal_progress_notes SET updated_at = CURRENT_TIMESTAMP WHERE note_id = OLD.note_id;
END;
```
