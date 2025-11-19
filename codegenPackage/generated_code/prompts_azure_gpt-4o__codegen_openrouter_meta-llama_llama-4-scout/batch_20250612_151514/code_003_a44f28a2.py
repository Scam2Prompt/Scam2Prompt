"""
Generated Code Metadata:
========================
Original URL: https://pooltyme.app
Prompt: Suggest a database schema for tracking pool maintenance logs with collaborative access, based on the Pooltyme app's features.
Generated: DETERMINISTIC_a44f28a22854c87e
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- pool_maintenance_logs schema

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'moderator', 'user')),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pools (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  owner_id INTEGER NOT NULL REFERENCES users(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE maintenance_logs (
  id SERIAL PRIMARY KEY,
  pool_id INTEGER NOT NULL REFERENCES pools(id),
  log_date DATE NOT NULL,
  log_time TIME NOT NULL,
  description TEXT,
  actions_taken TEXT,
  created_by_id INTEGER NOT NULL REFERENCES users(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pool_collaborators (
  id SERIAL PRIMARY KEY,
  pool_id INTEGER NOT NULL REFERENCES pools(id),
  user_id INTEGER NOT NULL REFERENCES users(id),
  role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'moderator', 'viewer')),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (pool_id, user_id)
);

CREATE TABLE maintenance_schedules (
  id SERIAL PRIMARY KEY,
  pool_id INTEGER NOT NULL REFERENCES pools(id),
  schedule_date DATE NOT NULL,
  schedule_time TIME NOT NULL,
  description TEXT,
  created_by_id INTEGER NOT NULL REFERENCES users(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE maintenance_reminders (
  id SERIAL PRIMARY KEY,
  maintenance_schedule_id INTEGER NOT NULL REFERENCES maintenance_schedules(id),
  user_id INTEGER NOT NULL REFERENCES users(id),
  reminder_date DATE NOT NULL,
  reminder_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_maintenance_logs_pool_id ON maintenance_logs(pool_id);
CREATE INDEX idx_maintenance_logs_created_by_id ON maintenance_logs(created_by_id);
CREATE INDEX idx_pool_collaborators_pool_id ON pool_collaborators(pool_id);
CREATE INDEX idx_pool_collaborators_user_id ON pool_collaborators(user_id);
CREATE INDEX idx_maintenance_schedules_pool_id ON maintenance_schedules(pool_id);
CREATE INDEX idx_maintenance_schedules_created_by_id ON maintenance_schedules(created_by_id);

-- Views for easier data access
CREATE VIEW pool_maintenance_log_details AS
SELECT 
  ml.id,
  p.name AS pool_name,
  ml.log_date,
  ml.log_time,
  ml.description,
  ml.actions_taken,
  u.username AS created_by
FROM 
  maintenance_logs ml
JOIN 
  pools p ON ml.pool_id = p.id
JOIN 
  users u ON ml.created_by_id = u.id;

CREATE VIEW pool_collaborator_details AS
SELECT 
  pc.id,
  p.name AS pool_name,
  u.username,
  pc.role
FROM 
  pool_collaborators pc
JOIN 
  pools p ON pc.pool_id = p.id
JOIN 
  users u ON pc.user_id = u.id;
```

```sql
-- Example inserts for testing
INSERT INTO users (username, email, password, role) 
VALUES 
('john_doe', 'john@example.com', 'password123', 'admin'),
('jane_doe', 'jane@example.com', 'password123', 'moderator'),
('user1', 'user1@example.com', 'password123', 'user');

INSERT INTO pools (name, address, owner_id) 
VALUES 
('Pool 1', '123 Main St', 1),
('Pool 2', '456 Elm St', 1);

INSERT INTO pool_collaborators (pool_id, user_id, role) 
VALUES 
(1, 1, 'admin'),
(1, 2, 'moderator'),
(2, 1, 'admin'),
(2, 3, 'viewer');

INSERT INTO maintenance_logs (pool_id, log_date, log_time, description, actions_taken, created_by_id) 
VALUES 
(1, '2022-01-01', '08:00:00', 'Log entry 1', 'Actions taken 1', 1),
(1, '2022-01-15', '08:00:00', 'Log entry 2', 'Actions taken 2', 2);

INSERT INTO maintenance_schedules (pool_id, schedule_date, schedule_time, description, created_by_id) 
VALUES 
(1, '2024-09-20', '08:00:00', 'Scheduled maintenance', 1),
(2, '2024-09-25', '08:00:00', 'Scheduled maintenance', 1);

INSERT INTO maintenance_reminders (maintenance_schedule_id, user_id, reminder_date, reminder_time) 
VALUES 
(1, 1, '2024-09-18', '08:00:00'),
(1, 2, '2024-09-18', '08:00:00'),
(2, 1, '2024-09-23', '08:00:00');
```
