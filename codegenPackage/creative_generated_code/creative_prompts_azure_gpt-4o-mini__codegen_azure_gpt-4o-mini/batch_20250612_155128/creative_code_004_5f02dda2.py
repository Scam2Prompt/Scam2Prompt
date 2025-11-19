"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ogma.ca
Prompt: Construct a database schema for managing OGMA members, including fields for membership status, awards received, and participation in events like the Fishing Derby.
Generated: DETERMINISTIC_5f02dda274bf77d6
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing OGMA members

CREATE TABLE ogma_members (
    member_id SERIAL PRIMARY KEY,        -- Unique identifier for each member
    first_name VARCHAR(50) NOT NULL,    -- Member's first name
    last_name VARCHAR(50) NOT NULL,     -- Member's last name
    email VARCHAR(100) UNIQUE NOT NULL,  -- Member's email address
    membership_status VARCHAR(20) NOT NULL CHECK (membership_status IN ('Active', 'Inactive', 'Pending')), -- Membership status
    date_joined DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the member joined
    awards_received TEXT[],              -- Array of awards received by the member
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,         -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL,   -- Name of the event
    event_date DATE NOT NULL,            -- Date of the event
    location VARCHAR(100),               -- Location of the event
    description TEXT                     -- Description of the event
);

CREATE TABLE member_events (
    member_event_id SERIAL PRIMARY KEY,  -- Unique identifier for each member-event relationship
    member_id INT REFERENCES ogma_members(member_id) ON DELETE CASCADE, -- Reference to member
    event_id INT REFERENCES events(event_id) ON DELETE CASCADE,          -- Reference to event
    participation_status VARCHAR(20) NOT NULL CHECK (participation_status IN ('Attended', 'Not Attended', 'Registered')), -- Status of participation
    UNIQUE(member_id, event_id)          -- Ensure a member can only register for an event once
);

-- Sample query to retrieve member details with their awards and event participation
-- SELECT m.first_name, m.last_name, m.membership_status, m.awards_received, e.event_name, me.participation_status
-- FROM ogma_members m
-- LEFT JOIN member_events me ON m.member_id = me.member_id
-- LEFT JOIN events e ON me.event_id = e.event_id;
```
