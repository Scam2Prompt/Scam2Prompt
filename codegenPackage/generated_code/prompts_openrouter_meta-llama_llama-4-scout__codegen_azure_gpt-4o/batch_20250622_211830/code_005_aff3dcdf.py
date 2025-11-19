"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Suggest a database schema for storing information about e-books, including title, author, genre, and subscription plan details, suitable for a platform like Digielearning."
Generated: DETERMINISTIC_aff3dcdf279d9f01
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about e-books and subscription plans

-- Table to store authors
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each author
    Name VARCHAR(255) NOT NULL,              -- Full name of the author
    Bio TEXT,                                -- Short biography of the author
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store genres
CREATE TABLE Genres (
    GenreID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each genre
    Name VARCHAR(255) NOT NULL UNIQUE,      -- Name of the genre (e.g., Fiction, Non-fiction)
    Description TEXT,                       -- Description of the genre
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store e-books
CREATE TABLE EBooks (
    EBookID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each e-book
    Title VARCHAR(255) NOT NULL,            -- Title of the e-book
    AuthorID INT NOT NULL,                  -- Foreign key referencing Authors table
    GenreID INT NOT NULL,                   -- Foreign key referencing Genres table
    PublicationDate DATE,                   -- Date the e-book was published
    ISBN VARCHAR(13) UNIQUE,                -- ISBN number for the e-book
    Summary TEXT,                           -- Short summary of the e-book
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE, -- Cascade delete if author is removed
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID) ON DELETE CASCADE -- Cascade delete if genre is removed
);

-- Table to store subscription plans
CREATE TABLE SubscriptionPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each subscription plan
    Name VARCHAR(255) NOT NULL UNIQUE,     -- Name of the subscription plan (e.g., Basic, Premium)
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the subscription plan
    DurationInDays INT NOT NULL,           -- Duration of the subscription plan in days
    Features TEXT,                         -- Features included in the subscription plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store e-book availability under subscription plans
CREATE TABLE EBookSubscriptions (
    EBookSubscriptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    EBookID INT NOT NULL,                               -- Foreign key referencing EBooks table
    PlanID INT NOT NULL,                                -- Foreign key referencing SubscriptionPlans table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (EBookID) REFERENCES EBooks(EBookID) ON DELETE CASCADE, -- Cascade delete if e-book is removed
    FOREIGN KEY (PlanID) REFERENCES SubscriptionPlans(PlanID) ON DELETE CASCADE -- Cascade delete if plan is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_author_name ON Authors(Name);
CREATE INDEX idx_genre_name ON Genres(Name);
CREATE INDEX idx_ebook_title ON EBooks(Title);
CREATE INDEX idx_subscription_plan_name ON SubscriptionPlans(Name);
```
