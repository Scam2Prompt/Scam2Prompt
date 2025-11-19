"""
Generated Code Metadata:
========================
Original URL: https://ahopefulme.com
Prompt: Design a database schema for a social network with tables for users, groups, posts, and events, inspired by the features of Hopeful Me.
Generated: DETERMINISTIC_dbeae515dec502f1
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a social network

-- Table: Users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    FullName VARCHAR(100),                 -- Full name of the user
    Bio TEXT,                              -- Short biography of the user
    ProfilePictureURL VARCHAR(255),        -- URL to the user's profile picture
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Groups
CREATE TABLE Groups (
    GroupID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each group
    GroupName VARCHAR(100) NOT NULL UNIQUE, -- Unique name for the group
    Description TEXT,                       -- Description of the group
    CreatedBy INT NOT NULL,                 -- UserID of the creator (foreign key)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the group was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table: Posts
CREATE TABLE Posts (
    PostID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each post
    UserID INT NOT NULL,                   -- UserID of the author (foreign key)
    GroupID INT,                           -- GroupID if the post belongs to a group (foreign key)
    Content TEXT NOT NULL,                 -- Content of the post
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the post was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (GroupID) REFERENCES Groups(GroupID) ON DELETE SET NULL -- Set GroupID to NULL if group is deleted
);

-- Table: Events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,        -- Name of the event
    Description TEXT,                       -- Description of the event
    EventDate DATETIME NOT NULL,            -- Date and time of the event
    CreatedBy INT NOT NULL,                 -- UserID of the creator (foreign key)
    GroupID INT,                            -- GroupID if the event is associated with a group (foreign key)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CreatedBy) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (GroupID) REFERENCES Groups(GroupID) ON DELETE SET NULL -- Set GroupID to NULL if group is deleted
);

-- Table: UserGroups (Many-to-Many relationship between Users and Groups)
CREATE TABLE UserGroups (
    UserID INT NOT NULL,                   -- UserID (foreign key)
    GroupID INT NOT NULL,                  -- GroupID (foreign key)
    JoinedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user joined the group
    PRIMARY KEY (UserID, GroupID),         -- Composite primary key
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (GroupID) REFERENCES Groups(GroupID) ON DELETE CASCADE -- Cascade delete if group is deleted
);

-- Table: EventParticipants (Many-to-Many relationship between Users and Events)
CREATE TABLE EventParticipants (
    UserID INT NOT NULL,                   -- UserID (foreign key)
    EventID INT NOT NULL,                  -- EventID (foreign key)
    RSVPStatus ENUM('Yes', 'No', 'Maybe') DEFAULT 'Maybe', -- RSVP status of the user
    JoinedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user joined the event
    PRIMARY KEY (UserID, EventID),         -- Composite primary key
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Cascade delete if event is deleted
);
```
