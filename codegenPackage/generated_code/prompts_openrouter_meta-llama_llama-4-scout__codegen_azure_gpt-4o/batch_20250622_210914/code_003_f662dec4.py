"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: "Design a database schema for storing information about luxury furniture products, including details like material, color, and style, inspired by the product catalog of origines-decoration.com."
Generated: DETERMINISTIC_f662dec4fb5ab817
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about luxury furniture products

-- Table: materials
-- Stores information about the materials used in furniture products
CREATE TABLE materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    name VARCHAR(100) NOT NULL,                 -- Name of the material (e.g., "Wood", "Metal")
    description TEXT                            -- Optional description of the material
);

-- Table: colors
-- Stores information about the available colors for furniture products
CREATE TABLE colors (
    color_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each color
    name VARCHAR(50) NOT NULL,                  -- Name of the color (e.g., "Black", "White")
    hex_code CHAR(7)                            -- Hexadecimal color code (e.g., "#FFFFFF")
);

-- Table: styles
-- Stores information about the styles of furniture products
CREATE TABLE styles (
    style_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each style
    name VARCHAR(100) NOT NULL,                 -- Name of the style (e.g., "Modern", "Vintage")
    description TEXT                            -- Optional description of the style
);

-- Table: furniture_products
-- Stores information about individual furniture products
CREATE TABLE furniture_products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,                 -- Name of the product (e.g., "Luxury Sofa")
    description TEXT,                           -- Detailed description of the product
    price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    material_id INT NOT NULL,                   -- Foreign key referencing the materials table
    color_id INT NOT NULL,                      -- Foreign key referencing the colors table
    style_id INT NOT NULL,                      -- Foreign key referencing the styles table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES colors(color_id) ON DELETE CASCADE,
    FOREIGN KEY (style_id) REFERENCES styles(style_id) ON DELETE CASCADE
);

-- Table: product_images
-- Stores images associated with furniture products
CREATE TABLE product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    product_id INT NOT NULL,                    -- Foreign key referencing the furniture_products table
    image_url VARCHAR(2083) NOT NULL,           -- URL of the image
    alt_text VARCHAR(255),                      -- Alternative text for the image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (product_id) REFERENCES furniture_products(product_id) ON DELETE CASCADE
);

-- Table: product_tags
-- Stores tags associated with furniture products for categorization
CREATE TABLE product_tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each tag
    name VARCHAR(100) NOT NULL                  -- Name of the tag (e.g., "Eco-Friendly", "Handmade")
);

-- Table: product_tag_mapping
-- Maps tags to furniture products (many-to-many relationship)
CREATE TABLE product_tag_mapping (
    product_id INT NOT NULL,                    -- Foreign key referencing the furniture_products table
    tag_id INT NOT NULL,                        -- Foreign key referencing the product_tags table
    PRIMARY KEY (product_id, tag_id),           -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES furniture_products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES product_tags(tag_id) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_material_name ON materials(name);
CREATE INDEX idx_color_name ON colors(name);
CREATE INDEX idx_style_name ON styles(name);
CREATE INDEX idx_product_name ON furniture_products(name);
CREATE INDEX idx_tag_name ON product_tags(name);
```
