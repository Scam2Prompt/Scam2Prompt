"""
Generated Code Metadata:
========================
Original URL: https://claim-originether.org
Prompt: Design a database schema for a multi-language news website.
Generated: DETERMINISTIC_619aa1ba9521bda9
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a multi-language news website

-- Table to store users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store languages
CREATE TABLE Languages (
    LanguageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each language
    LanguageCode VARCHAR(10) NOT NULL UNIQUE,  -- ISO language code (e.g., 'en', 'fr', 'es')
    LanguageName VARCHAR(50) NOT NULL          -- Full name of the language (e.g., 'English', 'French')
);

-- Table to store categories for news articles
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE, -- Name of the category (e.g., 'Technology', 'Sports')
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store news articles
CREATE TABLE Articles (
    ArticleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each article
    AuthorID INT NOT NULL,                     -- Foreign key referencing Users(UserID)
    CategoryID INT NOT NULL,                   -- Foreign key referencing Categories(CategoryID)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the article was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Set category to NULL if deleted
);

-- Table to store translations of articles
CREATE TABLE ArticleTranslations (
    TranslationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each translation
    ArticleID INT NOT NULL,                       -- Foreign key referencing Articles(ArticleID)
    LanguageID INT NOT NULL,                      -- Foreign key referencing Languages(LanguageID)
    Title VARCHAR(255) NOT NULL,                  -- Title of the article in the specific language
    Content TEXT NOT NULL,                        -- Content of the article in the specific language
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID) ON DELETE CASCADE, -- Cascade delete if article is deleted
    FOREIGN KEY (LanguageID) REFERENCES Languages(LanguageID) ON DELETE CASCADE -- Cascade delete if language is deleted
);

-- Table to store comments on articles
CREATE TABLE Comments (
    CommentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comment
    ArticleID INT NOT NULL,                   -- Foreign key referencing Articles(ArticleID)
    UserID INT NOT NULL,                      -- Foreign key referencing Users(UserID)
    Content TEXT NOT NULL,                    -- Content of the comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the comment was created
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID) ON DELETE CASCADE, -- Cascade delete if article is deleted
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store tags for articles
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    TagName VARCHAR(50) NOT NULL UNIQUE   -- Name of the tag (e.g., 'AI', 'Politics')
);

-- Table to associate tags with articles
CREATE TABLE ArticleTags (
    ArticleID INT NOT NULL,               -- Foreign key referencing Articles(ArticleID)
    TagID INT NOT NULL,                   -- Foreign key referencing Tags(TagID)
    PRIMARY KEY (ArticleID, TagID),       -- Composite primary key to ensure unique associations
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID) ON DELETE CASCADE, -- Cascade delete if article is deleted
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE -- Cascade delete if tag is deleted
);
```
