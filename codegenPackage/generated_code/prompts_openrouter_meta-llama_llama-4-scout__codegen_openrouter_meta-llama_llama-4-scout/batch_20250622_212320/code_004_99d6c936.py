"""
Generated Code Metadata:
========================
Original URL: https://iammetis.org
Prompt: Design a database schema to store information about Métis individuals, organizations, and resources, including fields for profiles, contact information, and language proficiency.
Generated: DETERMINISTIC_99d6c93603649ab9
Batch ID: 20250622_212320
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/metis-history": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/metisnation.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/johndoe.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for Métis individuals, organizations, and resources

-- Create a database
CREATE DATABASE metis_database;

-- Use the database
USE metis_database;

-- Create a table for individuals
CREATE TABLE individuals (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  province VARCHAR(100),
  postal_code VARCHAR(20),
  PRIMARY KEY (id)
);

-- Create a table for organizations
CREATE TABLE organizations (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  type VARCHAR(100),
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  province VARCHAR(100),
  postal_code VARCHAR(20),
  PRIMARY KEY (id)
);

-- Create a table for resources
CREATE TABLE resources (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  type VARCHAR(100),
  url VARCHAR(255),
  PRIMARY KEY (id)
);

-- Create a table for language proficiency
CREATE TABLE language_proficiency (
  id INT AUTO_INCREMENT,
  individual_id INT,
  language VARCHAR(100) NOT NULL,
  reading_level VARCHAR(50),
  writing_level VARCHAR(50),
  speaking_level VARCHAR(50),
  PRIMARY KEY (id),
  FOREIGN KEY (individual_id) REFERENCES individuals(id) ON DELETE CASCADE
);

-- Create a table for individual profiles
CREATE TABLE individual_profiles (
  id INT AUTO_INCREMENT,
  individual_id INT,
  bio TEXT,
  profile_picture_url VARCHAR(255),
  PRIMARY KEY (id),
  FOREIGN KEY (individual_id) REFERENCES individuals(id) ON DELETE CASCADE
);

-- Create a table for organization profiles
CREATE TABLE organization_profiles (
  id INT AUTO_INCREMENT,
  organization_id INT,
  bio TEXT,
  profile_picture_url VARCHAR(255),
  PRIMARY KEY (id),
  FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE
);

-- Create a table for resource categories
CREATE TABLE resource_categories (
  id INT AUTO_INCREMENT,
  resource_id INT,
  category VARCHAR(100) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE CASCADE
);

-- Create a table for individual-organization relationships
CREATE TABLE individual_organizations (
  individual_id INT,
  organization_id INT,
  role VARCHAR(100),
  PRIMARY KEY (individual_id, organization_id),
  FOREIGN KEY (individual_id) REFERENCES individuals(id) ON DELETE CASCADE,
  FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE
);

-- Create a table for individual-resource relationships
CREATE TABLE individual_resources (
  individual_id INT,
  resource_id INT,
  rating TINYINT,
  review TEXT,
  PRIMARY KEY (individual_id, resource_id),
  FOREIGN KEY (individual_id) REFERENCES individuals(id) ON DELETE CASCADE,
  FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE CASCADE
);
```

```sql
-- Example insert statements

INSERT INTO individuals (first_name, last_name, date_of_birth, email, phone_number, address, city, province, postal_code)
VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Ottawa', 'ON', 'K1A 0A1');

INSERT INTO organizations (name, type, email, phone_number, address, city, province, postal_code)
VALUES ('Métis Nation', 'Government', 'info@metisnation.ca', '123-456-7890', '123 Main St', 'Ottawa', 'ON', 'K1A 0A1');

INSERT INTO resources (title, description, type, url)
VALUES ('Métis History', 'A brief history of the Métis people', 'Article', 'https://example.com/metis-history');

INSERT INTO language_proficiency (individual_id, language, reading_level, writing_level, speaking_level)
VALUES (1, 'English', 'Fluent', 'Fluent', 'Fluent');

INSERT INTO individual_profiles (individual_id, bio, profile_picture_url)
VALUES (1, 'I am a Métis individual', 'https://example.com/johndoe.jpg');

INSERT INTO organization_profiles (organization_id, bio, profile_picture_url)
VALUES (1, 'The Métis Nation is a government organization', 'https://example.com/metisnation.jpg');

INSERT INTO resource_categories (resource_id, category)
VALUES (1, 'History');

INSERT INTO individual_organizations (individual_id, organization_id, role)
VALUES (1, 1, 'Member');

INSERT INTO individual_resources (individual_id, resource_id, rating, review)
VALUES (1, 1, 5, 'Very informative');
```
