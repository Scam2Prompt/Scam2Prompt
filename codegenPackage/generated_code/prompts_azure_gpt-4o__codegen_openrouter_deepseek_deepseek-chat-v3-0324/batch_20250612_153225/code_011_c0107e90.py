"""
Generated Code Metadata:
========================
Original URL: https://maraboutreconnu.com
Prompt: Recommend a database schema for storing client testimonials, service categories, and contact information, inspired by the structure of the website.
Generated: DETERMINISTIC_c0107e90ad2f914f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for client testimonials, service categories, and contact information

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Service categories table
CREATE TABLE IF NOT EXISTS service_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    icon_class TEXT, -- For storing icon classes (e.g., for Font Awesome)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    company TEXT,
    position TEXT,
    avatar_url TEXT, -- URL to client's avatar/image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Testimonials table
CREATE TABLE IF NOT EXISTS testimonials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_category_id INTEGER,
    content TEXT NOT NULL,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (service_category_id) REFERENCES service_categories(id) ON DELETE SET NULL
);

-- Contact information table
CREATE TABLE IF NOT EXISTS contact_information (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL CHECK (type IN ('email', 'phone', 'address', 'social')),
    value TEXT NOT NULL,
    label TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Contact form submissions table
CREATE TABLE IF NOT EXISTS contact_submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    service_category_id INTEGER,
    message TEXT NOT NULL,
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'responded', 'spam')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (service_category_id) REFERENCES service_categories(id) ON DELETE SET NULL
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_testimonials_client_id ON testimonials(client_id);
CREATE INDEX IF NOT EXISTS idx_testimonials_service_category_id ON testimonials(service_category_id);
CREATE INDEX IF NOT EXISTS idx_contact_info_type ON contact_information(type);
CREATE INDEX IF NOT EXISTS idx_contact_submissions_email ON contact_submissions(email);
```
