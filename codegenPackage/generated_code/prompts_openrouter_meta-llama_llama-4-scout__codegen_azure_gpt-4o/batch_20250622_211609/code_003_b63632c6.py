"""
Generated Code Metadata:
========================
Original URL: https://fansliebe.com
Prompt: "Design a database schema for a social media platform with user subscriptions, content flagging, and private messaging, inspired by Fansliebe's features."
Generated: DETERMINISTIC_b63632c66e0b20bf
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a social media platform with user subscriptions, content flagging, and private messaging

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE, -- Unique username
    Email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address
    PasswordHash VARCHAR(255) NOT NULL, -- Hashed password for security
    ProfilePictureURL VARCHAR(255), -- URL to the user's profile picture
    Bio TEXT, -- User's bio
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to manage subscriptions between users
CREATE TABLE Subscriptions (
    SubscriptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subscription
    SubscriberID INT NOT NULL, -- User who is subscribing
    SubscribedToID INT NOT NULL, -- User being subscribed to
    SubscribedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Subscription timestamp
    FOREIGN KEY (SubscriberID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (SubscribedToID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store posts created by users
CREATE TABLE Posts (
    PostID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each post
    UserID INT NOT NULL, -- User who created the post
    Content TEXT NOT NULL, -- Post content
    MediaURL VARCHAR(255), -- URL to any media attached to the post
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Post creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to manage content flagging
CREATE TABLE ContentFlags (
    FlagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each flag
    PostID INT NOT NULL, -- Post being flagged
    FlaggedByID INT NOT NULL, -- User who flagged the post
    Reason TEXT NOT NULL, -- Reason for flagging
    FlaggedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Flagging timestamp
    FOREIGN KEY (PostID) REFERENCES Posts(PostID) ON DELETE CASCADE, -- Cascade delete if post is deleted
    FOREIGN KEY (FlaggedByID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to manage private messages between users
CREATE TABLE PrivateMessages (
    MessageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each message
    SenderID INT NOT NULL, -- User who sent the message
    ReceiverID INT NOT NULL, -- User who received the message
    MessageContent TEXT NOT NULL, -- Content of the message
    SentAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Message sent timestamp
    FOREIGN KEY (SenderID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if sender is deleted
    FOREIGN KEY (ReceiverID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if receiver is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_subscriptions ON Subscriptions(SubscriberID, SubscribedToID);
CREATE INDEX idx_posts_user ON Posts(UserID);
CREATE INDEX idx_flags_post ON ContentFlags(PostID);
CREATE INDEX idx_messages_sender_receiver ON PrivateMessages(SenderID, ReceiverID);
```
