"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Create a SQL database schema to manage photography client information, photo shoots, and image metadata for a studio like Officine dell'Immagine.
Generated: DETERMINISTIC_4bfff7088c3059b3
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for photography studio
CREATE DATABASE photography_studio;

-- Use the created database
USE photography_studio;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for photo shoots
CREATE TABLE photo_shoots (
  shoot_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  shoot_date DATE NOT NULL,
  shoot_location VARCHAR(255) NOT NULL,
  shoot_type VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (shoot_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for images
CREATE TABLE images (
  image_id INT AUTO_INCREMENT,
  shoot_id INT NOT NULL,
  image_filename VARCHAR(255) NOT NULL,
  image_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (image_id),
  FOREIGN KEY (shoot_id) REFERENCES photo_shoots(shoot_id) ON DELETE CASCADE
);

-- Create table for image metadata
CREATE TABLE image_metadata (
  metadata_id INT AUTO_INCREMENT,
  image_id INT NOT NULL,
  camera_model VARCHAR(50),
  lens_model VARCHAR(50),
  aperture FLOAT,
  shutter_speed FLOAT,
  iso INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (metadata_id),
  FOREIGN KEY (image_id) REFERENCES images(image_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_client_id ON photo_shoots (client_id);
CREATE INDEX idx_shoot_id ON images (shoot_id);
CREATE INDEX idx_image_id ON image_metadata (image_id);
```

```sql
-- Example insert statements
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO photo_shoots (client_id, shoot_date, shoot_location, shoot_type)
VALUES (1, '2022-01-01', 'New York', 'Portrait');

INSERT INTO images (shoot_id, image_filename, image_description)
VALUES (1, 'image1.jpg', 'Client portrait');

INSERT INTO image_metadata (image_id, camera_model, lens_model, aperture, shutter_speed, iso)
VALUES (1, 'Canon EOS 5D', 'EF 50mm f/1.2L', 2.8, 1/125, 200);

INSERT INTO payments (client_id, payment_date, payment_amount, payment_method)
VALUES (1, '2022-01-15', 1000.00, 'Credit Card');
```
