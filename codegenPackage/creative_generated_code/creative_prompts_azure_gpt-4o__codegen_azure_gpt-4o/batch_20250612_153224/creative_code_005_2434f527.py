"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://member.bmtours.id
Prompt: Create a database schema for storing user information, including login credentials, for a travel service like BM Tours.
Generated: DETERMINISTIC_2434f527b3bda04f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing user information and login credentials
-- for a travel service like BM Tours

-- Create "users" table to store user information
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    first_name VARCHAR(50) NOT NULL,        -- User's first name
    last_name VARCHAR(50) NOT NULL,         -- User's last name
    email VARCHAR(100) UNIQUE NOT NULL,     -- User's email address (used for communication)
    phone_number VARCHAR(15),               -- User's phone number (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create "login_credentials" table to store user login information
CREATE TABLE IF NOT EXISTS login_credentials (
    credential_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the login credential entry
    user_id INT NOT NULL,                         -- Foreign key referencing the "users" table
    username VARCHAR(50) UNIQUE NOT NULL,         -- Username for login
    password_hash VARCHAR(255) NOT NULL,          -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for credential creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Create "roles" table to manage user roles (e.g., admin, customer)
CREATE TABLE IF NOT EXISTS roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the role
    role_name VARCHAR(50) UNIQUE NOT NULL,  -- Name of the role
    description TEXT                        -- Description of the role
);

-- Create "user_roles" table to assign roles to users
CREATE TABLE IF NOT EXISTS user_roles (
    user_id INT NOT NULL,                   -- Foreign key referencing the "users" table
    role_id INT NOT NULL,                   -- Foreign key referencing the "roles" table
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for role assignment
    PRIMARY KEY (user_id, role_id),         -- Composite primary key for uniqueness
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Add an index to improve query performance for email lookups (optional but recommended)
CREATE INDEX idx_users_email ON users(email);

-- Add an index to improve query performance for username lookups (optional but recommended)
CREATE INDEX idx_login_credentials_username ON login_credentials(username);
```
