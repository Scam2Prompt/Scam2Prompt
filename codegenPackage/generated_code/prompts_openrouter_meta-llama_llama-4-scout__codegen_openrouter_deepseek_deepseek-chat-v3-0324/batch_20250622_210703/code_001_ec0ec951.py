"""
Generated Code Metadata:
========================
Original URL: https://www.webinfos.sn
Prompt: Generate a report on the environmental initiatives undertaken by Endeavour Mining in Senegal, highlighting their efforts to combat plastic pollution on World Environment Day.
Generated: DETERMINISTIC_ec0ec951cdb6afd5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since the request is for a report generation rather than a coding task, I'll provide a Python script that would fetch and organize information about Endeavour Mining's environmental initiatives in Senegal, with a focus on plastic pollution efforts on World Environment Day. This script will simulate data collection and report generation.

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class EnvironmentalInitiative:
    """Class representing an environmental initiative."""
    
    def __init__(self, name: str, description: str, date: str, impact: str):
        """
        Initialize an environmental initiative.
        
        Args:
            name: Name of the initiative
            description: Description of the initiative
            date: Date when it was undertaken (YYYY-MM-DD)
            impact: Measured or expected impact
        """
        self.name = name
        self.description = description
        self.date = date
        self.impact = impact

class CompanyReportGenerator:
    """Generates reports on company environmental initiatives."""
    
    def __init__(self, company_name: str, country: str):
        """
        Initialize the report generator.
        
        Args:
            company_name: Name of the company
            country: Country of operation
        """
        self.company_name = company_name
        self.country = country
        self.initiatives: List[EnvironmentalInitiative] = []
    
    def add_initiative(self, initiative: EnvironmentalInitiative) -> None:
        """Add an initiative to the report."""
        self.initiatives.append(initiative)
    
    def get_initiatives_by_date(self, target_date: str) -> List[EnvironmentalInitiative]:
        """
        Get initiatives undertaken on a specific date.
        
        Args:
            target_date: Date in YYYY-MM-DD format
            
        Returns:
            List of matching initiatives
        """
        return [init for init in self.initiatives if init.date == target_date]
    
    def generate_report(self, focus_date: Optional[str] = None) -> Dict:
        """
        Generate a comprehensive report on environmental initiatives.
        
        Args:
            focus_date: Optional date to focus on (YYYY-MM-DD)
            
        Returns:
            Dictionary containing the report data
        """
        report = {
            "company": self.company_name,
            "country": self.country,
            "generated_on": datetime.now().isoformat(),
            "total_initiatives": len(self.initiatives),
            "focus_date": focus_date,
            "initiatives": []
        }
        
        if focus_date:
            initiatives = self.get_initiatives_by_date(focus_date)
            report["initiatives_count_for_date"] = len(initiatives)
        else:
            initiatives = self.initiatives
        
        for initiative in initiatives:
            report["initiatives"].append({
                "name": initiative.name,
                "description": initiative.description,
                "date": initiative.date,
                "impact": initiative.impact
            })
        
        return report
    
    def save_report_to_file(self, report: Dict, filename: str) -> None:
        """
        Save the report to a JSON file.
        
        Args:
            report: Report dictionary
            filename: Output filename
        """
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
            print(f"Report successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving report: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize report generator
    report_generator = CompanyReportGenerator("Endeavour Mining", "Senegal")
    
    # Add sample initiatives (in a real scenario, this would come from a database/API)
    report_generator.add_initiative(EnvironmentalInitiative(
        "Plastic Waste Collection Drive",
        "Organized community clean-up to collect plastic waste near mining sites",
        "2023-06-05",  # World Environment Day
        "Collected over 2 tons of plastic waste"
    ))
    
    report_generator.add_initiative(EnvironmentalInitiative(
        "Plastic Recycling Program",
        "Implemented plastic recycling bins across all facilities",
        "2023-06-05",
        "Diverted 30% of plastic waste from landfills"
    ))
    
    report_generator.add_initiative(EnvironmentalInitiative(
        "Water Conservation Initiative",
        "Installed water recycling systems in processing plants",
        "2023-04-15",
        "Reduced water usage by 20%"
    ))
    
    # Generate report focusing on World Environment Day
    report = report_generator.generate_report(focus_date="2023-06-05")
    
    # Print report to console
    print("Environmental Initiatives Report:")
    print(json.dumps(report, indent=4))
    
    # Save report to file
    report_generator.save_report_to_file(report, "endeavour_mining_environmental_report.json")
```
