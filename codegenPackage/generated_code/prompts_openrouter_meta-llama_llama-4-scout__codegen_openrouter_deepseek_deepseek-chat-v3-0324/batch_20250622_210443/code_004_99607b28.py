"""
Generated Code Metadata:
========================
Original URL: https://genteparaservir.org
Prompt: Design a simple database schema for storing information about members, events, and donations for an organization similar to Gente Para Servir.
Generated: DETERMINISTIC_99607b28290f6f44
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Gente Para Servir-like organization

-- Members table to store information about organization members
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    membership_status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (membership_status IN ('active', 'inactive', 'pending')),
    birth_date DATE,
    skills TEXT,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Events table to store information about organization events
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL,
    description TEXT,
    event_date TIMESTAMP NOT NULL,
    location VARCHAR(255) NOT NULL,
    organizer_id INTEGER REFERENCES members(member_id),
    max_attendees INTEGER,
    status VARCHAR(20) NOT NULL DEFAULT 'planned' CHECK (status IN ('planned', 'completed', 'cancelled')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Event attendance junction table
CREATE TABLE event_attendance (
    attendance_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    attendance_status VARCHAR(20) NOT NULL DEFAULT 'registered' CHECK (attendance_status IN ('registered', 'attended', 'no-show')),
    hours_volunteered DECIMAL(5,2),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(event_id, member_id)
);

-- Donations table to track financial contributions
CREATE TABLE donations (
    donation_id SERIAL PRIMARY KEY,
    donor_id INTEGER NOT NULL REFERENCES members(member_id),
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),
    donation_date DATE NOT NULL DEFAULT CURRENT_DATE,
    payment_method VARCHAR(50) NOT NULL CHECK (payment_method IN ('cash', 'check', 'credit_card', 'bank_transfer', 'other')),
    payment_reference VARCHAR(100),
    purpose VARCHAR(255),
    is_recurring BOOLEAN DEFAULT FALSE,
    recurring_frequency VARCHAR(20),
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Expenses table to track organization expenditures
CREATE TABLE expenses (
    expense_id SERIAL PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),
    expense_date DATE NOT NULL DEFAULT CURRENT_DATE,
    category VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    approved_by INTEGER REFERENCES members(member_id),
    receipt_attached BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_members_email ON members(email);
CREATE INDEX idx_events_date ON events(event_date);
CREATE INDEX idx_donations_donor ON donations(donor_id);
CREATE INDEX idx_donations_date ON donations(donation_date);
CREATE INDEX idx_expenses_date ON expenses(expense_date);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers to automatically update timestamps
CREATE TRIGGER update_member_timestamp
BEFORE UPDATE ON members
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_event_timestamp
BEFORE UPDATE ON events
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_attendance_timestamp
BEFORE UPDATE ON event_attendance
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_donation_timestamp
BEFORE UPDATE ON donations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_expense_timestamp
BEFORE UPDATE ON expenses
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
