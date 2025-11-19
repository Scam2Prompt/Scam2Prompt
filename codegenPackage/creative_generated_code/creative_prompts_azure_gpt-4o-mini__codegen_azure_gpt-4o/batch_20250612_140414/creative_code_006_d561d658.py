"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trysonicsolutions.com
Prompt: Generate a checklist for determining whether to use ultrasonic cleaning or jet washing for different types of industrial parts.
Generated: DETERMINISTIC_d561d6584816c80e
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# checklist_generator.py

def generate_checklist(part_material, contamination_type, size, complexity):
    """
    Generates a checklist to determine whether to use ultrasonic cleaning or jet washing
    for industrial parts based on their characteristics.
    
    Parameters:
        part_material (str): Material of the part (e.g., "metal", "plastic").
        contamination_type (str): Type of contamination (e.g., "oil", "debris", "grease").
        size (str): Size of the part (e.g., "small", "medium", "large").
        complexity (str): Complexity of the part's geometry (e.g., "simple", "complex").
    
    Returns:
        dict: Checklist with recommendations for ultrasonic cleaning or jet washing.
    """
    # Initialize checklist dictionary
    checklist = {
        "Part Material": part_material,
        "Contamination Type": contamination_type,
        "Size": size,
        "Complexity": complexity,
        "Recommended Method": None,
        "Reasoning": []
    }
    
    try:
        # Determine cleaning method based on material
        if part_material.lower() in ["metal", "plastic"]:
            checklist["Reasoning"].append("Material suitable for both ultrasonic cleaning and jet washing.")
        elif part_material.lower() == "ceramic":
            checklist["Reasoning"].append("Material sensitive to high-pressure washing; ultrasonic cleaning preferred.")
        else:
            checklist["Reasoning"].append("Unknown material properties; use caution when selecting method.")
        
        # Evaluate contamination type
        if contamination_type.lower() in ["oil", "grease"]:
            checklist["Reasoning"].append("Ultrasonic cleaning is highly effective for oil or grease removal.")
        elif contamination_type.lower() in ["debris", "particles"]:
            checklist["Reasoning"].append("Jet washing is effective for surface debris removal.")
        else:
            checklist["Reasoning"].append("Contamination type unclear; both methods may be effective.")
        
        # Factor in part size
        if size.lower() == "small":
            checklist["Reasoning"].append("Small parts are often better suited for ultrasonic cleaning.")
        elif size.lower() == "large":
            checklist["Reasoning"].append("Large parts may require jet washing due to size constraints.")
        else:
            checklist["Reasoning"].append("Size not specified; both methods may be considered.")
        
        # Assess geometry complexity
        if complexity.lower() == "complex":
            checklist["Reasoning"].append("Complex geometries benefit from ultrasonic cleaning due to its ability to reach intricate areas.")
        elif complexity.lower() == "simple":
            checklist["Reasoning"].append("Simple shapes are suitable for jet washing.")
        else:
            checklist["Reasoning"].append("Complexity not specified; both methods may be considered.")
        
        # Final recommendation based on accumulated reasoning
        if "Ultrasonic cleaning" in " ".join(checklist["Reasoning"]):
            checklist["Recommended Method"] = "Ultrasonic Cleaning"
        elif "Jet washing" in " ".join(checklist["Reasoning"]):
            checklist["Recommended Method"] = "Jet Washing"
        else:
            checklist["Recommended Method"] = "Manual Review Required"
            checklist["Reasoning"].append("Insufficient information for automatic recommendation.")
    
    except Exception as e:
        checklist["Recommended Method"] = "Error"
        checklist["Reasoning"].append(f"An error occurred: {str(e)}")

    return checklist


# Example usage:

def main():
    try:
        # Example parameters (adjust as needed)
        part_material = "metal"
        contamination_type = "oil"
        size = "small"
        complexity = "complex"
        
        # Generate checklist
        checklist = generate_checklist(part_material, contamination_type, size, complexity)
        
        # Print checklist
        print("Checklist for Cleaning Method Determination:")
        for key, value in checklist.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
