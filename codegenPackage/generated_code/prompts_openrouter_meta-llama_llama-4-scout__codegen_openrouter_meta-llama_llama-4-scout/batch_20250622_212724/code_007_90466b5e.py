"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Design a database schema for a system to manage certifications and memberships for a professional organization like the Colegio de Psicologos de Oruro.
Generated: DETERMINISTIC_90466b5e2699b054
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the Colegio de Psicologos de Oruro
CREATE DATABASE colegio_psicologos;

-- Use the database
USE colegio_psicologos;

-- Create a table for members
CREATE TABLE miembros (
  id_miembro INT AUTO_INCREMENT,
  nombres VARCHAR(50) NOT NULL,
  apellidos VARCHAR(50) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  correo_electronico VARCHAR(100) UNIQUE NOT NULL,
  telefono VARCHAR(20),
  direccion VARCHAR(200),
  PRIMARY KEY (id_miembro)
);

-- Create a table for certifications
CREATE TABLE certificaciones (
  id_certificacion INT AUTO_INCREMENT,
  nombre_certificacion VARCHAR(100) NOT NULL,
  descripcion_certificacion TEXT,
  fecha_vencimiento DATE,
  PRIMARY KEY (id_certificacion)
);

-- Create a table for membership types
CREATE TABLE tipos_miembros (
  id_tipo_miembro INT AUTO_INCREMENT,
  nombre_tipo_miembro VARCHAR(50) NOT NULL,
  descripcion_tipo_miembro TEXT,
  PRIMARY KEY (id_tipo_miembro)
);

-- Create a table for member certifications
CREATE TABLE miembro_certificaciones (
  id_miembro INT NOT NULL,
  id_certificacion INT NOT NULL,
  fecha_obtencion DATE NOT NULL,
  fecha_vencimiento DATE,
  PRIMARY KEY (id_miembro, id_certificacion),
  FOREIGN KEY (id_miembro) REFERENCES miembros(id_miembro),
  FOREIGN KEY (id_certificacion) REFERENCES certificaciones(id_certificacion)
);

-- Create a table for member memberships
CREATE TABLE miembro_miembros (
  id_miembro INT NOT NULL,
  id_tipo_miembro INT NOT NULL,
  fecha_afiliacion DATE NOT NULL,
  fecha_vencimiento DATE,
  PRIMARY KEY (id_miembro, id_tipo_miembro),
  FOREIGN KEY (id_miembro) REFERENCES miembros(id_miembro),
  FOREIGN KEY (id_tipo_miembro) REFERENCES tipos_miembros(id_tipo_miembro)
);

-- Create a table for payments
CREATE TABLE pagos (
  id_pago INT AUTO_INCREMENT,
  id_miembro INT NOT NULL,
  fecha_pago DATE NOT NULL,
  monto DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id_pago),
  FOREIGN KEY (id_miembro) REFERENCES miembros(id_miembro)
);

-- Create a table for events
CREATE TABLE eventos (
  id_evento INT AUTO_INCREMENT,
  nombre_evento VARCHAR(100) NOT NULL,
  fecha_evento DATE NOT NULL,
  hora_evento TIME NOT NULL,
  lugar_evento VARCHAR(200) NOT NULL,
  PRIMARY KEY (id_evento)
);

-- Create a table for member events
CREATE TABLE miembro_eventos (
  id_miembro INT NOT NULL,
  id_evento INT NOT NULL,
  fecha_asistencia DATE,
  PRIMARY KEY (id_miembro, id_evento),
  FOREIGN KEY (id_miembro) REFERENCES miembros(id_miembro),
  FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
);

-- Create indexes on foreign keys
CREATE INDEX idx_miembro_certificaciones_id_miembro ON miembro_certificaciones(id_miembro);
CREATE INDEX idx_miembro_certificaciones_id_certificacion ON miembro_certificaciones(id_certificacion);
CREATE INDEX idx_miembro_miembros_id_miembro ON miembro_miembros(id_miembro);
CREATE INDEX idx_miembro_miembros_id_tipo_miembro ON miembro_miembros(id_tipo_miembro);
CREATE INDEX idx_pagos_id_miembro ON pagos(id_miembro);
CREATE INDEX idx_miembro_eventos_id_miembro ON miembro_eventos(id_miembro);
CREATE INDEX idx_miembro_eventos_id_evento ON miembro_eventos(id_evento);
```

```sql
-- Insert some sample data
INSERT INTO miembros (nombres, apellidos, fecha_nacimiento, correo_electronico, telefono, direccion)
VALUES 
('Juan', 'Pérez', '1990-01-01', 'juan.perez@example.com', '123456789', 'Calle 123'),
('María', 'González', '1995-06-15', 'maria.gonzalez@example.com', '987654321', 'Calle 456');

INSERT INTO certificaciones (nombre_certificacion, descripcion_certificacion, fecha_vencimiento)
VALUES 
('Certificación en Psicología Clínica', 'Certificación para psicólogos clínicos', '2025-01-01'),
('Certificación en Psicología Educativa', 'Certificación para psicólogos educativos', '2028-06-15');

INSERT INTO tipos_miembros (nombre_tipo_miembro, descripcion_tipo_miembro)
VALUES 
('Miembro Activo', 'Miembros activos del Colegio de Psicólogos de Oruro'),
('Miembro Pasivo', 'Miembros pasivos del Colegio de Psicólogos de Oruro');

INSERT INTO miembro_certificaciones (id_miembro, id_certificacion, fecha_obtencion, fecha_vencimiento)
VALUES 
(1, 1, '2020-01-01', '2025-01-01'),
(2, 2, '2022-06-15', '2028-06-15');

INSERT INTO miembro_miembros (id_miembro, id_tipo_miembro, fecha_afiliacion, fecha_vencimiento)
VALUES 
(1, 1, '2018-01-01', NULL),
(2, 2, '2020-06-15', NULL);

INSERT INTO pagos (id_miembro, fecha_pago, monto)
VALUES 
(1, '2022-01-01', 100.00),
(2, '2022-06-15', 50.00);

INSERT INTO eventos (nombre_evento, fecha_evento, hora_evento, lugar_evento)
VALUES 
('Conferencia sobre Psicología Clínica', '2023-03-15', '10:00:00', 'Auditorio del Colegio de Psicólogos de Oruro'),
('Taller sobre Psicología Educativa', '2023-09-20', '14:00:00', 'Sala de Conferencias del Colegio de Psicólogos de Oruro');

INSERT INTO miembro_eventos (id_miembro, id_evento, fecha_asistencia)
VALUES 
(1, 1, '2023-03-15'),
(2, 2, '2023-09-20');
```
