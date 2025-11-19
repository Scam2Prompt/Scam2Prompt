"""
Generated Code Metadata:
========================
Original URL: https://wooflix.click
Prompt: Design a database schema to store and manage the extensive content library of Wooflix, including metadata for movies and TV shows.
Generated: DETERMINISTIC_033a2f11ef5698da
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Wooflix content library

-- Table to store general information about movies and TV shows
CREATE TABLE Content (
    content_id SERIAL PRIMARY KEY, -- Unique identifier for each content item
    title VARCHAR(255) NOT NULL, -- Title of the movie or TV show
    description TEXT, -- Brief description of the content
    release_date DATE, -- Release date of the content
    content_type VARCHAR(50) NOT NULL CHECK (content_type IN ('Movie', 'TV Show')), -- Type of content (Movie or TV Show)
    duration_minutes INT CHECK (duration_minutes > 0), -- Duration in minutes (for movies or episodes)
    language VARCHAR(50), -- Language of the content
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store genres associated with content
CREATE TABLE Genre (
    genre_id SERIAL PRIMARY KEY, -- Unique identifier for each genre
    name VARCHAR(100) NOT NULL UNIQUE -- Name of the genre (e.g., Action, Comedy, Drama)
);

-- Junction table to associate content with multiple genres
CREATE TABLE ContentGenre (
    content_id INT NOT NULL, -- Foreign key referencing Content table
    genre_id INT NOT NULL, -- Foreign key referencing Genre table
    PRIMARY KEY (content_id, genre_id), -- Composite primary key
    FOREIGN KEY (content_id) REFERENCES Content(content_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store cast and crew information
CREATE TABLE Person (
    person_id SERIAL PRIMARY KEY, -- Unique identifier for each person
    name VARCHAR(255) NOT NULL, -- Name of the person
    role VARCHAR(100) NOT NULL CHECK (role IN ('Actor', 'Director', 'Writer', 'Producer')), -- Role of the person
    bio TEXT, -- Brief biography of the person
    birth_date DATE -- Birth date of the person
);

-- Junction table to associate content with cast and crew
CREATE TABLE ContentPerson (
    content_id INT NOT NULL, -- Foreign key referencing Content table
    person_id INT NOT NULL, -- Foreign key referencing Person table
    role_description VARCHAR(255), -- Description of the role (e.g., character name for actors)
    PRIMARY KEY (content_id, person_id), -- Composite primary key
    FOREIGN KEY (content_id) REFERENCES Content(content_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (person_id) REFERENCES Person(person_id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store user ratings and reviews
CREATE TABLE Review (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    content_id INT NOT NULL, -- Foreign key referencing Content table
    user_id INT NOT NULL, -- Foreign key referencing User table (assuming a User table exists)
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5), -- Rating given by the user (1 to 5)
    review_text TEXT, -- Review text provided by the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (content_id) REFERENCES Content(content_id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store seasons for TV shows
CREATE TABLE Season (
    season_id SERIAL PRIMARY KEY, -- Unique identifier for each season
    content_id INT NOT NULL, -- Foreign key referencing Content table
    season_number INT NOT NULL CHECK (season_number > 0), -- Season number
    description TEXT, -- Brief description of the season
    FOREIGN KEY (content_id) REFERENCES Content(content_id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store episodes for TV shows
CREATE TABLE Episode (
    episode_id SERIAL PRIMARY KEY, -- Unique identifier for each episode
    season_id INT NOT NULL, -- Foreign key referencing Season table
    title VARCHAR(255) NOT NULL, -- Title of the episode
    description TEXT, -- Brief description of the episode
    episode_number INT NOT NULL CHECK (episode_number > 0), -- Episode number within the season
    duration_minutes INT CHECK (duration_minutes > 0), -- Duration in minutes
    release_date DATE, -- Release date of the episode
    FOREIGN KEY (season_id) REFERENCES Season(season_id) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for performance optimization
CREATE INDEX idx_content_title ON Content(title);
CREATE INDEX idx_genre_name ON Genre(name);
CREATE INDEX idx_person_name ON Person(name);
CREATE INDEX idx_review_rating ON Review(rating);
CREATE INDEX idx_season_number ON Season(season_number);
CREATE INDEX idx_episode_number ON Episode(episode_number);
```
