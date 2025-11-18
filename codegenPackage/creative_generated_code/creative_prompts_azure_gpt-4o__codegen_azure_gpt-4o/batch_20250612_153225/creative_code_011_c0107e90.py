"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Recommend a database schema for storing client testimonials, service categories, and contact information, inspired by the structure of the website.
Generated: DETERMINISTIC_c0107e90ad2f914f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for storing client testimonials, service categories, and contact information

-- Table for storing client testimonials
CREATE TABLE ClientTestimonials (
    TestimonialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each testimonial
    ClientName VARCHAR(255) NOT NULL,             -- Name of the client giving the testimonial
    ClientEmail VARCHAR(255) DEFAULT NULL,        -- Optional client email for contact
    TestimonialText TEXT NOT NULL,                -- The actual testimonial text
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Optional rating (1 to 5 scale)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the testimonial was created
);

-- Table for storing service categories
CREATE TABLE ServiceCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,    -- Name of the service category
    Description TEXT DEFAULT NULL,                -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the category was created
);

-- Table for storing contact information
CREATE TABLE ContactInformation (
    ContactID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the contact record
    FullName VARCHAR(255) NOT NULL,               -- Full name of the contact person
    Email VARCHAR(255) NOT NULL UNIQUE,           -- Email address of the contact person
    PhoneNumber VARCHAR(25) DEFAULT NULL,         -- Optional phone number
    Message TEXT NOT NULL,                        -- Message sent by the contact person
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the message was created
);

-- Ensure foreign key relationships (if needed in the future):
-- Testimonials can be optionally tied to a service category (many-to-one relationship)
ALTER TABLE ClientTestimonials 
ADD COLUMN CategoryID INT DEFAULT NULL,
ADD FOREIGN KEY (CategoryID) REFERENCES ServiceCategories(CategoryID)
ON DELETE SET NULL ON UPDATE CASCADE;

-- Indexing for faster queries (e.g., email lookups)
CREATE INDEX idx_client_email ON ClientTestimonials(ClientEmail);
CREATE INDEX idx_contact_email ON ContactInformation(Email);
```
