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
-- Database schema for character customization options

-- Create a table for storing character types
CREATE TABLE CharacterTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each character type
    name VARCHAR(50) NOT NULL UNIQUE, -- Name of the character type (e.g., Human, Elf)
    description TEXT -- Description of the character type
);

-- Create a table for storing customization categories
CREATE TABLE CustomizationCategories (
    id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(50) NOT NULL UNIQUE, -- Name of the customization category (e.g., Accessories, Body, Bottoms)
    description TEXT -- Description of the customization category
);

-- Create a table for storing customization options
CREATE TABLE CustomizationOptions (
    id SERIAL PRIMARY KEY, -- Unique identifier for each customization option
    category_id INT NOT NULL, -- Foreign key referencing the customization category
    name VARCHAR(50) NOT NULL, -- Name of the customization option (e.g., Hat, Shirt, Pants)
    image_url VARCHAR(255), -- URL to an image representing the customization option
    attributes JSONB, -- JSONB field to store additional attributes (e.g., color, size)
    FOREIGN KEY (category_id) REFERENCES CustomizationCategories(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing character customizations
CREATE TABLE CharacterCustomizations (
    id SERIAL PRIMARY KEY, -- Unique identifier for each customization record
    character_type_id INT NOT NULL, -- Foreign key referencing the character type
    customization_option_id INT NOT NULL, -- Foreign key referencing the customization option
    FOREIGN KEY (character_type_id) REFERENCES CharacterTypes(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (customization_option_id) REFERENCES CustomizationOptions(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing user profiles
CREATE TABLE UserProfiles (
    id SERIAL PRIMARY KEY, -- Unique identifier for each user profile
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the profile was created
);

-- Create a table for storing user character customizations
CREATE TABLE UserCharacterCustomizations (
    id SERIAL PRIMARY KEY, -- Unique identifier for each user customization record
    user_id INT NOT NULL, -- Foreign key referencing the user profile
    character_customization_id INT NOT NULL, -- Foreign key referencing the character customization
    FOREIGN KEY (user_id) REFERENCES UserProfiles(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (character_customization_id) REFERENCES CharacterCustomizations(id) ON DELETE CASCADE -- Ensures referential integrity
);
```
