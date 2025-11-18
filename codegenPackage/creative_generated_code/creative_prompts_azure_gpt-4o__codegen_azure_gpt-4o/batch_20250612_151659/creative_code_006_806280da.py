"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahopefulme.com
Prompt: Develop a database schema for a platform like HopefulMe, including tables for users, posts, events, group chats, and e-book downloads.
Generated: DETERMINISTIC_806280da24360aa3
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a platform similar to HopefulMe

-- Table: Users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email of the user, must be unique
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    ProfilePictureURL VARCHAR(255),        -- Optional URL for profile picture
    Bio TEXT,                              -- Optional short bio of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: Posts
CREATE TABLE Posts (
    PostID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each post
    UserID INT NOT NULL,                   -- Foreign key for the user who created the post
    Title VARCHAR(100) NOT NULL,           -- Title of the post
    Content TEXT NOT NULL,                 -- Content of the post
    ImageURL VARCHAR(255),                 -- Optional URL for an image in the post
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Post creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: Events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    UserID INT NOT NULL,                    -- Foreign key for the organizer of the event
    EventName VARCHAR(100) NOT NULL,        -- Name of the event
    Description TEXT NOT NULL,              -- Description of the event
    EventDate DATETIME NOT NULL,            -- Date and time of the event
    Location VARCHAR(255),                  -- Optional location of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Event creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: GroupChats
CREATE TABLE GroupChats (
    GroupChatID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the group chat
    AdminUserID INT NOT NULL,                   -- Foreign key for the admin user of the group chat
    GroupName VARCHAR(100) NOT NULL,            -- Name of the group chat
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Group chat creation timestamp
    FOREIGN KEY (AdminUserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: GroupChatMessages
CREATE TABLE GroupChatMessages (
    MessageID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each message
    GroupChatID INT NOT NULL,                  -- Foreign key for the group chat
    SenderUserID INT NOT NULL,                 -- Foreign key for the sender of the message
    MessageContent TEXT NOT NULL,              -- Content of the message
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Message creation timestamp
    FOREIGN KEY (GroupChatID) REFERENCES GroupChats(GroupChatID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (SenderUserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: EBookDownloads
CREATE TABLE EBookDownloads (
    DownloadID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the download record
    UserID INT NOT NULL,                       -- Foreign key for the user downloading the e-book
    EBookTitle VARCHAR(100) NOT NULL,          -- Title of the e-book
    DownloadDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Download timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes and constraints for optimization
CREATE INDEX idx_UserID_Posts ON Posts(UserID);
CREATE INDEX idx_UserID_Events ON Events(UserID);
CREATE INDEX idx_AdminUserID_GroupChats ON GroupChats(AdminUserID);
CREATE INDEX idx_UserID_EBookDownloads ON EBookDownloads(UserID);
```
