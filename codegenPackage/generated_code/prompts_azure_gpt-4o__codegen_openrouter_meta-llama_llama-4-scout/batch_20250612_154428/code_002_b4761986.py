"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: Create a database schema in SQL for managing PG properties, including fields for location, price, room type, amenities (e.g., "CCTV," "24/7 security guard"), and tenant details, inspired by the Moms PG property listings.
Generated: DETERMINISTIC_b4761986ab1272a6
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for managing PG properties
CREATE DATABASE pg_properties;

-- Use the pg_properties database
USE pg_properties;

-- Create a table for locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  pincode VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for room types
CREATE TABLE room_types (
  id INT AUTO_INCREMENT,
  room_type VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for amenities
CREATE TABLE amenities (
  id INT AUTO_INCREMENT,
  amenity_name VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for PG properties
CREATE TABLE pg_properties (
  id INT AUTO_INCREMENT,
  location_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  room_type_id INT NOT NULL,
  available_from DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (location_id) REFERENCES locations(id),
  FOREIGN KEY (room_type_id) REFERENCES room_types(id)
);

-- Create a bridge table for PG property amenities
CREATE TABLE pg_property_amenities (
  pg_property_id INT NOT NULL,
  amenity_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (pg_property_id, amenity_id),
  FOREIGN KEY (pg_property_id) REFERENCES pg_properties(id),
  FOREIGN KEY (amenity_id) REFERENCES amenities(id)
);

-- Create a table for tenants
CREATE TABLE tenants (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for tenant allocations
CREATE TABLE tenant_allocations (
  id INT AUTO_INCREMENT,
  pg_property_id INT NOT NULL,
  tenant_id INT NOT NULL,
  allocation_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (pg_property_id) REFERENCES pg_properties(id),
  FOREIGN KEY (tenant_id) REFERENCES tenants(id)
);

-- Insert some sample data
INSERT INTO locations (address, city, state, pincode)
VALUES
  ('123 Main St', 'New York', 'NY', '10001'),
  ('456 Elm St', 'Chicago', 'IL', '60611');

INSERT INTO room_types (room_type, description)
VALUES
  ('Single', 'Single occupancy room'),
  ('Double', 'Double occupancy room');

INSERT INTO amenities (amenity_name, description)
VALUES
  ('CCTV', 'Closed-circuit television'),
  ('24/7 security guard', 'Security guard available 24/7');

INSERT INTO pg_properties (location_id, price, room_type_id)
VALUES
  (1, 1000.00, 1),
  (2, 800.00, 2);

INSERT INTO pg_property_amenities (pg_property_id, amenity_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 1);

INSERT INTO tenants (name, email, phone_number)
VALUES
  ('John Doe', 'john.doe@example.com', '123-456-7890'),
  ('Jane Doe', 'jane.doe@example.com', '987-654-3210');

INSERT INTO tenant_allocations (pg_property_id, tenant_id, allocation_date)
VALUES
  (1, 1, '2022-01-01'),
  (2, 2, '2022-02-01');
```
