"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Write a SQL query to design a database schema for storing information about tourist sites in Marchigüe, including details about the windmills, Hacienda Histórica de Marchigüe, and other attractions.
Generated: DETERMINISTIC_b29d61538c5064a3
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing information about tourist sites in Marchigüe
-- This schema includes details about windmills, Hacienda Histórica de Marchigüe, and other attractions.

-- Create the main table for tourist sites
CREATE TABLE TouristSites (
    SiteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each site
    Name VARCHAR(255) NOT NULL,            -- Name of the tourist site
    Description TEXT,                      -- Detailed description of the site
    Location VARCHAR(255),                 -- Location of the site (e.g., address or coordinates)
    Category ENUM('Windmill', 'Hacienda', 'Other') NOT NULL, -- Category of the site
    OpeningHours VARCHAR(255),             -- Opening hours of the site
    EntryFee DECIMAL(10, 2),               -- Entry fee for the site (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for storing images related to tourist sites
CREATE TABLE SiteImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each image
    SiteID INT NOT NULL,                    -- Foreign key referencing the TouristSites table
    ImageURL VARCHAR(2083) NOT NULL,        -- URL of the image
    Caption VARCHAR(255),                   -- Caption or description of the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (SiteID) REFERENCES TouristSites(SiteID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing reviews of tourist sites
CREATE TABLE SiteReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    SiteID INT NOT NULL,                     -- Foreign key referencing the TouristSites table
    ReviewerName VARCHAR(255),               -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating (1 to 5 stars)
    Comment TEXT,                            -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (SiteID) REFERENCES TouristSites(SiteID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing events related to tourist sites
CREATE TABLE SiteEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    SiteID INT NOT NULL,                    -- Foreign key referencing the TouristSites table
    EventName VARCHAR(255) NOT NULL,        -- Name of the event
    EventDate DATE NOT NULL,                -- Date of the event
    Description TEXT,                       -- Detailed description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (SiteID) REFERENCES TouristSites(SiteID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing contact information for tourist sites
CREATE TABLE SiteContacts (
    ContactID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contact
    SiteID INT NOT NULL,                      -- Foreign key referencing the TouristSites table
    PhoneNumber VARCHAR(20),                  -- Phone number for the site
    Email VARCHAR(255),                       -- Email address for the site
    WebsiteURL VARCHAR(2083),                 -- Website URL for the site
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (SiteID) REFERENCES TouristSites(SiteID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Ensure the database schema is optimized and ready for production use.
-- Indexes can be added later based on query performance analysis.
```
