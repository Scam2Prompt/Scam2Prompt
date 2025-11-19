"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: "Design a database schema for an art studio that stores information about artists, sculptures, paintings, and other creative products, and provide a sample query to retrieve product details."
Generated: DETERMINISTIC_1997dd7f3a2570bc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an art studio

-- Create a table for artists
CREATE TABLE Artists (
    artist_id SERIAL PRIMARY KEY, -- Unique identifier for each artist
    name VARCHAR(100) NOT NULL, -- Name of the artist
    bio TEXT, -- Biography of the artist
    date_of_birth DATE, -- Date of birth of the artist
    nationality VARCHAR(50) -- Nationality of the artist
);

-- Create a table for sculptures
CREATE TABLE Sculptures (
    sculpture_id SERIAL PRIMARY KEY, -- Unique identifier for each sculpture
    title VARCHAR(100) NOT NULL, -- Title of the sculpture
    artist_id INT REFERENCES Artists(artist_id) ON DELETE CASCADE, -- Foreign key referencing Artists
    material VARCHAR(50), -- Material used for the sculpture
    height DECIMAL(5,2), -- Height of the sculpture in meters
    width DECIMAL(5,2), -- Width of the sculpture in meters
    depth DECIMAL(5,2), -- Depth of the sculpture in meters
    created_at DATE -- Date when the sculpture was created
);

-- Create a table for paintings
CREATE TABLE Paintings (
    painting_id SERIAL PRIMARY KEY, -- Unique identifier for each painting
    title VARCHAR(100) NOT NULL, -- Title of the painting
    artist_id INT REFERENCES Artists(artist_id) ON DELETE CASCADE, -- Foreign key referencing Artists
    medium VARCHAR(50), -- Medium used for the painting (e.g., oil, acrylic)
    dimensions VARCHAR(50), -- Dimensions of the painting (e.g., 24x36 inches)
    created_at DATE -- Date when the painting was created
);

-- Create a table for other creative products
CREATE TABLE CreativeProducts (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(100) NOT NULL, -- Name of the product
    artist_id INT REFERENCES Artists(artist_id) ON DELETE CASCADE, -- Foreign key referencing Artists
    product_type VARCHAR(50), -- Type of product (e.g., print, digital art)
    price DECIMAL(10,2), -- Price of the product
    created_at DATE -- Date when the product was created
);

-- Sample query to retrieve product details along with artist information
SELECT 
    p.product_id,
    p.name AS product_name,
    p.product_type,
    p.price,
    a.name AS artist_name,
    a.nationality AS artist_nationality
FROM 
    CreativeProducts p
JOIN 
    Artists a ON p.artist_id = a.artist_id
WHERE 
    p.price > 100; -- Example condition to filter products by price
```
