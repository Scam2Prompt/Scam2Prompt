"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: Create a database schema to store member profiles, event details, and subscription statuses for a social-first networking platform like Sync Connects.
Generated: DETERMINISTIC_8517a6eda86b8309
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Sync Connects platform

-- Create the database
CREATE DATABASE SyncConnects;

-- Switch to the new database
USE SyncConnects;

-- Table to store member profiles
CREATE TABLE MemberProfiles (
    member_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    username VARCHAR(50) NOT NULL UNIQUE,      -- Unique username for the member
    email VARCHAR(100) NOT NULL UNIQUE,         -- Unique email address for the member
    password_hash VARCHAR(255) NOT NULL,        -- Hashed password for security
    profile_picture VARCHAR(255),                -- URL to the member's profile picture
    bio TEXT,                                    -- Optional bio for the member
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the account was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the profile was last updated
);

-- Table to store event details
CREATE TABLE Events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL,           -- Name of the event
    event_description TEXT,                       -- Description of the event
    event_date DATETIME NOT NULL,                -- Date and time of the event
    location VARCHAR(255),                        -- Location of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the event was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the event was last updated
);

-- Table to store subscription statuses for members
CREATE TABLE Subscriptions (
    subscription_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subscription
    member_id INT NOT NULL,                         -- ID of the member who is subscribed
    event_id INT NOT NULL,                          -- ID of the event the member is subscribed to
    status ENUM('active', 'inactive', 'canceled') NOT NULL, -- Status of the subscription
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the subscription was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the subscription was last updated
    FOREIGN KEY (member_id) REFERENCES MemberProfiles(member_id) ON DELETE CASCADE, -- Foreign key constraint to ensure referential integrity
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE -- Foreign key constraint to ensure referential integrity
);

-- Indexing for performance optimization
CREATE INDEX idx_member_username ON MemberProfiles(username);
CREATE INDEX idx_event_date ON Events(event_date);
CREATE INDEX idx_subscription_member ON Subscriptions(member_id);
CREATE INDEX idx_subscription_event ON Subscriptions(event_id);
```
