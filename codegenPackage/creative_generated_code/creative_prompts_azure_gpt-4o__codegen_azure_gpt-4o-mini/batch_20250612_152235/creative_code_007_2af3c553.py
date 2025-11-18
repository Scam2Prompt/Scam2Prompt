"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinxcash.com
Prompt: Write a SQL database schema for an event company to manage clients, events, venues, and staff assignments, reflecting the organizational structure described on the webpage.
Generated: DETERMINISTIC_2af3c5535b3d3cb1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema for an Event Company

-- Drop existing tables if they exist (for development/testing purposes)
DROP TABLE IF EXISTS StaffAssignments;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Venues;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Staff;

-- Table for Clients
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,    -- Client's name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email (must be unique)
    phone VARCHAR(15),              -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for Venues
CREATE TABLE Venues (
    venue_id SERIAL PRIMARY KEY, -- Unique identifier for each venue
    name VARCHAR(100) NOT NULL,  -- Venue name
    address VARCHAR(255) NOT NULL, -- Venue address
    capacity INT NOT NULL,        -- Maximum capacity of the venue
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for Events
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    client_id INT NOT NULL,       -- Foreign key to Clients
    venue_id INT NOT NULL,        -- Foreign key to Venues
    event_date DATE NOT NULL,     -- Date of the event
    description TEXT,             -- Event description
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Cascade delete for clients
    FOREIGN KEY (venue_id) REFERENCES Venues(venue_id) ON DELETE SET NULL -- Set venue_id to NULL if venue is deleted
);

-- Table for Staff
CREATE TABLE Staff (
    staff_id SERIAL PRIMARY KEY,  -- Unique identifier for each staff member
    name VARCHAR(100) NOT NULL,    -- Staff member's name
    role VARCHAR(50) NOT NULL,     -- Staff member's role (e.g., Coordinator, Technician)
    email VARCHAR(100) UNIQUE NOT NULL, -- Staff member's email (must be unique)
    phone VARCHAR(15),              -- Staff member's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for Staff Assignments
CREATE TABLE StaffAssignments (
    assignment_id SERIAL PRIMARY KEY, -- Unique identifier for each assignment
    event_id INT NOT NULL,             -- Foreign key to Events
    staff_id INT NOT NULL,             -- Foreign key to Staff
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Assignment timestamp
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE, -- Cascade delete for events
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id) ON DELETE CASCADE -- Cascade delete for staff
);
```
