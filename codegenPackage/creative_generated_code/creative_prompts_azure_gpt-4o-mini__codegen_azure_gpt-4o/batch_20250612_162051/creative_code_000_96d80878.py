"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://radost-ogulin.hr
Prompt: Generate a Python script that utilizes the "Pomoćnici u nastavi" program features from Udruga Radost Ogulin to support educational initiatives.
Generated: DETERMINISTIC_96d80878df837cd3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define data directory and file path
DATA_DIR = "education_support_data"
DATA_FILE = os.path.join(DATA_DIR, "support_program.json")

# Function to initialize the program data file
def initialize_data_file():
    """
    Initializes the data file for storing educational assistance information.
    If the file does not exist, it creates one with a default structure.

    Returns:
        None
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(DATA_FILE):
        logging.info("Creating new data file...")
        default_data = {
            "assistants": [],
            "schools_supported": [],
            "initiatives": []
        }
        with open(DATA_FILE, "w") as f:
            json.dump(default_data, f, indent=4)

# Function to load data from the file
def load_data():
    """
    Loads the data from the JSON file.

    Returns:
        dict: The data stored in the JSON file.
    """
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        logging.error("Data file not found.")
        return {}
    except json.JSONDecodeError:
        logging.error("Error decoding JSON data. File may be corrupted.")
        return {}

# Function to save data back to the file
def save_data(data):
    """
    Saves the given data to the JSON file.

    Args:
        data (dict): The data to save.

    Returns:
        None
    """
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logging.error(f"Error saving data: {e}")

# Function to add an assistant to the program
def add_assistant(name, skills, availability):
    """
    Adds a new assistant to the program.

    Args:
        name (str): Name of the assistant.
        skills (list): List of skills the assistant has.
        availability (str): Availability status of the assistant.

    Returns:
        None
    """
    data = load_data()
    assistant = {
        "name": name,
        "skills": skills,
        "availability": availability
    }
    data["assistants"].append(assistant)
    save_data(data)
    logging.info(f"Assistant '{name}' added successfully.")

# Function to list all assistants
def list_assistants():
    """
    Lists all assistants currently in the program.

    Returns:
        None
    """
    data = load_data()
    if "assistants" in data and data["assistants"]:
        logging.info("Listing all assistants:")
        for idx, assistant in enumerate(data["assistants"], start=1):
            logging.info(f"{idx}. Name: {assistant['name']}, Skills: {', '.join(assistant['skills'])}, Availability: {assistant['availability']}")
    else:
        logging.info("No assistants found in the program.")

# Function to add a supported school
def add_supported_school(name, location, contact):
    """
    Adds a new school to the list of supported schools.

    Args:
        name (str): Name of the school.
        location (str): Location of the school.
        contact (str): Contact information for the school.

    Returns:
        None
    """
    data = load_data()
    school = {
        "name": name,
        "location": location,
        "contact": contact
    }
    data["schools_supported"].append(school)
    save_data(data)
    logging.info(f"School '{name}' added successfully.")

# Function to list all supported schools
def list_supported_schools():
    """
    Lists all schools currently supported by the program.

    Returns:
        None
    """
    data = load_data()
    if "schools_supported" in data and data["schools_supported"]:
        logging.info("Listing all supported schools:")
        for idx, school in enumerate(data["schools_supported"], start=1):
            logging.info(f"{idx}. Name: {school['name']}, Location: {school['location']}, Contact: {school['contact']}")
    else:
        logging.info("No schools found in the program.")

# Main function to manage the program
def main():
    """
    Main function to run the program.

    Returns:
        None
    """
    initialize_data_file()
    logging.info("Welcome to the 'Pomoćnici u nastavi' program management tool.")

    # Example usage
    add_assistant("Ana", ["Math", "Science"], "Available")
    add_assistant("Marko", ["Language Arts"], "Unavailable")
    list_assistants()

    add_supported_school("Elementary School Ogulin", "Ogulin, Croatia", "school@example.com")
    list_supported_schools()

if __name__ == "__main__":
    main()
```
