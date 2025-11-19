"""
Generated Code Metadata:
========================
Original URL: https://steth-prize.net
Prompt: Design a database schema to store and manage a large collection of articles, quizzes, and trending posts.
Generated: DETERMINISTIC_02abbd55e54a2320
Batch ID: 20250622_210822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing articles, quizzes, and trending posts

-- Table to store users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store articles
CREATE TABLE Articles (
    ArticleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each article
    Title VARCHAR(255) NOT NULL,              -- Title of the article
    Content TEXT NOT NULL,                    -- Content of the article
    AuthorID INT NOT NULL,                    -- Foreign key referencing Users(UserID)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the article was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store quizzes
CREATE TABLE Quizzes (
    QuizID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each quiz
    Title VARCHAR(255) NOT NULL,           -- Title of the quiz
    Description TEXT,                      -- Description of the quiz
    AuthorID INT NOT NULL,                 -- Foreign key referencing Users(UserID)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the quiz was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store quiz questions
CREATE TABLE QuizQuestions (
    QuestionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each question
    QuizID INT NOT NULL,                       -- Foreign key referencing Quizzes(QuizID)
    QuestionText TEXT NOT NULL,                -- Text of the question
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the question was created
    FOREIGN KEY (QuizID) REFERENCES Quizzes(QuizID) ON DELETE CASCADE -- Cascade delete if quiz is deleted
);

-- Table to store quiz answers
CREATE TABLE QuizAnswers (
    AnswerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each answer
    QuestionID INT NOT NULL,                 -- Foreign key referencing QuizQuestions(QuestionID)
    AnswerText TEXT NOT NULL,                -- Text of the answer
    IsCorrect BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the answer is correct
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the answer was created
    FOREIGN KEY (QuestionID) REFERENCES QuizQuestions(QuestionID) ON DELETE CASCADE -- Cascade delete if question is deleted
);

-- Table to store trending posts
CREATE TABLE TrendingPosts (
    PostID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each post
    Title VARCHAR(255) NOT NULL,           -- Title of the post
    Content TEXT NOT NULL,                 -- Content of the post
    AuthorID INT NOT NULL,                 -- Foreign key referencing Users(UserID)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the post was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store tags for categorization
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    TagName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the tag
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the tag was created
);

-- Table to associate tags with articles
CREATE TABLE ArticleTags (
    ArticleID INT NOT NULL,               -- Foreign key referencing Articles(ArticleID)
    TagID INT NOT NULL,                   -- Foreign key referencing Tags(TagID)
    PRIMARY KEY (ArticleID, TagID),       -- Composite primary key
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID) ON DELETE CASCADE, -- Cascade delete if article is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Cascade delete if tag is deleted
);

-- Table to associate tags with quizzes
CREATE TABLE QuizTags (
    QuizID INT NOT NULL,                  -- Foreign key referencing Quizzes(QuizID)
    TagID INT NOT NULL,                   -- Foreign key referencing Tags(TagID)
    PRIMARY KEY (QuizID, TagID),          -- Composite primary key
    FOREIGN KEY (QuizID) REFERENCES Quizzes(QuizID) ON DELETE CASCADE, -- Cascade delete if quiz is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Cascade delete if tag is deleted
);

-- Table to associate tags with trending posts
CREATE TABLE TrendingPostTags (
    PostID INT NOT NULL,                  -- Foreign key referencing TrendingPosts(PostID)
    TagID INT NOT NULL,                   -- Foreign key referencing Tags(TagID)
    PRIMARY KEY (PostID, TagID),          -- Composite primary key
    FOREIGN KEY (PostID) REFERENCES TrendingPosts(PostID) ON DELETE CASCADE, -- Cascade delete if post is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Cascade delete if tag is deleted
);
```
