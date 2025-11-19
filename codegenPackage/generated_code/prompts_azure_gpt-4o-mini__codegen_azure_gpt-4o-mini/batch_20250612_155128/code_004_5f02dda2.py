"""
Generated Code Metadata:
========================
Original URL: https://ogma.ca
Prompt: Construct a database schema for managing OGMA members, including fields for membership status, awards received, and participation in events like the Fishing Derby.
Generated: DETERMINISTIC_5f02dda274bf77d6
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing OGMA members

CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY, -- Unique identifier for each member
    first_name VARCHAR(50) NOT NULL, -- Member's first name
    last_name VARCHAR(50) NOT NULL, -- Member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Member's email address
    membership_status VARCHAR(20) NOT NULL CHECK (membership_status IN ('Active', 'Inactive', 'Pending')), -- Status of membership
    date_joined DATE NOT NULL DEFAULT CURRENT_DATE, -- Date when the member joined
    awards_received TEXT, -- Awards received by the member, stored as a comma-separated list
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL, -- Name of the event
    event_date DATE NOT NULL, -- Date of the event
    location VARCHAR(100), -- Location of the event
    description TEXT -- Description of the event
);

CREATE TABLE MemberEvents (
    member_event_id SERIAL PRIMARY KEY, -- Unique identifier for each member-event relationship
    member_id INT NOT NULL, -- Foreign key referencing Members
    event_id INT NOT NULL, -- Foreign key referencing Events
    participation_status VARCHAR(20) NOT NULL CHECK (participation_status IN ('Attended', 'Registered', 'Cancelled')), -- Status of participation
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_member_email ON Members(email);
CREATE INDEX idx_event_name ON Events(event_name);
CREATE INDEX idx_member_event ON MemberEvents(member_id, event_id);
```
