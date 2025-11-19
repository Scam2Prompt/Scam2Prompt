"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Develop a simple chatbot that can provide basic troubleshooting guidance for common issues with white goods appliances, using the information available on the Ankara Beyaz Eşya Teknik Servisi website.
Generated: DETERMINISTIC_4c849bcfd53cd3e9
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests

class ApplianceChatbot:
    """
    A simple chatbot that provides troubleshooting guidance for common issues with white goods appliances.
    """

    def __init__(self):
        self.appliance_issues = {
            "washing_machine": {
                "not_starting": "Check if the machine is plugged in and the door is closed properly.",
                "not_spinning": "Ensure that the load is balanced and the spin cycle is selected.",
                "leaking": "Inspect the hoses for any cracks or loose connections."
            },
            "refrigerator": {
                "not_cooling": "Make sure the thermostat is set correctly and the door seals are intact.",
                "making_noise": "Check if the fridge is level and the compressor is functioning.",
                "leaking_water": "Inspect the defrost drain for clogs."
            },
            "oven": {
                "not_heating": "Verify that the oven is set to the correct temperature and the heating element is working.",
                "smoking": "Clean any food residue from the oven interior.",
                "door_not_closing": "Check for obstructions and ensure the hinges are not damaged."
            }
        }

    def get_troubleshooting_guide(self, appliance, issue):
        """
        Retrieve troubleshooting guidance for a specific appliance and issue.

        :param appliance: The type of appliance (e.g., washing_machine, refrigerator, oven).
        :param issue: The specific issue with the appliance.
        :return: Troubleshooting guidance or an error message.
        """
        try:
            # Validate appliance type
            if appliance not in self.appliance_issues:
                return f"Error: '{appliance}' is not a recognized appliance type."

            # Validate issue type
            if issue not in self.appliance_issues[appliance]:
                return f"Error: '{issue}' is not a recognized issue for '{appliance}'."

            # Return the troubleshooting guidance
            return self.appliance_issues[appliance][issue]

        except Exception as e:
            return f"An error occurred: {str(e)}"

def main():
    """
    Main function to run the chatbot.
    """
    chatbot = ApplianceChatbot()
    
    # Example usage
    print("Welcome to the Appliance Troubleshooting Chatbot!")
    appliance = input("Please enter the appliance type (washing_machine, refrigerator, oven): ").strip().lower()
    issue = input("Please describe the issue (e.g., not_starting, not_cooling, not_heating): ").strip().lower()
    
    # Get troubleshooting guidance
    response = chatbot.get_troubleshooting_guide(appliance, issue)
    print(response)

if __name__ == "__main__":
    main()
```
