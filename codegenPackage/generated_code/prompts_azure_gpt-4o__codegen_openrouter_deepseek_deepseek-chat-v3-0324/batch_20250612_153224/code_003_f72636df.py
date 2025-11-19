"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: Write a script to manage emergency preparedness plans for organizations, incorporating key elements from GESEC's "Plan y Preparación ante Emergencias" service.
Generated: DETERMINISTIC_f72636dfbb5b7d63
Batch ID: 20250612_153224
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

class EmergencyPlanManager:
    """
    A class to manage emergency preparedness plans for organizations.
    Incorporates key elements from GESEC's "Plan y Preparación ante Emergencias" service.
    """

    def __init__(self, data_file: str = "emergency_plans.json"):
        """
        Initialize the EmergencyPlanManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing emergency plans. Defaults to "emergency_plans.json".
        """
        self.data_file = data_file
        self.plans = self._load_plans()

    def _load_plans(self) -> Dict[str, Dict]:
        """
        Load emergency plans from the data file.
        
        Returns:
            Dict[str, Dict]: Dictionary of emergency plans.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading plans: {e}")
            return {}

    def _save_plans(self) -> bool:
        """
        Save emergency plans to the data file.
        
        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.plans, f, indent=4, ensure_ascii=False)
            return True
        except (IOError, TypeError) as e:
            print(f"Error saving plans: {e}")
            return False

    def create_plan(
        self,
        organization_id: str,
        plan_name: str,
        emergency_types: List[str],
        contact_persons: List[Dict[str, str]],
        evacuation_routes: List[Dict[str, str]],
        emergency_supplies: List[str],
        procedures: Dict[str, str],
        last_review_date: Optional[str] = None
    ) -> bool:
        """
        Create a new emergency preparedness plan.
        
        Args:
            organization_id (str): Unique identifier for the organization.
            plan_name (str): Name of the emergency plan.
            emergency_types (List[str]): Types of emergencies covered (e.g., fire, earthquake).
            contact_persons (List[Dict[str, str]]): List of contact persons with name, role, and phone.
            evacuation_routes (List[Dict[str, str]]): List of evacuation routes with description and map reference.
            emergency_supplies (List[str]): List of emergency supplies.
            procedures (Dict[str, str]): Dictionary of procedures for different emergency types.
            last_review_date (Optional[str]): Last review date in YYYY-MM-DD format. Defaults to current date.
            
        Returns:
            bool: True if plan was created successfully, False otherwise.
        """
        if organization_id in self.plans:
            print(f"Organization {organization_id} already has a plan.")
            return False

        if not last_review_date:
            last_review_date = datetime.now().strftime("%Y-%m-%d")

        self.plans[organization_id] = {
            "plan_name": plan_name,
            "emergency_types": emergency_types,
            "contact_persons": contact_persons,
            "evacuation_routes": evacuation_routes,
            "emergency_supplies": emergency_supplies,
            "procedures": procedures,
            "last_review_date": last_review_date,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return self._save_plans()

    def update_plan(
        self,
        organization_id: str,
        plan_name: Optional[str] = None,
        emergency_types: Optional[List[str]] = None,
        contact_persons: Optional[List[Dict[str, str]]] = None,
        evacuation_routes: Optional[List[Dict[str, str]]] = None,
        emergency_supplies: Optional[List[str]] = None,
        procedures: Optional[Dict[str, str]] = None,
        update_review_date: bool = True
    ) -> bool:
        """
        Update an existing emergency preparedness plan.
        
        Args:
            organization_id (str): Unique identifier for the organization.
            plan_name (Optional[str]): Updated plan name. Defaults to None.
            emergency_types (Optional[List[str]]): Updated emergency types. Defaults to None.
            contact_persons (Optional[List[Dict[str, str]]]): Updated contact persons. Defaults to None.
            evacuation_routes (Optional[List[Dict[str, str]]]): Updated evacuation routes. Defaults to None.
            emergency_supplies (Optional[List[str]]): Updated emergency supplies. Defaults to None.
            procedures (Optional[Dict[str, str]]): Updated procedures. Defaults to None.
            update_review_date (bool): Whether to update the last review date. Defaults to True.
            
        Returns:
            bool: True if plan was updated successfully, False otherwise.
        """
        if organization_id not in self.plans:
            print(f"Organization {organization_id} does not have a plan.")
            return False

        plan = self.plans[organization_id]

        if plan_name:
            plan["plan_name"] = plan_name
        if emergency_types:
            plan["emergency_types"] = emergency_types
        if contact_persons:
            plan["contact_persons"] = contact_persons
        if evacuation_routes:
            plan["evacuation_routes"] = evacuation_routes
        if emergency_supplies:
            plan["emergency_supplies"] = emergency_supplies
        if procedures:
            plan["procedures"] = procedures
        if update_review_date:
            plan["last_review_date"] = datetime.now().strftime("%Y-%m-%d")

        return self._save_plans()

    def get_plan(self, organization_id: str) -> Optional[Dict[str, Union[str, List, Dict]]]:
        """
        Retrieve an emergency preparedness plan.
        
        Args:
            organization_id (str): Unique identifier for the organization.
            
        Returns:
            Optional[Dict[str, Union[str, List, Dict]]]: The emergency plan if found, None otherwise.
        """
        return self.plans.get(organization_id)

    def delete_plan(self, organization_id: str) -> bool:
        """
        Delete an emergency preparedness plan.
        
        Args:
            organization_id (str): Unique identifier for the organization.
            
        Returns:
            bool: True if plan was deleted successfully, False otherwise.
        """
        if organization_id not in self.plans:
            print(f"Organization {organization_id} does not have a plan.")
            return False

        del self.plans[organization_id]
        return self._save_plans()

    def list_plans(self) -> List[str]:
        """
        List all organization IDs with emergency plans.
        
        Returns:
            List[str]: List of organization IDs.
        """
        return list(self.plans.keys())

    def validate_plan(self, organization_id: str) -> Dict[str, Union[bool, List[str]]]:
        """
        Validate if a plan contains all required elements.
        
        Args:
            organization_id (str): Unique identifier for the organization.
            
        Returns:
            Dict[str, Union[bool, List[str]]]: Dictionary with 'valid' boolean and 'missing_fields' list.
        """
        required_fields = [
            "plan_name",
            "emergency_types",
            "contact_persons",
            "evacuation_routes",
            "emergency_supplies",
            "procedures",
            "last_review_date"
        ]

        plan = self.get_plan(organization_id)
        if not plan:
            return {"valid": False, "missing_fields": ["Plan not found"]}

        missing_fields = [
            field for field in required_fields 
            if field not in plan or not plan[field]
        ]

        return {
            "valid": len(missing_fields) == 0,
            "missing_fields": missing_fields
        }

    def export_plan(self, organization_id: str, output_file: str) -> bool:
        """
        Export an emergency plan to a JSON file.
        
        Args:
            organization_id (str): Unique identifier for the organization.
            output_file (str): Path to the output JSON file.
            
        Returns:
            bool: True if export was successful, False otherwise.
        """
        plan = self.get_plan(organization_id)
        if not plan:
            print(f"Organization {organization_id} does not have a plan.")
            return False

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(plan, f, indent=4, ensure_ascii=False)
            return True
        except IOError as e:
            print(f"Error exporting plan: {e}")
            return False

    def import_plan(self, organization_id: str, input_file: str) -> bool:
        """
        Import an emergency plan from a JSON file.
        
        Args:
            organization_id (str): Unique identifier for the organization.
