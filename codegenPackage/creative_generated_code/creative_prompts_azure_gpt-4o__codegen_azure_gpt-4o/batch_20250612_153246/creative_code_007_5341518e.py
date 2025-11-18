"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visitabroadtravels.com.np
Prompt: Write a SQL query to store and retrieve travel package details (e.g., peak climbing and cultural heritage tours) offered by "Visit Abroad Travels" in a database.
Generated: DETERMINISTIC_5341518e5584cb9b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for Visit Abroad Travels
CREATE DATABASE VisitAbroadTravels;

-- Use the newly created database
USE VisitAbroadTravels;

-- Create a table to store travel package details
CREATE TABLE TravelPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each travel package
    PackageName VARCHAR(255) NOT NULL,                 -- Name of the travel package
    Description TEXT NOT NULL,                         -- Detailed description of the travel package
    Category VARCHAR(100),                             -- Type of package (e.g., Peak Climbing, Cultural Heritage)
    DurationDays INT NOT NULL,                         -- Duration of the package in days
    Price DECIMAL(10, 2) NOT NULL,                     -- Cost of the package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Insert sample data into the TravelPackages table
INSERT INTO TravelPackages (PackageName, Description, Category, DurationDays, Price)
VALUES 
('Everest Base Camp Trek', 'A thrilling trek to the Everest Base Camp in Nepal.', 'Peak Climbing', 14, 1200.00),
('Bhutan Cultural Tour', 'Experience Bhutan\'s rich culture and heritage.', 'Cultural Heritage', 7, 800.00),
('Machu Picchu Adventure', 'Explore the ancient Inca citadel of Machu Picchu.', 'Cultural Heritage', 5, 1000.00),
('Island Peak Climbing', 'A challenging climb to Island Peak in Nepal.', 'Peak Climbing', 12, 1500.00);

-- Query to retrieve travel package details
SELECT 
    PackageID,
    PackageName,
    Description,
    Category,
    DurationDays,
    Price,
    CreatedAt,
    UpdatedAt
FROM 
    TravelPackages
ORDER BY 
    PackageName ASC; -- Order results alphabetically by package name

-- Query to retrieve travel packages based on a specific category (e.g., Peak Climbing)
SELECT 
    PackageID,
    PackageName,
    Description,
    DurationDays,
    Price
FROM 
    TravelPackages
WHERE 
    Category = 'Peak Climbing'
ORDER BY 
    DurationDays DESC; -- Order results by duration (descending)

-- Error handling: Ensure that the database connection and queries are handled properly within your application code (e.g., in PHP, Python, or other languages).
```
