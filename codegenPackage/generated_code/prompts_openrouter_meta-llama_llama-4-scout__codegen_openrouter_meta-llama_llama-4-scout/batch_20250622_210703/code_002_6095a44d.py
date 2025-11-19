"""
Generated Code Metadata:
========================
Original URL: https://kadma-wine.co.il
Prompt: "Generate a sample database schema for storing information about wines, including varieties, vintages, and tasting notes, inspired by Kadma Wine's offerings."
Generated: DETERMINISTIC_6095a44db60e46c3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for wine information
CREATE DATABASE IF NOT EXISTS wine_database;

-- Use the wine database
USE wine_database;

-- Create a table for wine varieties
CREATE TABLE IF NOT EXISTS wine_varieties (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for wine producers
CREATE TABLE IF NOT EXISTS wine_producers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  region VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for wine vintages
CREATE TABLE IF NOT EXISTS wine_vintages (
  id INT AUTO_INCREMENT,
  producer_id INT NOT NULL,
  variety_id INT NOT NULL,
  vintage INT NOT NULL,
  wine_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (producer_id) REFERENCES wine_producers(id) ON DELETE CASCADE,
  FOREIGN KEY (variety_id) REFERENCES wine_varieties(id) ON DELETE CASCADE
);

-- Create a table for tasting notes
CREATE TABLE IF NOT EXISTS tasting_notes (
  id INT AUTO_INCREMENT,
  vintage_id INT NOT NULL,
  note TEXT NOT NULL,
  rating TINYINT UNSIGNED,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (vintage_id) REFERENCES wine_vintages(id) ON DELETE CASCADE
);

-- Create a table for wine labels
CREATE TABLE IF NOT EXISTS wine_labels (
  id INT AUTO_INCREMENT,
  vintage_id INT NOT NULL,
  label_name VARCHAR(255) NOT NULL,
  label_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (vintage_id) REFERENCES wine_vintages(id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO wine_varieties (name, description)
VALUES 
('Chardonnay', 'Buttery and oaky'),
('Pinot Noir', 'Light-bodied and fruity'),
('Cabernet Sauvignon', 'Full-bodied and tannic');

INSERT INTO wine_producers (name, region, country)
VALUES 
('Kadma Wine', 'Napa Valley', 'USA'),
('Domaine de la Romanée-Conti', 'Burgundy', 'France'),
('Château Lafite Rothschild', 'Bordeaux', 'France');

INSERT INTO wine_vintages (producer_id, variety_id, vintage, wine_name, description)
VALUES 
(1, 1, 2015, 'Kadma Chardonnay', 'Buttery and oaky with hints of vanilla'),
(1, 2, 2018, 'Kadma Pinot Noir', 'Light-bodied with flavors of cherry and earth'),
(2, 2, 2010, 'Domaine de la Romanée-Conti Bourgogne', 'Complex with flavors of dark fruit and spice');

INSERT INTO tasting_notes (vintage_id, note, rating)
VALUES 
(1, 'This Chardonnay is rich and creamy with a long finish.', 4),
(2, 'This Pinot Noir is light-bodied and fruity with high acidity.', 4),
(3, 'This Bourgogne is complex with flavors of dark fruit and spice.', 5);

INSERT INTO wine_labels (vintage_id, label_name, label_description)
VALUES 
(1, 'Kadma Reserve', 'A special reserve label from Kadma Wine'),
(2, 'Kadma Vineyard Selection', 'A selection of the best Pinot Noir from Kadma Wine''s vineyard'),
(3, 'Domaine de la Romanée-Conti Bourgogne', 'A premium label from Domaine de la Romanée-Conti');
```
