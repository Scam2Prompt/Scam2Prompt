"""
Generated Code Metadata:
========================
Original URL: https://ipb.ac.id
Prompt: Design a database schema to store information about IPB University's research centers, research news, and scientific publications; provide a SQL code snippet to create the schema.
Generated: DETERMINISTIC_7898963da4dc4f33
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL code to create a database schema for IPB University's research centers, research news, and scientific publications

-- Create a database for the research centers
CREATE DATABASE IF NOT EXISTS ipb_research;

-- Use the created database
USE ipb_research;

-- Table to store information about research centers
CREATE TABLE IF NOT EXISTS research_centers (
    center_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each research center
    center_name VARCHAR(255) NOT NULL,         -- Name of the research center
    description TEXT,                           -- Description of the research center
    established_year YEAR,                      -- Year the center was established
    location VARCHAR(255),                      -- Location of the research center
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store research news related to the research centers
CREATE TABLE IF NOT EXISTS research_news (
    news_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each news article
    center_id INT,                              -- Foreign key referencing the research center
    title VARCHAR(255) NOT NULL,                -- Title of the news article
    content TEXT NOT NULL,                      -- Content of the news article
    published_date DATE NOT NULL,               -- Date the news article was published
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (center_id) REFERENCES research_centers(center_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to store scientific publications
CREATE TABLE IF NOT EXISTS scientific_publications (
    publication_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each publication
    center_id INT,                                  -- Foreign key referencing the research center
    title VARCHAR(255) NOT NULL,                    -- Title of the publication
    authors VARCHAR(255) NOT NULL,                  -- Authors of the publication
    publication_date DATE NOT NULL,                 -- Date of publication
    journal_name VARCHAR(255),                      -- Name of the journal
    doi VARCHAR(255),                               -- Digital Object Identifier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (center_id) REFERENCES research_centers(center_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Indexes can be added for performance optimization as needed
```
