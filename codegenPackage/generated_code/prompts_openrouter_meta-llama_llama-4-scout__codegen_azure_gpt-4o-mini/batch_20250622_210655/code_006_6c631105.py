"""
Generated Code Metadata:
========================
Original URL: https://byamed.net
Prompt: Design a database schema for a high-end web design and development agency, incorporating data models for client projects, services, and portfolios, similar to the ones managed by Amed Abraham.
Generated: DETERMINISTIC_6c631105f2c23e4d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a high-end web design and development agency

-- Create a table for clients
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(255) NOT NULL, -- Client's name
    email VARCHAR(255) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(20), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for services offered by the agency
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    name VARCHAR(255) NOT NULL, -- Name of the service
    description TEXT, -- Description of the service
    price DECIMAL(10, 2) NOT NULL, -- Price of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for client projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing Clients
    service_id INT NOT NULL, -- Foreign key referencing Services
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Project start date
    end_date DATE, -- Project end date
    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'In Progress', 'Completed', 'On Hold')), -- Project status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for portfolios showcasing completed projects
CREATE TABLE Portfolios (
    portfolio_id SERIAL PRIMARY KEY, -- Unique identifier for each portfolio entry
    project_id INT NOT NULL, -- Foreign key referencing Projects
    description TEXT, -- Description of the project in the portfolio
    image_url VARCHAR(255), -- URL of the project image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for testimonials from clients
CREATE TABLE Testimonials (
    testimonial_id SERIAL PRIMARY KEY, -- Unique identifier for each testimonial
    client_id INT NOT NULL, -- Foreign key referencing Clients
    content TEXT NOT NULL, -- Content of the testimonial
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for tracking agency employees
CREATE TABLE Employees (
    employee_id SERIAL PRIMARY KEY, -- Unique identifier for each employee
    name VARCHAR(255) NOT NULL, -- Employee's name
    role VARCHAR(100) NOT NULL, -- Employee's role in the agency
    email VARCHAR(255) UNIQUE NOT NULL, -- Employee's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);
```
