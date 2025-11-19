"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Design a database schema for a system to manage certifications and memberships for a professional organization like the Colegio de Psicologos de Oruro.
Generated: DETERMINISTIC_90466b5e2699b054
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing certifications and memberships for a professional organization

-- Create a table to store information about members
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY, -- Unique identifier for each member
    first_name VARCHAR(50) NOT NULL, -- Member's first name
    last_name VARCHAR(50) NOT NULL, -- Member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Member's email address
    phone VARCHAR(15), -- Member's phone number
    membership_start_date DATE NOT NULL, -- Date when the membership started
    membership_end_date DATE, -- Date when the membership ended (NULL if active)
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'suspended')) DEFAULT 'active' -- Membership status
);

-- Create a table to store information about certifications
CREATE TABLE Certifications (
    certification_id SERIAL PRIMARY KEY, -- Unique identifier for each certification
    certification_name VARCHAR(100) NOT NULL, -- Name of the certification
    issuing_organization VARCHAR(100) NOT NULL, -- Organization that issued the certification
    issue_date DATE NOT NULL, -- Date when the certification was issued
    expiration_date DATE, -- Date when the certification expires (NULL if lifetime)
    member_id INT REFERENCES Members(member_id) ON DELETE CASCADE -- Foreign key to link certification to a member
);

-- Create a table to store the history of membership renewals
CREATE TABLE MembershipRenewals (
    renewal_id SERIAL PRIMARY KEY, -- Unique identifier for each renewal
    member_id INT REFERENCES Members(member_id) ON DELETE CASCADE, -- Foreign key to link renewal to a member
    renewal_date DATE NOT NULL, -- Date of the renewal
    renewal_fee DECIMAL(10, 2) NOT NULL, -- Fee paid for the renewal
    payment_status VARCHAR(20) CHECK (payment_status IN ('paid', 'pending', 'failed')) DEFAULT 'paid' -- Status of the payment
);

-- Create a table to store the history of certifications obtained by members
CREATE TABLE MemberCertifications (
    member_certification_id SERIAL PRIMARY KEY, -- Unique identifier for each member certification record
    member_id INT REFERENCES Members(member_id) ON DELETE CASCADE, -- Foreign key to link to a member
    certification_id INT REFERENCES Certifications(certification_id) ON DELETE CASCADE, -- Foreign key to link to a certification
    obtained_date DATE NOT NULL, -- Date when the certification was obtained
    UNIQUE(member_id, certification_id) -- Ensure a member cannot obtain the same certification multiple times
);

-- Create a table to store organization events related to certifications and memberships
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL, -- Name of the event
    event_date DATE NOT NULL, -- Date of the event
    location VARCHAR(100), -- Location of the event
    description TEXT -- Description of the event
);

-- Create a table to link members to events they attended
CREATE TABLE MemberEvents (
    member_event_id SERIAL PRIMARY KEY, -- Unique identifier for each member event record
    member_id INT REFERENCES Members(member_id) ON DELETE CASCADE, -- Foreign key to link to a member
    event_id INT REFERENCES Events(event_id) ON DELETE CASCADE, -- Foreign key to link to an event
    attendance_status VARCHAR(20) CHECK (attendance_status IN ('attended', 'not attended')) DEFAULT 'attended', -- Attendance status
    UNIQUE(member_id, event_id) -- Ensure a member cannot register for the same event multiple times
);

-- Indexes for performance optimization
CREATE INDEX idx_member_email ON Members(email);
CREATE INDEX idx_certification_name ON Certifications(certification_name);
CREATE INDEX idx_event_date ON Events(event_date);
```
