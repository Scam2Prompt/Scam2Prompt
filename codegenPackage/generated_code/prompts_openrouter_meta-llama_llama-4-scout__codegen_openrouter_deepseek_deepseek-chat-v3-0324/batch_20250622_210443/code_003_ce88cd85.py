"""
Generated Code Metadata:
========================
Original URL: https://safargenie.com
Prompt: "Design a database schema for storing information about tour packages, including destinations, themes, and pricing, for a travel company like SafarGenie."
Generated: DETERMINISTIC_ce88cd8598fba7c7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Tour Packages (PostgreSQL)

```sql
-- Database schema for SafarGenie tour packages
-- Includes tables for destinations, themes, pricing, and package details

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for storing destination information
CREATE TABLE destinations (
    destination_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    region VARCHAR(100),
    description TEXT,
    climate VARCHAR(50),
    best_time_to_visit VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_destination_name_country UNIQUE (name, country)
);

-- Table for storing tour themes/categories
CREATE TABLE themes (
    theme_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing tour packages
CREATE TABLE tour_packages (
    package_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    duration_days INTEGER NOT NULL CHECK (duration_days > 0),
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('Easy', 'Moderate', 'Challenging', 'Expert')),
    min_group_size INTEGER DEFAULT 1 CHECK (min_group_size > 0),
    max_group_size INTEGER CHECK (max_group_size >= min_group_size),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for package-destination relationship (many-to-many)
CREATE TABLE package_destinations (
    package_id UUID REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    destination_id UUID REFERENCES destinations(destination_id) ON DELETE CASCADE,
    is_primary BOOLEAN DEFAULT FALSE,
    visit_order INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (package_id, destination_id)
);

-- Junction table for package-theme relationship (many-to-many)
CREATE TABLE package_themes (
    package_id UUID REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    theme_id UUID REFERENCES themes(theme_id) ON DELETE CASCADE,
    PRIMARY KEY (package_id, theme_id)
);

-- Table for storing pricing information
CREATE TABLE package_pricing (
    pricing_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    package_id UUID NOT NULL REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    price_per_person DECIMAL(10, 2) NOT NULL CHECK (price_per_person > 0),
    currency VARCHAR(3) DEFAULT 'USD',
    valid_from DATE NOT NULL,
    valid_to DATE,
    is_current BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_date_range CHECK (valid_to IS NULL OR valid_to >= valid_from)
);

-- Table for storing inclusions (what's included in the package)
CREATE TABLE package_inclusions (
    inclusion_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    package_id UUID NOT NULL REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    description TEXT NOT NULL,
    category VARCHAR(50) CHECK (category IN ('Accommodation', 'Meals', 'Transport', 'Activities', 'Other')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing exclusions (what's not included in the package)
CREATE TABLE package_exclusions (
    exclusion_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    package_id UUID NOT NULL REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    description TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing itinerary details
CREATE TABLE package_itinerary (
    itinerary_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    package_id UUID NOT NULL REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    day_number INTEGER NOT NULL CHECK (day_number > 0),
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    accommodation VARCHAR(200),
    meals_included VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_day_per_package UNIQUE (package_id, day_number)
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for all tables with updated_at fields
CREATE TRIGGER update_destinations_modtime
BEFORE UPDATE ON destinations
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_themes_modtime
BEFORE UPDATE ON themes
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_tour_packages_modtime
BEFORE UPDATE ON tour_packages
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

-- Indexes for performance optimization
CREATE INDEX idx_package_destinations_destination ON package_destinations(destination_id);
CREATE INDEX idx_package_themes_theme ON package_themes(theme_id);
CREATE INDEX idx_package_pricing_package ON package_pricing(package_id);
CREATE INDEX idx_package_pricing_current ON package_pricing(is_current);
CREATE INDEX idx_package_itinerary_package ON package_itinerary(package_id);
```
