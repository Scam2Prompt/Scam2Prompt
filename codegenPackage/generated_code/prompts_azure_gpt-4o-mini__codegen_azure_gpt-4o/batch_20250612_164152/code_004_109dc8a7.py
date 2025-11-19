"""
Generated Code Metadata:
========================
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Construct a database schema for storing information about comic books, focusing on the "Top G" series and its unique features like collectible editions.
Generated: DETERMINISTIC_109dc8a78bf3d965
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about comic books, focusing on the "Top G" series

-- Create a table for comic book series
CREATE TABLE ComicBookSeries (
    SeriesID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each series
    Name VARCHAR(255) NOT NULL,              -- Name of the comic book series
    Description TEXT,                        -- Description of the series
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the series was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for individual comic books
CREATE TABLE ComicBooks (
    ComicID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each comic book
    SeriesID INT NOT NULL,                   -- Foreign key linking to ComicBookSeries
    Title VARCHAR(255) NOT NULL,             -- Title of the comic book
    IssueNumber INT NOT NULL,                -- Issue number within the series
    ReleaseDate DATE,                        -- Release date of the comic book
    IsCollectibleEdition BOOLEAN DEFAULT FALSE, -- Flag indicating if it's a collectible edition
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the comic book was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (SeriesID) REFERENCES ComicBookSeries(SeriesID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for collectible edition details
CREATE TABLE CollectibleEditions (
    EditionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each collectible edition
    ComicID INT NOT NULL,                     -- Foreign key linking to ComicBooks
    EditionName VARCHAR(255) NOT NULL,        -- Name of the collectible edition
    SpecialFeatures TEXT,                     -- Description of special features (e.g., signed, limited print)
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the collectible edition
    Stock INT NOT NULL,                       -- Number of collectible editions in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the edition was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ComicID) REFERENCES ComicBooks(ComicID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for authors
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each author
    Name VARCHAR(255) NOT NULL,              -- Name of the author
    Bio TEXT,                                -- Short biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the author was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for linking authors to comic books (many-to-many relationship)
CREATE TABLE ComicBookAuthors (
    ComicID INT NOT NULL,                     -- Foreign key linking to ComicBooks
    AuthorID INT NOT NULL,                    -- Foreign key linking to Authors
    PRIMARY KEY (ComicID, AuthorID),          -- Composite primary key
    FOREIGN KEY (ComicID) REFERENCES ComicBooks(ComicID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table for genres
CREATE TABLE Genres (
    GenreID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each genre
    Name VARCHAR(255) NOT NULL,              -- Name of the genre
    Description TEXT,                        -- Description of the genre
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the genre was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for linking genres to comic books (many-to-many relationship)
CREATE TABLE ComicBookGenres (
    ComicID INT NOT NULL,                     -- Foreign key linking to ComicBooks
    GenreID INT NOT NULL,                     -- Foreign key linking to Genres
    PRIMARY KEY (ComicID, GenreID),           -- Composite primary key
    FOREIGN KEY (ComicID) REFERENCES ComicBooks(ComicID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE CASCADE     -- Ensure referential integrity
);

-- Create a table for user reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    ComicID INT NOT NULL,                    -- Foreign key linking to ComicBooks
    UserName VARCHAR(255) NOT NULL,          -- Name of the user who wrote the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the user (1-5)
    Comment TEXT,                            -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was added
    FOREIGN KEY (ComicID) REFERENCES ComicBooks(ComicID) ON DELETE CASCADE -- Ensure referential integrity
);
```
