"""
Generated Code Metadata:
========================
Original URL: https://whitecasino.net
Prompt: Design a database schema to store information about various online casinos, their games, and user reviews, inspired by WhiteCasino.net's content and features.
Generated: DETERMINISTIC_bb7dc23d346ba6c7
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about online casinos, their games, and user reviews

-- Table to store information about online casinos
CREATE TABLE Casinos (
    CasinoID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each casino
    Name VARCHAR(255) NOT NULL,              -- Name of the casino
    WebsiteURL VARCHAR(255) NOT NULL,        -- URL of the casino's website
    Country VARCHAR(100),                    -- Country where the casino operates
    EstablishedYear INT,                     -- Year the casino was established
    LicenseInfo VARCHAR(255),                -- Licensing information
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about games offered by casinos
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each game
    CasinoID INT NOT NULL,                   -- Foreign key referencing Casinos table
    Name VARCHAR(255) NOT NULL,              -- Name of the game
    Type VARCHAR(100),                       -- Type of the game (e.g., Slot, Poker, Blackjack)
    Provider VARCHAR(255),                   -- Game provider (e.g., NetEnt, Microgaming)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE -- Cascade delete if casino is removed
);

-- Table to store user reviews for casinos
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    CasinoID INT NOT NULL,                   -- Foreign key referencing Casinos table
    UserName VARCHAR(255) NOT NULL,          -- Name of the user who submitted the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the user (1 to 5)
    Comment TEXT,                            -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE -- Cascade delete if casino is removed
);

-- Table to store user reviews for games
CREATE TABLE GameReviews (
    GameReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game review
    GameID INT NOT NULL,                         -- Foreign key referencing Games table
    UserName VARCHAR(255) NOT NULL,              -- Name of the user who submitted the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the user (1 to 5)
    Comment TEXT,                                -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Cascade delete if game is removed
);

-- Table to store additional features or bonuses offered by casinos
CREATE TABLE CasinoFeatures (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feature
    CasinoID INT NOT NULL,                    -- Foreign key referencing Casinos table
    FeatureName VARCHAR(255) NOT NULL,        -- Name of the feature (e.g., Welcome Bonus, Free Spins)
    Description TEXT,                         -- Description of the feature
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE -- Cascade delete if casino is removed
);

-- Table to store payment methods supported by casinos
CREATE TABLE PaymentMethods (
    PaymentMethodID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment method
    CasinoID INT NOT NULL,                          -- Foreign key referencing Casinos table
    MethodName VARCHAR(255) NOT NULL,               -- Name of the payment method (e.g., Visa, PayPal)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE -- Cascade delete if casino is removed
);

-- Table to store supported currencies for casinos
CREATE TABLE SupportedCurrencies (
    CurrencyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each currency
    CasinoID INT NOT NULL,                     -- Foreign key referencing Casinos table
    CurrencyCode VARCHAR(10) NOT NULL,         -- Currency code (e.g., USD, EUR)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CasinoID) REFERENCES Casinos(CasinoID) ON DELETE CASCADE -- Cascade delete if casino is removed
);
```
