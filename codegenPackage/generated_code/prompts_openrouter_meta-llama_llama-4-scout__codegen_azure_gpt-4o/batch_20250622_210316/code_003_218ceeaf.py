"""
Generated Code Metadata:
========================
Original URL: https://mollinari.com.pl
Prompt: Design a database schema for storing information about a restaurant like Mollinari, including tables for menu items, reservations, and customer reviews.
Generated: DETERMINISTIC_218ceeafc78a901d
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Restaurant Management System

-- Table: Restaurants
-- Stores basic information about the restaurant
CREATE TABLE Restaurants (
    RestaurantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the restaurant
    Name VARCHAR(255) NOT NULL,                  -- Name of the restaurant
    Address VARCHAR(255) NOT NULL,               -- Address of the restaurant
    PhoneNumber VARCHAR(15),                     -- Contact number
    Email VARCHAR(255),                          -- Email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: MenuItems
-- Stores information about menu items offered by the restaurant
CREATE TABLE MenuItems (
    MenuItemID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the menu item
    RestaurantID INT NOT NULL,                   -- Foreign key referencing Restaurants table
    Name VARCHAR(255) NOT NULL,                  -- Name of the menu item
    Description TEXT,                            -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the menu item
    IsAvailable BOOLEAN DEFAULT TRUE,           -- Availability status of the menu item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID) ON DELETE CASCADE
);

-- Table: Reservations
-- Stores information about reservations made by customers
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the reservation
    RestaurantID INT NOT NULL,                    -- Foreign key referencing Restaurants table
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer
    CustomerPhone VARCHAR(15) NOT NULL,           -- Contact number of the customer
    ReservationDate DATE NOT NULL,                -- Date of the reservation
    ReservationTime TIME NOT NULL,                -- Time of the reservation
    NumberOfGuests INT NOT NULL,                  -- Number of guests for the reservation
    SpecialRequests TEXT,                         -- Special requests from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID) ON DELETE CASCADE
);

-- Table: CustomerReviews
-- Stores reviews provided by customers for the restaurant
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the review
    RestaurantID INT NOT NULL,                   -- Foreign key referencing Restaurants table
    CustomerName VARCHAR(255) NOT NULL,          -- Name of the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                             -- Review text provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_restaurant_name ON Restaurants(Name);
CREATE INDEX idx_menuitem_name ON MenuItems(Name);
CREATE INDEX idx_reservation_date ON Reservations(ReservationDate);
CREATE INDEX idx_review_rating ON CustomerReviews(Rating);
```
