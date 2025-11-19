"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Design a database schema to store information about temperature control shipments, including cargo details, transportation routes, and delivery schedules for a company like Calmar Transport."
Generated: DETERMINISTIC_10ced2a51b74e404
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for temperature control shipments

CREATE TABLE Cargo (
    cargo_id SERIAL PRIMARY KEY, -- Unique identifier for each cargo
    description VARCHAR(255) NOT NULL, -- Description of the cargo
    weight DECIMAL(10, 2) NOT NULL, -- Weight of the cargo in kilograms
    temperature_range VARCHAR(50) NOT NULL, -- Required temperature range for the cargo
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of cargo creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE TransportationRoute (
    route_id SERIAL PRIMARY KEY, -- Unique identifier for each transportation route
    origin VARCHAR(255) NOT NULL, -- Origin location of the shipment
    destination VARCHAR(255) NOT NULL, -- Destination location of the shipment
    distance DECIMAL(10, 2) NOT NULL, -- Distance of the route in kilometers
    estimated_time DECIMAL(10, 2) NOT NULL, -- Estimated time for the route in hours
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of route creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

CREATE TABLE DeliverySchedule (
    schedule_id SERIAL PRIMARY KEY, -- Unique identifier for each delivery schedule
    cargo_id INT NOT NULL, -- Foreign key referencing Cargo
    route_id INT NOT NULL, -- Foreign key referencing TransportationRoute
    scheduled_departure TIMESTAMP NOT NULL, -- Scheduled departure time
    scheduled_arrival TIMESTAMP NOT NULL, -- Scheduled arrival time
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the delivery (Pending, In Transit, Delivered, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of schedule creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (cargo_id) REFERENCES Cargo(cargo_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (route_id) REFERENCES TransportationRoute(route_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_cargo_description ON Cargo(description);
CREATE INDEX idx_route_origin_destination ON TransportationRoute(origin, destination);
CREATE INDEX idx_delivery_status ON DeliverySchedule(status);
```
