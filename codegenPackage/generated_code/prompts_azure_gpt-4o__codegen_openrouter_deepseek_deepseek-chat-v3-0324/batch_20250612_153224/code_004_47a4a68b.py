"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Create a database schema to store information about grain and fruit production, field mapping, and visit logs, ensuring compatibility with both web and mobile platforms as described on Azagros.
Generated: DETERMINISTIC_47a4a68bb43146a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Azagros grain and fruit production tracking system

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table to store user information
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'manager', 'field_agent', 'viewer')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Farms table
CREATE TABLE farms (
    farm_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    farm_name VARCHAR(100) NOT NULL,
    location GEOGRAPHY(POINT, 4326),
    address TEXT,
    total_area DECIMAL(10, 2), -- in hectares
    owner_id UUID REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Fields table
CREATE TABLE fields (
    field_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    field_name VARCHAR(100) NOT NULL,
    farm_id UUID REFERENCES farms(farm_id) ON DELETE CASCADE,
    crop_type VARCHAR(50) CHECK (crop_type IN ('grain', 'fruit', 'vegetable', 'other')),
    crop_variety VARCHAR(100),
    area DECIMAL(10, 2), -- in hectares
    planting_date DATE,
    expected_harvest_date DATE,
    soil_type VARCHAR(50),
    boundaries GEOGRAPHY(POLYGON, 4326),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Field visits table
CREATE TABLE field_visits (
    visit_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    field_id UUID REFERENCES fields(field_id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(user_id),
    visit_date TIMESTAMP WITH TIME ZONE NOT NULL,
    notes TEXT,
    health_status VARCHAR(20) CHECK (health_status IN ('excellent', 'good', 'fair', 'poor', 'critical')),
    growth_stage VARCHAR(50),
    pest_presence BOOLEAN DEFAULT FALSE,
    disease_presence BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Visit images table
CREATE TABLE visit_images (
    image_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    visit_id UUID REFERENCES field_visits(visit_id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    caption VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Production records table
CREATE TABLE production_records (
    record_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    field_id UUID REFERENCES fields(field_id) ON DELETE CASCADE,
    record_date DATE NOT NULL,
    yield_amount DECIMAL(10, 2), -- in kg or tons
    yield_unit VARCHAR(10) CHECK (yield_unit IN ('kg', 'ton')),
    quality_rating INTEGER CHECK (quality_rating BETWEEN 1 AND 5),
    harvest_method VARCHAR(50),
    storage_location VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Weather data table
CREATE TABLE weather_data (
    weather_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    field_id UUID REFERENCES fields(field_id) ON DELETE CASCADE,
    record_date DATE NOT NULL,
    temperature DECIMAL(5, 2), -- in Celsius
    humidity DECIMAL(5, 2), -- percentage
    rainfall DECIMAL(5, 2), -- in mm
    wind_speed DECIMAL(5, 2), -- in km/h
    weather_condition VARCHAR(50),
    source VARCHAR(50) CHECK (source IN ('station', 'api', 'manual')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Irrigation records table
CREATE TABLE irrigation_records (
    irrigation_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    field_id UUID REFERENCES fields(field_id) ON DELETE CASCADE,
    irrigation_date DATE NOT NULL,
    water_amount DECIMAL(10, 2), -- in liters
    method VARCHAR(50),
    duration_minutes INTEGER,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Fertilization records table
CREATE TABLE fertilization_records (
    fertilization_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    field_id UUID REFERENCES fields(field_id) ON DELETE CASCADE,
    application_date DATE NOT NULL,
    fertilizer_type VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2), -- in kg
    method VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Pest control records table
CREATE TABLE pest_control_records (
    control_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    field_id UUID REFERENCES fields(field_id) ON DELETE CASCADE,
    application_date DATE NOT NULL,
    pest_type VARCHAR(100),
    control_method VARCHAR(100) NOT NULL,
    product_used VARCHAR(100),
    amount DECIMAL(10, 2),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Field tasks table
CREATE TABLE field_tasks (
    task_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    field_id UUID REFERENCES fields(field_id) ON DELETE CASCADE,
    assigned_to UUID REFERENCES users(user_id),
    task_type VARCHAR(50) NOT NULL,
    description TEXT,
    due_date DATE,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'in_progress', 'completed', 'cancelled')),
    priority VARCHAR(10) CHECK (priority IN ('low', 'medium', 'high', 'critical')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Audit log table
CREATE TABLE audit_logs (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(user_id),
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    entity_id UUID,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_fields_farm_id ON fields(farm_id);
CREATE INDEX idx_field_visits_field_id ON field_visits(field_id);
CREATE INDEX idx_production_records_field_id ON production_records(field_id);
CREATE INDEX idx_weather_data_field_id ON weather_data(field_id);
CREATE INDEX idx_field_tasks_field_id ON field_tasks(field_id);
CREATE INDEX idx_field_tasks_assigned_to ON field_tasks(assigned_to);
CREATE INDEX idx_audit_logs_user_id ON audit_logs(user_id);

-- Create function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for tables with updated_at fields
CREATE TRIGGER update_users_timestamp
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_farms_timestamp
BEFORE UPDATE ON farms
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_fields_timestamp
BEFORE UPDATE ON fields
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_field_visits_timestamp
BEFORE UPDATE ON field_visits
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_production_records_timestamp
BEFORE UPDATE ON production_records
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_field_tasks_timestamp
BEFORE UPDATE ON field_tasks
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
