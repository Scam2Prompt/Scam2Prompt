"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: Create a sample database schema to store information about volunteers, equipment, and activities for a civil protection group like the one in Torre d'Isola.
Generated: DETERMINISTIC_d598f0a283d5b077
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Civil Protection Volunteer Management System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Volunteer table
CREATE TABLE volunteers (
    volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    emergency_contact_name TEXT NOT NULL,
    emergency_contact_phone TEXT NOT NULL,
    blood_type TEXT CHECK(blood_type IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
    medical_conditions TEXT,
    allergies TEXT,
    skills TEXT,
    certification_level TEXT,
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    active_status BOOLEAN NOT NULL DEFAULT TRUE,
    notes TEXT
);

-- Equipment table
CREATE TABLE equipment (
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL CHECK(category IN ('Medical', 'Rescue', 'Communication', 'Vehicle', 'Other')),
    description TEXT,
    serial_number TEXT UNIQUE,
    purchase_date DATE,
    purchase_price REAL,
    current_value REAL,
    status TEXT NOT NULL CHECK(status IN ('Available', 'In Use', 'Maintenance', 'Retired')) DEFAULT 'Available',
    location TEXT NOT NULL,
    last_inspection_date DATE,
    next_inspection_date DATE,
    notes TEXT
);

-- Activity types table
CREATE TABLE activity_types (
    activity_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    required_certification TEXT,
    risk_level TEXT CHECK(risk_level IN ('Low', 'Medium', 'High'))
);

-- Activities table
CREATE TABLE activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity_type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    location TEXT NOT NULL,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Planned', 'Ongoing', 'Completed', 'Cancelled')) DEFAULT 'Planned',
    coordinator_id INTEGER NOT NULL,
    notes TEXT,
    FOREIGN KEY (activity_type_id) REFERENCES activity_types(activity_type_id),
    FOREIGN KEY (coordinator_id) REFERENCES volunteers(volunteer_id),
    CHECK (end_datetime > start_datetime)
);

-- Volunteer participation in activities
CREATE TABLE volunteer_participation (
    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    volunteer_id INTEGER NOT NULL,
    activity_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    check_in_time DATETIME,
    check_out_time DATETIME,
    hours_worked REAL GENERATED ALWAYS AS (
        CASE 
            WHEN check_in_time IS NULL OR check_out_time IS NULL THEN 0
            ELSE (julianday(check_out_time) - julianday(check_in_time)) * 24
        END
    ) STORED,
    notes TEXT,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id),
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id),
    UNIQUE (volunteer_id, activity_id)
);

-- Equipment usage in activities
CREATE TABLE equipment_usage (
    usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER NOT NULL,
    activity_id INTEGER NOT NULL,
    assigned_to INTEGER,
    check_out_time DATETIME NOT NULL,
    check_in_time DATETIME,
    condition_on_return TEXT CHECK(condition_on_return IN ('Good', 'Damaged', 'Lost')),
    notes TEXT,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id),
    FOREIGN KEY (assigned_to) REFERENCES volunteers(volunteer_id),
    CHECK (check_in_time IS NULL OR check_in_time >= check_out_time)
);

-- Training records
CREATE TABLE training_records (
    training_id INTEGER PRIMARY KEY AUTOINCREMENT,
    volunteer_id INTEGER NOT NULL,
    training_type TEXT NOT NULL,
    training_date DATE NOT NULL,
    instructor TEXT NOT NULL,
    expiration_date DATE,
    certification_number TEXT,
    notes TEXT,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id)
);

-- Incident reports
CREATE TABLE incident_reports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity_id INTEGER,
    reported_by INTEGER NOT NULL,
    report_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    incident_date DATETIME NOT NULL,
    incident_type TEXT NOT NULL,
    description TEXT NOT NULL,
    actions_taken TEXT NOT NULL,
    follow_up_required BOOLEAN NOT NULL DEFAULT FALSE,
    follow_up_details TEXT,
    severity TEXT CHECK(severity IN ('Minor', 'Moderate', 'Major', 'Critical')),
    status TEXT CHECK(status IN ('Open', 'In Progress', 'Resolved', 'Closed')) DEFAULT 'Open',
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id),
    FOREIGN KEY (reported_by) REFERENCES volunteers(volunteer_id)
);

-- Equipment maintenance log
CREATE TABLE maintenance_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER NOT NULL,
    maintenance_date DATE NOT NULL,
    maintenance_type TEXT NOT NULL CHECK(maintenance_type IN ('Routine', 'Repair', 'Inspection', 'Upgrade')),
    performed_by TEXT NOT NULL,
    description TEXT NOT NULL,
    parts_replaced TEXT,
    cost REAL,
    next_maintenance_date DATE,
    notes TEXT,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

-- Inventory items (consumables)
CREATE TABLE inventory (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    unit TEXT NOT NULL,
    minimum_stock INTEGER NOT NULL DEFAULT 1,
    location TEXT NOT NULL,
    expiry_date DATE,
    supplier TEXT,
    notes TEXT,
    CHECK (quantity >= 0)
);

-- Inventory transactions
CREATE TABLE inventory_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER NOT NULL,
    transaction_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('Purchase', 'Consumption', 'Adjustment', 'Donation')),
    quantity INTEGER NOT NULL,
    unit_price REAL,
    total_cost REAL GENERATED ALWAYS AS (quantity * unit_price) STORED,
    performed_by INTEGER NOT NULL,
    activity_id INTEGER,
    notes TEXT,
    FOREIGN KEY (item_id) REFERENCES inventory(item_id),
    FOREIGN KEY (performed_by) REFERENCES volunteers(volunteer_id),
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id)
);

-- Create indexes for performance
CREATE INDEX idx_volunteer_name ON volunteers(last_name, first_name);
CREATE INDEX idx_equipment_status ON equipment(status);
CREATE INDEX idx_activities_dates ON activities(start_datetime, end_datetime);
CREATE INDEX idx_participation_volunteer ON volunteer_participation(volunteer_id);
CREATE INDEX idx_participation_activity ON volunteer_participation(activity_id);
CREATE INDEX idx_equipment_usage_activity ON equipment_usage(activity_id);
CREATE INDEX idx_training_volunteer ON training_records(volunteer_id);
CREATE INDEX idx_incident_activity ON incident_reports(activity_id);
CREATE INDEX idx_maintenance_equipment ON maintenance_log(equipment_id);
CREATE INDEX idx_inventory_category ON inventory(category);
```
