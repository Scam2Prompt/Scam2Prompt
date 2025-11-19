"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Design a database schema to store information about the initiatives, team members, and donors of the Jiyo Jaago Foundation, and provide a Python script to interact with the database.
Generated: DETERMINISTIC_89c34785fc74ccd2
Batch ID: 20250622_210655
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
CREATE DATABASE jiyo_jaago_foundation;

-- Use database
USE jiyo_jaago_foundation;

-- Create table for initiatives
CREATE TABLE initiatives (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for team members
CREATE TABLE team_members (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for donors
CREATE TABLE donors (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    donation_amount DECIMAL(10, 2),
    donation_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for initiative team members
CREATE TABLE initiative_team_members (
    initiative_id INT,
    team_member_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (initiative_id, team_member_id),
    FOREIGN KEY (initiative_id) REFERENCES initiatives(id),
    FOREIGN KEY (team_member_id) REFERENCES team_members(id)
);

-- Create table for initiative donors
CREATE TABLE initiative_donors (
    initiative_id INT,
    donor_id INT,
    donation_amount DECIMAL(10, 2),
    donation_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (initiative_id, donor_id),
    FOREIGN KEY (initiative_id) REFERENCES initiatives(id),
    FOREIGN KEY (donor_id) REFERENCES donors(id)
);
```

```python
# db_interaction.py

import mysql.connector
from mysql.connector import Error

class DatabaseInteraction:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database successfully")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Disconnected from database successfully")

    def create_initiative(self, name, description, start_date, end_date):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO initiatives (name, description, start_date, end_date)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (name, description, start_date, end_date))
            self.connection.commit()
            print("Initiative created successfully")
        except Error as e:
            print(f"Error creating initiative: {e}")

    def create_team_member(self, first_name, last_name, email, role):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO team_members (first_name, last_name, email, role)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (first_name, last_name, email, role))
            self.connection.commit()
            print("Team member created successfully")
        except Error as e:
            print(f"Error creating team member: {e}")

    def create_donor(self, first_name, last_name, email, donation_amount, donation_date):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO donors (first_name, last_name, email, donation_amount, donation_date)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (first_name, last_name, email, donation_amount, donation_date))
            self.connection.commit()
            print("Donor created successfully")
        except Error as e:
            print(f"Error creating donor: {e}")

    def assign_team_member_to_initiative(self, initiative_id, team_member_id):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO initiative_team_members (initiative_id, team_member_id)
                VALUES (%s, %s)
            """
            cursor.execute(query, (initiative_id, team_member_id))
            self.connection.commit()
            print("Team member assigned to initiative successfully")
        except Error as e:
            print(f"Error assigning team member to initiative: {e}")

    def assign_donor_to_initiative(self, initiative_id, donor_id, donation_amount, donation_date):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO initiative_donors (initiative_id, donor_id, donation_amount, donation_date)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (initiative_id, donor_id, donation_amount, donation_date))
            self.connection.commit()
            print("Donor assigned to initiative successfully")
        except Error as e:
            print(f"Error assigning donor to initiative: {e}")


def main():
    db_interaction = DatabaseInteraction("localhost", "jiyo_jaago_foundation", "root", "password")
    db_interaction.connect()

    # Example usage:
    db_interaction.create_initiative("Education Initiative", "Providing education to underprivileged children", "2022-01-01", "2022-12-31")
    db_interaction.create_team_member("John", "Doe", "john.doe@example.com", "Manager")
    db_interaction.create_donor("Jane", "Doe", "jane.doe@example.com", 1000.00, "2022-01-15")
    db_interaction.assign_team_member_to_initiative(1, 1)
    db_interaction.assign_donor_to_initiative(1, 1, 1000.00, "2022-01-15")

    db_interaction.disconnect()


if __name__ == "__main__":
    main()
```
