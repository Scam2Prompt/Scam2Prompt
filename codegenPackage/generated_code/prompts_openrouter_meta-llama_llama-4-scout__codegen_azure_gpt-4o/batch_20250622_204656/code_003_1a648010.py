"""
Generated Code Metadata:
========================
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: "Design a database schema to store information about glass products, including product types, materials, and dimensions, inspired by the product offerings on the Maryart website."
Generated: DETERMINISTIC_1a6480100eae495d
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about glass products

-- Table to store product types (e.g., vase, bowl, plate, etc.)
CREATE TABLE ProductTypes (
    ProductTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for product type
<<<<<<< HEAD
    Name VARCHAR(100) NOT NULL,                   -- Name of the product type
=======
    Name VARCHAR(255) NOT NULL,                   -- Name of the product type
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    Description TEXT                              -- Optional description of the product type
);

-- Table to store materials used in glass products (e.g., glass, crystal, etc.)
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for material
<<<<<<< HEAD
    Name VARCHAR(100) NOT NULL,                   -- Name of the material
=======
    Name VARCHAR(255) NOT NULL,                   -- Name of the material
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    Description TEXT                              -- Optional description of the material
);

-- Table to store glass products
CREATE TABLE GlassProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the product
    Name VARCHAR(255) NOT NULL,                   -- Name of the product
    ProductTypeID INT NOT NULL,                   -- Foreign key referencing ProductTypes
    MaterialID INT NOT NULL,                      -- Foreign key referencing Materials
<<<<<<< HEAD
    Height DECIMAL(10, 2) NULL,                   -- Height of the product in cm (optional)
    Width DECIMAL(10, 2) NULL,                    -- Width of the product in cm (optional)
    Depth DECIMAL(10, 2) NULL,                    -- Depth of the product in cm (optional)
    Weight DECIMAL(10, 2) NULL,                   -- Weight of the product in kg (optional)
=======
    Height DECIMAL(10, 2) NULL,                   -- Height of the product in cm
    Width DECIMAL(10, 2) NULL,                    -- Width of the product in cm
    Depth DECIMAL(10, 2) NULL,                    -- Depth of the product in cm
    Weight DECIMAL(10, 2) NULL,                   -- Weight of the product in kg
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    Description TEXT,                             -- Optional description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductTypeID) REFERENCES ProductTypes(ProductTypeID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the image
    ProductID INT NOT NULL,                       -- Foreign key referencing GlassProducts
    ImageURL VARCHAR(2083) NOT NULL,              -- URL of the image
<<<<<<< HEAD
    AltText VARCHAR(255) NULL,                    -- Alternative text for the image
=======
    AltText VARCHAR(255),                         -- Alternative text for the image
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp when the image was added
    FOREIGN KEY (ProductID) REFERENCES GlassProducts(ProductID) ON DELETE CASCADE
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the review
    ProductID INT NOT NULL,                       -- Foreign key referencing GlassProducts
    ReviewerName VARCHAR(255) NOT NULL,           -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating (1 to 5 stars)
<<<<<<< HEAD
    Comment TEXT NULL,                            -- Optional review comment
=======
    Comment TEXT,                                 -- Optional review comment
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp when the review was added
    FOREIGN KEY (ProductID) REFERENCES GlassProducts(ProductID) ON DELETE CASCADE
);

<<<<<<< HEAD
-- Table to store product tags (e.g., "handmade", "decorative", etc.)
CREATE TABLE Tags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for the tag
    Name VARCHAR(100) NOT NULL UNIQUE,            -- Name of the tag
    Description TEXT NULL                         -- Optional description of the tag
);

-- Table to associate tags with products (many-to-many relationship)
CREATE TABLE ProductTags (
    ProductID INT NOT NULL,                       -- Foreign key referencing GlassProducts
    TagID INT NOT NULL,                           -- Foreign key referencing Tags
    PRIMARY KEY (ProductID, TagID),               -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES GlassProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE
);
=======
-- Indexes for optimizing queries
CREATE INDEX idx_product_name ON GlassProducts(Name);
CREATE INDEX idx_material_name ON Materials(Name);
CREATE INDEX idx_product_type_name ON ProductTypes(Name);
CREATE INDEX idx_image_product_id ON ProductImages(ProductID);
CREATE INDEX idx_review_product_id ON ProductReviews(ProductID);
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
