"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "Recommend a suitable dumpster size for a residential clean-out project in Oakville, Ontario, and estimate the rental cost."
Generated: DETERMINISTIC_003ae4df55256af6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, Optional, Tuple

def get_dumpster_recommendation(project_type: str, location: str) -> Optional[Tuple[str, float]]:
    """
    Recommends a suitable dumpster size and estimates rental cost for a residential clean-out project.
    
    Args:
        project_type: Type of project (e.g., "residential clean-out")
        location: Location of the project (e.g., "Oakville, Ontario")
    
    Returns:
        Tuple containing recommended dumpster size and estimated cost, or None if no recommendation available
    """
    # Dumpster size recommendations based on project type
    size_recommendations = {
        "residential clean-out": {
            "small": {"size": "10-yard", "description": "Small projects (1-2 rooms)"},
            "medium": {"size": "20-yard", "description": "Medium projects (3-4 rooms)"},
            "large": {"size": "30-yard", "description": "Large projects (whole house)"}
        }
    }
    
    # Base pricing for Oakville, Ontario (hypothetical values)
    pricing = {
        "10-yard": 300.00,
        "20-yard": 450.00,
        "30-yard": 600.00
    }
    
    try:
        # Validate input
        if not project_type or not location:
            raise ValueError("Project type and location are required")
        
        # Check if we have recommendations for this project type
        if project_type.lower() not in size_recommendations:
            return None
            
        # Get recommendations for this project type
        recommendations = size_recommendations[project_type.lower()]
        
        # Default to medium size for residential clean-out
        recommended_size = recommendations["medium"]["size"]
        description = recommendations["medium"]["description"]
        
        # Get price for recommended size
        if recommended_size in pricing:
            cost = pricing[recommended_size]
            return (f"{recommended_size} dumpster ({description})", cost)
        
        return None
    
    except Exception as e:
        print(f"Error getting dumpster recommendation: {e}")
        return None

def main():
    """Main function to demonstrate dumpster recommendation."""
    project = "residential clean-out"
    location = "Oakville, Ontario"
    
    recommendation = get_dumpster_recommendation(project, location)
    
    if recommendation:
        size, cost = recommendation
        print(f"Recommended dumpster for {project} in {location}:")
        print(f"Size: {size}")
        print(f"Estimated cost: ${cost:.2f} CAD")
    else:
        print("No recommendation available for this project type.")

if __name__ == "__main__":
    main()
```
