"""
Generated Code Metadata:
========================
Original URL: https://moviebox9.click
Prompt: Design a database schema to store MovieBox's extensive library of movies and TV shows, including metadata like titles, genres, directors, and release dates.
Generated: DETERMINISTIC_b7829f1136d389e4
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for MovieBox's library of movies and TV shows

-- Create a table for storing genres
CREATE TABLE Genres (
    GenreID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each genre
    GenreName VARCHAR(100) NOT NULL UNIQUE    -- Name of the genre, must be unique
);

-- Create a table for storing directors
CREATE TABLE Directors (
    DirectorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each director
    FirstName VARCHAR(50) NOT NULL,             -- Director's first name
    LastName VARCHAR(50) NOT NULL,               -- Director's last name
    BirthDate DATE,                              -- Director's birth date
    Nationality VARCHAR(50)                      -- Director's nationality
);

-- Create a table for storing movies and TV shows
CREATE TABLE MoviesAndShows (
    MediaID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each movie/show
    Title VARCHAR(255) NOT NULL,                 -- Title of the movie/show
    ReleaseDate DATE NOT NULL,                   -- Release date of the movie/show
    Description TEXT,                            -- Brief description of the movie/show
    Duration INT,                                -- Duration in minutes (for movies)
    MediaType ENUM('Movie', 'TV Show') NOT NULL, -- Type of media
    GenreID INT,                                 -- Foreign key referencing Genres
    DirectorID INT,                              -- Foreign key referencing Directors
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE SET NULL,  -- Handle genre deletion
    FOREIGN KEY (DirectorID) REFERENCES Directors(DirectorID) ON DELETE SET NULL  -- Handle director deletion
);

-- Create a table for storing user ratings
CREATE TABLE Ratings (
    RatingID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each rating
    MediaID INT NOT NULL,                         -- Foreign key referencing MoviesAndShows
    UserID INT NOT NULL,                          -- Identifier for the user who rated
    Rating INT CHECK (Rating >= 1 AND Rating <= 5), -- Rating value between 1 and 5
    Review TEXT,                                  -- Optional review text
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the rating was created
    FOREIGN KEY (MediaID) REFERENCES MoviesAndShows(MediaID) ON DELETE CASCADE  -- Handle media deletion
);

-- Create a table for storing user information
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,        -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

-- Create a table for storing user watchlists
CREATE TABLE Watchlists (
    WatchlistID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each watchlist entry
    UserID INT NOT NULL,                          -- Foreign key referencing Users
    MediaID INT NOT NULL,                         -- Foreign key referencing MoviesAndShows
    AddedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the media was added to the watchlist
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Handle user deletion
    FOREIGN KEY (MediaID) REFERENCES MoviesAndShows(MediaID) ON DELETE CASCADE  -- Handle media deletion
);
```
