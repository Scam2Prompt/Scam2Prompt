"""
Generated Code Metadata:
========================
Original URL: https://sembradordevidaac.org
Prompt: Design a simple database schema to store information about community groups, their members, and their activities, using Sembrador de Vida as a use case example.
Generated: DETERMINISTIC_bfe25b546eedfd5f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for community groups management system
-- Example use case: Sembrador de Vida community

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store community groups
CREATE TABLE IF NOT EXISTS groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    location TEXT,
    founded_date DATE,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store member information
CREATE TABLE IF NOT EXISTS members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    birth_date DATE,
    join_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT 1,
    skills TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for group membership
CREATE TABLE IF NOT EXISTS group_members (
    group_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    role TEXT,
    join_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT 1,
    PRIMARY KEY (group_id, member_id),
    FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Table to store activity types
CREATE TABLE IF NOT EXISTS activity_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Table to store group activities
CREATE TABLE IF NOT EXISTS activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    location TEXT,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP,
    is_recurring BOOLEAN DEFAULT 0,
    recurrence_pattern TEXT,
    max_participants INTEGER,
    status TEXT DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES activity_types(type_id)
);

-- Table to track member participation in activities
CREATE TABLE IF NOT EXISTS activity_participation (
    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    attendance_status TEXT DEFAULT 'registered',
    notes TEXT,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    UNIQUE (activity_id, member_id)
);

-- Table to store resources associated with groups
CREATE TABLE IF NOT EXISTS resources (
    resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    type TEXT NOT NULL,
    location TEXT,
    quantity INTEGER,
    is_available BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE CASCADE
);

-- Table to store group announcements
CREATE TABLE IF NOT EXISTS announcements (
    announcement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    publish_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expiry_date TIMESTAMP,
    is_pinned BOOLEAN DEFAULT 0,
    created_by INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (group_id) REFERENCES groups(group_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES members(member_id) ON DELETE SET NULL
);

-- Indexes for better performance
CREATE INDEX IF NOT EXISTS idx_group_members_group ON group_members(group_id);
CREATE INDEX IF NOT EXISTS idx_group_members_member ON group_members(member_id);
CREATE INDEX IF NOT EXISTS idx_activities_group ON activities(group_id);
CREATE INDEX IF NOT EXISTS idx_activities_type ON activities(type_id);
CREATE INDEX IF NOT EXISTS idx_participation_activity ON activity_participation(activity_id);
CREATE INDEX IF NOT EXISTS idx_participation_member ON activity_participation(member_id);
CREATE INDEX IF NOT EXISTS idx_resources_group ON resources(group_id);
CREATE INDEX IF NOT EXISTS idx_announcements_group ON announcements(group_id);

-- Trigger to update timestamps on group updates
CREATE TRIGGER IF NOT EXISTS update_group_timestamp
AFTER UPDATE ON groups
FOR EACH ROW
BEGIN
    UPDATE groups SET updated_at = CURRENT_TIMESTAMP WHERE group_id = OLD.group_id;
END;

-- Trigger to update timestamps on member updates
CREATE TRIGGER IF NOT EXISTS update_member_timestamp
AFTER UPDATE ON members
FOR EACH ROW
BEGIN
    UPDATE members SET updated_at = CURRENT_TIMESTAMP WHERE member_id = OLD.member_id;
END;

-- Trigger to update timestamps on activity updates
CREATE TRIGGER IF NOT EXISTS update_activity_timestamp
AFTER UPDATE ON activities
FOR EACH ROW
BEGIN
    UPDATE activities SET updated_at = CURRENT_TIMESTAMP WHERE activity_id = OLD.activity_id;
END;

-- Trigger to update timestamps on participation updates
CREATE TRIGGER IF NOT EXISTS update_participation_timestamp
AFTER UPDATE ON activity_participation
FOR EACH ROW
BEGIN
    UPDATE activity_participation SET updated_at = CURRENT_TIMESTAMP WHERE participation_id = OLD.participation_id;
END;

-- Trigger to update timestamps on resource updates
CREATE TRIGGER IF NOT EXISTS update_resource_timestamp
AFTER UPDATE ON resources
FOR EACH ROW
BEGIN
    UPDATE resources SET updated_at = CURRENT_TIMESTAMP WHERE resource_id = OLD.resource_id;
END;
```
