"""
Generated Code Metadata:
========================
Original URL: https://myrmp.org
Prompt: Design a database schema to store information about members, events, and resources for a professional organization like RMP.
Generated: DETERMINISTIC_af8b6f3b093964aa
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a professional organization management system

-- Members table to store information about organization members
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    membership_status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (membership_status IN ('active', 'inactive', 'pending', 'suspended')),
    professional_title VARCHAR(100),
    organization VARCHAR(100),
    bio TEXT,
    profile_picture_url VARCHAR(255),
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Member addresses table (one-to-many relationship with members)
CREATE TABLE member_addresses (
    address_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    address_type VARCHAR(20) NOT NULL CHECK (address_type IN ('home', 'work', 'other')),
    street_address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'United States',
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE (member_id, address_type)
);

-- Events table to store information about organization events
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    location VARCHAR(100) NOT NULL,
    max_attendees INTEGER,
    registration_deadline TIMESTAMP,
    event_status VARCHAR(20) NOT NULL DEFAULT 'upcoming' CHECK (event_status IN ('upcoming', 'ongoing', 'completed', 'cancelled')),
    created_by INTEGER REFERENCES members(member_id),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_datetime CHECK (end_datetime > start_datetime)
);

-- Event registration table (many-to-many relationship between members and events)
CREATE TABLE event_registrations (
    registration_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    attendance_status VARCHAR(20) NOT NULL DEFAULT 'registered' CHECK (attendance_status IN ('registered', 'attended', 'no-show', 'cancelled')),
    payment_status VARCHAR(20) NOT NULL DEFAULT 'unpaid' CHECK (payment_status IN ('unpaid', 'paid', 'partial', 'refunded')),
    notes TEXT,
    UNIQUE (event_id, member_id)
);

-- Resources table for organization documents, links, etc.
CREATE TABLE resources (
    resource_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    resource_type VARCHAR(50) NOT NULL CHECK (resource_type IN ('document', 'link', 'video', 'other')),
    url VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    uploader_id INTEGER REFERENCES members(member_id),
    access_level VARCHAR(20) NOT NULL DEFAULT 'member' CHECK (access_level IN ('public', 'member', 'board', 'admin')),
    file_size INTEGER,
    file_type VARCHAR(50)
);

-- Resource access log table
CREATE TABLE resource_access_log (
    access_id SERIAL PRIMARY KEY,
    resource_id INTEGER NOT NULL REFERENCES resources(resource_id) ON DELETE CASCADE,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    access_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    action VARCHAR(20) NOT NULL CHECK (action IN ('view', 'download', 'edit', 'delete'))
);

-- Committees table
CREATE TABLE committees (
    committee_id SERIAL PRIMARY KEY,
    committee_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_date DATE NOT NULL DEFAULT CURRENT_DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Committee memberships (many-to-many relationship between members and committees)
CREATE TABLE committee_memberships (
    membership_id SERIAL PRIMARY KEY,
    committee_id INTEGER NOT NULL REFERENCES committees(committee_id) ON DELETE CASCADE,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL DEFAULT 'member' CHECK (role IN ('chair', 'vice-chair', 'secretary', 'treasurer', 'member')),
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    end_date DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (committee_id, member_id)
);

-- Payments table for membership dues and event fees
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50) NOT NULL CHECK (payment_method IN ('credit_card', 'bank_transfer', 'check', 'cash', 'other')),
    payment_status VARCHAR(20) NOT NULL DEFAULT 'completed' CHECK (payment_status IN ('pending', 'completed', 'failed', 'refunded')),
    payment_for VARCHAR(50) NOT NULL CHECK (payment_for IN ('membership', 'event', 'donation', 'other')),
    related_event_id INTEGER REFERENCES events(event_id),
    notes TEXT,
    receipt_number VARCHAR(50) UNIQUE
);

-- Announcements table
CREATE TABLE announcements (
    announcement_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    publish_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expiry_date TIMESTAMP,
    author_id INTEGER REFERENCES members(member_id),
    priority VARCHAR(20) NOT NULL DEFAULT 'normal' CHECK (priority IN ('low', 'normal', 'high', 'urgent')),
    target_audience VARCHAR(20) NOT NULL DEFAULT 'all' CHECK (target_audience IN ('all', 'members', 'board', 'committee'))
);

-- Create indexes for better performance
CREATE INDEX idx_member_email ON members(email);
CREATE INDEX idx_member_status ON members(membership_status);
CREATE INDEX idx_event_dates ON events(start_datetime, end_datetime);
CREATE INDEX idx_event_status ON events(event_status);
CREATE INDEX idx_registration_event ON event_registrations(event_id);
CREATE INDEX idx_registration_member ON event_registrations(member_id);
CREATE INDEX idx_resource_type ON resources(resource_type);
CREATE INDEX idx_resource_access ON resource_access_log(resource_id);
CREATE INDEX idx_committee_active ON committees(is_active);
CREATE INDEX idx_payment_member ON payments(member_id);
CREATE INDEX idx_payment_status ON payments(payment_status);
CREATE INDEX idx_announcement_dates ON announcements(publish_date, expiry_date);
```
