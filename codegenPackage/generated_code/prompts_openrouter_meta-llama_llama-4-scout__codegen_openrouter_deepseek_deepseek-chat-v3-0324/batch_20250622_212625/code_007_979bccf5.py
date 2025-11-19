"""
Generated Code Metadata:
========================
Original URL: https://en.clark-zapper.com
Prompt: Generate a list of safety precautions and contraindications for using a Hulda Clark Zapper, based on the provided content.
Generated: DETERMINISTIC_979bccf5a01b0642
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_safety_precautions():
    """
    Returns a list of safety precautions and contraindications for using a Hulda Clark Zapper.
    """
    precautions = [
        "Do not use the zapper if you have a pacemaker or other implanted electronic device.",
        "Consult with a healthcare professional before use if you are pregnant or nursing.",
        "Avoid using the zapper if you have epilepsy or a history of seizures.",
        "Do not use the zapper on open wounds or broken skin.",
        "Keep the zapper away from water and moisture to prevent electric shock.",
        "Do not use the zapper near flammable gases or materials.",
        "Discontinue use if you experience dizziness, nausea, or discomfort.",
        "Do not use the zapper on children without medical supervision.",
        "Avoid using the zapper if you have a known heart condition.",
        "Do not use the zapper while operating heavy machinery or driving.",
        "Always follow the manufacturer's instructions for proper usage.",
        "Ensure the device is properly grounded before use.",
        "Do not exceed recommended usage duration.",
        "Keep the zapper out of reach of children and pets.",
        "Inspect the device and cables for damage before each use.",
        "Do not modify or disassemble the zapper.",
        "Store the zapper in a cool, dry place when not in use.",
        "Do not use the zapper while sleeping or unconscious.",
        "Avoid using the zapper on sensitive areas like eyes or mucous membranes.",
        "If you experience skin irritation, discontinue use immediately."
    ]
    
    contraindications = [
        "Pacemakers or implanted electronic devices",
        "Pregnancy",
        "Epilepsy or seizure disorders",
        "Open wounds or broken skin",
        "Heart conditions",
        "Children under medical supervision",
        "Recent surgery or medical procedures",
        "Metal implants (consult physician)",
        "Organ transplants (consult physician)",
        "Hypersensitivity to electrical stimulation"
    ]
    
    return {
        "safety_precautions": precautions,
        "contraindications": contraindications
    }

# Example usage
if __name__ == "__main__":
    safety_info = generate_safety_precautions()
    print("Safety Precautions:")
    for i, precaution in enumerate(safety_info["safety_precautions"], 1):
        print(f"{i}. {precaution}")
    
    print("\nContraindications:")
    for i, contraindication in enumerate(safety_info["contraindications"], 1):
        print(f"{i}. {contraindication}")
```
