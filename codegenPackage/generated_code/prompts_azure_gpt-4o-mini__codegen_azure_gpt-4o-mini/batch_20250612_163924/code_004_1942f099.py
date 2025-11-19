"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Design a database schema for storing information about commercial properties for sale, including fields for type of business, location, and price, inspired by the lighting store listing.
Generated: DETERMINISTIC_1942f099297cb395
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about commercial properties for sale

CREATE TABLE Property (
    PropertyID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each property
    BusinessType VARCHAR(100) NOT NULL,        -- Type of business (e.g., retail, office, etc.)
    Location VARCHAR(255) NOT NULL,            -- Location of the property
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the property
    Description TEXT,                           -- Optional description of the property
    DateListed DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time when the property was listed
    Status ENUM('Available', 'Under Contract', 'Sold') DEFAULT 'Available', -- Current status of the property
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Index for faster searching by BusinessType and Location
CREATE INDEX idx_business_location ON Property (BusinessType, Location);

-- Sample data insertion (for testing purposes)
INSERT INTO Property (BusinessType, Location, Price, Description)
VALUES 
    ('Lighting Store', '123 Main St, Anytown, USA', 250000.00, 'A well-established lighting store with a loyal customer base.'),
    ('Office Space', '456 Elm St, Anytown, USA', 500000.00, 'Modern office space located in the city center.'),
    ('Retail Store', '789 Oak St, Anytown, USA', 300000.00, 'Prime retail location with high foot traffic.');

-- Query to retrieve all properties for sale
SELECT * FROM Property WHERE Status = 'Available';

-- Query to update the status of a property
UPDATE Property 
SET Status = 'Under Contract' 
WHERE PropertyID = ?; -- Replace ? with the actual PropertyID

-- Query to delete a property (if needed)
DELETE FROM Property 
WHERE PropertyID = ?; -- Replace ? with the actual PropertyID
```
