"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Generate a sample database schema to store information about entrepreneurs, businesses, and training courses, using Italian as the primary language.
Generated: DETERMINISTIC_1839eca183d02ad1
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS imprenditori;

-- Use database
USE imprenditori;

-- Create table for entrepreneurs
CREATE TABLE IF NOT EXISTS imprenditori (
  id_imprenditore INT AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  cognome VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  telefono VARCHAR(20),
  data_nascita DATE,
  PRIMARY KEY (id_imprenditore)
);

-- Create table for businesses
CREATE TABLE IF NOT EXISTS aziende (
  id_azienda INT AUTO_INCREMENT,
  ragione_sociale VARCHAR(255) NOT NULL,
  partita_iva VARCHAR(20) UNIQUE NOT NULL,
  indirizzo VARCHAR(255) NOT NULL,
  citta VARCHAR(100) NOT NULL,
  provincia VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_azienda)
);

-- Create table for training courses
CREATE TABLE IF NOT EXISTS corsi_formazione (
  id_corso INT AUTO_INCREMENT,
  titolo VARCHAR(255) NOT NULL,
  descrizione TEXT,
  data_inizio DATE,
  data_fine DATE,
  PRIMARY KEY (id_corso)
);

-- Create table for entrepreneur-business relationships
CREATE TABLE IF NOT EXISTS imprenditori_aziende (
  id_imprenditore INT NOT NULL,
  id_azienda INT NOT NULL,
  ruolo VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_imprenditore, id_azienda),
  FOREIGN KEY (id_imprenditore) REFERENCES imprenditori(id_imprenditore) ON DELETE CASCADE,
  FOREIGN KEY (id_azienda) REFERENCES aziende(id_azienda) ON DELETE CASCADE
);

-- Create table for course registrations
CREATE TABLE IF NOT EXISTS iscrizioni_corsi (
  id_imprenditore INT NOT NULL,
  id_corso INT NOT NULL,
  data_iscrizione DATE NOT NULL,
  PRIMARY KEY (id_imprenditore, id_corso),
  FOREIGN KEY (id_imprenditore) REFERENCES imprenditori(id_imprenditore) ON DELETE CASCADE,
  FOREIGN KEY (id_corso) REFERENCES corsi_formazione(id_corso) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX idx_imprenditori_email ON imprenditori(email);
CREATE INDEX idx_aziende_partita_iva ON aziende(partita_iva);
CREATE INDEX idx_corsi_titolo ON corsi_formazione(titolo);

-- Insert sample data
INSERT INTO imprenditori (nome, cognome, email, telefono, data_nascita)
VALUES 
  ('Giovanni', 'Rossi', 'giovanni.rossi@example.com', '1234567890', '1990-01-01'),
  ('Maria', 'Verdi', 'maria.verdi@example.com', '9876543210', '1995-06-15');

INSERT INTO aziende (ragione_sociale, partita_iva, indirizzo, citta, provincia)
VALUES 
  ('Rossi Srl', '12345678901', 'Via Milano 1', 'Roma', 'RM'),
  ('Verdi Spa', '98765432101', 'Via Torino 2', 'Milano', 'MI');

INSERT INTO corsi_formazione (titolo, descrizione, data_inizio, data_fine)
VALUES 
  ('Corso di Marketing', 'Corso di marketing digitale', '2022-01-01', '2022-06-30'),
  ('Corso di Management', 'Corso di gestione aziendale', '2022-07-01', '2022-12-31');

INSERT INTO imprenditori_aziende (id_imprenditore, id_azienda, ruolo)
VALUES 
  (1, 1, 'Proprietario'),
  (2, 2, 'Socio');

INSERT INTO iscrizioni_corsi (id_imprenditore, id_corso, data_iscrizione)
VALUES 
  (1, 1, '2022-01-15'),
  (2, 2, '2022-07-15');
```
