"""
Generated Code Metadata:
========================
Original URL: https://bda.mcupr.ac.th
Prompt: "Design a database schema to store information about various Buddhist art pieces, including the พระพุทธรูปประจําวันเกิดวันพฤหัสบดี พระปางตรัสรู้หรือปางสมาธิ."
Generated: DETERMINISTIC_20f2866787d1ed31
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Buddhist art pieces
CREATE TABLE artists (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_year INTEGER,
    death_year INTEGER,
    nationality VARCHAR(50),
    biography TEXT
);

CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE periods (
    period_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    start_year INTEGER,
    end_year INTEGER,
    description TEXT
);

CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    country VARCHAR(50),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8)
);

CREATE TABLE mudras (
    mudra_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    meaning TEXT
);

CREATE TABLE buddha_images (
    image_id SERIAL PRIMARY KEY,
    thai_name VARCHAR(100) NOT NULL,
    english_name VARCHAR(100),
    description TEXT,
    height_cm DECIMAL(8, 2),
    width_cm DECIMAL(8, 2),
    depth_cm DECIMAL(8, 2),
    weight_kg DECIMAL(8, 2),
    creation_year INTEGER,
    artist_id INTEGER REFERENCES artists(artist_id),
    material_id INTEGER REFERENCES materials(material_id),
    period_id INTEGER REFERENCES periods(period_id),
    current_location_id INTEGER REFERENCES locations(location_id),
    mudra_id INTEGER REFERENCES mudras(mudra_id),
    is_birthday_image BOOLEAN DEFAULT FALSE,
    weekday VARCHAR(10) CHECK (weekday IN ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')),
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE image_attributes (
    attribute_id SERIAL PRIMARY KEY,
    image_id INTEGER REFERENCES buddha_images(image_id) ON DELETE CASCADE,
    attribute_name VARCHAR(50) NOT NULL,
    attribute_value TEXT NOT NULL
);

CREATE TABLE image_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE image_category_mapping (
    mapping_id SERIAL PRIMARY KEY,
    image_id INTEGER REFERENCES buddha_images(image_id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES image_categories(category_id) ON DELETE CASCADE,
    UNIQUE (image_id, category_id)
);

-- Indexes for better performance
CREATE INDEX idx_buddha_images_weekday ON buddha_images(weekday);
CREATE INDEX idx_buddha_images_mudra ON buddha_images(mudra_id);
CREATE INDEX idx_buddha_images_material ON buddha_images(material_id);
CREATE INDEX idx_buddha_images_period ON buddha_images(period_id);

-- Trigger to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_buddha_images_timestamp
BEFORE UPDATE ON buddha_images
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

-- Insert sample data for Thursday Buddha image
INSERT INTO mudras (name, description, meaning) VALUES 
('Dhyana Mudra', 'Meditation gesture', 'Represents concentration, meditation, and attainment of spiritual perfection');

INSERT INTO buddha_images (
    thai_name, 
    english_name, 
    description, 
    is_birthday_image, 
    weekday, 
    mudra_id
) VALUES (
    'พระพุทธรูปประจําวันเกิดวันพฤหัสบดี พระปางตรัสรู้หรือปางสมาธิ', 
    'Thursday Buddha Image in Enlightenment or Meditation Posture', 
    'The Buddha image for those born on Thursday, in either the Enlightenment or Meditation posture', 
    TRUE, 
    'Thursday', 
    1
);
```
