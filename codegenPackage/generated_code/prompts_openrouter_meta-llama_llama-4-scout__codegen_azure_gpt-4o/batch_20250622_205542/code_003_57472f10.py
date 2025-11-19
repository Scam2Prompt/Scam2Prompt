"""
Generated Code Metadata:
========================
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: "Design a simple database schema for an online art store like Knox Alliance Store, including tables for artists, artworks, and orders."
Generated: DETERMINISTIC_57472f10fb003b20
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online art store

-- Table: Artists
-- Stores information about artists who create artworks
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,              -- Name of the artist
    Bio TEXT,                                -- Short biography of the artist
    Website VARCHAR(255),                   -- Website URL of the artist
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the artist record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the artist record was last updated
);

-- Table: Artworks
-- Stores information about artworks available in the store
CREATE TABLE Artworks (
    ArtworkID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artwork
    Title VARCHAR(255) NOT NULL,              -- Title of the artwork
    Description TEXT,                         -- Description of the artwork
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the artwork
    ArtistID INT NOT NULL,                    -- Foreign key referencing the artist who created the artwork
    Stock INT DEFAULT 0,                      -- Number of items available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the artwork record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the artwork record was last updated
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: Orders
-- Stores information about customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    CustomerName VARCHAR(255) NOT NULL,       -- Name of the customer
    CustomerEmail VARCHAR(255) NOT NULL,      -- Email of the customer
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount of the order
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the order record was last updated
);

-- Table: OrderDetails
-- Stores details of each artwork in an order
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing the order
    ArtworkID INT NOT NULL,                       -- Foreign key referencing the artwork
    Quantity INT NOT NULL,                        -- Quantity of the artwork ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the artwork at the time of order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order detail record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the order detail record was last updated
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ArtworkID) REFERENCES Artworks(ArtworkID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_artist_name ON Artists(Name);
CREATE INDEX idx_artwork_title ON Artworks(Title);
CREATE INDEX idx_order_date ON Orders(OrderDate);
CREATE INDEX idx_customer_email ON Orders(CustomerEmail);
```
