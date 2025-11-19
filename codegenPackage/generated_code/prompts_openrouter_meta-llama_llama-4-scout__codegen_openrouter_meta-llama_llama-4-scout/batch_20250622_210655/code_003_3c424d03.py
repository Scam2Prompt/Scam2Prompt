"""
Generated Code Metadata:
========================
Original URL: https://karaokeheaven.uk
Prompt: Design a database schema to store information about karaoke rooms, events, and song libraries for a venue like Karaoke Heaven, which has 7 locations in London and offers various events like birthday parties and corporate events.
Generated: DETERMINISTIC_3c424d03fe7dd640
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

-- Create database for Karaoke Heaven
CREATE DATABASE karaoke_heaven;

-- Use the database
USE karaoke_heaven;

-- Create table for venues
CREATE TABLE venues (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  postcode VARCHAR(20) NOT NULL,
  phone_number VARCHAR(20),
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for karaoke rooms
CREATE TABLE karaoke_rooms (
  id INT AUTO_INCREMENT,
  venue_id INT NOT NULL,
  room_name VARCHAR(255) NOT NULL,
  capacity INT NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (venue_id) REFERENCES venues(id) ON DELETE CASCADE
);

-- Create table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  event_type ENUM('birthday_party', 'corporate_event', 'other') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for event bookings
CREATE TABLE event_bookings (
  id INT AUTO_INCREMENT,
  karaoke_room_id INT NOT NULL,
  event_id INT NOT NULL,
  booking_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (karaoke_room_id) REFERENCES karaoke_rooms(id) ON DELETE CASCADE,
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

-- Create table for song libraries
CREATE TABLE song_libraries (
  id INT AUTO_INCREMENT,
  karaoke_room_id INT NOT NULL,
  song_title VARCHAR(255) NOT NULL,
  artist VARCHAR(100) NOT NULL,
  genre VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (karaoke_room_id) REFERENCES karaoke_rooms(id) ON DELETE CASCADE
);

-- Insert sample data for venues
INSERT INTO venues (name, address, city, postcode, phone_number, email)
VALUES
  ('Karaoke Heaven - London', '123 Oxford St', 'London', 'W1D 1AT', '020 7000 1234', 'london@karaokeheaven.com'),
  ('Karaoke Heaven - Camden', '456 Camden High St', 'London', 'NW1 0NE', '020 7000 5678', 'camden@karaokeheaven.com'),
  ('Karaoke Heaven - Shoreditch', '789 Brick Lane', 'London', 'E1 6SE', '020 7000 9012', 'shoreditch@karaokeheaven.com'),
  ('Karaoke Heaven - Covent Garden', '321 Covent Garden', 'London', 'WC2E 8RD', '020 7000 1111', 'coventgarden@karaokeheaven.com'),
  ('Karaoke Heaven - Leicester Square', '901 Leicester Square', 'London', 'WC2H 7LR', '020 7000 2222', 'leicester_square@karaokeheaven.com'),
  ('Karaoke Heaven - Soho', '234 Dean St', 'London', 'W1D 3BP', '020 7000 3333', 'soho@karaokeheaven.com'),
  ('Karaoke Heaven - King's Cross', '567 King's Cross St', 'London', 'N1C 4BU', '020 7000 4444', 'kingscross@karaokeheaven.com');

-- Insert sample data for karaoke rooms
INSERT INTO karaoke_rooms (venue_id, room_name, capacity, description)
VALUES
  (1, 'Room 1', 10, 'Small room for private parties'),
  (1, 'Room 2', 20, 'Medium room for group events'),
  (2, 'Room 1', 15, 'Small room for birthday parties'),
  (3, 'Room 1', 30, 'Large room for corporate events'),
  (4, 'Room 1', 8, 'Small room for private singing'),
  (5, 'Room 1', 25, 'Medium room for group singing'),
  (6, 'Room 1', 12, 'Small room for casual singing'),
  (7, 'Room 1', 40, 'Large room for big events');

-- Insert sample data for events
INSERT INTO events (name, description, event_type)
VALUES
  ('Birthday Party', 'Private birthday party', 'birthday_party'),
  ('Corporate Event', 'Company event for employees', 'corporate_event'),
  ('Karaoke Night', 'Public karaoke night', 'other');

-- Insert sample data for event bookings
INSERT INTO event_bookings (karaoke_room_id, event_id, booking_date, start_time, end_time)
VALUES
  (1, 1, '2024-09-20', '18:00:00', '22:00:00'),
  (2, 2, '2024-09-21', '10:00:00', '14:00:00'),
  (3, 3, '2024-09-22', '19:00:00', '23:00:00');

-- Insert sample data for song libraries
INSERT INTO song_libraries (karaoke_room_id, song_title, artist, genre)
VALUES
  (1, 'Happy', 'Pharrell Williams', 'Pop'),
  (1, 'Uptown Funk', 'Mark Ronson ft. Bruno Mars', 'Funk'),
  (2, 'I Will Always Love You', 'Whitney Houston', 'Ballad'),
  (3, 'Bohemian Rhapsody', 'Queen', 'Rock'),
  (4, 'We Are the Champions', 'Queen', 'Rock');
```
