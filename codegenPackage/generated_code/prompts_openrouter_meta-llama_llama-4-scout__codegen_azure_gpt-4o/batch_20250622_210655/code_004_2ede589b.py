"""
Generated Code Metadata:
========================
Original URL: https://restauranteycoffeeshopsancarlos.com
Prompt: Create a SQL database schema to store information about restaurant locations, menus, and orders for a chain of restaurants including Restaurante y Coffee Shop San Carlos in Guatemala.
Generated: DETERMINISTIC_2ede589ba418732f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a restaurant chain database

-- Create a database
CREATE DATABASE RestaurantChain;

-- Use the created database
USE RestaurantChain;

-- Table to store restaurant locations
CREATE TABLE Restaurants (
    RestaurantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each restaurant
    Name VARCHAR(255) NOT NULL,                  -- Name of the restaurant
    Address VARCHAR(255) NOT NULL,               -- Address of the restaurant
    City VARCHAR(100) NOT NULL,                  -- City where the restaurant is located
    Country VARCHAR(100) NOT NULL,               -- Country where the restaurant is located
    PhoneNumber VARCHAR(20),                     -- Contact phone number
    OpeningHours VARCHAR(255)                    -- Opening hours of the restaurant
);

-- Table to store menu items
CREATE TABLE MenuItems (
    MenuItemID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each menu item
    RestaurantID INT NOT NULL,                   -- Foreign key to associate menu item with a restaurant
    Name VARCHAR(255) NOT NULL,                  -- Name of the menu item
    Description TEXT,                            -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the menu item
    Category VARCHAR(100),                       -- Category of the menu item (e.g., Appetizer, Main Course, Dessert)
    IsAvailable BOOLEAN DEFAULT TRUE,            -- Availability status of the menu item
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID) ON DELETE CASCADE
);

-- Table to store customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each order
    RestaurantID INT NOT NULL,                   -- Foreign key to associate order with a restaurant
    OrderDate DATETIME NOT NULL,                 -- Date and time when the order was placed
    CustomerName VARCHAR(255) NOT NULL,          -- Name of the customer who placed the order
    CustomerPhone VARCHAR(20),                   -- Contact phone number of the customer
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount of the order
    Status VARCHAR(50) DEFAULT 'Pending',        -- Status of the order (e.g., Pending, Completed, Cancelled)
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID) ON DELETE CASCADE
);

-- Table to store order details (items in an order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key to associate order detail with an order
    MenuItemID INT NOT NULL,                      -- Foreign key to associate order detail with a menu item
    Quantity INT NOT NULL,                        -- Quantity of the menu item ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the menu item at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (MenuItemID) REFERENCES MenuItems(MenuItemID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_restaurant_city ON Restaurants (City);
CREATE INDEX idx_menuitem_category ON MenuItems (Category);
CREATE INDEX idx_order_status ON Orders (Status);

-- Error handling and constraints
-- Ensure that price and quantity are positive values
ALTER TABLE MenuItems ADD CONSTRAINT chk_price_positive CHECK (Price > 0);
ALTER TABLE OrderDetails ADD CONSTRAINT chk_quantity_positive CHECK (Quantity > 0);
ALTER TABLE OrderDetails ADD CONSTRAINT chk_price_positive_order CHECK (Price > 0);
```
