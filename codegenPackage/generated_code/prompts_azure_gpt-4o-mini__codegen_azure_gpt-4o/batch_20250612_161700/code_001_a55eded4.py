"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Write a Python script that automates the management of glass and aluminum project proposals, similar to the project management solutions provided by CristalesGraf.
Generated: DETERMINISTIC_a55eded4a91c7a7e
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime

# Constants
DATA_FILE = "project_proposals.json"

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)  # Initialize with an empty list

# Function to load project proposals from the file
def load_proposals():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save project proposals to the file
def save_proposals(proposals):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(proposals, file, indent=4)
    except Exception as e:
        print(f"Error saving proposals: {e}")

# Function to add a new project proposal
def add_proposal(client_name, project_type, description, estimated_cost):
    proposals = load_proposals()
    new_proposal = {
        "id": len(proposals) + 1,
        "client_name": client_name,
        "project_type": project_type,
        "description": description,
        "estimated_cost": estimated_cost,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    proposals.append(new_proposal)
    save_proposals(proposals)
    print(f"Proposal for {client_name} added successfully.")

# Function to list all project proposals
def list_proposals():
    proposals = load_proposals()
    if not proposals:
        print("No proposals found.")
        return
    for proposal in proposals:
        print(f"ID: {proposal['id']}, Client: {proposal['client_name']}, Type: {proposal['project_type']}, "
              f"Status: {proposal['status']}, Created At: {proposal['created_at']}")

# Function to update the status of a proposal
def update_proposal_status(proposal_id, new_status):
    proposals = load_proposals()
    for proposal in proposals:
        if proposal['id'] == proposal_id:
            proposal['status'] = new_status
            save_proposals(proposals)
            print(f"Proposal ID {proposal_id} status updated to {new_status}.")
            return
    print(f"Proposal ID {proposal_id} not found.")

# Function to delete a proposal
def delete_proposal(proposal_id):
    proposals = load_proposals()
    updated_proposals = [proposal for proposal in proposals if proposal['id'] != proposal_id]
    if len(proposals) == len(updated_proposals):
        print(f"Proposal ID {proposal_id} not found.")
        return
    save_proposals(updated_proposals)
    print(f"Proposal ID {proposal_id} deleted successfully.")

# Main menu for user interaction
def main():
    while True:
        print("\nGlass and Aluminum Project Proposal Management")
        print("1. Add Proposal")
        print("2. List Proposals")
        print("3. Update Proposal Status")
        print("4. Delete Proposal")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            client_name = input("Enter client name: ")
            project_type = input("Enter project type (e.g., Glass, Aluminum): ")
            description = input("Enter project description: ")
            try:
                estimated_cost = float(input("Enter estimated cost: "))
            except ValueError:
                print("Invalid cost. Please enter a numeric value.")
                continue
            add_proposal(client_name, project_type, description, estimated_cost)
        elif choice == "2":
            list_proposals()
        elif choice == "3":
            try:
                proposal_id = int(input("Enter proposal ID to update: "))
                new_status = input("Enter new status (e.g., Approved, Rejected): ")
                update_proposal_status(proposal_id, new_status)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "4":
            try:
                proposal_id = int(input("Enter proposal ID to delete: "))
                delete_proposal(proposal_id)
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
