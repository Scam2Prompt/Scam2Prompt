"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Create a database schema for managing cleaning service plans (weekly, biweekly, monthly) and tracking customer preferences for specific cleaning details.
Generated: DETERMINISTIC_8178cc03e562e8b9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for cleaning service management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create table for customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for cleaning service plans
CREATE TABLE IF NOT EXISTS service_plans (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_name TEXT NOT NULL UNIQUE,
    frequency TEXT NOT NULL CHECK(frequency IN ('weekly', 'biweekly', 'monthly')),
    base_price DECIMAL(10, 2) NOT NULL CHECK(base_price >= 0),
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for cleaning tasks
CREATE TABLE IF NOT EXISTS cleaning_tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL UNIQUE,
    description TEXT,
    standard_duration_minutes INTEGER CHECK(standard_duration_minutes > 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for plan tasks (many-to-many relationship between plans and tasks)
CREATE TABLE IF NOT EXISTS plan_tasks (
    plan_task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    is_optional BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plan_id) REFERENCES service_plans(plan_id) ON DELETE CASCADE,
    FOREIGN KEY (task_id) REFERENCES cleaning_tasks(task_id) ON DELETE CASCADE,
    UNIQUE(plan_id, task_id)
);

-- Create table for customer subscriptions
CREATE TABLE IF NOT EXISTS customer_subscriptions (
    subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    plan_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    special_instructions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES service_plans(plan_id) ON DELETE RESTRICT
);

-- Create table for customer preferences (customizations to their plan)
CREATE TABLE IF NOT EXISTS customer_preferences (
    preference_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subscription_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    preference_type TEXT NOT NULL CHECK(preference_type IN ('include', 'exclude', 'modify')),
    preference_details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subscription_id) REFERENCES customer_subscriptions(subscription_id) ON DELETE CASCADE,
    FOREIGN KEY (task_id) REFERENCES cleaning_tasks(task_id) ON DELETE CASCADE,
    UNIQUE(subscription_id, task_id)
);

-- Create table for cleaning service appointments
CREATE TABLE IF NOT EXISTS service_appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subscription_id INTEGER NOT NULL,
    scheduled_date DATE NOT NULL,
    scheduled_time TIME NOT NULL,
    actual_start_time TIMESTAMP,
    actual_end_time TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('scheduled', 'in-progress', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subscription_id) REFERENCES customer_subscriptions(subscription_id) ON DELETE CASCADE
);

-- Create table for appointment tasks (what was actually done)
CREATE TABLE IF NOT EXISTS appointment_tasks (
    appointment_task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('completed', 'skipped', 'partial')),
    notes TEXT,
    duration_minutes INTEGER CHECK(duration_minutes > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (appointment_id) REFERENCES service_appointments(appointment_id) ON DELETE CASCADE,
    FOREIGN KEY (task_id) REFERENCES cleaning_tasks(task_id) ON DELETE RESTRICT
);

-- Create trigger to update timestamp on customer updates
CREATE TRIGGER IF NOT EXISTS update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

-- Create trigger to update timestamp on service plan updates
CREATE TRIGGER IF NOT EXISTS update_service_plan_timestamp
AFTER UPDATE ON service_plans
FOR EACH ROW
BEGIN
    UPDATE service_plans SET updated_at = CURRENT_TIMESTAMP WHERE plan_id = OLD.plan_id;
END;

-- Create trigger to update timestamp on subscription updates
CREATE TRIGGER IF NOT EXISTS update_subscription_timestamp
AFTER UPDATE ON customer_subscriptions
FOR EACH ROW
BEGIN
    UPDATE customer_subscriptions SET updated_at = CURRENT_TIMESTAMP WHERE subscription_id = OLD.subscription_id;
END;

-- Create trigger to update timestamp on preference updates
CREATE TRIGGER IF NOT EXISTS update_preference_timestamp
AFTER UPDATE ON customer_preferences
FOR EACH ROW
BEGIN
    UPDATE customer_preferences SET updated_at = CURRENT_TIMESTAMP WHERE preference_id = OLD.preference_id;
END;

-- Create index for frequently queried fields
CREATE INDEX IF NOT EXISTS idx_customer_email ON customers(email);
CREATE INDEX IF NOT EXISTS idx_subscription_customer ON customer_subscriptions(customer_id);
CREATE INDEX IF NOT EXISTS idx_subscription_plan ON customer_subscriptions(plan_id);
CREATE INDEX IF NOT EXISTS idx_appointment_date ON service_appointments(scheduled_date);
CREATE INDEX IF NOT EXISTS idx_appointment_status ON service_appointments(status);
```
