"""
Generated Code Metadata:
========================
Original URL: https://afunabb.cl
Prompt: Design a database schema for managing member information and benefits for an association like AFUNABB Chillán, focusing on community engagement and support.
Generated: DETERMINISTIC_e7cb8bccf11a9f6b
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for AFUNABB Chillán member management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Members table to store basic member information
CREATE TABLE IF NOT EXISTS members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT CHECK(phone GLOB '[0-9]*'),
    address TEXT,
    city TEXT,
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    membership_status TEXT NOT NULL CHECK(membership_status IN ('active', 'inactive', 'suspended', 'pending')),
    profile_picture BLOB,
    bio TEXT,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Member authentication credentials
CREATE TABLE IF NOT EXISTS member_auth (
    member_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    last_login TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Member roles and permissions
CREATE TABLE IF NOT EXISTS roles (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS member_roles (
    member_id INTEGER,
    role_id INTEGER,
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (member_id, role_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);

-- Benefits available to members
CREATE TABLE IF NOT EXISTS benefits (
    benefit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    benefit_name TEXT NOT NULL,
    description TEXT,
    benefit_type TEXT NOT NULL CHECK(benefit_type IN ('discount', 'service', 'event', 'other')),
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Member-benefit assignments
CREATE TABLE IF NOT EXISTS member_benefits (
    member_id INTEGER,
    benefit_id INTEGER,
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
    redeemed_date DATE,
    notes TEXT,
    PRIMARY KEY (member_id, benefit_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (benefit_id) REFERENCES benefits(benefit_id) ON DELETE CASCADE
);

-- Events organized by the association
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    location TEXT NOT NULL,
    max_attendees INTEGER,
    registration_deadline DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Member event participation
CREATE TABLE IF NOT EXISTS event_attendance (
    member_id INTEGER,
    event_id INTEGER,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    attendance_status TEXT NOT NULL CHECK(attendance_status IN ('registered', 'attended', 'cancelled', 'no-show')),
    feedback TEXT,
    PRIMARY KEY (member_id, event_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Member contributions (donations, volunteer hours, etc.)
CREATE TABLE IF NOT EXISTS contributions (
    contribution_id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    contribution_type TEXT NOT NULL CHECK(contribution_type IN ('donation', 'volunteer', 'other')),
    amount DECIMAL(10, 2),
    hours DECIMAL(5, 2),
    description TEXT,
    contribution_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Communication history with members
CREATE TABLE IF NOT EXISTS communications (
    communication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    communication_type TEXT NOT NULL CHECK(communication_type IN ('email', 'sms', 'call', 'letter', 'meeting')),
    subject TEXT,
    content TEXT NOT NULL,
    sent_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('sent', 'delivered', 'read', 'failed')),
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Member documents (contracts, IDs, etc.)
CREATE TABLE IF NOT EXISTS member_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    document_type TEXT NOT NULL CHECK(document_type IN ('id', 'contract', 'payment', 'other')),
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Member payment records
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('cash', 'transfer', 'card', 'other')),
    payment_reference TEXT,
    status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'failed', 'refunded')),
    notes TEXT,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_member_status ON members(membership_status);
CREATE INDEX IF NOT EXISTS idx_member_email ON members(email);
CREATE INDEX IF NOT EXISTS idx_benefit_active ON benefits(is_active);
CREATE INDEX IF NOT EXISTS idx_event_date ON events(event_date);
CREATE INDEX IF NOT EXISTS idx_contribution_date ON contributions(contribution_date);
CREATE INDEX IF NOT EXISTS idx_payment_status ON payments(status);
```
