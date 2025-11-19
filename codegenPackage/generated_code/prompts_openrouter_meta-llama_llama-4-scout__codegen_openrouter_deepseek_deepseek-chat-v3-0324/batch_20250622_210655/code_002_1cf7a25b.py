"""
Generated Code Metadata:
========================
Original URL: https://bandadorada.com
Prompt: Generate a sample database schema for managing client information, event details, and payment records for an orchestra service like Orquesta Dorada.
Generated: DETERMINISTIC_1cf7a25b2f1c2d1d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Orquesta Dorada orchestra service

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Clients table
CREATE TABLE clients (
    client_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Event types table
CREATE TABLE event_types (
    event_type_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    min_musicians INTEGER NOT NULL,
    max_musicians INTEGER NOT NULL,
    duration_minutes INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Events table
CREATE TABLE events (
    event_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    event_type_id INTEGER NOT NULL REFERENCES event_types(event_type_id),
    name VARCHAR(200) NOT NULL,
    description TEXT,
    event_date TIMESTAMP WITH TIME ZONE NOT NULL,
    location TEXT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    number_of_musicians INTEGER NOT NULL,
    special_requests TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (status IN ('pending', 'confirmed', 'completed', 'cancelled')),
    CHECK (number_of_musicians > 0)
);

-- Musicians table
CREATE TABLE musicians (
    musician_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    instrument VARCHAR(100) NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    CHECK (hourly_rate > 0)
);

-- Event musicians junction table
CREATE TABLE event_musicians (
    event_id UUID NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    musician_id UUID NOT NULL REFERENCES musicians(musician_id) ON DELETE CASCADE,
    PRIMARY KEY (event_id, musician_id)
);

-- Payment methods table
CREATE TABLE payment_methods (
    payment_method_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT
);

-- Payments table
CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_id UUID NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    payment_method_id INTEGER NOT NULL REFERENCES payment_methods(payment_method_id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP WITH TIME ZONE NOT NULL,
    transaction_reference VARCHAR(100),
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (amount > 0),
    CHECK (status IN ('pending', 'completed', 'failed', 'refunded'))
);

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_client_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_event_timestamp
BEFORE UPDATE ON events
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_musician_timestamp
BEFORE UPDATE ON musicians
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_payment_timestamp
BEFORE UPDATE ON payments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Insert default payment methods
INSERT INTO payment_methods (name, description) VALUES 
('Cash', 'Payment made with cash'),
('Credit Card', 'Payment made with credit card'),
('Bank Transfer', 'Payment made via bank transfer'),
('Check', 'Payment made with check'),
('Other', 'Other payment methods');

-- Insert sample event types
INSERT INTO event_types (name, description, base_price, min_musicians, max_musicians, duration_minutes) VALUES 
('Wedding Ceremony', 'Classical music for wedding ceremonies', 1200.00, 3, 8, 60),
('Corporate Event', 'Music for corporate events and galas', 1500.00, 4, 12, 120),
('Private Party', 'Music for private celebrations', 1000.00, 2, 6, 90),
('Concert Performance', 'Full orchestra concert performance', 2500.00, 10, 30, 120),
('Background Music', 'Light background music for events', 800.00, 1, 4, 180);
```
