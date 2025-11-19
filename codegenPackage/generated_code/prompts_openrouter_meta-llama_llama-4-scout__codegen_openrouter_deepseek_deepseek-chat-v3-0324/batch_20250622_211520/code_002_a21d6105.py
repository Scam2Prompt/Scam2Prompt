"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: "Write a Python script to manage client relationships and project portfolios for an interior design company like Meezan Interior Solutions, including features for tracking project awards and client feedback."
Generated: DETERMINISTIC_a21d61058eaa5d01
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

# Constants
DATA_FILE = "client_portfolio.json"
DATE_FORMAT = "%Y-%m-%d"

class ClientPortfolioManager:
    """
    A class to manage client relationships and project portfolios for an interior design company.
    Includes features for tracking project awards and client feedback.
    """

    def __init__(self):
        """Initialize the portfolio manager and load existing data."""
        self.data = self._load_data()

    def _load_data(self) -> Dict:
        """
        Load client portfolio data from JSON file.
        Creates a new file if it doesn't exist.
        
        Returns:
            Dict: The loaded data or empty structure if new file
        """
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r') as file:
                    return json.load(file)
            return {"clients": [], "projects": []}
        except Exception as e:
            print(f"Error loading data file: {e}")
            return {"clients": [], "projects": []}

    def _save_data(self) -> None:
        """Save the current data to the JSON file."""
        try:
            with open(DATA_FILE, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error saving data file: {e}")

    def add_client(self, name: str, contact: str, email: str, address: str) -> bool:
        """
        Add a new client to the portfolio.
        
        Args:
            name: Client name
            contact: Contact number
            email: Email address
            address: Physical address
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not all([name, contact, email, address]):
            print("All client fields are required.")
            return False

        # Check if client already exists
        if any(client["name"].lower() == name.lower() for client in self.data["clients"]):
            print(f"Client '{name}' already exists.")
            return False

        new_client = {
            "id": len(self.data["clients"]) + 1,
            "name": name,
            "contact": contact,
            "email": email,
            "address": address,
            "date_added": datetime.now().strftime(DATE_FORMAT),
            "feedback": []
        }

        self.data["clients"].append(new_client)
        self._save_data()
        return True

    def add_project(self, client_id: int, name: str, description: str, budget: float, 
                    start_date: str, end_date: str) -> bool:
        """
        Add a new project to the portfolio.
        
        Args:
            client_id: ID of the client
            name: Project name
            description: Project description
            budget: Project budget
            start_date: Project start date (YYYY-MM-DD)
            end_date: Project end date (YYYY-MM-DD)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Validate dates
            datetime.strptime(start_date, DATE_FORMAT)
            datetime.strptime(end_date, DATE_FORMAT)
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return False

        if not all([client_id, name, description, budget, start_date, end_date]):
            print("All project fields are required.")
            return False

        # Check if client exists
        if not any(client["id"] == client_id for client in self.data["clients"]):
            print(f"Client ID {client_id} not found.")
            return False

        new_project = {
            "id": len(self.data["projects"]) + 1,
            "client_id": client_id,
            "name": name,
            "description": description,
            "budget": budget,
            "start_date": start_date,
            "end_date": end_date,
            "status": "planned",
            "award_date": None,
            "completion_date": None
        }

        self.data["projects"].append(new_project)
        self._save_data()
        return True

    def record_project_award(self, project_id: int, award_date: str) -> bool:
        """
        Record when a project was awarded.
        
        Args:
            project_id: ID of the project
            award_date: Date project was awarded (YYYY-MM-DD)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            datetime.strptime(award_date, DATE_FORMAT)
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return False

        project = self._get_project_by_id(project_id)
        if not project:
            print(f"Project ID {project_id} not found.")
            return False

        project["award_date"] = award_date
        project["status"] = "awarded"
        self._save_data()
        return True

    def record_project_completion(self, project_id: int, completion_date: str) -> bool:
        """
        Record when a project was completed.
        
        Args:
            project_id: ID of the project
            completion_date: Date project was completed (YYYY-MM-DD)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            datetime.strptime(completion_date, DATE_FORMAT)
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return False

        project = self._get_project_by_id(project_id)
        if not project:
            print(f"Project ID {project_id} not found.")
            return False

        project["completion_date"] = completion_date
        project["status"] = "completed"
        self._save_data()
        return True

    def add_client_feedback(self, client_id: int, project_id: int, 
                           rating: int, comments: str) -> bool:
        """
        Add client feedback for a project.
        
        Args:
            client_id: ID of the client
            project_id: ID of the project
            rating: Rating (1-5)
            comments: Feedback comments
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not (1 <= rating <= 5):
            print("Rating must be between 1 and 5.")
            return False

        client = self._get_client_by_id(client_id)
        if not client:
            print(f"Client ID {client_id} not found.")
            return False

        if not self._get_project_by_id(project_id):
            print(f"Project ID {project_id} not found.")
            return False

        feedback = {
            "project_id": project_id,
            "date": datetime.now().strftime(DATE_FORMAT),
            "rating": rating,
            "comments": comments
        }

        client["feedback"].append(feedback)
        self._save_data()
        return True

    def _get_client_by_id(self, client_id: int) -> Optional[Dict]:
        """Helper method to get client by ID."""
        return next((client for client in self.data["clients"] if client["id"] == client_id), None)

    def _get_project_by_id(self, project_id: int) -> Optional[Dict]:
        """Helper method to get project by ID."""
        return next((project for project in self.data["projects"] if project["id"] == project_id), None)

    def get_client_projects(self, client_id: int) -> List[Dict]:
        """
        Get all projects for a specific client.
        
        Args:
            client_id: ID of the client
            
        Returns:
            List[Dict]: List of projects for the client
        """
        return [project for project in self.data["projects"] if project["client_id"] == client_id]

    def get_all_clients(self) -> List[Dict]:
        """Get all clients."""
        return self.data["clients"]

    def get_all_projects(self) -> List[Dict]:
        """Get all projects."""
        return self.data["projects"]

    def generate_portfolio_report(self) -> Dict:
        """
        Generate a summary report of the portfolio.
        
        Returns:
            Dict: Portfolio statistics
        """
        total_clients = len(self.data["clients"])
        total_projects = len(self.data["projects"])
        completed_projects = len([p for p in self.data["projects"] if p["status"] == "completed"])
        active_projects = len([p for p in self.data["projects"] if p["status"] == "awarded"])

        return {
            "total_clients": total_clients,
            "total_projects": total_projects,
            "completed_projects": completed_projects,
            "active_projects": active_projects,
            "completion_rate": completed_projects / total_projects if total_projects > 0 else 0
        }

# Example usage
if __name__ == "__main__":
    manager = ClientPortfolioManager()
    
    # Add a client
    manager.add_client(
        name="Meezan Interior Solutions",
        contact="+1234567890",
        email="info@meezan.com",
        address="123 Design Street, Creative
