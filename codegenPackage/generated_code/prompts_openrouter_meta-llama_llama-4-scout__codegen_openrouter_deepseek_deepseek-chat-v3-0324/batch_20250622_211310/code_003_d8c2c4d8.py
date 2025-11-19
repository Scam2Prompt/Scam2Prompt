"""
Generated Code Metadata:
========================
Original URL: https://immediatevortex.co
Prompt: Design a basic database schema for storing user information, educational company details, and investment resources, and provide a SQL code to create the schema.
Generated: DETERMINISTIC_d8c2c4d8ffd3e1ad
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for user information, educational company details, and investment resources

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create Users table to store user information
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE,
    phone_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    CHECK (email LIKE '%@%.%')
);

-- Create EducationalCompanies table
CREATE TABLE EducationalCompanies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    description TEXT,
    website_url TEXT,
    founded_date DATE,
    headquarters_location TEXT,
    contact_email TEXT NOT NULL,
    contact_phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    CHECK (contact_email LIKE '%@%.%')
);

-- Create InvestmentResources table
CREATE TABLE InvestmentResources (
    resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_name TEXT NOT NULL,
    resource_type TEXT NOT NULL, -- e.g., 'book', 'course', 'video', 'article'
    description TEXT,
    url TEXT,
    cost DECIMAL(10, 2),
    currency TEXT DEFAULT 'USD',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1
);

-- Create UserEducation table (junction table for many-to-many relationship between Users and EducationalCompanies)
CREATE TABLE UserEducation (
    user_education_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    company_id INTEGER NOT NULL,
    enrollment_date DATE,
    graduation_date DATE,
    degree_earned TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (company_id) REFERENCES EducationalCompanies(company_id) ON DELETE CASCADE,
    UNIQUE(user_id, company_id)
);

-- Create UserInvestments table (junction table for many-to-many relationship between Users and InvestmentResources)
CREATE TABLE UserInvestments (
    user_investment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    resource_id INTEGER NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount_paid DECIMAL(10, 2),
    currency TEXT DEFAULT 'USD',
    is_completed BOOLEAN DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (resource_id) REFERENCES InvestmentResources(resource_id) ON DELETE CASCADE,
    UNIQUE(user_id, resource_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_users_email ON Users(email);
CREATE INDEX idx_users_username ON Users(username);
CREATE INDEX idx_educational_companies_name ON EducationalCompanies(company_name);
CREATE INDEX idx_investment_resources_name ON InvestmentResources(resource_name);
CREATE INDEX idx_user_education_user ON UserEducation(user_id);
CREATE INDEX idx_user_education_company ON UserEducation(company_id);
CREATE INDEX idx_user_investments_user ON UserInvestments(user_id);
CREATE INDEX idx_user_investments_resource ON UserInvestments(resource_id);

-- Create trigger to update timestamps on record update
CREATE TRIGGER update_user_timestamp
AFTER UPDATE ON Users
FOR EACH ROW
BEGIN
    UPDATE Users SET updated_at = CURRENT_TIMESTAMP WHERE user_id = OLD.user_id;
END;

CREATE TRIGGER update_educational_company_timestamp
AFTER UPDATE ON EducationalCompanies
FOR EACH ROW
BEGIN
    UPDATE EducationalCompanies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;

CREATE TRIGGER update_investment_resource_timestamp
AFTER UPDATE ON InvestmentResources
FOR EACH ROW
BEGIN
    UPDATE InvestmentResources SET updated_at = CURRENT_TIMESTAMP WHERE resource_id = OLD.resource_id;
END;

CREATE TRIGGER update_user_education_timestamp
AFTER UPDATE ON UserEducation
FOR EACH ROW
BEGIN
    UPDATE UserEducation SET updated_at = CURRENT_TIMESTAMP WHERE user_education_id = OLD.user_education_id;
END;

CREATE TRIGGER update_user_investment_timestamp
AFTER UPDATE ON UserInvestments
FOR EACH ROW
BEGIN
    UPDATE UserInvestments SET updated_at = CURRENT_TIMESTAMP WHERE user_investment_id = OLD.user_investment_id;
END;
```
