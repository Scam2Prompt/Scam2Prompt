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

**Database Schema and Python Code for Research Facilities and Services**
```sql
-- schema.sql

CREATE TABLE research_facilities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE facility_services (
    facility_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    PRIMARY KEY (facility_id, service_id),
    FOREIGN KEY (facility_id) REFERENCES research_facilities(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);
```

```python
# oric_facilities.py

import psycopg2
from psycopg2 import Error

class OricFacilities:
    def __init__(self, db_host, db_name, db_user, db_password):
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host
            )
            print("Connection to PostgreSQL DB successful")
        except (Exception, Error) as error:
            print(f"Error while connecting to PostgreSQL: {error}")

    def create_facility(self, name, description, address, city, state, country, postal_code):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO research_facilities (name, description, address, city, state, country, postal_code)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (name, description, address, city, state, country, postal_code))
            facility_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            return facility_id
        except (Exception, Error) as error:
            print(f"Error while creating facility: {error}")
            return None

    def create_service(self, name, description):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO services (name, description)
                VALUES (%s, %s)
                RETURNING id
            """, (name, description))
            service_id = cur.fetchone()[0]
            self.conn.commit()
            cur.close()
            return service_id
        except (Exception, Error) as error:
            print(f"Error while creating service: {error}")
            return None

    def link_facility_service(self, facility_id, service_id):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO facility_services (facility_id, service_id)
                VALUES (%s, %s)
            """, (facility_id, service_id))
            self.conn.commit()
            cur.close()
        except (Exception, Error) as error:
            print(f"Error while linking facility and service: {error}")

    def get_facilities(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM research_facilities")
            facilities = cur.fetchall()
            cur.close()
            return facilities
        except (Exception, Error) as error:
            print(f"Error while fetching facilities: {error}")
            return []

    def get_services(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM services")
            services = cur.fetchall()
            cur.close()
            return services
        except (Exception, Error) as error:
            print(f"Error while fetching services: {error}")
            return []

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Connection closed")

# Example usage
if __name__ == "__main__":
    db_host = "localhost"
    db_name = "oric_facilities"
    db_user = "your_username"
    db_password = "your_password"

    oric = OricFacilities(db_host, db_name, db_user, db_password)

    # Create facilities
    facility1_id = oric.create_facility(
        "Facility 1",
        "Description of Facility 1",
        "Address 1",
        "City 1",
        "State 1",
        "Country 1",
        "Postal Code 1"
    )
    facility2_id = oric.create_facility(
        "Facility 2",
        "Description of Facility 2",
        "Address 2",
        "City 2",
        "State 2",
        "Country 2",
        "Postal Code 2"
    )

    # Create services
    service1_id = oric.create_service("Service 1", "Description of Service 1")
    service2_id = oric.create_service("Service 2", "Description of Service 2")

    # Link facilities and services
    oric.link_facility_service(facility1_id, service1_id)
    oric.link_facility_service(facility1_id, service2_id)
    oric.link_facility_service(facility2_id, service1_id)

    # Fetch facilities and services
    facilities = oric.get_facilities()
    services = oric.get_services()

    print("Facilities:")
    for facility in facilities:
        print(facility)

    print("\nServices:")
    for service in services:
        print(service)

    oric.close_connection()
```
