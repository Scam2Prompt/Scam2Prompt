"""
Generated Code Metadata:
========================
Original URL: https://ifesty.com.br
Prompt: Design a database schema for an online event planning platform like ifesty.com.br, including tables for users, ads, and services offered.
Generated: DETERMINISTIC_d087c05715af2cbf
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online event planning platform

-- Table: Users
-- Stores information about users of the platform
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,    -- Email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    PhoneNumber VARCHAR(20),               -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Ads
-- Stores advertisements posted by users
CREATE TABLE Ads (
    AdID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each ad
    UserID INT NOT NULL,                   -- Foreign key referencing Users table
    Title VARCHAR(255) NOT NULL,           -- Title of the advertisement
    Description TEXT NOT NULL,             -- Detailed description of the ad
    Price DECIMAL(10, 2) NOT NULL,         -- Price for the service or product
    Location VARCHAR(255),                 -- Location where the service is offered
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the ad was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table: Services
-- Stores information about services offered on the platform
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Name of the service
    Description TEXT NOT NULL,                -- Detailed description of the service
    Category VARCHAR(255) NOT NULL,           -- Category of the service (e.g., catering, photography)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: AdServices
-- Many-to-Many relationship between Ads and Services
CREATE TABLE AdServices (
    AdID INT NOT NULL,                        -- Foreign key referencing Ads table
    ServiceID INT NOT NULL,                   -- Foreign key referencing Services table
    PRIMARY KEY (AdID, ServiceID),            -- Composite primary key
    FOREIGN KEY (AdID) REFERENCES Ads(AdID) ON DELETE CASCADE, -- Cascade delete if ad is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Table: UserFavorites
-- Stores information about users' favorite ads
CREATE TABLE UserFavorites (
    FavoriteID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each favorite entry
    UserID INT NOT NULL,                        -- Foreign key referencing Users table
    AdID INT NOT NULL,                          -- Foreign key referencing Ads table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the favorite was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (AdID) REFERENCES Ads(AdID) ON DELETE CASCADE -- Cascade delete if ad is removed
);

-- Table: Reviews
-- Stores reviews for ads posted by users
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    AdID INT NOT NULL,                       -- Foreign key referencing Ads table
    UserID INT NOT NULL,                     -- Foreign key referencing Users table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    Comment TEXT,                            -- Optional comment for the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (AdID) REFERENCES Ads(AdID) ON DELETE CASCADE, -- Cascade delete if ad is removed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(Email); -- Index for quick lookup by email
CREATE INDEX idx_ad_user ON Ads(UserID);     -- Index for quick lookup of ads by user
CREATE INDEX idx_service_category ON Services(Category); -- Index for quick lookup by category
CREATE INDEX idx_favorites_user ON UserFavorites(UserID); -- Index for quick lookup of favorites by user
CREATE INDEX idx_reviews_ad ON Reviews(AdID); -- Index for quick lookup of reviews by ad
```
