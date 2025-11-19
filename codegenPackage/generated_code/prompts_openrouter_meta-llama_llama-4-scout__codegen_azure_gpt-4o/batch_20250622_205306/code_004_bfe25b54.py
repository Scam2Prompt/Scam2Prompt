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
-- Database Schema for "Sembrador de Vida" Community Groups

-- Table to store information about community groups
CREATE TABLE CommunityGroups (
    GroupID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each group
    GroupName VARCHAR(255) NOT NULL,        -- Name of the community group
    Description TEXT,                       -- Description of the group
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the group was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about members of the community groups
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    FirstName VARCHAR(255) NOT NULL,         -- First name of the member
    LastName VARCHAR(255) NOT NULL,          -- Last name of the member
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the member
    PhoneNumber VARCHAR(20),                 -- Phone number of the member
    JoinedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the member joined
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store the relationship between members and community groups
CREATE TABLE GroupMembers (
    GroupID INT NOT NULL,                    -- Foreign key referencing CommunityGroups
    MemberID INT NOT NULL,                   -- Foreign key referencing Members
    Role VARCHAR(50),                        -- Role of the member in the group (e.g., Leader, Participant)
    JoinedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the member joined the group
    PRIMARY KEY (GroupID, MemberID),         -- Composite primary key to ensure unique relationships
    FOREIGN KEY (GroupID) REFERENCES CommunityGroups(GroupID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE        -- Cascade delete
);

-- Table to store information about activities organized by community groups
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity
    GroupID INT NOT NULL,                       -- Foreign key referencing CommunityGroups
    ActivityName VARCHAR(255) NOT NULL,         -- Name of the activity
    Description TEXT,                           -- Description of the activity
    ActivityDate DATE NOT NULL,                 -- Date of the activity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the activity was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (GroupID) REFERENCES CommunityGroups(GroupID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store the relationship between members and activities
CREATE TABLE ActivityParticipants (
    ActivityID INT NOT NULL,                   -- Foreign key referencing Activities
    MemberID INT NOT NULL,                     -- Foreign key referencing Members
    ParticipationRole VARCHAR(50),             -- Role of the member in the activity (e.g., Organizer, Attendee)
    PRIMARY KEY (ActivityID, MemberID),        -- Composite primary key to ensure unique relationships
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE         -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_group_name ON CommunityGroups(GroupName);
CREATE INDEX idx_member_email ON Members(Email);
CREATE INDEX idx_activity_date ON Activities(ActivityDate);
```
