"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.com
Prompt: Design a database schema to store information about investment education firms, users, and registration processes on a platform like Immediate Peak.
Generated: DETERMINISTIC_cb8dd6b5dca462a9
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for investment education platform

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing investment education firms
CREATE TABLE IF NOT EXISTS firms (
    firm_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    website_url TEXT,
    logo_url TEXT,
    founded_date DATE,
    headquarters TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_firm_name UNIQUE (name)
);

-- Table for storing user roles
CREATE TABLE IF NOT EXISTS roles (
    role_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_role_name UNIQUE (name)
);

-- Table for storing platform users
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    date_of_birth DATE,
    role_id INTEGER,
    is_verified BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (role_id) REFERENCES roles(role_id),
    CONSTRAINT unique_user_email UNIQUE (email)
);

-- Table for storing registration processes
CREATE TABLE IF NOT EXISTS registration_processes (
    process_id INTEGER PRIMARY KEY AUTOINCREMENT,
    firm_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (firm_id) REFERENCES firms(firm_id) ON DELETE CASCADE
);

-- Table for storing registration steps
CREATE TABLE IF NOT EXISTS registration_steps (
    step_id INTEGER PRIMARY KEY AUTOINCREMENT,
    process_id INTEGER NOT NULL,
    step_order INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    content_url TEXT,
    is_required BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (process_id) REFERENCES registration_processes(process_id) ON DELETE CASCADE,
    CONSTRAINT unique_step_order_per_process UNIQUE (process_id, step_order)
);

-- Table for tracking user registrations
CREATE TABLE IF NOT EXISTS user_registrations (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    process_id INTEGER NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_date TIMESTAMP,
    status TEXT DEFAULT 'pending', -- pending, in_progress, completed, cancelled
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (process_id) REFERENCES registration_processes(process_id) ON DELETE CASCADE,
    CONSTRAINT unique_user_process_registration UNIQUE (user_id, process_id)
);

-- Table for tracking user progress through registration steps
CREATE TABLE IF NOT EXISTS user_registration_progress (
    progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration_id INTEGER NOT NULL,
    step_id INTEGER NOT NULL,
    completion_date TIMESTAMP,
    status TEXT DEFAULT 'pending', -- pending, completed
    notes TEXT,
    FOREIGN KEY (registration_id) REFERENCES user_registrations(registration_id) ON DELETE CASCADE,
    FOREIGN KEY (step_id) REFERENCES registration_steps(step_id) ON DELETE CASCADE,
    CONSTRAINT unique_registration_step_progress UNIQUE (registration_id, step_id)
);

-- Table for storing user verification tokens
CREATE TABLE IF NOT EXISTS verification_tokens (
    token_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    token TEXT NOT NULL,
    token_type TEXT NOT NULL, -- email_verification, password_reset, etc.
    expires_at TIMESTAMP NOT NULL,
    is_used BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Table for audit logging
CREATE TABLE IF NOT EXISTS audit_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT NOT NULL,
    entity_type TEXT,
    entity_id INTEGER,
    old_values TEXT,
    new_values TEXT,
    ip_address TEXT,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_user_registrations_user_id ON user_registrations(user_id);
CREATE INDEX IF NOT EXISTS idx_user_registrations_process_id ON user_registrations(process_id);
CREATE INDEX IF NOT EXISTS idx_user_registration_progress_registration_id ON user_registration_progress(registration_id);
CREATE INDEX IF NOT EXISTS idx_verification_tokens_user_id ON verification_tokens(user_id);
CREATE INDEX IF NOT EXISTS idx_verification_tokens_token ON verification_tokens(token);
```
