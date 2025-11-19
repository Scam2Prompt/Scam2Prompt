"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Create a database schema to manage cross-docking operations, including efficient loading and unloading solutions like those described in Calmar Transport's lumper services.
Generated: DETERMINISTIC_e955172502e3f60d
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for cross-docking operations
CREATE DATABASE cross_docking;

-- Use the database
USE cross_docking;

-- Create table for warehouses
CREATE TABLE warehouses (
  warehouse_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  PRIMARY KEY (warehouse_id)
);

-- Create table for trucks
CREATE TABLE trucks (
  truck_id INT AUTO_INCREMENT,
  license_plate VARCHAR(20) NOT NULL,
  make VARCHAR(50) NOT NULL,
  model VARCHAR(50) NOT NULL,
  capacity DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (truck_id)
);

-- Create table for shipments
CREATE TABLE shipments (
  shipment_id INT AUTO_INCREMENT,
  shipment_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  origin_warehouse_id INT,
  destination_warehouse_id INT,
  expected_arrival_time DATETIME,
  expected_departure_time DATETIME,
  actual_arrival_time DATETIME,
  actual_departure_time DATETIME,
  truck_id INT,
  PRIMARY KEY (shipment_id),
  FOREIGN KEY (origin_warehouse_id) REFERENCES warehouses(warehouse_id),
  FOREIGN KEY (destination_warehouse_id) REFERENCES warehouses(warehouse_id),
  FOREIGN KEY (truck_id) REFERENCES trucks(truck_id)
);

-- Create table for cross-docking operations
CREATE TABLE cross_docking_operations (
  operation_id INT AUTO_INCREMENT,
  shipment_id INT NOT NULL,
  warehouse_id INT NOT NULL,
  operation_type VARCHAR(50) NOT NULL CHECK (operation_type IN ('loading', 'unloading')),
  start_time DATETIME NOT NULL,
  end_time DATETIME,
  PRIMARY KEY (operation_id),
  FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id),
  FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- Create table for lumper services
CREATE TABLE lumper_services (
  service_id INT AUTO_INCREMENT,
  operation_id INT NOT NULL,
  service_type VARCHAR(50) NOT NULL CHECK (service_type IN ('lumper', 'dock')),
  service_time DATETIME NOT NULL,
  service_status VARCHAR(50) NOT NULL CHECK (service_status IN ('pending', 'completed')),
  PRIMARY KEY (service_id),
  FOREIGN KEY (operation_id) REFERENCES cross_docking_operations(operation_id)
);

