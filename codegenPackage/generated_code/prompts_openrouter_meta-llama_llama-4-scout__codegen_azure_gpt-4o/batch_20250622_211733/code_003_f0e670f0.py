"""
Generated Code Metadata:
========================
Original URL: https://tekanslotcepat.site
Prompt: Design a database schema for storing game information, including slots, live casino, and togel, on a platform like Tekanslot, ensuring support for multiple game providers.
Generated: DETERMINISTIC_f0e670f03d6ff446
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing game information on a platform like Tekanslot
-- Supports multiple game types (slots, live casino, togel) and multiple game providers

-- Table to store game providers
CREATE TABLE GameProviders (
    ProviderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each provider
    Name VARCHAR(255) NOT NULL,                -- Name of the provider
    WebsiteURL VARCHAR(255),                   -- Optional URL for the provider's website
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the provider was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store game categories (e.g., Slots, Live Casino, Togel)
CREATE TABLE GameCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL UNIQUE,         -- Name of the category (e.g., Slots, Live Casino, Togel)
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store individual games
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each game
    Name VARCHAR(255) NOT NULL,                -- Name of the game
    ProviderID INT NOT NULL,                   -- Foreign key referencing GameProviders
    CategoryID INT NOT NULL,                   -- Foreign key referencing GameCategories
    Description TEXT,                          -- Optional description of the game
    ReleaseDate DATE,                          -- Optional release date of the game
    IsActive BOOLEAN DEFAULT TRUE,             -- Indicates if the game is active on the platform
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the game was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProviderID) REFERENCES GameProviders(ProviderID) ON DELETE CASCADE,
    FOREIGN KEY (CategoryID) REFERENCES GameCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store game metadata (e.g., RTP, volatility, etc.)
CREATE TABLE GameMetadata (
    MetadataID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each metadata entry
    GameID INT NOT NULL,                       -- Foreign key referencing Games
    Key VARCHAR(255) NOT NULL,                 -- Metadata key (e.g., RTP, Volatility)
    Value VARCHAR(255) NOT NULL,               -- Metadata value (e.g., 96.5%, High)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the metadata was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE
);

-- Table to store game images (e.g., thumbnails, banners)
CREATE TABLE GameImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image entry
    GameID INT NOT NULL,                       -- Foreign key referencing Games
    ImageURL VARCHAR(255) NOT NULL,            -- URL of the image
    Type ENUM('thumbnail', 'banner', 'other') NOT NULL, -- Type of image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE
);

-- Table to store game availability by region (optional feature)
CREATE TABLE GameAvailability (
    AvailabilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each availability entry
    GameID INT NOT NULL,                           -- Foreign key referencing Games
    Region VARCHAR(255) NOT NULL,                 -- Region where the game is available (e.g., US, EU, Asia)
    IsAvailable BOOLEAN DEFAULT TRUE,             -- Indicates if the game is available in the region
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the availability was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_provider_name ON GameProviders(Name);
CREATE INDEX idx_category_name ON GameCategories(Name);
CREATE INDEX idx_game_name ON Games(Name);
CREATE INDEX idx_metadata_key ON GameMetadata(Key);
CREATE INDEX idx_image_type ON GameImages(Type);
CREATE INDEX idx_availability_region ON GameAvailability(Region);
```
