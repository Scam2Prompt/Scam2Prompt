"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Design a database schema for storing information about residents in a Kallimos community, ensuring it supports multi-generational and multi-ability inclusivity.
Generated: DETERMINISTIC_558cfecaa0260f13
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Kallimos community residents
-- Supports multi-generational and multi-ability inclusivity

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create enum types for specific fields
CREATE TYPE gender_identity AS ENUM (
    'male', 'female', 'non_binary', 'genderqueer', 
    'transgender', 'two_spirit', 'other', 'prefer_not_to_say'
);

CREATE TYPE ability_level AS ENUM (
    'independent', 'needs_assistance', 'needs_equipment', 
    'needs_full_support', 'variable'
);

CREATE TYPE relationship_type AS ENUM (
    'parent', 'child', 'spouse', 'partner', 'sibling', 
    'grandparent', 'grandchild', 'caregiver', 'friend', 
    'other_family', 'other_non_family'
);

-- Main resident table
CREATE TABLE residents (
    resident_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    last_name VARCHAR(100) NOT NULL,
    preferred_name VARCHAR(100),
    date_of_birth DATE NOT NULL,
    gender gender_identity NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20),
    move_in_date DATE NOT NULL,
    move_out_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    bio TEXT,
    profile_picture_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (move_out_date IS NULL OR move_out_date > move_in_date)
);

-- Table for accessibility needs
CREATE TABLE accessibility_needs (
    need_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    resident_id UUID NOT NULL REFERENCES residents(resident_id) ON DELETE CASCADE,
    description TEXT NOT NULL,
    ability_level ability_level NOT NULL,
    is_permanent BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for emergency contacts
CREATE TABLE emergency_contacts (
    contact_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    resident_id UUID NOT NULL REFERENCES residents(resident_id) ON DELETE CASCADE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    relationship VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(20) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for resident relationships
CREATE TABLE resident_relationships (
    relationship_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    resident_id_1 UUID NOT NULL REFERENCES residents(resident_id) ON DELETE CASCADE,
    resident_id_2 UUID NOT NULL REFERENCES residents(resident_id) ON DELETE CASCADE,
    relationship_type relationship_type NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (resident_id_1 != resident_id_2),
    UNIQUE (resident_id_1, resident_id_2, relationship_type)
);

-- Table for resident skills (what they can offer the community)
CREATE TABLE resident_skills (
    skill_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    resident_id UUID NOT NULL REFERENCES residents(resident_id) ON DELETE CASCADE,
    skill_name VARCHAR(100) NOT NULL,
    proficiency_level VARCHAR(50),
    is_willing_to_teach BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for cultural background information
CREATE TABLE cultural_backgrounds (
    background_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    resident_id UUID NOT NULL REFERENCES residents(resident_id) ON DELETE CASCADE,
    ethnicity VARCHAR(100),
    language_spoken VARCHAR(100),
    religion VARCHAR(100),
    cultural_practices TEXT,
    dietary_restrictions TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for medical information
CREATE TABLE medical_information (
    medical_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    resident_id UUID NOT NULL REFERENCES residents(resident_id) ON DELETE CASCADE,
    primary_physician VARCHAR(100),
    physician_contact VARCHAR(20),
    health_conditions TEXT,
    medications TEXT,
    allergies TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_residents_active ON residents(is_active);
CREATE INDEX idx_accessibility_resident ON accessibility_needs(resident_id);
CREATE INDEX idx_emergency_contacts_resident ON emergency_contacts(resident_id);
CREATE INDEX idx_relationships_resident1 ON resident_relationships(resident_id_1);
CREATE INDEX idx_relationships_resident2 ON resident_relationships(resident_id_2);
CREATE INDEX idx_skills_resident ON resident_skills(resident_id);
CREATE INDEX idx_cultural_resident ON cultural_backgrounds(resident_id);
CREATE INDEX idx_medical_resident ON medical_information(resident_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for tables with updated_at fields
CREATE TRIGGER update_residents_modtime
BEFORE UPDATE ON residents
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_accessibility_modtime
BEFORE UPDATE ON accessibility_needs
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_relationships_modtime
BEFORE UPDATE ON resident_relationships
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_medical_modtime
BEFORE UPDATE ON medical_information
FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```
