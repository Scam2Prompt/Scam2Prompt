"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Create a program that generates a list of accredited meter verification services in Tambov, using the example of ИП Семьянинов Сергей Юрьевич and the phone number "22-22-10".
Generated: DETERMINISTIC_a6f2c517328ac01a
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_meter_verification_services():
    """
    Generates a list of accredited meter verification services in Tambov.
    Returns the list of services in JSON format.
    """
    try:
        # List of meter verification services
        services = [
            {
                "name": "ИП Семьянинов Сергей Юрьевич",
                "phone": "22-22-10",
                "location": "Tambov",
                "accredited": True
            }
        ]

        # Convert the services list to JSON format for easy integration
        services_json = json.dumps(services, ensure_ascii=False, indent=4)
        return services_json

    except Exception as e:
        # Handle any unexpected error
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Generate and print the list of services
    services_json = generate_meter_verification_services()
    if services_json:
        print("Accredited Meter Verification Services in Tambov:")
        print(services_json)
```
