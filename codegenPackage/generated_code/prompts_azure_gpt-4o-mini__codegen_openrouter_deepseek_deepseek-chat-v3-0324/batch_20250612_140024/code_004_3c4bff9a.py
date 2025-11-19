"""
Generated Code Metadata:
========================
Original URL: https://carehelpers.pt
Prompt: Design a database schema in SQL for managing client information and service requests for a home care provider like CARE HELPERS, focusing on activities of daily living and technical aids.
Generated: DETERMINISTIC_3c4bff9a0b0ea223
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a home care provider (CARE HELPERS)
-- Manages client information, service requests, activities of daily living, and technical aids

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table - stores basic client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email TEXT,
    emergency_contact_name TEXT NOT NULL,
    emergency_contact_phone TEXT NOT NULL,
    date_registered DATE DEFAULT CURRENT_DATE,
    active BOOLEAN DEFAULT 1,
    notes TEXT,
    CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Caregivers table - stores information about care providers
CREATE TABLE caregivers (
    caregiver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other', 'Prefer not to say')),
    phone_number TEXT NOT NULL,
    email TEXT NOT NULL,
    qualification TEXT NOT NULL,
    date_hired DATE NOT NULL,
    active BOOLEAN DEFAULT 1,
    CHECK (email LIKE '%@%.%')
);

-- Activities of Daily Living (ADL) categories
CREATE TABLE adl_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Technical aids categories
CREATE TABLE technical_aid_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Service types table
CREATE TABLE service_types (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_adl BOOLEAN NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES adl_categories(category_id) ON DELETE SET NULL,
    CHECK (is_adl IN (0, 1))
);

-- Technical aids inventory
CREATE TABLE technical_aids (
    aid_id INTEGER PRIMARY KEY AUTOINCREMENT,
    aid_name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    quantity_available INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES technical_aid_categories(category_id) ON DELETE CASCADE
);

-- Client service requests
CREATE TABLE service_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    requested_date DATE NOT NULL,
    start_date DATE,
    end_date DATE,
    frequency TEXT CHECK(frequency IN ('Once', 'Daily', 'Weekly', 'Bi-weekly', 'Monthly')),
    status TEXT NOT NULL CHECK(status IN ('Pending', 'Approved', 'In Progress', 'Completed', 'Cancelled')),
    priority TEXT CHECK(priority IN ('Low', 'Medium', 'High', 'Urgent')),
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service_types(service_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR start_date <= end_date)
);

-- Caregiver assignments
CREATE TABLE caregiver_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    caregiver_id INTEGER NOT NULL,
    assignment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT NOT NULL CHECK(status IN ('Assigned', 'In Progress', 'Completed', 'Cancelled')),
    notes TEXT,
    FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE,
    FOREIGN KEY (caregiver_id) REFERENCES caregivers(caregiver_id) ON DELETE CASCADE
);

-- Client ADL assessments
CREATE TABLE adl_assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    assessment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    assessor_id INTEGER NOT NULL,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (assessor_id) REFERENCES caregivers(caregiver_id) ON DELETE CASCADE
);

-- ADL assessment details
CREATE TABLE adl_assessment_details (
    detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    capability_level INTEGER CHECK(capability_level BETWEEN 1 AND 5),
    notes TEXT,
    FOREIGN KEY (assessment_id) REFERENCES adl_assessments(assessment_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service_types(service_id) ON DELETE CASCADE
);

-- Technical aids assigned to clients
CREATE TABLE client_technical_aids (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    aid_id INTEGER NOT NULL,
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
    return_date DATE,
    quantity INTEGER NOT NULL DEFAULT 1,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (aid_id) REFERENCES technical_aids(aid_id) ON DELETE CASCADE,
    CHECK (return_date IS NULL OR assigned_date <= return_date),
    CHECK (quantity > 0)
);

-- Service visit logs
CREATE TABLE service_visits (
    visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL,
    visit_date DATE NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME,
    status TEXT NOT NULL CHECK(status IN ('Completed', 'No Show', 'Cancelled', 'Incomplete')),
    notes TEXT,
    FOREIGN KEY (assignment_id) REFERENCES caregiver_assignments(assignment_id) ON DELETE CASCADE,
    CHECK (end_time IS NULL OR start_time <= end_time)
);

-- Billing information
CREATE TABLE billing (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    invoice_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'Paid', 'Overdue', 'Cancelled')),
    payment_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (due_date >= invoice_date),
    CHECK (payment_date IS NULL OR payment_date >= invoice_date)
);

-- Billing line items
CREATE TABLE billing_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    service_id INTEGER,
    aid_id INTEGER,
    description TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES billing(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service_types(service_id) ON DELETE SET NULL,
    FOREIGN KEY (aid_id) REFERENCES technical_aids(aid_id) ON DELETE SET NULL,
    CHECK (quantity > 0),
    CHECK (unit_price >= 0)
);

-- Create indexes for performance optimization
CREATE INDEX idx_client_name ON clients(last_name, first_name);
CREATE INDEX idx_service_request_client ON service_requests(client_id);
CREATE INDEX idx_service_request_status ON service_requests(status);
CREATE INDEX idx_caregiver_assignments ON caregiver_assignments(request_id, caregiver_id);
CREATE INDEX idx_service_visits_date ON service_visits(visit_date);
CREATE INDEX idx_billing_client ON billing(client_id);
CREATE INDEX idx_billing_status ON billing(status);
```
