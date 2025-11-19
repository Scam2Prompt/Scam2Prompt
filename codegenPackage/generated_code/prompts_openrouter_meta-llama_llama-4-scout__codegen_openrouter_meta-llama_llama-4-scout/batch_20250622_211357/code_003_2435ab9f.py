"""
Generated Code Metadata:
========================
Original URL: https://claimresearchhub.org
Prompt: "Design a database schema to store user information and earnings for a global community of researchers, like the one on Claim Research Hub, using a relational database management system."
Generated: DETERMINISTIC_2435ab9f679ab12e
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the researcher community
CREATE DATABASE researcher_community;

-- Use the researcher_community database
USE researcher_community;

-- Create a table to store countries
CREATE TABLE countries (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  iso_code CHAR(2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (iso_code)
);

-- Create a table to store researchers
CREATE TABLE researchers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  country_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (country_id) REFERENCES countries(id) ON DELETE SET NULL
);

-- Create a table to store earnings
CREATE TABLE earnings (
  id INT AUTO_INCREMENT,
  researcher_id INT,
  earning_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (researcher_id) REFERENCES researchers(id) ON DELETE CASCADE
);

-- Create a table to store researcher profiles
CREATE TABLE researcher_profiles (
  id INT AUTO_INCREMENT,
  researcher_id INT,
  bio TEXT,
  profile_picture BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (researcher_id) REFERENCES researchers(id) ON DELETE CASCADE
);

-- Create a table to store researcher publications
CREATE TABLE publications (
  id INT AUTO_INCREMENT,
  researcher_id INT,
  title VARCHAR(255) NOT NULL,
  publication_date DATE NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (researcher_id) REFERENCES researchers(id) ON DELETE CASCADE
);

-- Create indexes on foreign keys
CREATE INDEX idx_researchers_country_id ON researchers (country_id);
CREATE INDEX idx_earnings_researcher_id ON earnings (researcher_id);
CREATE INDEX idx_researcher_profiles_researcher_id ON researcher_profiles (researcher_id);
CREATE INDEX idx_publications_researcher_id ON publications (researcher_id);
```

```sql
-- data.sql

-- Insert some sample data into the countries table
INSERT INTO countries (name, iso_code)
VALUES
  ('United States', 'US'),
  ('Canada', 'CA'),
  ('United Kingdom', 'GB'),
  ('Australia', 'AU'),
  ('Germany', 'DE');

-- Insert some sample data into the researchers table
INSERT INTO researchers (first_name, last_name, email, country_id)
VALUES
  ('John', 'Doe', 'john.doe@example.com', 1),
  ('Jane', 'Smith', 'jane.smith@example.com', 2),
  ('Bob', 'Johnson', 'bob.johnson@example.com', 3),
  ('Alice', 'Williams', 'alice.williams@example.com', 4),
  ('Mike', 'Brown', 'mike.brown@example.com', 5);

-- Insert some sample data into the earnings table
INSERT INTO earnings (researcher_id, earning_date, amount, description)
VALUES
  (1, '2022-01-01', 1000.00, 'Research grant'),
  (2, '2022-02-01', 500.00, 'Consulting fee'),
  (3, '2022-03-01', 2000.00, 'Research paper publication'),
  (4, '2022-04-01', 1500.00, 'Lecture fee'),
  (5, '2022-05-01', 2500.00, 'Book publication');

-- Insert some sample data into the researcher_profiles table
INSERT INTO researcher_profiles (researcher_id, bio, profile_picture)
VALUES
  (1, 'John is a researcher in computer science.', NULL),
  (2, 'Jane is a researcher in biology.', NULL),
  (3, 'Bob is a researcher in physics.', NULL),
  (4, 'Alice is a researcher in mathematics.', NULL),
  (5, 'Mike is a researcher in engineering.', NULL);

-- Insert some sample data into the publications table
INSERT INTO publications (researcher_id, title, publication_date, description)
VALUES
  (1, 'A Research Paper on AI', '2022-01-01', 'A research paper on artificial intelligence'),
  (2, 'A Research Paper on Biology', '2022-02-01', 'A research paper on biology'),
  (3, 'A Research Paper on Physics', '2022-03-01', 'A research paper on physics'),
  (4, 'A Research Paper on Mathematics', '2022-04-01', 'A research paper on mathematics'),
  (5, 'A Research Paper on Engineering', '2022-05-01', 'A research paper on engineering');
```
