"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Design a database schema for managing client projects in a cosmetic manufacturing business, reflecting the full-service approach outlined by Fabricare Cosmeticos.
Generated: DETERMINISTIC_250a8f375eaeb49d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Fabricare Cosmeticos client project management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    company TEXT,
    address TEXT,
    tax_id TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CHECK (email LIKE '%@%.%')
);

-- Project types table
CREATE TABLE project_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATETIME,
    target_date DATETIME,
    completion_date DATETIME,
    status TEXT NOT NULL DEFAULT 'planning' CHECK (status IN ('planning', 'active', 'on-hold', 'completed', 'cancelled')),
    priority INTEGER DEFAULT 3 CHECK (priority BETWEEN 1 AND 5),
    budget REAL CHECK (budget >= 0),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES project_types(type_id),
    CHECK (target_date IS NULL OR start_date IS NULL OR target_date >= start_date),
    CHECK (completion_date IS NULL OR start_date IS NULL OR completion_date >= start_date)
);

-- Product categories table
CREATE TABLE product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    category_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    formulation TEXT,
    target_market TEXT,
    regulatory_requirements TEXT,
    status TEXT NOT NULL DEFAULT 'development' CHECK (status IN ('development', 'testing', 'production', 'discontinued')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Project milestones table
CREATE TABLE milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATETIME,
    completion_date DATETIME,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'in-progress', 'completed', 'delayed')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CHECK (completion_date IS NULL OR due_date IS NULL OR completion_date >= due_date)
);

-- Project tasks table
CREATE TABLE tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    milestone_id INTEGER,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    assigned_to TEXT,
    due_date DATETIME,
    completion_date DATETIME,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'in-progress', 'completed', 'delayed')),
    priority INTEGER DEFAULT 3 CHECK (priority BETWEEN 1 AND 5),
    FOREIGN KEY (milestone_id) REFERENCES milestones(milestone_id) ON DELETE SET NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CHECK (completion_date IS NULL OR due_date IS NULL OR completion_date >= due_date)
);

-- Project documents table
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK (type IN ('specification', 'formulation', 'report', 'contract', 'other')),
    file_path TEXT NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project meetings table
CREATE TABLE meetings (
    meeting_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    agenda TEXT,
    scheduled_time DATETIME NOT NULL,
    duration_minutes INTEGER CHECK (duration_minutes > 0),
    location TEXT,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Meeting participants table
CREATE TABLE meeting_participants (
    participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    meeting_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    email TEXT,
    role TEXT,
    attended BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (meeting_id) REFERENCES meetings(meeting_id) ON DELETE CASCADE
);

-- Project expenses table
CREATE TABLE expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    category TEXT NOT NULL CHECK (category IN ('materials', 'labor', 'testing', 'shipping', 'other')),
    amount REAL NOT NULL CHECK (amount > 0),
    description TEXT NOT NULL,
    expense_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    approved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project notes table
CREATE TABLE project_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    author TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_private BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_products_project ON products(project_id);
CREATE INDEX idx_tasks_project ON tasks(project_id);
CREATE INDEX idx_tasks_milestone ON tasks(milestone_id);
CREATE INDEX idx_milestones_project ON milestones(project_id);
CREATE INDEX idx_documents_project ON documents(project_id);
CREATE INDEX idx_expenses_project ON expenses(project_id);
```
