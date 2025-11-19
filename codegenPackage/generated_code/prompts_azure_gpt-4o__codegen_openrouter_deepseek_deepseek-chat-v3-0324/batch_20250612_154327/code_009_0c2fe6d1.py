"""
Generated Code Metadata:
========================
Original URL: https://stakehelp.com
Prompt: Provide a solution for automating the management of casino game site data, including group company lists and business activities, as outlined by Medipal Holdings Co., Ltd.
Generated: DETERMINISTIC_0c2fe6d15f142f26
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
import os
from typing import List, Dict, Optional
from datetime import datetime
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CasinoDataManager:
    """
    A class to manage casino game site data including group company lists and business activities.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the data manager with a directory to store data files.
        
        Args:
            data_dir (str): Directory path for storing data files. Defaults to "data".
        """
        self.data_dir = Path(data_dir)
        self.companies_file = self.data_dir / "companies.json"
        self.activities_file = self.data_dir / "activities.csv"
        
        # Create data directory if it doesn't exist
        self.data_dir.mkdir(exist_ok=True)
        
        # Initialize empty data structures if files don't exist
        if not self.companies_file.exists():
            self._initialize_companies_file()
        if not self.activities_file.exists():
            self._initialize_activities_file()
    
    def _initialize_companies_file(self) -> None:
        """Initialize the companies JSON file with an empty list."""
        try:
            with open(self.companies_file, 'w') as f:
                json.dump([], f)
            logger.info(f"Created new companies file at {self.companies_file}")
        except IOError as e:
            logger.error(f"Failed to initialize companies file: {e}")
            raise
    
    def _initialize_activities_file(self) -> None:
        """Initialize the activities CSV file with headers."""
        try:
            with open(self.activities_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp", "company_id", "activity_type", 
                    "description", "amount", "currency"
                ])
            logger.info(f"Created new activities file at {self.activities_file}")
        except IOError as e:
            logger.error(f"Failed to initialize activities file: {e}")
            raise
    
    def add_company(self, company_data: Dict) -> None:
        """
        Add a new company to the companies list.
        
        Args:
            company_data (Dict): Dictionary containing company details with keys:
                - id: Unique identifier for the company
                - name: Company name
                - country: Country of operation
                - license_number: Gaming license number
                - status: Current operational status
        """
        required_fields = {'id', 'name', 'country', 'license_number', 'status'}
        if not required_fields.issubset(company_data.keys()):
            raise ValueError(f"Company data must contain all required fields: {required_fields}")
        
        try:
            # Read existing companies
            with open(self.companies_file, 'r') as f:
                companies = json.load(f)
            
            # Check for duplicate ID
            if any(c['id'] == company_data['id'] for c in companies):
                raise ValueError(f"Company with ID {company_data['id']} already exists")
            
            # Add new company
            companies.append(company_data)
            
            # Write back to file
            with open(self.companies_file, 'w') as f:
                json.dump(companies, f, indent=2)
            
            logger.info(f"Added new company: {company_data['name']} (ID: {company_data['id']})")
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Failed to add company: {e}")
            raise
    
    def get_companies(self) -> List[Dict]:
        """
        Retrieve the list of all companies.
        
        Returns:
            List[Dict]: List of company dictionaries
        """
        try:
            with open(self.companies_file, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Failed to retrieve companies: {e}")
            raise
    
    def record_activity(self, company_id: str, activity_type: str, 
                       description: str, amount: float, currency: str = "USD") -> None:
        """
        Record a business activity for a company.
        
        Args:
            company_id (str): ID of the company
            activity_type (str): Type of activity (e.g., "deposit", "withdrawal", "game_result")
            description (str): Description of the activity
            amount (float): Monetary amount involved
            currency (str): Currency code. Defaults to "USD".
        """
        # Validate company exists
        companies = self.get_companies()
        if not any(c['id'] == company_id for c in companies):
            raise ValueError(f"Company with ID {company_id} not found")
        
        timestamp = datetime.now().isoformat()
        activity_data = {
            "timestamp": timestamp,
            "company_id": company_id,
            "activity_type": activity_type,
            "description": description,
            "amount": amount,
            "currency": currency
        }
        
        try:
            with open(self.activities_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    activity_data["timestamp"],
                    activity_data["company_id"],
                    activity_data["activity_type"],
                    activity_data["description"],
                    activity_data["amount"],
                    activity_data["currency"]
                ])
            logger.info(f"Recorded activity for company {company_id}: {activity_type}")
        except IOError as e:
            logger.error(f"Failed to record activity: {e}")
            raise
    
    def get_activities(self, company_id: Optional[str] = None) -> List[Dict]:
        """
        Retrieve business activities, optionally filtered by company ID.
        
        Args:
            company_id (Optional[str]): If provided, filter activities by this company ID
            
        Returns:
            List[Dict]: List of activity dictionaries
        """
        activities = []
        try:
            with open(self.activities_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert amount to float
                    row['amount'] = float(row['amount'])
                    activities.append(row)
        except (IOError, ValueError) as e:
            logger.error(f"Failed to retrieve activities: {e}")
            raise
        
        if company_id:
            activities = [a for a in activities if a['company_id'] == company_id]
        
        return activities
    
    def generate_report(self, output_file: str = "report.csv") -> None:
        """
        Generate a consolidated report of companies and their activities.
        
        Args:
            output_file (str): Path to save the report. Defaults to "report.csv".
        """
        try:
            companies = self.get_companies()
            activities = self.get_activities()
            
            # Prepare report data
            report_data = []
            for company in companies:
                company_activities = [a for a in activities if a['company_id'] == company['id']]
                total_amount = sum(a['amount'] for a in company_activities)
                
                report_data.append({
                    "company_id": company['id'],
                    "company_name": company['name'],
                    "country": company['country'],
                    "license_number": company['license_number'],
                    "status": company['status'],
                    "activity_count": len(company_activities),
                    "total_amount": total_amount,
                    "currency": "USD"  # Assuming all amounts are in USD for the report
                })
            
            # Write report to CSV
            output_path = Path(output_file)
            with open(output_path, 'w', newline='') as f:
                fieldnames = [
                    "company_id", "company_name", "country", "license_number",
                    "status", "activity_count", "total_amount", "currency"
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(report_data)
            
            logger.info(f"Generated report at {output_path}")
        except Exception as e:
            logger.error(f"Failed to generate report: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize data manager
        manager = CasinoDataManager()
        
        # Add sample companies
        manager.add_company({
            "id": "medipal001",
            "name": "Medipal Holdings Co., Ltd.",
            "country": "Japan",
            "license_number": "JP123456",
            "status": "active"
        })
        
        manager.add_company({
            "id": "casino777",
            "name": "777 Casino Group",
            "country": "Malta",
            "license_number": "MT654321",
            "status": "active"
        })
        
        # Record sample activities
        manager.record_activity(
            company_id="medipal001",
            activity_type="deposit",
            description="Initial funding",
            amount=1000000.00
        )
        
        manager.record_activity(
            company_id="casino777",
            activity_type="game_result",
            description
