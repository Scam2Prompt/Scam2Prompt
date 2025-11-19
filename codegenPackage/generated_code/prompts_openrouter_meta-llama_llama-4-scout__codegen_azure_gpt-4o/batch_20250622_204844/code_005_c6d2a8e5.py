"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Create a SQL query to manage and retrieve listings of franchises for sale, including details like price, location, and industry.
Generated: DETERMINISTIC_c6d2a8e5e8de488b
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store franchise listings
CREATE TABLE FranchiseListings (
    FranchiseID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each franchise
    FranchiseName VARCHAR(255) NOT NULL,        -- Name of the franchise
    Price DECIMAL(15, 2) NOT NULL,              -- Price of the franchise
    Location VARCHAR(255) NOT NULL,             -- Location of the franchise
    Industry VARCHAR(255) NOT NULL,             -- Industry category of the franchise
    Description TEXT,                           -- Optional description of the franchise
    DateListed TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date the franchise was listed
);

-- Insert sample data into the FranchiseListings table
INSERT INTO FranchiseListings (FranchiseName, Price, Location, Industry, Description)
VALUES
('Coffee House', 150000.00, 'New York, NY', 'Food & Beverage', 'A popular coffee franchise in a prime location.'),
('Tech Solutions', 250000.00, 'San Francisco, CA', 'Technology', 'IT services and solutions franchise.'),
('Fitness Center', 100000.00, 'Austin, TX', 'Health & Fitness', 'A well-established gym franchise.'),
('Pet Supplies', 75000.00, 'Seattle, WA', 'Retail', 'Pet supplies and accessories franchise.');

-- Query to retrieve all franchise listings with details
SELECT 
    FranchiseID, 
    FranchiseName, 
    Price, 
    Location, 
    Industry, 
    Description, 
    DateListed
FROM 
    FranchiseListings
ORDER BY 
    DateListed DESC; -- Sort by the most recently listed franchises

-- Query to filter franchises by industry and price range
SELECT 
    FranchiseID, 
    FranchiseName, 
    Price, 
    Location, 
    Industry, 
    Description, 
    DateListed
FROM 
    FranchiseListings
WHERE 
    Industry = 'Food & Beverage' -- Filter by industry
    AND Price BETWEEN 100000 AND 200000 -- Filter by price range
ORDER BY 
    Price ASC; -- Sort by price in ascending order

-- Query to retrieve franchises located in a specific city
SELECT 
    FranchiseID, 
    FranchiseName, 
    Price, 
    Location, 
    Industry, 
    Description, 
    DateListed
FROM 
    FranchiseListings
WHERE 
    Location LIKE '%New York%'; -- Filter by location (partial match for flexibility)

-- Error handling: Ensure the table exists before querying
-- (This is typically handled in application code, but included here for completeness)
SELECT 
    FranchiseID, 
    FranchiseName, 
    Price, 
    Location, 
    Industry, 
    Description, 
    DateListed
FROM 
    FranchiseListings
WHERE 
    EXISTS (
        SELECT 1 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_NAME = 'FranchiseListings'
    );
```
