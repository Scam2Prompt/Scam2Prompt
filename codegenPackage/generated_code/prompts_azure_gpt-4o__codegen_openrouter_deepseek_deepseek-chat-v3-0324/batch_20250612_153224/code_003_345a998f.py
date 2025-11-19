"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Provide an example of a database schema for managing governance policies and organizational decisions, inspired by the "الحوكمة السياسات واللوائح" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_345a998f4a95907b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Governance Policies and Organizational Decisions Management
-- Inspired by جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS organizations (
    organization_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    establishment_date DATE,
    status TEXT CHECK(status IN ('active', 'inactive', 'suspended')) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS policy_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    organization_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS policies (
    policy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    version TEXT NOT NULL,
    effective_date DATE NOT NULL,
    review_date DATE,
    status TEXT CHECK(status IN ('draft', 'active', 'archived', 'under_review')) DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES policy_categories(category_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS policy_attachments (
    attachment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_id INTEGER NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_type TEXT,
    file_size INTEGER,
    description TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS decision_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    organization_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS decisions (
    decision_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    type_id INTEGER NOT NULL,
    decision_date DATE NOT NULL,
    effective_date DATE,
    status TEXT CHECK(status IN ('proposed', 'approved', 'rejected', 'implemented')) DEFAULT 'proposed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES decision_types(type_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS decision_votes (
    vote_id INTEGER PRIMARY KEY AUTOINCREMENT,
    decision_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    vote_value TEXT CHECK(vote_value IN ('yes', 'no', 'abstain')) NOT NULL,
    comments TEXT,
    voted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (decision_id) REFERENCES decisions(decision_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS policy_reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_id INTEGER NOT NULL,
    review_date DATE NOT NULL,
    reviewed_by TEXT NOT NULL,
    review_notes TEXT,
    status TEXT CHECK(status IN ('approved', 'needs_revision', 'rejected')) NOT NULL,
    next_review_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS policy_compliance (
    compliance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_id INTEGER NOT NULL,
    check_date DATE NOT NULL,
    checked_by TEXT NOT NULL,
    compliance_status TEXT CHECK(compliance_status IN ('compliant', 'non_compliant', 'partial')) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (policy_id) REFERENCES policies(policy_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_policies_category ON policies(category_id);
CREATE INDEX IF NOT EXISTS idx_policies_status ON policies(status);
CREATE INDEX IF NOT EXISTS idx_decisions_type ON decisions(type_id);
CREATE INDEX IF NOT EXISTS idx_decisions_status ON decisions(status);
CREATE INDEX IF NOT EXISTS idx_votes_decision ON decision_votes(decision_id);
CREATE INDEX IF NOT EXISTS idx_policy_reviews ON policy_reviews(policy_id);
CREATE INDEX IF NOT EXISTS idx_policy_compliance ON policy_compliance(policy_id);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_organization_timestamp
AFTER UPDATE ON organizations
FOR EACH ROW
BEGIN
    UPDATE organizations SET updated_at = CURRENT_TIMESTAMP WHERE organization_id = NEW.organization_id;
END;

CREATE TRIGGER IF NOT EXISTS update_policy_category_timestamp
AFTER UPDATE ON policy_categories
FOR EACH ROW
BEGIN
    UPDATE policy_categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = NEW.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_policy_timestamp
AFTER UPDATE ON policies
FOR EACH ROW
BEGIN
    UPDATE policies SET updated_at = CURRENT_TIMESTAMP WHERE policy_id = NEW.policy_id;
END;

CREATE TRIGGER IF NOT EXISTS update_decision_type_timestamp
AFTER UPDATE ON decision_types
FOR EACH ROW
BEGIN
    UPDATE decision_types SET updated_at = CURRENT_TIMESTAMP WHERE type_id = NEW.type_id;
END;

CREATE TRIGGER IF NOT EXISTS update_decision_timestamp
AFTER UPDATE ON decisions
FOR EACH ROW
BEGIN
    UPDATE decisions SET updated_at = CURRENT_TIMESTAMP WHERE decision_id = NEW.decision_id;
END;
```
