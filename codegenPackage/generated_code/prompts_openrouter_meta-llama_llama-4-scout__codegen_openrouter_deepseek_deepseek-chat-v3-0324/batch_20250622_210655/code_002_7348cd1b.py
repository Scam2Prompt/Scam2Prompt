"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Generate a list of research facilities and services offered by ORIC and suggest a database schema to store information about these facilities.
Generated: DETERMINISTIC_7348cd1bb590c659
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for ORIC research facilities and services

# Facility types and services offered by ORIC
ORIC_FACILITIES = [
    {
        "name": "Advanced Materials Research Lab",
        "services": [
            "Material characterization",
            "Nanomaterial synthesis",
            "Surface analysis"
        ],
        "equipment": [
            "SEM",
            "XRD",
            "AFM"
        ],
        "contact": "materials@oric.edu"
    },
    {
        "name": "Computational Research Center",
        "services": [
            "High-performance computing",
            "Data analysis",
            "Molecular modeling"
        ],
        "equipment": [
            "GPU clusters",
            "Data servers",
            "Visualization workstations"
        ],
        "contact": "crc@oric.edu"
    },
    {
        "name": "Biotechnology Research Facility",
        "services": [
            "DNA sequencing",
            "Cell culture",
            "Protein purification"
        ],
        "equipment": [
            "PCR machines",
            "Flow cytometer",
            "Centrifuges"
        ],
        "contact": "biotech@oric.edu"
    },
    {
        "name": "Energy Research Lab",
        "services": [
            "Battery testing",
            "Solar cell characterization",
            "Fuel cell research"
        ],
        "equipment": [
            "Battery cyclers",
            "Solar simulators",
            "Electrochemical workstations"
        ],
        "contact": "energy@oric.edu"
    }
]

# SQL schema for storing ORIC facilities information
SQL_SCHEMA = """
CREATE TABLE facilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    location TEXT,
    contact_email TEXT NOT NULL,
    operational_hours TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    facility_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    cost REAL,
    FOREIGN KEY (facility_id) REFERENCES facilities(id) ON DELETE CASCADE
);

CREATE TABLE equipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    facility_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    availability BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (facility_id) REFERENCES facilities(id) ON DELETE CASCADE
);

CREATE TABLE staff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    facility_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    position TEXT,
    email TEXT,
    phone TEXT,
    FOREIGN KEY (facility_id) REFERENCES facilities(id) ON DELETE CASCADE
);

CREATE TABLE bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    facility_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    service_id INTEGER,
    equipment_id INTEGER,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    purpose TEXT,
    status TEXT DEFAULT 'pending',
    FOREIGN KEY (facility_id) REFERENCES facilities(id),
    FOREIGN KEY (service_id) REFERENCES services(id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(id)
);
"""

# NoSQL schema (MongoDB) alternative
NOSQL_SCHEMA = {
    "collection": "oric_facilities",
    "schema": {
        "bsonType": "object",
        "required": ["name", "contact_email"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "Name of the facility"
            },
            "description": {
                "bsonType": "string",
                "description": "Detailed description of the facility"
            },
            "location": {
                "bsonType": "string",
                "description": "Physical location of the facility"
            },
            "contact_email": {
                "bsonType": "string",
                "description": "Primary contact email"
            },
            "operational_hours": {
                "bsonType": "string",
                "description": "Operating hours of the facility"
            },
            "services": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "name": {"bsonType": "string"},
                        "description": {"bsonType": "string"},
                        "cost": {"bsonType": "double"}
                    }
                }
            },
            "equipment": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "name": {"bsonType": "string"},
                        "description": {"bsonType": "string"},
                        "availability": {"bsonType": "bool"}
                    }
                }
            },
            "staff": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "name": {"bsonType": "string"},
                        "position": {"bsonType": "string"},
                        "email": {"bsonType": "string"},
                        "phone": {"bsonType": "string"}
                    }
                }
            }
        }
    }
}
```
