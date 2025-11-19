"""
Generated Code Metadata:
========================
Original URL: https://corfucoastalcollection.com
Prompt: Create a SQL database schema to store information about villas and plots for sale in Corfu, including fields for location, price, and features like sea view.
Generated: DETERMINISTIC_604192fcac96a24d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Corfu Villas and Plots Database

CREATE TABLE locations (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    area VARCHAR(100) NOT NULL,
    district VARCHAR(100) NOT NULL,
    coordinates POINT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_area (area),
    INDEX idx_district (district)
);

CREATE TABLE properties (
    property_id INT PRIMARY KEY AUTO_INCREMENT,
    location_id INT NOT NULL,
    property_type ENUM('villa', 'plot') NOT NULL,
    title VARCHAR(200) NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    area_sqm DECIMAL(10, 2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    listing_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    INDEX idx_property_type (property_type),
    INDEX idx_price (price),
    INDEX idx_availability (is_available)
);

CREATE TABLE villa_features (
    feature_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT NOT NULL,
    bedrooms INT NOT NULL,
    bathrooms INT NOT NULL,
    floors INT NOT NULL,
    has_pool BOOLEAN DEFAULT FALSE,
    has_garden BOOLEAN DEFAULT FALSE,
    has_garage BOOLEAN DEFAULT FALSE,
    sea_view BOOLEAN DEFAULT FALSE,
    distance_to_sea DECIMAL(5, 2) COMMENT 'Distance in meters',
    construction_year YEAR,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    INDEX idx_sea_view (sea_view),
    INDEX idx_bedrooms (bedrooms)
);

CREATE TABLE plot_features (
    feature_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT NOT NULL,
    is_flat BOOLEAN DEFAULT FALSE,
    has_road_access BOOLEAN DEFAULT TRUE,
    has_utilities BOOLEAN DEFAULT FALSE,
    zoning_type VARCHAR(50),
    sea_view BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    INDEX idx_sea_view (sea_view),
    INDEX idx_zoning (zoning_type)
);

CREATE TABLE property_media (
    media_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT NOT NULL,
    media_type ENUM('image', 'video', 'document') NOT NULL,
    url VARCHAR(255) NOT NULL,
    caption VARCHAR(200),
    is_primary BOOLEAN DEFAULT FALSE,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    INDEX idx_primary (is_primary)
);

CREATE TABLE property_tags (
    tag_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT NOT NULL,
    tag VARCHAR(50) NOT NULL,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    INDEX idx_tag (tag)
);

CREATE TABLE price_history (
    history_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT NOT NULL,
    old_price DECIMAL(12, 2) NOT NULL,
    new_price DECIMAL(12, 2) NOT NULL,
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    change_reason VARCHAR(200),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    INDEX idx_change_date (change_date)
);
```