-- Create table for warehouse equipment
CREATE TABLE warehouse_equipment (
  equipment_id INT AUTO_INCREMENT,
  warehouse_id INT NOT NULL,
  equipment_type VARCHAR(50) NOT NULL CHECK (equipment_type IN ('forklift', 'crane')),
  equipment_status VARCHAR(50) NOT NULL CHECK (equipment_status IN ('available', 'in-use', 'maintenance')),
  PRIMARY KEY (equipment_id),
  FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- Create table for equipment assignments
CREATE TABLE equipment_assignments (
  assignment_id INT AUTO_INCREMENT,
  equipment_id INT NOT NULL,
  operation_id INT NOT NULL,
  assignment_time DATETIME NOT NULL,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (equipment_id) REFERENCES warehouse_equipment(equipment_id),
  FOREIGN KEY (operation_id) REFERENCES cross_docking_operations(operation_id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_shipments_warehouse_id ON shipments (origin_warehouse_id, destination_warehouse_id);
CREATE INDEX idx_cross_docking_operations_shipment_id ON cross_docking_operations (shipment_id);
CREATE INDEX idx_lumper_services_operation_id ON lumper_services (operation_id);
```

```python
# models.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime, DECIMAL, ForeignKey, CheckConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://user:password@host:port/cross_docking')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Warehouse(Base):
    __tablename__ = 'warehouses'
    warehouse_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    zip_code = Column(String(20), nullable=False)

class Truck(Base):
    __tablename__ = 'trucks'
    truck_id = Column(Integer, primary_key=True)
    license_plate = Column(String(20), nullable=False)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    capacity = Column(DECIMAL(10, 2), nullable=False)

class Shipment(Base):
    __tablename__ = 'shipments'
    shipment_id = Column(Integer, primary_key=True)
    shipment_status = Column(String(50), nullable=False, default='pending')
    origin_warehouse_id = Column(Integer, ForeignKey('warehouses.warehouse_id'))
    destination_warehouse_id = Column(Integer, ForeignKey('warehouses.warehouse_id'))
    expected_arrival_time = Column(DateTime)
    expected_departure_time = Column(DateTime)
    actual_arrival_time = Column(DateTime)
    actual_departure_time = Column(DateTime)
    truck_id = Column(Integer, ForeignKey('trucks.truck_id'))
    origin_warehouse = relationship('Warehouse', foreign_keys=[origin_warehouse_id])
    destination_warehouse = relationship('Warehouse', foreign_keys=[destination_warehouse_id])
    truck = relationship('Truck', foreign_keys=[truck_id])

class CrossDockingOperation(Base):
    __tablename__ = 'cross_docking_operations'
    operation_id = Column(Integer, primary_key=True)
    shipment_id = Column(Integer, ForeignKey('shipments.shipment_id'), nullable=False)
    warehouse_id = Column(Integer, ForeignKey('warehouses.warehouse_id'), nullable=False)
    operation_type = Column(String(50), nullable=False, CheckConstraint('operation_type IN (\'loading\', \'unloading\')'))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    shipment = relationship('Shipment', foreign_keys=[shipment_id])
    warehouse = relationship('Warehouse', foreign_keys=[warehouse_id])

class LumperService(Base):
    __tablename__ = 'lumper_services'
    service_id = Column(Integer, primary_key=True)
    operation_id = Column(Integer, ForeignKey('cross_docking_operations.operation_id'), nullable=False)
    service_type = Column(String(50), nullable=False, CheckConstraint('service_type IN (\'lumper\', \'dock\')'))
    service_time = Column(DateTime, nullable=False)
    service_status = Column(String(50), nullable=False, CheckConstraint('service_status IN (\'pending\', \'completed\')'))
    operation = relationship('CrossDockingOperation', foreign_keys=[operation_id])

Base.metadata.create_all(engine)
```

```python
# main.py

from models import session, Warehouse, Truck, Shipment, CrossDockingOperation, LumperService

def create_warehouse(name, address, city, state, country, zip_code):
    warehouse = Warehouse(name=name, address=address, city=city, state=state, country=country, zip_code=zip_code)
    session.add(warehouse)
    session.commit()

def create_truck(license_plate, make, model, capacity):
    truck = Truck(license_plate=license_plate, make=make, model=model, capacity=capacity)
    session.add(truck)
    session.commit()

def create_shipment(origin_warehouse_id, destination_warehouse_id, expected_arrival_time, expected_departure_time, truck_id):
    shipment = Shipment(origin_warehouse_id=origin_warehouse_id, destination_warehouse_id=destination_warehouse_id, expected_arrival_time=expected_arrival_time, expected_departure_time=expected_departure_time, truck_id=truck_id)
    session.add(shipment)
    session.commit()

def create_cross_docking_operation(shipment_id, warehouse_id, operation_type, start_time):
    operation = CrossDockingOperation(shipment_id=shipment_id, warehouse_id=warehouse_id, operation_type=operation_type, start_time=start_time)
    session.add(operation)
    session.commit()

def create_lumper_service(operation_id, service_type, service_time):
    service = LumperService(operation_id=operation_id, service_type=service_type, service_time=service_time, service_status='pending')
    session.add(service)
    session.commit()

if __name__ == '__main__':
    # Create a warehouse
    create_warehouse('Warehouse 1', '123 Main St', 'Anytown', 'CA', 'USA', '12345')

    # Create a truck
    create_truck('ABC123', 'Ford', 'F-150', 1000.0)

    # Create a shipment
    create_shipment(1, 1, '2024-01-01 08:00:00', '2024-01-01 12:00:00', 1)

    # Create a cross-docking operation
    create_cross_docking_operation(1, 1, 'loading', '2024-01-01 08:00:00')

    # Create a lumper service
    create_lumper_service(1, 'lumper', '2024-01-01 08:30:00')
```
