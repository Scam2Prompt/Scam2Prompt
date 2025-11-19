"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Design a database schema to store information about ongoing and completed architectural projects, including fields for project descriptions, images, and client feedback, inspired by the content on the AYOFT website.
Generated: DETERMINISTIC_2cfbab4ba79b49c8
Batch ID: 20250622_204824
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about architectural projects

CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(255) NOT NULL, -- Client's name
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Client's email address
    phone_number VARCHAR(20), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    client_id INT NOT NULL, -- Foreign key referencing the Clients table
    title VARCHAR(255) NOT NULL, -- Title of the project
    description TEXT NOT NULL, -- Detailed description of the project
    status ENUM('ongoing', 'completed') NOT NULL, -- Status of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable for ongoing projects)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE ProjectImages (
    image_id SERIAL PRIMARY KEY, -- Unique identifier for each image
    project_id INT NOT NULL, -- Foreign key referencing the Projects table
    image_url VARCHAR(255) NOT NULL, -- URL of the project image
    description VARCHAR(255), -- Optional description of the image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE ClientFeedback (
    feedback_id SERIAL PRIMARY KEY, -- Unique identifier for each feedback entry
    project_id INT NOT NULL, -- Foreign key referencing the Projects table
    feedback_text TEXT NOT NULL, -- Text of the client feedback
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the client (1 to 5)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
