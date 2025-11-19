"""
Generated Code Metadata:
========================
Original URL: https://celestia.events
Prompt: Design a database schema for storing information about events, performers, artists, and vendors for a festival like Celestia, and write a brief explanation of the schema.
Generated: DETERMINISTIC_bbd61c9732f18fd4
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the festival
CREATE DATABASE festival;

-- Use the festival database
USE festival;

-- Create a table for artists
CREATE TABLE artists (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for performers
CREATE TABLE performers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  artist_id INT,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE SET NULL
);

-- Create a table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_time DATETIME NOT NULL,
  end_time DATETIME NOT NULL,
  performer_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (performer_id) REFERENCES performers(id) ON DELETE SET NULL
);

-- Create a table for vendors
CREATE TABLE vendors (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for vendor products
CREATE TABLE vendor_products (
  id INT AUTO_INCREMENT,
  vendor_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (vendor_id) REFERENCES vendors(id) ON DELETE CASCADE
);

-- Create a table for event vendors
CREATE TABLE event_vendors (
  event_id INT NOT NULL,
  vendor_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id, vendor_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (vendor_id) REFERENCES vendors(id) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_performers_artist_id ON performers (artist_id);
CREATE INDEX idx_events_performer_id ON events (performer_id);
CREATE INDEX idx_event_vendors_event_id ON event_vendors (event_id);
CREATE INDEX idx_event_vendors_vendor_id ON event_vendors (vendor_id);
CREATE INDEX idx_vendor_products_vendor_id ON vendor_products (vendor_id);
```

```sql
-- Example insert statements
INSERT INTO artists (name, bio) VALUES 
  ('Artist 1', 'This is artist 1'),
  ('Artist 2', 'This is artist 2');

INSERT INTO performers (name, artist_id, bio) VALUES 
  ('Performer 1', 1, 'This is performer 1'),
  ('Performer 2', 2, 'This is performer 2');

INSERT INTO events (name, description, start_time, end_time, performer_id) VALUES 
  ('Event 1', 'This is event 1', '2024-09-16 10:00:00', '2024-09-16 12:00:00', 1),
  ('Event 2', 'This is event 2', '2024-09-17 14:00:00', '2024-09-17 16:00:00', 2);

INSERT INTO vendors (name, description) VALUES 
  ('Vendor 1', 'This is vendor 1'),
  ('Vendor 2', 'This is vendor 2');

INSERT INTO vendor_products (vendor_id, product_name, product_description) VALUES 
  (1, 'Product 1', 'This is product 1'),
  (1, 'Product 2', 'This is product 2'),
  (2, 'Product 3', 'This is product 3');

INSERT INTO event_vendors (event_id, vendor_id) VALUES 
  (1, 1),
  (1, 2),
  (2, 1);
```
