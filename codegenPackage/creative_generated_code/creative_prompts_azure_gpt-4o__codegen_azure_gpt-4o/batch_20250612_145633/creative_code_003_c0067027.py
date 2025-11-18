"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megami.live
Prompt: Develop a database schema for organizing a VOD platform's catalog of Japanese martial arts movies, including fields for genre, choreography style, and combat techniques.
Generated: DETERMINISTIC_c00670270fb55fa8
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for VOD platform's catalog of Japanese martial arts movies

-- Table to store genres of movies
CREATE TABLE Genres (
    GenreID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each genre
    GenreName VARCHAR(100) NOT NULL UNIQUE, -- Name of the genre (e.g., Samurai, Ninja, Historical)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the genre was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store choreography styles
CREATE TABLE ChoreographyStyles (
    StyleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each choreography style
    StyleName VARCHAR(100) NOT NULL UNIQUE, -- Name of the choreography style (e.g., Swordplay, Hand-to-Hand, Acrobatics)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the style was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store combat techniques
CREATE TABLE CombatTechniques (
    TechniqueID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each combat technique
    TechniqueName VARCHAR(100) NOT NULL UNIQUE, -- Name of the combat technique (e.g., Iaido, Ninjutsu, Judo)
    Description TEXT, -- Description of the technique (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the technique was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store the catalog of movies
CREATE TABLE Movies (
    MovieID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each movie
    Title VARCHAR(255) NOT NULL, -- Title of the movie
    ReleaseYear INT NOT NULL, -- Year the movie was released
    Director VARCHAR(255), -- Name of the director (optional)
    GenreID INT NOT NULL, -- Genre of the movie (FK from Genres)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the movie was added to the system
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    CONSTRAINT FK_Genre FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) 
        ON DELETE CASCADE ON UPDATE CASCADE -- Enforce valid genre relationships
);

-- Table to associate movies with choreography styles
CREATE TABLE MovieChoreographyStyles (
    MovieID INT NOT NULL, -- Associated movie (FK from Movies)
    StyleID INT NOT NULL, -- Associated choreography style (FK from ChoreographyStyles)
    PRIMARY KEY (MovieID, StyleID), -- Composite primary key to prevent duplicates
    CONSTRAINT FK_Movie FOREIGN KEY (MovieID) REFERENCES Movies(MovieID) 
        ON DELETE CASCADE ON UPDATE CASCADE, -- Enforce valid movie relationships
    CONSTRAINT FK_Style FOREIGN KEY (StyleID) REFERENCES ChoreographyStyles(StyleID) 
        ON DELETE CASCADE ON UPDATE CASCADE -- Enforce valid style relationships
);

-- Table to associate movies with combat techniques
CREATE TABLE MovieCombatTechniques (
    MovieID INT NOT NULL, -- Associated movie (FK from Movies)
    TechniqueID INT NOT NULL, -- Associated combat technique (FK from CombatTechniques)
    PRIMARY KEY (MovieID, TechniqueID), -- Composite primary key to prevent duplicates
    CONSTRAINT FK_Movie_Combat FOREIGN KEY (MovieID) REFERENCES Movies(MovieID) 
        ON DELETE CASCADE ON UPDATE CASCADE, -- Enforce valid movie relationships
    CONSTRAINT FK_Technique FOREIGN KEY (TechniqueID) REFERENCES CombatTechniques(TechniqueID) 
        ON DELETE CASCADE ON UPDATE CASCADE -- Enforce valid technique relationships
);

-- Optional: Indexes for faster search and queries
CREATE INDEX idx_movie_title ON Movies (Title);
CREATE INDEX idx_genre_name ON Genres (GenreName);
CREATE INDEX idx_choreography_name ON ChoreographyStyles (StyleName);
CREATE INDEX idx_combat_technique_name ON CombatTechniques (TechniqueName);
```
