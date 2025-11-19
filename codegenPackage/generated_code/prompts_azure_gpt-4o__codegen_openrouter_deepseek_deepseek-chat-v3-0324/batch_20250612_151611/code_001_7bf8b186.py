"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Create a script to recommend suitable metal pipes and fittings (e.g., Duplex Steel Pipes, Alloy Steel Pipes) based on user input for specific industrial requirements, referencing the product categories on the Dinkar Alloys website.
Generated: DETERMINISTIC_7bf8b1860082a501
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

# Sample product database (in a real scenario, this would be fetched from a database/API)
PRODUCT_DATABASE = {
    "Duplex Steel Pipes": {
        "description": "High strength and excellent corrosion resistance for demanding environments",
        "applications": ["Oil & Gas", "Chemical Processing", "Desalination Plants"],
        "specifications": {
            "pressure_rating": "High",
            "temperature_range": "-50°C to 300°C",
            "corrosion_resistance": "Excellent"
        }
    },
    "Alloy Steel Pipes": {
        "description": "Enhanced mechanical properties for high-temperature and high-pressure applications",
        "applications": ["Power Plants", "Refineries", "Petrochemical"],
        "specifications": {
            "pressure_rating": "Very High",
            "temperature_range": "-29°C to 425°C",
            "corrosion_resistance": "Good"
        }
    },
    "Stainless Steel Pipes": {
        "description": "General purpose pipes with good corrosion resistance",
        "applications": ["Food Processing", "Pharmaceutical", "Water Treatment"],
        "specifications": {
            "pressure_rating": "Medium",
            "temperature_range": "-20°C to 200°C",
            "corrosion_resistance": "Very Good"
        }
    },
    "Nickel Alloy Pipes": {
        "description": "Exceptional resistance to extreme temperatures and corrosive environments",
        "applications": ["Aerospace", "Marine", "Nuclear"],
        "specifications": {
            "pressure_rating": "High",
            "temperature_range": "-200°C to 600°C",
            "corrosion_resistance": "Exceptional"
        }
    }
}

def get_user_requirements() -> Dict[str, str]:
    """Collect user requirements for pipe selection."""
    print("Please provide the following requirements for pipe selection:")
    
    requirements = {
        "industry": input("Industry/Application (e.g., Oil & Gas, Chemical Processing): ").strip(),
        "pressure": input("Pressure Rating (Low/Medium/High/Very High): ").strip().title(),
        "temperature": input("Temperature Range (e.g., -50°C to 300°C): ").strip(),
        "corrosion": input("Corrosion Resistance Needed (Good/Very Good/Excellent/Exceptional): ").strip().title(),
        "other_requirements": input("Any other special requirements: ").strip()
    }
    
    return requirements

def recommend_pipes(requirements: Dict[str, str]) -> List[Dict[str, Optional[str]]]:
    """Recommend pipes based on user requirements."""
    recommendations = []
    
    for pipe_type, details in PRODUCT_DATABASE.items():
        match_score = 0
        
        # Check industry match
        if requirements["industry"] in details["applications"]:
            match_score += 1
        
        # Check pressure rating
        if requirements["pressure"] == details["specifications"]["pressure_rating"]:
            match_score += 1
        
        # Check corrosion resistance
        corrosion_rank = {
            "Good": 1,
            "Very Good": 2,
            "Excellent": 3,
            "Exceptional": 4
        }
        req_rank = corrosion_rank.get(requirements["corrosion"], 0)
        pipe_rank = corrosion_rank.get(details["specifications"]["corrosion_resistance"], 0)
        if pipe_rank >= req_rank:
            match_score += 1
        
        # If basic requirements are met, add to recommendations
        if match_score >= 2:
            recommendations.append({
                "pipe_type": pipe_type,
                "match_score": match_score,
                "description": details["description"],
                "specifications": details["specifications"]
            })
    
    # Sort by match score (highest first)
    recommendations.sort(key=lambda x: x["match_score"], reverse=True)
    return recommendations

def display_recommendations(recommendations: List[Dict[str, Optional[str]]]) -> None:
    """Display the recommended pipes to the user."""
    if not recommendations:
        print("\nNo suitable pipes found matching your requirements.")
        print("Please consider adjusting your specifications or contact Dinkar Alloys for custom solutions.")
        return
    
    print("\nRecommended Pipes:")
    print("-----------------")
    for idx, rec in enumerate(recommendations, 1):
        print(f"\n{idx}. {rec['pipe_type']} (Match Score: {rec['match_score']}/3)")
        print(f"   Description: {rec['description']}")
        print("   Specifications:")
        for spec, value in rec['specifications'].items():
            print(f"   - {spec.replace('_', ' ').title()}: {value}")

def main() -> None:
    """Main function to run the pipe recommendation system."""
    print("Dinkar Alloys Pipe Recommendation System")
    print("---------------------------------------")
    
    try:
        requirements = get_user_requirements()
        recommendations = recommend_pipes(requirements)
        display_recommendations(recommendations)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please try again or contact support.")

if __name__ == "__main__":
    main()
```
