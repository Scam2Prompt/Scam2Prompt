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
-- Database schema for a professional organization (e.g., RMP)

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Resources;
DROP TABLE IF EXISTS Event_Resources;

-- Table to store member information
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,          -- Unique identifier for each member
    first_name VARCHAR(50) NOT NULL,      -- Member's first name
    last_name VARCHAR(50) NOT NULL,       -- Member's last name
    email VARCHAR(100) UNIQUE NOT NULL,   -- Member's email address (unique)
    phone VARCHAR(15),                     -- Member's phone number
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the member joined
    status VARCHAR(20) DEFAULT 'active'    -- Status of the member (active/inactive)
);

-- Table to store event information
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,           -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL,     -- Name of the event
    event_date TIMESTAMP NOT NULL,         -- Date and time of the event
    location VARCHAR(100),                  -- Location of the event
    description TEXT,                      -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the event was created
);

-- Table to store resources associated with events
CREATE TABLE Resources (
    resource_id SERIAL PRIMARY KEY,        -- Unique identifier for each resource
    resource_name VARCHAR(100) NOT NULL,  -- Name of the resource
    resource_type VARCHAR(50),             -- Type of resource (e.g., equipment, material)
    availability BOOLEAN DEFAULT TRUE,      -- Availability status of the resource
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the resource was created
);

-- Junction table to associate resources with events
CREATE TABLE Event_Resources (
    event_id INT NOT NULL,                 -- Foreign key referencing Events
    resource_id INT NOT NULL,              -- Foreign key referencing Resources
    quantity INT DEFAULT 1,                -- Quantity of the resource needed for the event
    PRIMARY KEY (event_id, resource_id),   -- Composite primary key
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (resource_id) REFERENCES Resources(resource_id) ON DELETE CASCADE -- Cascade delete
);

-- Sample data insertion (for testing purposes)
INSERT INTO Members (first_name, last_name, email, phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

INSERT INTO Events (event_name, event_date, location, description) VALUES
('Annual Conference', '2023-11-15 09:00:00', 'Convention Center', 'Annual gathering of members.'),
('Monthly Meeting', '2023-10-10 18:00:00', 'Office', 'Discussion on upcoming projects.');

INSERT INTO Resources (resource_name, resource_type, availability) VALUES
('Projector', 'Equipment', TRUE),
('Whiteboard', 'Equipment', TRUE);

INSERT INTO Event_Resources (event_id, resource_id, quantity) VALUES
(1, 1, 2),  -- 2 Projectors for Annual Conference
(2, 2, 1);  -- 1 Whiteboard for Monthly Meeting
```
