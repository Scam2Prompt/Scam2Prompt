"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eyemagazine.gr
Prompt: Create a database schema to store information about optometry-related events, such as AthenaVision 2025 and ZEUS+DIONE boutique openings, as described on Eye Magazine.
Generated: DETERMINISTIC_26b287db63451619
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready database schema for optometry-related events using SQL:

```sql
-- Optometry Events Database Schema
-- This schema is designed to store information related to optometry events, ensuring scalability and proper normalization.

-- Table to store event information
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each event
    Name VARCHAR(255) NOT NULL,                   -- Name of the event
    Description TEXT,                             -- Detailed description of the event
    Location VARCHAR(255),                        -- Location where the event is held
    StartDate DATE NOT NULL,                      -- Start date of the event
    EndDate DATE,                                 -- End date of the event (Optional if single-day event)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store categories/types of events
CREATE TABLE EventCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL UNIQUE,            -- Name of the category (e.g., Conference, Boutique Opening)
    Description TEXT                              -- Description of the category
);

-- Table to associate events with categories (many-to-many relationship)
CREATE TABLE EventCategoryMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the mapping
    EventID INT NOT NULL,                         -- Foreign key referencing Events
    CategoryID INT NOT NULL,                      -- Foreign key referencing EventCategories
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete ensures mappings are removed when an event is deleted
    FOREIGN KEY (CategoryID) REFERENCES EventCategories(CategoryID) ON DELETE CASCADE -- Cascade delete ensures mappings are removed when a category is deleted
);

-- Table to store media assets related to events
CREATE TABLE EventMedia (
    MediaID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each media asset
    EventID INT NOT NULL,                         -- Foreign key referencing Events
    MediaURL VARCHAR(2083) NOT NULL,              -- URL for the media asset
    MediaType ENUM('Image', 'Video', 'Document') NOT NULL, -- Type of media
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp when the media asset is created
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Cascade delete ensures media assets are removed when an event is deleted
);

-- Table to store sponsors related to events
CREATE TABLE EventSponsors (
    SponsorID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each sponsor
    Name VARCHAR(255) NOT NULL,                   -- Name of the sponsor
    WebsiteURL VARCHAR(2083),                     -- Sponsor's website URL
    Description TEXT                              -- Description of the sponsor
);

-- Table to associate sponsors with events (many-to-many relationship)
CREATE TABLE EventSponsorMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the mapping
    EventID INT NOT NULL,                         -- Foreign key referencing Events
    SponsorID INT NOT NULL,                       -- Foreign key referencing EventSponsors
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete ensures mappings are removed when an event is deleted
    FOREIGN KEY (SponsorID) REFERENCES EventSponsors(SponsorID) ON DELETE CASCADE -- Cascade delete ensures mappings are removed when a sponsor is deleted
);

-- Table to store attendees for events
CREATE TABLE EventAttendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each attendee
    EventID INT NOT NULL,                         -- Foreign key referencing Events
    Name VARCHAR(255) NOT NULL,                   -- Name of the attendee
    Email VARCHAR(255) NOT NULL UNIQUE,           -- Email of the attendee
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the attendee registered
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Cascade delete ensures attendees are removed when an event is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_event_name ON Events(Name);      -- Index for faster searching by event name
CREATE INDEX idx_category_name ON EventCategories(Name); -- Index for faster searching by category name
CREATE INDEX idx_sponsor_name ON EventSponsors(Name); -- Index for faster searching by sponsor name

-- Error Handling and Best Practices
-- Ensure proper constraints and defaults are in place (e.g., NOT NULL, ENUM validations)
-- Use CASCADE to maintain referential integrity during deletions

-- End of schema
```

This schema is designed with normalization, scalability, and data integrity in mind. It includes cascading relationships for efficient cleanup of dependent data while maintaining performance with indexes.
