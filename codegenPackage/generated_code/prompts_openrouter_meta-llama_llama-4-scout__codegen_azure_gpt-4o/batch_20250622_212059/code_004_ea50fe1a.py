"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Design a database schema to store menu and wine information for a restaurant and winery like Bodega Jean Bousquet, including tables for menu items, wine varieties, and customer reservations.
Generated: DETERMINISTIC_ea50fe1a931b9de1
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a restaurant and winery

-- Table to store menu items
CREATE TABLE MenuItems (
    MenuItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each menu item
    Name VARCHAR(255) NOT NULL,                -- Name of the menu item
    Description TEXT,                          -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the menu item
    Category VARCHAR(100),                     -- Category (e.g., Appetizer, Main Course, Dessert)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the menu item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store wine varieties
CREATE TABLE WineVarieties (
    WineID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each wine
    Name VARCHAR(255) NOT NULL,                -- Name of the wine
    Type VARCHAR(100) NOT NULL,                -- Type of wine (e.g., Red, White, Rosé)
    Year INT,                                  -- Year of production
    Description TEXT,                          -- Description of the wine
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the wine
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the wine was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store customer reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,          -- Email of the customer
    ReservationDate DATE NOT NULL,                -- Date of the reservation
    ReservationTime TIME NOT NULL,                -- Time of the reservation
    NumberOfGuests INT NOT NULL,                  -- Number of guests for the reservation
    SpecialRequests TEXT,                         -- Special requests from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the reservation was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store the relationship between menu items and wine varieties (pairings)
CREATE TABLE MenuWinePairings (
    PairingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each pairing
    MenuItemID INT NOT NULL,                  -- Foreign key referencing MenuItems
    WineID INT NOT NULL,                      -- Foreign key referencing WineVarieties
    Notes TEXT,                               -- Notes about the pairing
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the pairing was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (MenuItemID) REFERENCES MenuItems(MenuItemID) ON DELETE CASCADE,
    FOREIGN KEY (WineID) REFERENCES WineVarieties(WineID) ON DELETE CASCADE
);

-- Indexes for faster querying
CREATE INDEX idx_menu_category ON MenuItems(Category);
CREATE INDEX idx_wine_type ON WineVarieties(Type);
CREATE INDEX idx_reservation_date_time ON Reservations(ReservationDate, ReservationTime);
```
