"""
Generated Code Metadata:
========================
Original URL: https://gudrus.com
Prompt: Design a database schema for storing information about video courses, tutorials, and user subscriptions on a platform like DeepMarket.
Generated: DETERMINISTIC_8b47d6de24032ed1
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a video course platform like DeepMarket

-- Table to store information about users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about video courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    Title VARCHAR(255) NOT NULL,             -- Title of the course
    Description TEXT,                        -- Detailed description of the course
    InstructorID INT NOT NULL,               -- Foreign key referencing the instructor
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (InstructorID) REFERENCES Users(UserID) ON DELETE CASCADE -- Link to the instructor
);

-- Table to store information about tutorials within a course
CREATE TABLE Tutorials (
    TutorialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tutorial
    CourseID INT NOT NULL,                     -- Foreign key referencing the course
    Title VARCHAR(255) NOT NULL,               -- Title of the tutorial
    VideoURL VARCHAR(2083) NOT NULL,           -- URL of the video
    Duration INT NOT NULL,                     -- Duration of the tutorial in seconds
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the tutorial was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Link to the course
);

-- Table to store user subscriptions to courses
CREATE TABLE Subscriptions (
    SubscriptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subscription
    UserID INT NOT NULL,                           -- Foreign key referencing the user
    CourseID INT NOT NULL,                         -- Foreign key referencing the course
    SubscribedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the subscription was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Link to the user
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Link to the course
);

-- Table to store reviews for courses
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    UserID INT NOT NULL,                     -- Foreign key referencing the user
    CourseID INT NOT NULL,                   -- Foreign key referencing the course
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    Comment TEXT,                            -- Optional comment for the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Link to the user
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Link to the course
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users(Email);
CREATE INDEX idx_course_title ON Courses(Title);
CREATE INDEX idx_tutorial_course ON Tutorials(CourseID);
CREATE INDEX idx_subscription_user_course ON Subscriptions(UserID, CourseID);
CREATE INDEX idx_review_user_course ON Reviews(UserID, CourseID);
```
