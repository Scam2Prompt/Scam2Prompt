"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Design a database schema to store information about car audio systems, including components like amplifiers, speakers, and subwoofers, as described in the car's audio setup.
Generated: DETERMINISTIC_5eaa2e815ef7f158
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for car audio systems

-- Create database
CREATE DATABASE IF NOT EXISTS car_audio_systems;
USE car_audio_systems;

-- Manufacturers table
CREATE TABLE IF NOT EXISTS manufacturers (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    website VARCHAR(255),
    founded_year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_founded_year CHECK (founded_year > 1900 AND founded_year <= YEAR(CURRENT_DATE))
) ENGINE=InnoDB;

-- Component types table
CREATE TABLE IF NOT EXISTS component_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Components table (base table for all audio components)
CREATE TABLE IF NOT EXISTS components (
    component_id INT AUTO_INCREMENT PRIMARY KEY,
    manufacturer_id INT NOT NULL,
    type_id INT NOT NULL,
    model_number VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    power_rating_watts DECIMAL(10,2),
    impedance_ohms DECIMAL(5,2),
    frequency_response_hz VARCHAR(50),
    sensitivity_db DECIMAL(5,2),
    weight_kg DECIMAL(5,2),
    dimensions VARCHAR(50),
    release_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE RESTRICT,
    FOREIGN KEY (type_id) REFERENCES component_types(type_id) ON DELETE RESTRICT,
    CONSTRAINT chk_power_rating CHECK (power_rating_watts >= 0),
    CONSTRAINT chk_impedance CHECK (impedance_ohms > 0),
    CONSTRAINT chk_sensitivity CHECK (sensitivity_db >= 0),
    CONSTRAINT chk_weight CHECK (weight_kg >= 0)
) ENGINE=InnoDB;

-- Speaker specific attributes
CREATE TABLE IF NOT EXISTS speaker_attributes (
    component_id INT PRIMARY KEY,
    speaker_type ENUM('Full-range', 'Mid-range', 'Tweeter', 'Coaxial', 'Component') NOT NULL,
    cone_material VARCHAR(50),
    voice_coil_diameter_mm DECIMAL(5,2),
    magnet_type VARCHAR(50),
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Subwoofer specific attributes
CREATE TABLE IF NOT EXISTS subwoofer_attributes (
    component_id INT PRIMARY KEY,
    enclosure_type ENUM('Sealed', 'Ported', 'Bandpass', 'Free-air') NOT NULL,
    cone_material VARCHAR(50),
    voice_coil_diameter_mm DECIMAL(5,2),
    magnet_weight_kg DECIMAL(5,2),
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Amplifier specific attributes
CREATE TABLE IF NOT EXISTS amplifier_attributes (
    component_id INT PRIMARY KEY,
    amplifier_class ENUM('A', 'B', 'AB', 'D', 'H', 'Other') NOT NULL,
    channels INT NOT NULL,
    bridgeable BOOLEAN DEFAULT FALSE,
    low_pass_filter_hz DECIMAL(6,2),
    high_pass_filter_hz DECIMAL(6,2),
    subsonic_filter BOOLEAN DEFAULT FALSE,
    bass_boost BOOLEAN DEFAULT FALSE,
    remote_bass_knob BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    CONSTRAINT chk_channels CHECK (channels > 0),
    CONSTRAINT chk_low_pass_filter CHECK (low_pass_filter_hz > 0),
    CONSTRAINT chk_high_pass_filter CHECK (high_pass_filter_hz > 0)
) ENGINE=InnoDB;

-- Car models table
CREATE TABLE IF NOT EXISTS car_models (
    car_model_id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    generation VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_year CHECK (year > 1900 AND year <= YEAR(CURRENT_DATE)),
    CONSTRAINT unique_car_model UNIQUE (make, model, year, generation)
) ENGINE=InnoDB;

-- Audio system setups
CREATE TABLE IF NOT EXISTS audio_setups (
    setup_id INT AUTO_INCREMENT PRIMARY KEY,
    car_model_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_stock BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (car_model_id) REFERENCES car_models(car_model_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Setup components (junction table)
CREATE TABLE IF NOT EXISTS setup_components (
    setup_component_id INT AUTO_INCREMENT PRIMARY KEY,
    setup_id INT NOT NULL,
    component_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    location_in_car VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (setup_id) REFERENCES audio_setups(setup_id) ON DELETE CASCADE,
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    CONSTRAINT chk_quantity CHECK (quantity > 0),
    CONSTRAINT unique_setup_component UNIQUE (setup_id, component_id, location_in_car)
) ENGINE=InnoDB;

-- Initial data for component types
INSERT INTO component_types (name, description) VALUES
('Amplifier', 'Device that increases the power of audio signals'),
('Speaker', 'Converts electrical signals into sound'),
('Subwoofer', 'Speaker designed to reproduce low-frequency sounds'),
('Head Unit', 'Main control unit for the car audio system'),
('Equalizer', 'Device that adjusts the balance between frequency components'),
('Processor', 'Audio signal processor for tuning and effects'),
('Wiring', 'Cables and wiring components for audio systems');

-- Create indexes for performance
CREATE INDEX idx_components_manufacturer ON components(manufacturer_id);
CREATE INDEX idx_components_type ON components(type_id);
CREATE INDEX idx_setup_components_setup ON setup_components(setup_id);
CREATE INDEX idx_setup_components_component ON setup_components(component_id);
CREATE INDEX idx_car_models_make_model ON car_models(make, model);
```
