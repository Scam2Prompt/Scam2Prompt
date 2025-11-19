"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: "Design a database schema for storing client testimonials, project details, and product information for a company specializing in UPVC window and door systems installations."
Generated: DETERMINISTIC_d872e681365a04f7
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for UPVC window and door systems company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postcode TEXT NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Products table for UPVC window and door systems
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    category TEXT NOT NULL CHECK(category IN ('Window', 'Door', 'Conservatory', 'Other')),
    material TEXT NOT NULL DEFAULT 'UPVC',
    energy_rating TEXT CHECK(energy_rating IN ('A', 'B', 'C', 'D', 'E', 'F', 'G')),
    price DECIMAL(10, 2) NOT NULL CHECK(price > 0),
    warranty_years INTEGER DEFAULT 10 CHECK(warranty_years > 0),
    is_active BOOLEAN DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Projects table for installation projects
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    completion_date DATE,
    status TEXT NOT NULL DEFAULT 'Pending' CHECK(status IN ('Pending', 'In Progress', 'Completed', 'Cancelled')),
    total_cost DECIMAL(10, 2) CHECK(total_cost >= 0),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Project products junction table (many-to-many relationship)
CREATE TABLE project_products (
    project_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1 CHECK(quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL CHECK(unit_price > 0),
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT,
    UNIQUE(project_id, product_id)
);

-- Testimonials table for client feedback
CREATE TABLE testimonials (
    testimonial_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_id INTEGER,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    comment TEXT NOT NULL,
    approval_status TEXT NOT NULL DEFAULT 'Pending' CHECK(approval_status IN ('Pending', 'Approved', 'Rejected')),
    submission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    published_date DATETIME,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL
);

-- Product images table
CREATE TABLE product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT 0,
    caption TEXT,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Project images table
CREATE TABLE project_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_before BOOLEAN NOT NULL,
    caption TEXT,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_project_products_project ON project_products(project_id);
CREATE INDEX idx_project_products_product ON project_products(product_id);
CREATE INDEX idx_testimonials_client ON testimonials(client_id);
CREATE INDEX idx_testimonials_project ON testimonials(project_id);
CREATE INDEX idx_product_images_product ON product_images(product_id);
CREATE INDEX idx_project_images_project ON project_images(project_id);
```
