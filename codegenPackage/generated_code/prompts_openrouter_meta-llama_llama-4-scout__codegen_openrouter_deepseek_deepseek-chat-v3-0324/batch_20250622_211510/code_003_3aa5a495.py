"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: "Design a database schema for a construction project management system, incorporating features like project tracking, team collaboration, and client communication, similar to Albatros SPA's approach to project management."
Generated: DETERMINISTIC_3aa5a495f2b19d9e
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Construction Project Management System

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table to store all system users
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'project_manager', 'team_member', 'client')),
    phone_number VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE
);

-- Projects table
CREATE TABLE projects (
    project_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(50) NOT NULL CHECK (status IN ('planned', 'in_progress', 'on_hold', 'completed', 'cancelled')),
    budget DECIMAL(15, 2),
    client_id UUID REFERENCES users(user_id),
    project_manager_id UUID REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Project team members junction table
CREATE TABLE project_team_members (
    project_id UUID REFERENCES projects(project_id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(user_id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL CHECK (role IN ('manager', 'engineer', 'architect', 'contractor', 'supervisor')),
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (project_id, user_id)
);

-- Tasks table
CREATE TABLE tasks (
    task_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(project_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) NOT NULL CHECK (status IN ('todo', 'in_progress', 'in_review', 'completed', 'blocked')),
    priority VARCHAR(20) CHECK (priority IN ('low', 'medium', 'high', 'critical')),
    due_date DATE,
    assigned_to UUID REFERENCES users(user_id),
    created_by UUID REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Task dependencies
CREATE TABLE task_dependencies (
    task_id UUID REFERENCES tasks(task_id) ON DELETE CASCADE,
    depends_on_task_id UUID REFERENCES tasks(task_id) ON DELETE CASCADE,
    dependency_type VARCHAR(50) CHECK (dependency_type IN ('fs', 'ff', 'ss', 'sf')),
    PRIMARY KEY (task_id, depends_on_task_id)
);

-- Documents table
CREATE TABLE documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(project_id) ON DELETE CASCADE,
    uploaded_by UUID REFERENCES users(user_id),
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_type VARCHAR(100),
    file_size BIGINT,
    description TEXT,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    version VARCHAR(50)
);

-- Communication (messages/comments)
CREATE TABLE communications (
    communication_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(project_id) ON DELETE CASCADE,
    sender_id UUID REFERENCES users(user_id),
    message TEXT NOT NULL,
    parent_id UUID REFERENCES communications(communication_id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_read BOOLEAN DEFAULT FALSE
);

-- Communication recipients
CREATE TABLE communication_recipients (
    communication_id UUID REFERENCES communications(communication_id) ON DELETE CASCADE,
    recipient_id UUID REFERENCES users(user_id),
    PRIMARY KEY (communication_id, recipient_id)
);

-- Meetings table
CREATE TABLE meetings (
    meeting_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(project_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    location VARCHAR(255),
    organizer_id UUID REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Meeting attendees
CREATE TABLE meeting_attendees (
    meeting_id UUID REFERENCES meetings(meeting_id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(user_id),
    attendance_status VARCHAR(20) CHECK (attendance_status IN ('pending', 'accepted', 'declined')),
    PRIMARY KEY (meeting_id, user_id)
);

-- Project milestones
CREATE TABLE milestones (
    milestone_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(project_id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed_date DATE,
    status VARCHAR(50) NOT NULL CHECK (status IN ('pending', 'completed', 'delayed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Time tracking
CREATE TABLE time_entries (
    time_entry_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id),
    task_id UUID REFERENCES tasks(task_id) ON DELETE SET NULL,
    project_id UUID REFERENCES projects(project_id) ON DELETE CASCADE,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Expense tracking
CREATE TABLE expenses (
    expense_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID REFERENCES projects(project_id) ON DELETE CASCADE,
    category VARCHAR(100) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    description TEXT,
    expense_date DATE NOT NULL,
    submitted_by UUID REFERENCES users(user_id),
    approved_by UUID REFERENCES users(user_id),
    status VARCHAR(50) NOT NULL CHECK (status IN ('pending', 'approved', 'rejected')),
    receipt_path VARCHAR(512),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Audit log for tracking changes
CREATE TABLE audit_log (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id),
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(100) NOT NULL,
    record_id UUID,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_tasks_project_id ON tasks(project_id);
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_assigned_to ON tasks(assigned_to);
CREATE INDEX idx_time_entries_user_id ON time_entries(user_id);
CREATE INDEX idx_time_entries_project_id ON time_entries(project_id);
CREATE INDEX idx_communications_project_id ON communications(project_id);
CREATE INDEX idx_documents_project_id ON documents(project_id);

-- Function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_project_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_task_timestamp
BEFORE UPDATE ON tasks
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_milestone_timestamp
BEFORE UPDATE ON milestones
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_expense_timestamp
BEFORE UPDATE ON expenses
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_meeting_timestamp
BEFORE UPDATE ON meetings
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
