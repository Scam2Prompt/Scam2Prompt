"""
Generated Code Metadata:
========================
Original URL: https://fullmoonbird-next.vercel.app
Prompt: Design a simple database schema for storing character customization options (e.g., Accessories, Body, Bottoms) for a platform similar to https://fullmoonbird-next.vercel.app.
Generated: DETERMINISTIC_93303ac06a47ca63
Batch ID: 20250622_204755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing character customization options

-- Table to store categories of customization options (e.g., Accessories, Body, Bottoms)
CREATE TABLE CustomizationCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category (e.g., Accessories, Body, Bottoms)
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store individual customization options within a category
CREATE TABLE CustomizationOptions (
    OptionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each customization option
    CategoryID INT NOT NULL,                   -- Foreign key linking to the CustomizationCategories table
    Name VARCHAR(255) NOT NULL,                -- Name of the customization option (e.g., Hat, Shirt, Pants)
    ImageURL VARCHAR(2083),                    -- URL to the image representing the customization option
    IsDefault BOOLEAN DEFAULT FALSE,           -- Flag indicating if this is the default option for the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the option was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the option was last updated
    FOREIGN KEY (CategoryID) REFERENCES CustomizationCategories(CategoryID) -- Enforce relationship with categories
);

-- Table to store user-selected customization options
CREATE TABLE UserCustomizations (
    UserCustomizationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user customization record
    UserID INT NOT NULL,                                -- Identifier for the user (assumes a separate Users table exists)
    OptionID INT NOT NULL,                              -- Foreign key linking to the CustomizationOptions table
    SelectedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the customization option was selected
    FOREIGN KEY (OptionID) REFERENCES CustomizationOptions(OptionID) -- Enforce relationship with options
);

-- Indexes for optimizing queries
CREATE INDEX idx_category_name ON CustomizationCategories(Name); -- Index for quick lookup by category name
CREATE INDEX idx_option_name ON CustomizationOptions(Name);      -- Index for quick lookup by option name
CREATE INDEX idx_user_id ON UserCustomizations(UserID);          -- Index for quick lookup by user ID
```
