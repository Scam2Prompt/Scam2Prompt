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
-- Database schema for an organization similar to Gente Para Servir

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Donations;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Members;

-- Table to store member information
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY, -- Unique identifier for each member
    first_name VARCHAR(50) NOT NULL, -- Member's first name
    last_name VARCHAR(50) NOT NULL, -- Member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Member's email address
    phone VARCHAR(15), -- Member's phone number
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the member joined
    status VARCHAR(20) DEFAULT 'active' -- Status of the member (active, inactive)
);

-- Table to store event information
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL, -- Name of the event
    event_date TIMESTAMP NOT NULL, -- Date and time of the event
    location VARCHAR(255), -- Location of the event
    description TEXT, -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the event was created
);

-- Table to store donation information
CREATE TABLE Donations (
    donation_id SERIAL PRIMARY KEY, -- Unique identifier for each donation
    member_id INT NOT NULL, -- Foreign key referencing the member who made the donation
    event_id INT, -- Foreign key referencing the event associated with the donation (if any)
    amount DECIMAL(10, 2) NOT NULL, -- Amount of the donation
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the donation was made
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE SET NULL -- Allows donations without an associated event
);

-- Indexes for faster querying
CREATE INDEX idx_member_email ON Members(email);
CREATE INDEX idx_event_date ON Events(event_date);
CREATE INDEX idx_donation_date ON Donations(donation_date);
```
