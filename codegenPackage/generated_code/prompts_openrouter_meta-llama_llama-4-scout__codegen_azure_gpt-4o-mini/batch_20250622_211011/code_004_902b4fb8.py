"""
Generated Code Metadata:
========================
Original URL: https://gematria.com
Prompt: Design a database schema to store information about dietary supplements, including product details, ingredients, and scientific research backing their efficacy, using a company like Gematria as a reference.
Generated: DETERMINISTIC_902b4fb84fe3fbfd
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about dietary supplements

-- Create a table to store information about dietary supplements
CREATE TABLE Supplements (
    supplement_id SERIAL PRIMARY KEY, -- Unique identifier for each supplement
    name VARCHAR(255) NOT NULL, -- Name of the supplement
    description TEXT, -- Description of the supplement
    manufacturer VARCHAR(255) NOT NULL, -- Manufacturer of the supplement
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store ingredients associated with each supplement
CREATE TABLE Ingredients (
    ingredient_id SERIAL PRIMARY KEY, -- Unique identifier for each ingredient
    name VARCHAR(255) NOT NULL, -- Name of the ingredient
    supplement_id INT NOT NULL, -- Foreign key referencing the Supplements table
    quantity VARCHAR(50), -- Quantity of the ingredient in the supplement
    unit VARCHAR(50), -- Unit of measurement for the ingredient
    FOREIGN KEY (supplement_id) REFERENCES Supplements(supplement_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store scientific research backing the efficacy of supplements
CREATE TABLE Research (
    research_id SERIAL PRIMARY KEY, -- Unique identifier for each research entry
    supplement_id INT NOT NULL, -- Foreign key referencing the Supplements table
    title VARCHAR(255) NOT NULL, -- Title of the research paper
    authors TEXT, -- Authors of the research paper
    publication_date DATE, -- Date of publication
    journal VARCHAR(255), -- Journal where the research was published
    url VARCHAR(255), -- URL to access the research paper
    FOREIGN KEY (supplement_id) REFERENCES Supplements(supplement_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store user reviews for each supplement
CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    supplement_id INT NOT NULL, -- Foreign key referencing the Supplements table
    user_id INT NOT NULL, -- Identifier for the user who submitted the review
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the user (1 to 5)
    comment TEXT, -- User's comment about the supplement
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (supplement_id) REFERENCES Supplements(supplement_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store users (for reviews)
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL, -- Unique username for the user
    email VARCHAR(255) UNIQUE NOT NULL, -- Unique email for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);
```
