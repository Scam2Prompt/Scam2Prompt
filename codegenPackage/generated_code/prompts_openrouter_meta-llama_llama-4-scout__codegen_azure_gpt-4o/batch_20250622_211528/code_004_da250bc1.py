"""
Generated Code Metadata:
========================
Original URL: https://brocoflix.xyz
Prompt: Design a basic database schema for a streaming platform similar to BrocoFlix, including tables for movies, TV shows, user ratings, and content trending status.
Generated: DETERMINISTIC_da250bc157c03f39
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a streaming platform similar to BrocoFlix

-- Table to store information about movies
CREATE TABLE Movies (
    MovieID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each movie
    Title VARCHAR(255) NOT NULL,            -- Title of the movie
    ReleaseDate DATE,                       -- Release date of the movie
    Genre VARCHAR(100),                     -- Genre of the movie
    Duration INT,                           -- Duration of the movie in minutes
    Description TEXT,                       -- Brief description of the movie
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about TV shows
CREATE TABLE TVShows (
    ShowID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each TV show
    Title VARCHAR(255) NOT NULL,           -- Title of the TV show
    ReleaseDate DATE,                      -- Release date of the TV show
    Genre VARCHAR(100),                    -- Genre of the TV show
    Seasons INT,                           -- Number of seasons
    Episodes INT,                          -- Total number of episodes
    Description TEXT,                      -- Brief description of the TV show
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store user ratings for movies and TV shows
CREATE TABLE UserRatings (
    RatingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each rating
    UserID INT NOT NULL,                     -- ID of the user who provided the rating
    ContentType ENUM('Movie', 'TVShow') NOT NULL, -- Type of content being rated
    ContentID INT NOT NULL,                  -- ID of the movie or TV show being rated
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating value (1 to 5)
    Review TEXT,                             -- Optional user review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ContentID) REFERENCES Movies(MovieID) ON DELETE CASCADE, -- Foreign key for movies
    FOREIGN KEY (ContentID) REFERENCES TVShows(ShowID) ON DELETE CASCADE -- Foreign key for TV shows
);

-- Table to track trending status of content
CREATE TABLE TrendingStatus (
    TrendingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for trending status
    ContentType ENUM('Movie', 'TVShow') NOT NULL, -- Type of content
    ContentID INT NOT NULL,                  -- ID of the movie or TV show
    IsTrending BOOLEAN DEFAULT FALSE,        -- Whether the content is trending
    TrendingScore INT DEFAULT 0,             -- Score indicating the popularity of the content
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ContentID) REFERENCES Movies(MovieID) ON DELETE CASCADE, -- Foreign key for movies
    FOREIGN KEY (ContentID) REFERENCES TVShows(ShowID) ON DELETE CASCADE -- Foreign key for TV shows
);

-- Table to store user information (optional, for completeness)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(100) NOT NULL UNIQUE, -- Username of the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Indexes for optimizing queries
CREATE INDEX idx_movies_genre ON Movies(Genre);
CREATE INDEX idx_tvshows_genre ON TVShows(Genre);
CREATE INDEX idx_user_ratings_content ON UserRatings(ContentType, ContentID);
CREATE INDEX idx_trending_status_content ON TrendingStatus(ContentType, ContentID);
```
