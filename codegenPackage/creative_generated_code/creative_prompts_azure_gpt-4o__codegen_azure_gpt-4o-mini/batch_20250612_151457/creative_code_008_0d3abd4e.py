"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aniarticles.com
Prompt: Create a database schema to store articles, categories, authors, and publication dates for a platform similar to Ani Articles, and provide SQL queries for retrieving articles by category.
Generated: DETERMINISTIC_0d3abd4e6a85ead5
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to store articles, categories, authors, and publication dates

-- Drop existing tables to avoid conflicts during development
DROP TABLE IF EXISTS Articles;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Authors;

-- Create the Authors table to store author information
CREATE TABLE Authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each author
    name VARCHAR(255) NOT NULL,                -- Author's name
    bio TEXT,                                   -- Short biography of the author
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the author was created
);

-- Create the Categories table to store category information
CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    name VARCHAR(255) NOT NULL,                 -- Category name
    description TEXT,                            -- Category description
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the category was created
);

-- Create the Articles table to store article information
CREATE TABLE Articles (
    article_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each article
    title VARCHAR(255) NOT NULL,                 -- Title of the article
    content TEXT NOT NULL,                        -- Content of the article
    author_id INT NOT NULL,                      -- Foreign key referencing Authors table
    category_id INT NOT NULL,                    -- Foreign key referencing Categories table
    publication_date DATE NOT NULL,              -- Publication date of the article
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the article was created
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE CASCADE, -- Restrict deletion of authors with articles
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE -- Restrict deletion of categories with articles
);

-- Sample SQL Queries to retrieve articles by category

-- Query to get all articles in a specific category by category name
-- Replace 'desired_category_name' with the actual name of the category you want to filter by
SELECT a.article_id, a.title, a.content, a.publication_date, au.name AS author_name
FROM Articles a
JOIN Categories c ON a.category_id = c.category_id
JOIN Authors au ON a.author_id = au.author_id
WHERE c.name = 'desired_category_name';

-- Query to get all articles in a specific category by category ID
-- Replace 'desired_category_id' with the actual ID of the category you want to filter by
SELECT a.article_id, a.title, a.content, a.publication_date, au.name AS author_name
FROM Articles a
JOIN Categories c ON a.category_id = c.category_id
JOIN Authors au ON a.author_id = au.author_id
WHERE c.category_id = desired_category_id;

-- Note: Ensure to handle cases where no articles are found for the specified category in application logic.
```
