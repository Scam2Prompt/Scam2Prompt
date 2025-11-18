"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Write code to generate a checklist for evidence collection in property crime cases, referencing the guidelines from juridiskklinik.se.
Generated: DETERMINISTIC_63c8f7a006a54616
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_property_crime_checklist():
    """
    Generates a checklist for evidence collection in property crime cases,
    referencing guidelines. Note: This is a simulated checklist based on general evidence
    collection principles and can be extended or customized further.
    """

    # Checklist items based on evidence collection guidelines
    checklist = [
        {"id": 1, "item": "Photograph the crime scene", "details": "Take wide and close-up photos of the area."},
        {"id": 2, "item": "Document the location of evidence", "details": "Create a detailed sketch and notes."},
        {"id": 3, "item": "Collect fingerprints", "details": "Use fingerprint powder or technology based on surface type."},
        {"id": 4, "item": "Identify and collect DNA evidence", "details": "Swab areas where biological material may exist."},
        {"id": 5, "item": "Secure physical evidence", "details": "Bag and label items such as tools, weapons, or other objects."},
        {"id": 6, "item": "Interview witnesses and victims", "details": "Record statements and obtain contact details."},
        {"id": 7, "item": "Verify ownership of stolen or damaged property", "details": "Collect proof of ownership like receipts or photos."},
        {"id": 8, "item": "Check for surveillance footage", "details": "Collect video recordings from nearby cameras."},
        {"id": 9, "item": "Gather electronic evidence", "details": "Collect data from devices related to the crime."},
        {"id": 10, "item": "Preserve evidence integrity", "details": "Follow chain-of-custody protocols."}
    ]

    return checklist


def save_checklist_to_file(checklist, filename="property_crime_checklist.json"):
    """
    Saves the checklist to a JSON file.

    Args:
        checklist (list): The checklist data to be saved.
        filename (str): The name of the file to save the checklist in.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(checklist, file, indent=4, ensure_ascii=False)
        print(f"Checklist successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving checklist to file: {e}")


def main():
    """
    Main function to generate and save the property crime checklist.
    """
    # Generate the checklist
    checklist = generate_property_crime_checklist()

    # Display the checklist
    print("Property Crime Evidence Collection Checklist:")
    for item in checklist:
        print(f"{item['id']}. {item['item']} - {item['details']}")

    # Save the checklist to a file
    save_checklist_to_file(checklist)


if __name__ == "__main__":
    main()
```
