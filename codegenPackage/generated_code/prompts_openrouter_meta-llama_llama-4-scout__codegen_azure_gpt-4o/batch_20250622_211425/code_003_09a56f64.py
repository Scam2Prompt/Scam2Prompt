"""
Generated Code Metadata:
========================
Original URL: https://iteamworldwide.com
Prompt: "Design a database schema to store information about USANA products, their features, and customer testimonials, as seen on iTeamWorldwide.com."
Generated: DETERMINISTIC_09a56f64fc68f641
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about USANA products, their features, and customer testimonials

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Category VARCHAR(100),                    -- Category of the product (e.g., supplements, skincare)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store product features
CREATE TABLE ProductFeatures (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feature
    ProductID INT NOT NULL,                   -- Foreign key referencing the Products table
    FeatureDescription TEXT NOT NULL,         -- Description of the feature
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the feature was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure features are deleted if the product is deleted
);

-- Create a table to store customer testimonials
CREATE TABLE Testimonials (
    TestimonialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each testimonial
    ProductID INT NOT NULL,                       -- Foreign key referencing the Products table
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer providing the testimonial
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Customer rating (1 to 5 stars)
    Comment TEXT,                                 -- Customer's testimonial comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the testimonial was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure testimonials are deleted if the product is deleted
);

-- Create indexes for faster querying
CREATE INDEX idx_product_name ON Products(Name); -- Index on product name for quick search
CREATE INDEX idx_testimonial_rating ON Testimonials(Rating); -- Index on rating for filtering testimonials
```
