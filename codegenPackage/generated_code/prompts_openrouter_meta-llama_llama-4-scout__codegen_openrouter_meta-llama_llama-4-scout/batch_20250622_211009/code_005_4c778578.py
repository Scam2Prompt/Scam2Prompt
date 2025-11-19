"""
Generated Code Metadata:
========================
Original URL: https://munimala.gob.pe
Prompt: Write a SQL query to create a database schema for storing and managing normas y documentos legales, similar to those provided on the Municipalidad Distrital de Mala's website.
Generated: DETERMINISTIC_4c778578b1e37af6
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for storing and managing normas y documentos legales

-- Create database
CREATE DATABASE normas_legales;

-- Use database
USE normas_legales;

-- Create table for categorias de normas
CREATE TABLE categorias_normas (
  id_categoria INT AUTO_INCREMENT,
  nombre_categoria VARCHAR(255) NOT NULL,
  descripcion_categoria TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_categoria)
);

-- Create table for normas
CREATE TABLE normas (
  id_norma INT AUTO_INCREMENT,
  id_categoria INT NOT NULL,
  titulo_norma VARCHAR(255) NOT NULL,
  descripcion_norma TEXT,
  archivo_norma BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_norma),
  FOREIGN KEY (id_categoria) REFERENCES categorias_normas(id_categoria) ON DELETE CASCADE
);

-- Create table for documentos legales
CREATE TABLE documentos_legales (
  id_documento INT AUTO_INCREMENT,
  titulo_documento VARCHAR(255) NOT NULL,
  descripcion_documento TEXT,
  archivo_documento BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_documento)
);

-- Create table for categorias de documentos
CREATE TABLE categorias_documentos (
  id_categoria INT AUTO_INCREMENT,
  nombre_categoria VARCHAR(255) NOT NULL,
  descripcion_categoria TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_categoria)
);

-- Create bridge table for documentos and categorias
CREATE TABLE documentos_categorias (
  id_documento INT NOT NULL,
  id_categoria INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_documento, id_categoria),
  FOREIGN KEY (id_documento) REFERENCES documentos_legales(id_documento) ON DELETE CASCADE,
  FOREIGN KEY (id_categoria) REFERENCES categorias_documentos(id_categoria) ON DELETE CASCADE
);

-- Create table for users (for future authentication and authorization)
CREATE TABLE users (
  id_user INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_user)
);

-- Create table for revisions (for auditing and versioning)
CREATE TABLE revisions (
  id_revision INT AUTO_INCREMENT,
  id_norma INT,
  id_documento INT,
  revision_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_revision),
  FOREIGN KEY (id_norma) REFERENCES normas(id_norma) ON DELETE SET NULL,
  FOREIGN KEY (id_documento) REFERENCES documentos_legales(id_documento) ON DELETE SET NULL
);
```
