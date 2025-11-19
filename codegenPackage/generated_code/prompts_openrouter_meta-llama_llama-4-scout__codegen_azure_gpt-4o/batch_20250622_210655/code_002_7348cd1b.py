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
# Import necessary libraries
import sqlite3

# Function to create and initialize the database schema
def initialize_database():
    """
    Initializes the database schema for storing research facilities and services offered by ORIC.
    """
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect("oric_facilities.db")
        cursor = conn.cursor()

        # Create table for research facilities
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ResearchFacilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            location TEXT NOT NULL
        )
        """)

        # Create table for services offered
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            facility_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (facility_id) REFERENCES ResearchFacilities (id)
        )
        """)

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

# Function to add a research facility
def add_research_facility(name, description, location):
    """
    Adds a new research facility to the database.

    :param name: Name of the research facility
    :param description: Description of the research facility
    :param location: Location of the research facility
    """
    try:
        conn = sqlite3.connect("oric_facilities.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO ResearchFacilities (name, description, location)
        VALUES (?, ?, ?)
        """, (name, description, location))

        conn.commit()
        conn.close()
        print(f"Research facility '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding research facility: {e}")

# Function to add a service to a research facility
def add_service(facility_id, name, description):
    """
    Adds a new service to a specific research facility.

    :param facility_id: ID of the research facility
    :param name: Name of the service
    :param description: Description of the service
    """
    try:
        conn = sqlite3.connect("oric_facilities.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Services (facility_id, name, description)
        VALUES (?, ?, ?)
        """, (facility_id, name, description))

        conn.commit()
        conn.close()
        print(f"Service '{name}' added successfully to facility ID {facility_id}.")
    except sqlite3.Error as e:
        print(f"Error adding service: {e}")

# Function to retrieve all research facilities and their services
def get_facilities_and_services():
    """
    Retrieves all research facilities and their associated services.

    :return: List of facilities and their services
    """
    try:
        conn = sqlite3.connect("oric_facilities.db")
        cursor = conn.cursor()

        # Query to get all facilities
        cursor.execute("SELECT * FROM ResearchFacilities")
        facilities = cursor.fetchall()

        # Query to get all services
        cursor.execute("SELECT * FROM Services")
        services = cursor.fetchall()

        conn.close()

        # Organize data into a structured format
        result = []
        for facility in facilities:
            facility_id, name, description, location = facility
            facility_services = [
                {"id": service[0], "name": service[2], "description": service[3]}
                for service in services if service[1] == facility_id
            ]
            result.append({
                "id": facility_id,
                "name": name,
                "description": description,
                "location": location,
                "services": facility_services
            })

        return result
    except sqlite3.Error as e:
        print(f"Error retrieving facilities and services: {e}")
        return []

# Main execution
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add sample data
    add_research_facility("Advanced Research Lab", "A state-of-the-art research facility.", "Building A")
    add_research_facility("Innovation Hub", "Focuses on innovative projects and startups.", "Building B")

    add_service(1, "3D Printing", "Provides 3D printing services for prototypes.")
    add_service(1, "Material Testing", "Offers testing services for various materials.")
    add_service(2, "Startup Incubation", "Supports startups with resources and mentorship.")

    # Retrieve and display all facilities and services
    facilities = get_facilities_and_services()
    for facility in facilities:
        print(f"Facility: {facility['name']} (Location: {facility['location']})")
        print(f"Description: {facility['description']}")
        print("Services:")
        for service in facility['services']:
            print(f"  - {service['name']}: {service['description']}")
        print()
```
