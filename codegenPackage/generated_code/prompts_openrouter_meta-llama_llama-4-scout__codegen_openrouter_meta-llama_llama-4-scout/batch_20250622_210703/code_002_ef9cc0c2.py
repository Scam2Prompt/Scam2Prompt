"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Generate a sample database schema for storing information about various holistic therapies, including Cupping/Hijama, Fertility Massage, Lymphatic Drainage, and Medical Acupuncture, along with their benefits and potential side effects.
Generated: DETERMINISTIC_ef9cc0c27ee7354e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for holistic therapies
CREATE DATABASE holistic_therapies;

-- Use the holistic_therapies database
USE holistic_therapies;

-- Create a table for therapies
CREATE TABLE therapies (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for therapy benefits
CREATE TABLE therapy_benefits (
  id INT AUTO_INCREMENT,
  therapy_id INT NOT NULL,
  benefit VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (therapy_id) REFERENCES therapies(id) ON DELETE CASCADE
);

-- Create a table for therapy side effects
CREATE TABLE therapy_side_effects (
  id INT AUTO_INCREMENT,
  therapy_id INT NOT NULL,
  side_effect VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (therapy_id) REFERENCES therapies(id) ON DELETE CASCADE
);

-- Create a table for practitioners
CREATE TABLE practitioners (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for therapy sessions
CREATE TABLE therapy_sessions (
  id INT AUTO_INCREMENT,
  practitioner_id INT NOT NULL,
  therapy_id INT NOT NULL,
  client_name VARCHAR(255) NOT NULL,
  session_date DATE NOT NULL,
  session_time TIME NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (practitioner_id) REFERENCES practitioners(id) ON DELETE RESTRICT,
  FOREIGN KEY (therapy_id) REFERENCES therapies(id) ON DELETE RESTRICT
);

-- Insert sample data into therapies table
INSERT INTO therapies (name, description) 
VALUES 
  ('Cupping/Hijama', 'A traditional form of alternative medicine in which a local suction is created on the skin to mobilize blood flow.'),
  ('Fertility Massage', 'A type of massage therapy designed to promote fertility and reproductive health.'),
  ('Lymphatic Drainage', 'A gentle massage technique that encourages the natural drainage of the lymph, which carries waste products away from the tissues.'),
  ('Medical Acupuncture', 'A form of acupuncture that is used to treat a range of medical conditions, including pain, digestive issues, and stress.');

-- Insert sample data into therapy benefits table
INSERT INTO therapy_benefits (therapy_id, benefit) 
VALUES 
  (1, 'Relieves muscle tension and pain'),
  (1, 'Improves blood flow and reduces inflammation'),
  (2, 'Enhances fertility and reproductive health'),
  (2, 'Reduces stress and anxiety'),
  (3, 'Boosts immune system'),
  (3, 'Reduces swelling and inflammation'),
  (4, 'Relieves pain and discomfort'),
  (4, 'Improves mood and reduces stress');

-- Insert sample data into therapy side effects table
INSERT INTO therapy_side_effects (therapy_id, side_effect) 
VALUES 
  (1, 'Temporary bruising and discomfort'),
  (1, 'Dizziness and lightheadedness'),
  (2, 'Temporary discomfort and sensitivity'),
  (2, 'Emotional release and mood swings'),
  (3, 'Temporary swelling and discomfort'),
  (3, 'Increased urination'),
  (4, 'Temporary pain and discomfort'),
  (4, 'Dizziness and lightheadedness');

-- Insert sample data into practitioners table
INSERT INTO practitioners (name, email, phone) 
VALUES 
  ('John Doe', 'john.doe@example.com', '123-456-7890'),
  ('Jane Smith', 'jane.smith@example.com', '987-654-3210'),
  ('Bob Johnson', 'bob.johnson@example.com', '555-123-4567');

-- Insert sample data into therapy sessions table
INSERT INTO therapy_sessions (practitioner_id, therapy_id, client_name, session_date, session_time, notes) 
VALUES 
  (1, 1, 'Client1', '2022-01-01', '10:00:00', 'First session, client reported muscle tension'),
  (2, 2, 'Client2', '2022-01-05', '14:00:00', 'Client reported improved mood and reduced stress'),
  (3, 3, 'Client3', '2022-01-10', '16:00:00', 'Client reported reduced swelling and inflammation'),
  (1, 4, 'Client4', '2022-01-15', '12:00:00', 'Client reported relieved pain and discomfort');
```
