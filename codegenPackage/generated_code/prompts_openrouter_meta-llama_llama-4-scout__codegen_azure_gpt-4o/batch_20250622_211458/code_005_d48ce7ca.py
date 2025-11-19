"""
Generated Code Metadata:
========================
Original URL: https://ether-pool.org
Prompt: Create a mockup of a database schema to store classified ads data, considering the variety of categories and features offered on Kleinanzeigen.
Generated: DETERMINISTIC_d48ce7ca1cb925d6
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing classified ads data on Kleinanzeigen

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    PhoneNumber VARCHAR(15),               -- Optional phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store categories for classified ads
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL UNIQUE,         -- Name of the category (e.g., "Vehicles", "Real Estate")
    Description TEXT,                          -- Optional description of the category
    ParentCategoryID INT,                      -- Parent category for hierarchical structure (NULL if top-level)
    FOREIGN KEY (ParentCategoryID) REFERENCES Categories(CategoryID) -- Self-referencing foreign key
);

-- Table to store classified ads
CREATE TABLE Ads (
    AdID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each ad
    UserID INT NOT NULL,                      -- Reference to the user who posted the ad
    CategoryID INT NOT NULL,                  -- Reference to the category of the ad
    Title VARCHAR(255) NOT NULL,              -- Title of the ad
    Description TEXT NOT NULL,                -- Detailed description of the ad
    Price DECIMAL(10, 2),                     -- Price of the item/service (NULL if not applicable)
    Location VARCHAR(255),                    -- Location of the item/service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Ad creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    IsActive BOOLEAN DEFAULT TRUE,            -- Flag to indicate if the ad is active
    FOREIGN KEY (UserID) REFERENCES Users(UserID), -- Foreign key to Users table
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) -- Foreign key to Categories table
);

-- Table to store images associated with ads
CREATE TABLE AdImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each image
    AdID INT NOT NULL,                        -- Reference to the ad the image belongs to
    ImageURL VARCHAR(255) NOT NULL,           -- URL of the image
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Image upload timestamp
    FOREIGN KEY (AdID) REFERENCES Ads(AdID)   -- Foreign key to Ads table
);

-- Table to store user messages related to ads
CREATE TABLE Messages (
    MessageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each message
    SenderID INT NOT NULL,                    -- Reference to the user who sent the message
    ReceiverID INT NOT NULL,                  -- Reference to the user who received the message
    AdID INT NOT NULL,                        -- Reference to the ad the message is about
    Content TEXT NOT NULL,                    -- Content of the message
    SentAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Message sent timestamp
    FOREIGN KEY (SenderID) REFERENCES Users(UserID), -- Foreign key to Users table
    FOREIGN KEY (ReceiverID) REFERENCES Users(UserID), -- Foreign key to Users table
    FOREIGN KEY (AdID) REFERENCES Ads(AdID)   -- Foreign key to Ads table
);

-- Table to store ad favorites for users
CREATE TABLE Favorites (
    FavoriteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each favorite entry
    UserID INT NOT NULL,                       -- Reference to the user who favorited the ad
    AdID INT NOT NULL,                         -- Reference to the ad that was favorited
    FavoritedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the ad was favorited
    FOREIGN KEY (UserID) REFERENCES Users(UserID), -- Foreign key to Users table
    FOREIGN KEY (AdID) REFERENCES Ads(AdID),   -- Foreign key to Ads table
    UNIQUE(UserID, AdID)                       -- Ensure a user can favorite an ad only once
);

-- Table to store ad views for analytics
CREATE TABLE AdViews (
    ViewID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each view entry
    AdID INT NOT NULL,                        -- Reference to the ad that was viewed
    UserID INT,                               -- Reference to the user who viewed the ad (NULL for anonymous views)
    ViewedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the ad was viewed
    FOREIGN KEY (AdID) REFERENCES Ads(AdID),  -- Foreign key to Ads table
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Foreign key to Users table
);
```
