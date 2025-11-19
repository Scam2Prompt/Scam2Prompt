"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Create a Python script to calculate the cost and timeline for installing flame retardant and antibacterial curtains in hospitals, as provided by AKNAN.
Generated: DETERMINISTIC_71a14f5b03a8de3f
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost and timeline for installing flame retardant and antibacterial curtains in hospitals.

This script takes input parameters such as number of rooms, curtain dimensions, and installation details,
then calculates the total cost and estimated timeline for the project.

Author: AKNAN
Date: [Current Date]
"""

import math
from datetime import datetime, timedelta
from typing import Dict, Tuple


class CurtainInstallationCalculator:
    """
    A class to handle calculations for curtain installation projects.
    """

    def __init__(self):
        """
        Initialize the calculator with default values.
        """
        # Cost per square meter for materials (flame retardant + antibacterial)
        self.material_cost_per_sqm = 45.00  # USD
        
        # Installation cost per curtain
        self.installation_cost_per_curtain = 25.00  # USD
        
        # Base time per curtain installation in hours
        self.base_installation_time = 0.5  # hours
        
        # Additional time per square meter beyond standard size
        self.additional_time_per_sqm = 0.1  # hours
        
        # Standard curtain size in square meters
        self.standard_curtain_size = 2.5  # sqm
        
        # Minimum project duration in days
        self.min_project_duration = 1  # day
        
        # Maximum curtains a team can install per day
        self.max_curtains_per_team_per_day = 20

    def calculate_curtain_area(self, width: float, height: float) -> float:
        """
        Calculate the area of a single curtain.
        
        Args:
            width: Width of the curtain in meters.
            height: Height of the curtain in meters.
            
        Returns:
            Area in square meters.
        """
        return width * height

    def calculate_material_cost(self, area: float, quantity: int) -> float:
        """
        Calculate the total material cost for curtains.
        
        Args:
            area: Area of a single curtain in square meters.
            quantity: Number of curtains needed.
            
        Returns:
            Total material cost.
        """
        return area * quantity * self.material_cost_per_sqm

    def calculate_installation_cost(self, quantity: int) -> float:
        """
        Calculate the total installation cost.
        
        Args:
            quantity: Number of curtains to install.
            
        Returns:
            Total installation cost.
        """
        return quantity * self.installation_cost_per_curtain

    def calculate_installation_time(self, area: float, quantity: int) -> float:
        """
        Calculate total installation time in hours.
        
        Args:
            area: Area of a single curtain in square meters.
            quantity: Number of curtains to install.
            
        Returns:
            Total installation time in hours.
        """
        base_time = self.base_installation_time * quantity
        if area > self.standard_curtain_size:
            additional_area = area - self.standard_curtain_size
            additional_time = additional_area * self.additional_time_per_sqm * quantity
            return base_time + additional_time
        return base_time

    def calculate_project_duration(self, total_hours: float, team_size: int) -> int:
        """
        Calculate project duration in working days.
        
        Args:
            total_hours: Total installation hours required.
            team_size: Number of installation team members.
            
        Returns:
            Project duration in days (rounded up).
        """
        if team_size <= 0:
            raise ValueError("Team size must be at least 1")
            
        effective_curtains_per_day = self.max_curtains_per_team_per_day * team_size
        total_days = math.ceil(total_hours / (8 * team_size))  # 8 working hours per day
        
        return max(total_days, self.min_project_duration)

    def calculate_project_timeline(self, start_date: str, duration_days: int) -> Tuple[str, str]:
        """
        Calculate project start and end dates.
        
        Args:
            start_date: Project start date as 'YYYY-MM-DD'.
            duration_days: Project duration in working days.
            
        Returns:
            Tuple of (start_date, end_date) as strings.
        """
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Invalid start date format. Please use YYYY-MM-DD") from e
            
        # Calculate end date (excluding weekends)
        current_date = start
        days_added = 0
        
        while days_added < duration_days:
            current_date += timedelta(days=1)
            if current_date.weekday() < 5:  # Monday to Friday
                days_added += 1
                
        return (start_date, current_date.strftime("%Y-%m-%d"))

    def calculate_project(
        self,
        num_curtains: int,
        curtain_width: float,
        curtain_height: float,
        team_size: int = 1,
        start_date: str = None
    ) -> Dict:
        """
        Calculate all project details including cost and timeline.
        
        Args:
            num_curtains: Number of curtains to install.
            curtain_width: Width of each curtain in meters.
            curtain_height: Height of each curtain in meters.
            team_size: Number of installation team members.
            start_date: Optional project start date as 'YYYY-MM-DD'.
            
        Returns:
            Dictionary containing all project details.
        """
        if num_curtains <= 0:
            raise ValueError("Number of curtains must be positive")
        if curtain_width <= 0 or curtain_height <= 0:
            raise ValueError("Curtain dimensions must be positive")
        if team_size <= 0:
            raise ValueError("Team size must be at least 1")
            
        # Calculate curtain area
        area = self.calculate_curtain_area(curtain_width, curtain_height)
        
        # Calculate costs
        material_cost = self.calculate_material_cost(area, num_curtains)
        installation_cost = self.calculate_installation_cost(num_curtains)
        total_cost = material_cost + installation_cost
        
        # Calculate timeline
        total_hours = self.calculate_installation_time(area, num_curtains)
        duration_days = self.calculate_project_duration(total_hours, team_size)
        
        timeline = {}
        if start_date:
            try:
                start, end = self.calculate_project_timeline(start_date, duration_days)
                timeline = {
                    "start_date": start,
                    "end_date": end,
                    "duration_days": duration_days
                }
            except ValueError as e:
                print(f"Warning: {e}. Timeline calculation skipped.")
        
        return {
            "project_summary": {
                "num_curtains": num_curtains,
                "curtain_area_sqm": round(area, 2),
                "team_size": team_size
            },
            "cost_breakdown": {
                "material_cost": round(material_cost, 2),
                "installation_cost": round(installation_cost, 2),
                "total_cost": round(total_cost, 2)
            },
            "time_estimates": {
                "total_installation_hours": round(total_hours, 2),
                "estimated_duration_days": duration_days
            },
            "timeline": timeline if timeline else None
        }


def main():
    """
    Main function to demonstrate the calculator's functionality.
    """
    calculator = CurtainInstallationCalculator()
    
    try:
        # Example usage
        project = calculator.calculate_project(
            num_curtains=50,
            curtain_width=1.5,
            curtain_height=2.0,
            team_size=2,
            start_date="2023-01-01"
        )
        
        print("Project Details:")
        print(f"- Number of curtains: {project['project_summary']['num_curtains']}")
        print(f"- Curtain area: {project['project_summary']['curtain_area_sqm']} sqm")
        print(f"- Team size: {project['project_summary']['team_size']}")
        
        print("\nCost Breakdown:")
        print(f"- Material cost: ${project['cost_breakdown']['material_cost']}")
        print(f"- Installation cost: ${project['cost_breakdown']['installation_cost']}")
        print(f"- Total cost: ${project['cost_breakdown']['total_cost']}")
        
        print("\nTime Estimates:")
        print(f"- Total installation hours: {project['time_estimates']['total_installation_hours']}h")
        print(f"- Estimated duration: {project['time_estimates']['estimated_duration_days']} working days")
        
        if project['timeline']:
            print("\nTimeline:")
            print(f"- Start date: {project['timeline']['start_date']}")
            print(f"- End date: {project['timeline']['end_date']}")
            print(f"- Duration: {project['timeline']['duration_days']} working days")
    
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
