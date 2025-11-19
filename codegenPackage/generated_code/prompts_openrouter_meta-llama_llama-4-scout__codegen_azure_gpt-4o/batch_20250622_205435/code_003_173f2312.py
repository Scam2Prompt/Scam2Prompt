"""
Generated Code Metadata:
========================
Original URL: https://sallysui.com
Prompt: Design a basic database schema to store user-generated content and community interactions for a platform like Sally.
Generated: DETERMINISTIC_173f2312535a7b46
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for user-generated content and community interactions

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store user-generated content (e.g., posts)
CREATE TABLE Posts (
    PostID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each post
    UserID INT NOT NULL,                   -- Foreign key referencing the user who created the post
    Title VARCHAR(255) NOT NULL,           -- Title of the post
    Content TEXT NOT NULL,                 -- Content of the post
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the post was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store comments on posts
CREATE TABLE Comments (
    CommentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comment
    PostID INT NOT NULL,                      -- Foreign key referencing the post being commented on
    UserID INT NOT NULL,                      -- Foreign key referencing the user who created the comment
    Content TEXT NOT NULL,                    -- Content of the comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the comment was created
    FOREIGN KEY (PostID) REFERENCES Posts(PostID) ON DELETE CASCADE, -- Cascade delete if post is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store likes on posts
CREATE TABLE PostLikes (
    LikeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each like
    PostID INT NOT NULL,                   -- Foreign key referencing the post being liked
    UserID INT NOT NULL,                   -- Foreign key referencing the user who liked the post
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the like was created
    FOREIGN KEY (PostID) REFERENCES Posts(PostID) ON DELETE CASCADE, -- Cascade delete if post is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    UNIQUE (PostID, UserID) -- Ensure a user can only like a post once
);

-- Table to store likes on comments
CREATE TABLE CommentLikes (
    LikeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each like
    CommentID INT NOT NULL,                -- Foreign key referencing the comment being liked
    UserID INT NOT NULL,                   -- Foreign key referencing the user who liked the comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the like was created
    FOREIGN KEY (CommentID) REFERENCES Comments(CommentID) ON DELETE CASCADE, -- Cascade delete if comment is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    UNIQUE (CommentID, UserID) -- Ensure a user can only like a comment once
);

-- Table to store user followers (social interaction)
CREATE TABLE Followers (
    FollowerID INT NOT NULL, -- Foreign key referencing the user who is following
    FollowedID INT NOT NULL, -- Foreign key referencing the user being followed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the follow relationship was created
    FOREIGN KEY (FollowerID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if follower is deleted
    FOREIGN KEY (FollowedID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if followed user is deleted
    PRIMARY KEY (FollowerID, FollowedID) -- Ensure a user can only follow another user once
);
```
