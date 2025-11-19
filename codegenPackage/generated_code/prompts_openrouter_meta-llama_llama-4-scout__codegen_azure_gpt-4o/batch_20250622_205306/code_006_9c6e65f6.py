"""
Generated Code Metadata:
========================
Original URL: https://woopytee.com
Prompt: "Design a database schema to store information about t-shirts, including their designs, prices, and categories, similar to WoopyTee's product catalog."
Generated: DETERMINISTIC_9c6e65f6952d6f4c
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about t-shirts, their designs, prices, and categories

-- Table to store t-shirt categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category (e.g., "Men", "Women", "Kids")
    Description TEXT                           -- Optional description of the category
);

-- Table to store t-shirt designs
CREATE TABLE Designs (
    DesignID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each design
    Name VARCHAR(255) NOT NULL,                -- Name of the design (e.g., "Abstract Art", "Funny Quote")
    ImageURL VARCHAR(2083) NOT NULL,           -- URL to the design image
    Description TEXT                           -- Optional description of the design
);

-- Table to store t-shirt products
CREATE TABLE TShirts (
    TShirtID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each t-shirt
    Name VARCHAR(255) NOT NULL,                -- Name of the t-shirt (e.g., "Classic Tee")
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the t-shirt
    Stock INT NOT NULL DEFAULT 0,              -- Number of t-shirts available in stock
    CategoryID INT NOT NULL,                   -- Foreign key referencing Categories table
    DesignID INT NOT NULL,                     -- Foreign key referencing Designs table
    Size ENUM('XS', 'S', 'M', 'L', 'XL', 'XXL') NOT NULL, -- Available sizes
    Color VARCHAR(50) NOT NULL,                -- Color of the t-shirt
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the t-shirt was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE, -- Cascade delete for category
    FOREIGN KEY (DesignID) REFERENCES Designs(DesignID) ON DELETE CASCADE         -- Cascade delete for design
);

-- Table to store customer reviews for t-shirts
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    TShirtID INT NOT NULL,                     -- Foreign key referencing TShirts table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    Comment TEXT,                              -- Optional comment provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was added
    FOREIGN KEY (TShirtID) REFERENCES TShirts(TShirtID) ON DELETE CASCADE -- Cascade delete for t-shirt
);

-- Indexes for optimizing queries
CREATE INDEX idx_category_name ON Categories(Name);
CREATE INDEX idx_design_name ON Designs(Name);
CREATE INDEX idx_tshirt_name ON TShirts(Name);
CREATE INDEX idx_tshirt_price ON TShirts(Price);
CREATE INDEX idx_review_rating ON Reviews(Rating);
```
