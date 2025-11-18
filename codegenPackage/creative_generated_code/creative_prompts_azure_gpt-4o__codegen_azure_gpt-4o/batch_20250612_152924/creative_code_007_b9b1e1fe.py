"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Write a SQL query to store and retrieve tour package information, including themes like Temple Tours and Hill Station Tours, as seen on the "Safar Genie" website.
Generated: DETERMINISTIC_b9b1e1fe6548501e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create table to store tour package information
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,        -- Name of the tour package
    Theme VARCHAR(100) NOT NULL,              -- Theme of the tour package (e.g., Temple Tours, Hill Station Tours)
    Description TEXT,                         -- Detailed description of the tour package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the tour package
    DurationDays INT NOT NULL,                -- Duration of the tour package in days
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the package was last updated
);

-- Insert sample data into the TourPackages table
INSERT INTO TourPackages (PackageName, Theme, Description, Price, DurationDays)
VALUES 
    ('Sacred Temples of India', 'Temple Tours', 'A spiritual journey to the most revered temples in India.', 499.99, 5),
    ('Mystical Hill Retreat', 'Hill Station Tours', 'Relax and rejuvenate in the serene hill stations.', 699.99, 7);

-- Retrieve all tour packages with their details
SELECT 
    PackageID,
    PackageName,
    Theme,
    Description,
    Price,
    DurationDays,
    CreatedAt,
    UpdatedAt
FROM 
    TourPackages;

-- Retrieve tour packages filtered by theme (e.g., Temple Tours)
SELECT 
    PackageID,
    PackageName,
    Theme,
    Description,
    Price,
    DurationDays,
    CreatedAt,
    UpdatedAt
FROM 
    TourPackages
WHERE 
    Theme = 'Temple Tours';

-- Error handling for production scenarios:
-- Ensure proper validation and sanitization of user inputs before inserting or filtering data.
-- Use parameterized queries or prepared statements to avoid SQL injection attacks.
-- Example of a parameterized query in a programming language like Python:
-- cursor.execute("SELECT * FROM TourPackages WHERE Theme = %s", (user_input,))
```
