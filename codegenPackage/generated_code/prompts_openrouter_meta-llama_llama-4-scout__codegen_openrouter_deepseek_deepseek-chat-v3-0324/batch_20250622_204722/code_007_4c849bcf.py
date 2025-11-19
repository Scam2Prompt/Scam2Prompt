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
import json
from typing import Dict, List, Optional

class WhiteGoodsChatbot:
    """
    A simple chatbot that provides troubleshooting guidance for common white goods appliance issues.
    Data is based on information from Ankara Beyaz Eşya Teknik Servisi website.
    """
    
    def __init__(self):
        self.knowledge_base = self._load_knowledge_base()
    
    def _load_knowledge_base(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Load the knowledge base with appliance troubleshooting information.
        Returns:
            Dictionary containing appliance categories and their issues/solutions.
        """
        return {
            "refrigerator": {
                "not_cooling": [
                    "Check if the refrigerator is properly plugged in.",
                    "Ensure the thermostat is set to the correct temperature.",
                    "Clean the condenser coils at the back or bottom of the fridge.",
                    "Check if the door seals are intact and closing properly."
                ],
                "water_leakage": [
                    "Check if the defrost drain is clogged and clean it if necessary.",
                    "Ensure the refrigerator is level to prevent water pooling.",
                    "Inspect water supply lines for leaks if your fridge has a water dispenser."
                ],
                "noisy": [
                    "Check if the refrigerator is level and adjust the feet if needed.",
                    "Ensure nothing is touching the back of the fridge where the compressor is located.",
                    "Clean the fan blades if the noise is coming from the freezer section."
                ]
            },
            "washing_machine": {
                "not_spinning": [
                    "Check if the load is unbalanced and redistribute clothes.",
                    "Ensure the lid/door is properly closed (many machines won't spin if open).",
                    "Check for error codes and consult the manual.",
                    "Inspect the drive belt for wear or damage."
                ],
                "water_not_draining": [
                    "Check if the drain hose is kinked or clogged.",
                    "Clean the drain pump filter (usually located behind a small access panel).",
                    "Ensure the drain hose is properly installed."
                ],
                "excessive_vibration": [
                    "Ensure the machine is level on all sides.",
                    "Check if the shipping bolts were removed during installation.",
                    "Make sure the load is balanced and not too small."
                ]
            },
            "dishwasher": {
                "not_cleaning": [
                    "Check if the spray arms are clogged and clean them.",
                    "Ensure you're using the right detergent and proper amount.",
                    "Clean the filter at the bottom of the dishwasher.",
                    "Check water temperature (should be at least 120°F/50°C)."
                ],
                "not_draining": [
                    "Check for food debris blocking the drain.",
                    "Clean the drain filter and garbage disposal connection if applicable.",
                    "Inspect the drain hose for kinks or clogs."
                ],
                "leaking": [
                    "Check door seal for damage or food debris.",
                    "Ensure the dishwasher is level.",
                    "Inspect water inlet valve and hoses for leaks."
                ]
            },
            "oven": {
                "not_heating": [
                    "Check if the oven is properly plugged in or gas supply is on.",
                    "Verify the temperature settings are correct.",
                    "Check the heating element for damage (electric ovens).",
                    "For gas ovens, ensure the igniter is working."
                ],
                "uneven_cooking": [
                    "Check if the oven needs recalibration.",
                    "Use an oven thermometer to verify temperature accuracy.",
                    "Rotate dishes during cooking for more even results.",
                    "Ensure proper air circulation by not overcrowding."
                ],
                "door_not_closing": [
                    "Check for food debris blocking the door seal.",
                    "Inspect the door hinges and springs for damage.",
                    "Clean the door gasket and check for wear."
                ]
            }
        }
    
    def get_appliance_categories(self) -> List[str]:
        """
        Returns a list of supported appliance categories.
        """
        return list(self.knowledge_base.keys())
    
    def get_common_issues(self, appliance: str) -> List[str]:
        """
        Returns common issues for a given appliance category.
        
        Args:
            appliance: The appliance category (e.g., 'refrigerator')
            
        Returns:
            List of common issues or empty list if appliance not found
        """
        return list(self.knowledge_base.get(appliance, {}).keys())
    
    def get_troubleshooting_advice(self, appliance: str, issue: str) -> List[str]:
        """
        Provides troubleshooting steps for a specific appliance issue.
        
        Args:
            appliance: The appliance category (e.g., 'refrigerator')
            issue: The specific issue (e.g., 'not_cooling')
            
        Returns:
            List of troubleshooting steps or empty list if not found
        """
        return self.knowledge_base.get(appliance, {}).get(issue, [])
    
    def handle_user_query(self, appliance: str, issue: str) -> str:
        """
        Processes a user query and returns formatted troubleshooting advice.
        
        Args:
            appliance: The appliance category
            issue: The specific issue
            
        Returns:
            Formatted response with troubleshooting steps or error message
        """
        if appliance not in self.knowledge_base:
            return f"Sorry, I don't have information about {appliance}. Supported appliances are: {', '.join(self.get_appliance_categories())}"
        
        if issue not in self.knowledge_base[appliance]:
            return f"Sorry, I don't have information about '{issue}' for {appliance}. Common issues are: {', '.join(self.get_common_issues(appliance))}"
        
        solutions = self.get_troubleshooting_advice(appliance, issue)
        response = f"Here are some troubleshooting steps for {appliance} {issue}:\n"
        response += "\n".join(f"- {step}" for step in solutions)
        response += "\n\nIf the problem persists, contact Ankara Beyaz Eşya Teknik Servisi for professional assistance."
        
        return response


def main():
    """
    Main function to run the chatbot interactively.
    """
    chatbot = WhiteGoodsChatbot()
    print("Welcome to White Goods Troubleshooting Chatbot")
    print(f"Supported appliance categories: {', '.join(chatbot.get_appliance_categories())}")
    
    while True:
        print("\nEnter the appliance type (or 'quit' to exit):")
        appliance = input().strip().lower()
        
        if appliance == 'quit':
            print("Goodbye!")
            break
            
        if appliance not in chatbot.get_appliance_categories():
            print(f"Sorry, I don't have information about {appliance}. Please try one of these: {', '.join(chatbot.get_appliance_categories())}")
            continue
            
        print(f"Common issues for {appliance}: {', '.join(chatbot.get_common_issues(appliance))}")
        print("Enter the issue you're experiencing:")
        issue = input().strip().lower()
        
        response = chatbot.handle_user_query(appliance, issue)
        print("\n" + response)


if __name__ == "__main__":
    main()
```
