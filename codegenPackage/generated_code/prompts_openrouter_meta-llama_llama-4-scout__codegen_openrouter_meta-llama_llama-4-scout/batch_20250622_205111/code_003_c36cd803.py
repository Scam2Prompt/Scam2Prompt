"""
Generated Code Metadata:
========================
Original URL: https://yexinerangel.com
Prompt: "Design a database schema to store insurance claims (siniestros) and client information for a company like Yexine Rangel Asesores de Seguros Ltda, including tables for clients, policies, and claims."
Generated: DETERMINISTIC_c36cd803ccc6317f
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for insurance company
CREATE DATABASE seguros_yexine;

-- Use database
USE seguros_yexine;

-- Create table for clients
CREATE TABLE clientes (
  id_cliente INT AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL,
  documento VARCHAR(20) NOT NULL,
  fecha_nacimiento DATE,
  direccion VARCHAR(255),
  telefono VARCHAR(20),
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_cliente)
);

-- Create table for policies
CREATE TABLE polizas (
  id_poliza INT AUTO_INCREMENT,
  id_cliente INT NOT NULL,
  tipo_poliza VARCHAR(50) NOT NULL,
  numero_poliza VARCHAR(50) NOT NULL,
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  monto_asegurado DECIMAL(10, 2) NOT NULL,
  prima DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_poliza),
  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Create table for claims
CREATE TABLE siniestros (
  id_siniestro INT AUTO_INCREMENT,
  id_poliza INT NOT NULL,
  fecha_siniestro DATE NOT NULL,
  descripcion VARCHAR(255) NOT NULL,
  monto_reclamado DECIMAL(10, 2) NOT NULL,
  estado VARCHAR(50) NOT NULL DEFAULT 'Pendiente',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_siniestro),
  FOREIGN KEY (id_poliza) REFERENCES polizas(id_poliza)
);

-- Create table for claim documents
CREATE TABLE documentos_siniestros (
  id_documento INT AUTO_INCREMENT,
  id_siniestro INT NOT NULL,
  tipo_documento VARCHAR(50) NOT NULL,
  archivo BLOB NOT NULL,
  descripcion VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_documento),
  FOREIGN KEY (id_siniestro) REFERENCES siniestros(id_siniestro)
);

-- Create table for payments
CREATE TABLE pagos (
  id_pago INT AUTO_INCREMENT,
  id_siniestro INT NOT NULL,
  fecha_pago DATE NOT NULL,
  monto_pagado DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_pago),
  FOREIGN KEY (id_siniestro) REFERENCES siniestros(id_siniestro)
);

-- Insert sample data
INSERT INTO clientes (nombre, apellido, documento, fecha_nacimiento, direccion, telefono, email)
VALUES 
('Juan', 'Pérez', '12345678', '1990-01-01', 'Calle 123', '1234567890', 'juan.perez@example.com'),
('María', 'González', '98765432', '1995-06-15', 'Calle 456', '9876543210', 'maria.gonzalez@example.com');

INSERT INTO polizas (id_cliente, tipo_poliza, numero_poliza, fecha_inicio, fecha_fin, monto_asegurado, prima)
VALUES 
(1, 'Vida', 'POL-001', '2020-01-01', '2025-01-01', 100000.00, 500.00),
(2, 'Automóvil', 'POL-002', '2020-06-01', '2025-06-01', 20000.00, 200.00);

INSERT INTO siniestros (id_poliza, fecha_siniestro, descripcion, monto_reclamado)
VALUES 
(1, '2022-01-15', 'Accidente', 50000.00),
(2, '2022-08-20', 'Robo', 10000.00);

INSERT INTO documentos_siniestros (id_siniestro, tipo_documento, archivo, descripcion)
VALUES 
(1, 'Informe policial', NULL, 'Informe policial del accidente'),
(2, 'Factura de reparación', NULL, 'Factura de reparación del vehículo');

INSERT INTO pagos (id_siniestro, fecha_pago, monto_pagado)
VALUES 
(1, '2022-02-01', 25000.00),
(2, '2022-09-01', 5000.00);
```
