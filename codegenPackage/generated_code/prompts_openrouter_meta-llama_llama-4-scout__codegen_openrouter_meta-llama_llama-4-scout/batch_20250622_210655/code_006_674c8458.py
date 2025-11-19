"""
Generated Code Metadata:
========================
Original URL: https://www.al-aanqua.com
Prompt: Design a database schema for storing information about art and cultural events in the Arab world, inspired by the website's content.
Generated: DETERMINISTIC_674c84584a6b2c73
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing art and cultural events in the Arab world
CREATE DATABASE arab_cultural_events;

-- Use the database
USE arab_cultural_events;

-- Create a table for countries in the Arab world
CREATE TABLE countries (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  code VARCHAR(10) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY (code)
);

-- Create a table for cities in the Arab world
CREATE TABLE cities (
  id INT AUTO_INCREMENT,
  country_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (country_id) REFERENCES countries(id) ON DELETE CASCADE
);

-- Create a table for event types (e.g., exhibition, festival, concert)
CREATE TABLE event_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for art and cultural events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  city_id INT NOT NULL,
  event_type_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE,
  FOREIGN KEY (event_type_id) REFERENCES event_types(id) ON DELETE CASCADE
);

-- Create a table for event organizers
CREATE TABLE organizers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  PRIMARY KEY (id)
);

-- Create a table for event-organizer relationships
CREATE TABLE event_organizers (
  event_id INT NOT NULL,
  organizer_id INT NOT NULL,
  PRIMARY KEY (event_id, organizer_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (organizer_id) REFERENCES organizers(id) ON DELETE CASCADE
);

-- Create a table for artists and performers
CREATE TABLE artists (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  bio TEXT,
  PRIMARY KEY (id)
);

-- Create a table for event-artist relationships
CREATE TABLE event_artists (
  event_id INT NOT NULL,
  artist_id INT NOT NULL,
  PRIMARY KEY (event_id, artist_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE
);

-- Create a table for event tickets
CREATE TABLE tickets (
  id INT AUTO_INCREMENT,
  event_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  available INT NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

-- Create a table for ticket purchases
CREATE TABLE ticket_purchases (
  id INT AUTO_INCREMENT,
  ticket_id INT NOT NULL,
  purchaser_name VARCHAR(255) NOT NULL,
  purchaser_email VARCHAR(255) NOT NULL,
  purchase_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);
```

```sql
-- example_data.sql

-- Insert some example data into the database
INSERT INTO countries (name, code)
VALUES
  ('Egypt', 'EG'),
  ('Saudi Arabia', 'SA'),
  ('United Arab Emirates', 'AE'),
  ('Morocco', 'MA'),
  ('Tunisia', 'TN');

INSERT INTO cities (country_id, name)
VALUES
  (1, 'Cairo'),
  (2, 'Riyadh'),
  (3, 'Dubai'),
  (4, 'Marrakech'),
  (5, 'Tunis');

INSERT INTO event_types (name, description)
VALUES
  ('Exhibition', 'Art exhibition'),
  ('Festival', 'Music or cultural festival'),
  ('Concert', 'Live music concert');

INSERT INTO events (title, description, start_date, end_date, city_id, event_type_id)
VALUES
  ('Cairo Art Exhibition', 'A showcase of Egyptian art', '2024-03-01', '2024-03-31', 1, 1),
  ('Riyadh Music Festival', 'A music festival featuring local artists', '2024-04-01', '2024-04-05', 2, 2),
  ('Dubai Concert', 'A live concert featuring international artists', '2024-05-01', NULL, 3, 3);

INSERT INTO organizers (name, email, phone)
VALUES
  ('Egyptian Ministry of Culture', 'culture@egypt.gov', '202 12345678'),
  ('Riyadh Events', 'info@riyadhevents.com', '+966 555 123456'),
  ('Dubai Tourism', 'info@dubaitourism.ae', '+971 4 444 4444');

INSERT INTO event_organizers (event_id, organizer_id)
VALUES
  (1, 1),
  (2, 2),
  (3, 3);

INSERT INTO artists (name, bio)
VALUES
  ('Ahmed Shawqi', 'Egyptian poet and playwright'),
  ('Abdel Halim Hafez', 'Egyptian singer and actor'),
  ('Fairouz', 'Lebanese singer and actress');

INSERT INTO event_artists (event_id, artist_id)
VALUES
  (1, 1),
  (2, 2),
  (3, 3);

INSERT INTO tickets (event_id, price, available)
VALUES
  (1, 50.00, 100),
  (2, 20.00, 500),
  (3, 100.00, 200);

INSERT INTO ticket_purchases (ticket_id, purchaser_name, purchaser_email)
VALUES
  (1, 'John Doe', 'john@example.com'),
  (2, 'Jane Smith', 'jane@example.com'),
  (3, 'Bob Johnson', 'bob@example.com');
```
