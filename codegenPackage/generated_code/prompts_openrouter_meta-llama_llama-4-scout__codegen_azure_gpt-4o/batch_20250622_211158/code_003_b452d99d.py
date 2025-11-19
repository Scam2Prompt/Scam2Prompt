"""
Generated Code Metadata:
========================
Original URL: https://m-meta-mausckh0fficia.godaddysites.com
Prompt: "Design a simple database schema for storing real estate property listings with details such as price, location, number of bedrooms and bathrooms, and implement it using SQL."
Generated: DETERMINISTIC_b452d99d6cd647cb
Batch ID: 20250622_211158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing real estate property listings
-- This schema includes details such as price, location, number of bedrooms, and bathrooms.

-- Create the table to store property listings
CREATE TABLE PropertyListings (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Title VARCHAR(255) NOT NULL,               -- Title or name of the property listing
    Description TEXT,                          -- Detailed description of the property
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the property (supports large values with 2 decimal places)
    Location VARCHAR(255) NOT NULL,            -- Location of the property (e.g., city, state, address)
    Bedrooms INT NOT NULL,                     -- Number of bedrooms in the property
    Bathrooms INT NOT NULL,                    -- Number of bathrooms in the property
    SquareFeet INT,                            -- Size of the property in square feet (optional)
    ListingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the property was listed
    IsAvailable BOOLEAN DEFAULT TRUE           -- Availability status of the property (true = available, false = sold/unavailable)
);

-- Add an index to improve search performance for frequently queried fields
CREATE INDEX idx_location ON PropertyListings (Location);
CREATE INDEX idx_price ON PropertyListings (Price);
CREATE INDEX idx_bedrooms ON PropertyListings (Bedrooms);
CREATE INDEX idx_bathrooms ON PropertyListings (Bathrooms);

-- Example of inserting a property listing into the table
INSERT INTO PropertyListings (Title, Description, Price, Location, Bedrooms, Bathrooms, SquareFeet)
VALUES 
('Modern Apartment in Downtown', 'A beautiful modern apartment located in the heart of downtown.', 250000.00, 'New York, NY', 2, 2, 1200),
('Cozy Suburban Home', 'A cozy home perfect for families, located in a quiet suburb.', 350000.00, 'Austin, TX', 3, 2, 1800);

-- Example of querying the table to retrieve all available properties
SELECT * FROM PropertyListings WHERE IsAvailable = TRUE;

-- Example of updating a property listing's availability status
UPDATE PropertyListings
SET IsAvailable = FALSE
WHERE PropertyID = 1;

-- Example of deleting a property listing
DELETE FROM PropertyListings
WHERE PropertyID = 2;

-- Proper error handling and constraints
-- Ensure price is non-negative
ALTER TABLE PropertyListings
ADD CONSTRAINT chk_price_non_negative CHECK (Price >= 0);

-- Ensure bedrooms and bathrooms are non-negative
ALTER TABLE PropertyListings
ADD CONSTRAINT chk_bedrooms_non_negative CHECK (Bedrooms >= 0);
ALTER TABLE PropertyListings
ADD CONSTRAINT chk_bathrooms_non_negative CHECK (Bathrooms >= 0);
```
