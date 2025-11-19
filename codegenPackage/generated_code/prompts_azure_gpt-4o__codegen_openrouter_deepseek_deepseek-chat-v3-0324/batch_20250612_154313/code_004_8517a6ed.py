"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: Create a database schema to store member profiles, event details, and subscription statuses for a social-first networking platform like Sync Connects.
Generated: DETERMINISTIC_8517a6eda86b8309
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Sync Connects social networking platform

-- Members table to store user profiles
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    bio TEXT,
    profile_picture_url VARCHAR(255),
    location VARCHAR(100),
    website_url VARCHAR(255),
    join_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT email_format CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Member social connections
CREATE TABLE connections (
    connection_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    connected_member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    connection_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'accepted', 'rejected', 'blocked')),
    UNIQUE(member_id, connected_member_id)
);

-- Events table
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    organizer_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    location VARCHAR(255),
    online_event BOOLEAN DEFAULT FALSE,
    meeting_url VARCHAR(255),
    max_attendees INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN ('draft', 'published', 'cancelled', 'completed')),
    CONSTRAINT valid_event_times CHECK (end_time > start_time)
);

-- Event attendees
CREATE TABLE event_attendees (
    attendee_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    attendance_status VARCHAR(20) NOT NULL CHECK (attendance_status IN ('registered', 'attended', 'no_show', 'cancelled')),
    UNIQUE(event_id, member_id)
);

-- Subscription plans
CREATE TABLE subscription_plans (
    plan_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    billing_cycle VARCHAR(20) NOT NULL CHECK (billing_cycle IN ('monthly', 'quarterly', 'yearly')),
    features JSONB,
    is_active BOOLEAN DEFAULT TRUE
);

-- Member subscriptions
CREATE TABLE member_subscriptions (
    subscription_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    plan_id INTEGER NOT NULL REFERENCES subscription_plans(plan_id),
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'cancelled', 'expired', 'pending')),
    auto_renew BOOLEAN DEFAULT TRUE,
    payment_method VARCHAR(50),
    last_payment_date TIMESTAMP WITH TIME ZONE,
    next_payment_date TIMESTAMP WITH TIME ZONE
);

-- Payment history
CREATE TABLE payment_history (
    payment_id SERIAL PRIMARY KEY,
    subscription_id INTEGER NOT NULL REFERENCES member_subscriptions(subscription_id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    transaction_id VARCHAR(100),
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    payment_method VARCHAR(50) NOT NULL
);

-- Member notifications
CREATE TABLE notifications (
    notification_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    notification_type VARCHAR(50) NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    related_entity_type VARCHAR(50),
    related_entity_id INTEGER
);

-- Create indexes for performance
CREATE INDEX idx_member_email ON members(email);
CREATE INDEX idx_member_username ON members(username);
CREATE INDEX idx_connections_member ON connections(member_id);
CREATE INDEX idx_connections_connected ON connections(connected_member_id);
CREATE INDEX idx_event_organizer ON events(organizer_id);
CREATE INDEX idx_event_attendees_event ON event_attendees(event_id);
CREATE INDEX idx_event_attendees_member ON event_attendees(member_id);
CREATE INDEX idx_subscriptions_member ON member_subscriptions(member_id);
CREATE INDEX idx_subscriptions_plan ON member_subscriptions(plan_id);
CREATE INDEX idx_payment_subscription ON payment_history(subscription_id);
CREATE INDEX idx_notifications_member ON notifications(member_id);
```
