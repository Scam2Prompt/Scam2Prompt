"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Design a database schema for storing information about residents in a Kallimos community, ensuring it supports multi-generational and multi-ability inclusivity.
Generated: DETERMINISTIC_558cfecaa0260f13
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Kallimos Community Database Schema

-- Table to store information about residents
CREATE TABLE Residents (
    resident_id SERIAL PRIMARY KEY,         -- Unique identifier for each resident
    first_name VARCHAR(50) NOT NULL,       -- Resident's first name
    last_name VARCHAR(50) NOT NULL,        -- Resident's last name
    date_of_birth DATE NOT NULL,            -- Resident's date of birth
    gender VARCHAR(10),                      -- Resident's gender
    address VARCHAR(255) NOT NULL,          -- Resident's address
    phone_number VARCHAR(15),                -- Resident's contact number
    email VARCHAR(100),                      -- Resident's email address
    mobility_ability VARCHAR(50),            -- Mobility ability (e.g. wheelchair user, fully mobile)
    communication_ability VARCHAR(50),       -- Communication ability (e.g. hearing impaired, fully communicative)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store information about family relationships
CREATE TABLE FamilyRelationships (
    relationship_id SERIAL PRIMARY KEY,      -- Unique identifier for each relationship
    resident_id INT REFERENCES Residents(resident_id) ON DELETE CASCADE,  -- The resident in the relationship
    family_member_id INT REFERENCES Residents(resident_id) ON DELETE CASCADE, -- The family member
    relationship_type VARCHAR(50) NOT NULL,  -- Type of relationship (e.g. parent, child, sibling)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store additional support needs
CREATE TABLE SupportNeeds (
    support_need_id SERIAL PRIMARY KEY,       -- Unique identifier for each support need
    resident_id INT REFERENCES Residents(resident_id) ON DELETE CASCADE,  -- The resident needing support
    support_type VARCHAR(100) NOT NULL,       -- Type of support needed (e.g. physical therapy, sign language interpreter)
    description TEXT,                         -- Description of the support need
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store community activities and events
CREATE TABLE CommunityActivities (
    activity_id SERIAL PRIMARY KEY,           -- Unique identifier for each community activity
    activity_name VARCHAR(100) NOT NULL,     -- Name of the activity
    description TEXT,                         -- Detailed description of the activity
    activity_date DATE NOT NULL,              -- Date of the activity
    location VARCHAR(255) NOT NULL,           -- Location of the activity
    accessibility_features TEXT,               -- Accessibility features available (e.g. ramps, sign language)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to link residents to community activities
CREATE TABLE ResidentActivities (
    resident_activity_id SERIAL PRIMARY KEY,  -- Unique identifier for each resident activity link
    resident_id INT REFERENCES Residents(resident_id) ON DELETE CASCADE,  -- Resident participating
    activity_id INT REFERENCES CommunityActivities(activity_id) ON DELETE CASCADE, -- Community activity
    participation_status VARCHAR(50) NOT NULL, -- Status of participation (e.g. attending, interested)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Error handling
-- Ensure that all foreign key references are properly set up to maintain data integrity.
-- Always check for unique constraints where necessary, especially on email and phone numbers.
-- Implement proper indexing on commonly queried fields like last_name, date_of_birth, and family_member_id for optimization.
```
