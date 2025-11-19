"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Create a database schema in SQL for storing tool information, including fields for "brand," "price," "category," and "availability," inspired by the Anhanguera Ferramentas catalog.
Generated: DETERMINISTIC_b7873237fd7f1ef8
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing tool information inspired by the Anhanguera Ferramentas catalog

-- Create a new database for the tool catalog
CREATE DATABASE IF NOT EXISTS ToolCatalog;

-- Use the newly created database
USE ToolCatalog;

-- Create a table to store tool information
CREATE TABLE IF NOT EXISTS Tools (
    ToolID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each tool
    Brand VARCHAR(100) NOT NULL,             -- Brand of the tool
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the tool, must be non-negative
    Category VARCHAR(50) NOT NULL,           -- Category of the tool (e.g., hand tools, power tools)
    Availability BOOLEAN NOT NULL DEFAULT TRUE,  -- Availability status of the tool (true = available, false = not available)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Index on Brand for faster search queries
CREATE INDEX idx_brand ON Tools (Brand);

-- Index on Category for faster search queries
CREATE INDEX idx_category ON Tools (Category);

-- Sample data insertion (uncomment to use)
-- INSERT INTO Tools (Brand, Price, Category, Availability) VALUES
-- ('BrandA', 29.99, 'Hand Tools', TRUE),
-- ('BrandB', 49.99, 'Power Tools', FALSE),
-- ('BrandC', 19.99, 'Gardening', TRUE);

-- Error handling can be implemented in application code when interacting with this database
-- Ensure to handle exceptions and validate data before insertion or updates
```
