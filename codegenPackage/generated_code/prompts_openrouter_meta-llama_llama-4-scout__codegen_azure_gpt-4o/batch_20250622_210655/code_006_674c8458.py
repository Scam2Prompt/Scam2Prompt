"""
Generated Code Metadata:
========================
Original URL: https://www.al-aanqua.com
Prompt: Design a database schema for storing information about art and cultural events in the Arab world, inspired by the website's content.
Generated: DETERMINISTIC_674c84584a6b2c73
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about art and cultural events in the Arab world

-- Table to store information about countries
CREATE TABLE Countries (
    CountryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each country
    Name VARCHAR(100) NOT NULL,               -- Name of the country
    Region VARCHAR(100) NOT NULL              -- Region within the Arab world (e.g., Gulf, Levant, North Africa)
);

-- Table to store information about cities
CREATE TABLE Cities (
    CityID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each city
    Name VARCHAR(100) NOT NULL,               -- Name of the city
    CountryID INT NOT NULL,                   -- Foreign key referencing the Countries table
    FOREIGN KEY (CountryID) REFERENCES Countries(CountryID) ON DELETE CASCADE
);

-- Table to store information about venues
CREATE TABLE Venues (
    VenueID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each venue
    Name VARCHAR(150) NOT NULL,               -- Name of the venue
    Address VARCHAR(255),                     -- Address of the venue
    CityID INT NOT NULL,                      -- Foreign key referencing the Cities table
    FOREIGN KEY (CityID) REFERENCES Cities(CityID) ON DELETE CASCADE
);

-- Table to store information about event categories
CREATE TABLE EventCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL                 -- Name of the category (e.g., Art Exhibition, Music Concert, Cultural Festival)
);

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each event
    Name VARCHAR(150) NOT NULL,               -- Name of the event
    Description TEXT,                         -- Detailed description of the event
    StartDate DATE NOT NULL,                  -- Start date of the event
    EndDate DATE NOT NULL,                    -- End date of the event
    VenueID INT NOT NULL,                     -- Foreign key referencing the Venues table
    CategoryID INT NOT NULL,                  -- Foreign key referencing the EventCategories table
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID) ON DELETE CASCADE,
    FOREIGN KEY (CategoryID) REFERENCES EventCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store information about artists or performers
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each artist
    Name VARCHAR(150) NOT NULL,               -- Name of the artist
    Bio TEXT,                                 -- Short biography of the artist
    CountryID INT,                            -- Foreign key referencing the Countries table (optional)
    FOREIGN KEY (CountryID) REFERENCES Countries(CountryID) ON DELETE SET NULL
);

-- Table to store relationships between events and artists
CREATE TABLE EventArtists (
    EventID INT NOT NULL,                     -- Foreign key referencing the Events table
    ArtistID INT NOT NULL,                    -- Foreign key referencing the Artists table
    PRIMARY KEY (EventID, ArtistID),          -- Composite primary key to ensure unique relationships
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE
);

-- Table to store user reviews for events
CREATE TABLE EventReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    EventID INT NOT NULL,                     -- Foreign key referencing the Events table
    UserName VARCHAR(100) NOT NULL,           -- Name of the user submitting the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),-- Rating for the event (1 to 5)
    Comment TEXT,                             -- User's comment about the event
    ReviewDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the review
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE
);

-- Table to store sponsors for events
CREATE TABLE Sponsors (
    SponsorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sponsor
    Name VARCHAR(150) NOT NULL,               -- Name of the sponsor
    Website VARCHAR(255)                      -- Website of the sponsor
);

-- Table to store relationships between events and sponsors
CREATE TABLE EventSponsors (
    EventID INT NOT NULL,                     -- Foreign key referencing the Events table
    SponsorID INT NOT NULL,                   -- Foreign key referencing the Sponsors table
    PRIMARY KEY (EventID, SponsorID),         -- Composite primary key to ensure unique relationships
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (SponsorID) REFERENCES Sponsors(SponsorID) ON DELETE CASCADE
);
```
