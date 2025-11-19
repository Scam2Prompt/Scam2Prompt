"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Design a database schema for a platform that stores and manages art, music, and creative projects, using Kroo Nation's services as a reference.
Generated: DETERMINISTIC_b8a1d7985e153340
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a platform that stores and manages art, music, and creative projects

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    ProfilePictureURL VARCHAR(255),        -- URL to the user's profile picture
    Bio TEXT,                              -- Short biography of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store creative projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    UserID INT NOT NULL,                      -- Foreign key referencing the user who created the project
    Title VARCHAR(100) NOT NULL,              -- Title of the project
    Description TEXT,                         -- Detailed description of the project
    Category ENUM('Art', 'Music', 'Other') NOT NULL, -- Category of the project
    ThumbnailURL VARCHAR(255),               -- URL to the project's thumbnail image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store media files associated with projects
CREATE TABLE MediaFiles (
    MediaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each media file
    ProjectID INT NOT NULL,                 -- Foreign key referencing the project
    FileURL VARCHAR(255) NOT NULL,          -- URL to the media file
    FileType ENUM('Image', 'Audio', 'Video') NOT NULL, -- Type of media file
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the media file was uploaded
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is deleted
);

-- Table to store comments on projects
CREATE TABLE Comments (
    CommentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comment
    ProjectID INT NOT NULL,                   -- Foreign key referencing the project
    UserID INT NOT NULL,                      -- Foreign key referencing the user who made the comment
    Content TEXT NOT NULL,                    -- Content of the comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the comment was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store likes on projects
CREATE TABLE Likes (
    LikeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each like
    ProjectID INT NOT NULL,                -- Foreign key referencing the project
    UserID INT NOT NULL,                   -- Foreign key referencing the user who liked the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the like was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    UNIQUE (ProjectID, UserID) -- Ensure a user can only like a project once
);

-- Table to store tags for projects
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    Name VARCHAR(50) NOT NULL UNIQUE      -- Name of the tag
);

-- Table to associate tags with projects
CREATE TABLE ProjectTags (
    ProjectID INT NOT NULL,               -- Foreign key referencing the project
    TagID INT NOT NULL,                   -- Foreign key referencing the tag
    PRIMARY KEY (ProjectID, TagID),       -- Composite primary key to ensure unique association
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Cascade delete if tag is deleted
);

-- Table to store followers (user-to-user relationships)
CREATE TABLE Followers (
    FollowerID INT NOT NULL,              -- Foreign key referencing the user who is following
    FollowedID INT NOT NULL,              -- Foreign key referencing the user being followed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the follow relationship was created
    PRIMARY KEY (FollowerID, FollowedID), -- Composite primary key to ensure unique relationship
    FOREIGN KEY (FollowerID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if follower is deleted
    FOREIGN KEY (FollowedID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if followed user is deleted
);
```
