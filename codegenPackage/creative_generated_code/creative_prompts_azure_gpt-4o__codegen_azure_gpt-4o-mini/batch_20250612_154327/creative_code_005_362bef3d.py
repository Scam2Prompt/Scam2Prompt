"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tcs-campaigns.com
Prompt: Develop a solution using TCS AI Catapult Forward to onboard junior developers quickly with guided support and shared prompts.
Generated: DETERMINISTIC_362bef3dfa1e38a6
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for better traceability and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OnboardingModule:
    """
    This class provides functionalities for onboarding junior developers
    using guided support and shared prompts through TCS AI Catapult Forward.
    """

    def __init__(self):
        self.prompts = self.load_prompts()

    def load_prompts(self) -> Dict[str, str]:
        """
        Load prompts from a JSON file. This could also be loaded from a database or other sources.
        
        Returns:
            Dict[str, str]: A dictionary of prompts for onboarding.
        """
        try:
            with open('prompts.json', 'r') as file:
                prompts = json.load(file)
            logging.info("Prompts loaded successfully.")
            return prompts
        except FileNotFoundError:
            logging.error("The prompts file was not found.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from prompts file.")
            return {}

    def get_prompt(self, topic: str) -> str:
        """
        Retrieve a prompt based on the specified topic.

        Args:
            topic (str): The topic for which to retrieve the prompt.

        Returns:
            str: The corresponding prompt.
        """
        prompt = self.prompts.get(topic, "Prompt not found.")
        logging.info(f"Retrieved prompt for topic '{topic}'.")
        return prompt

    def guide_new_developer(self, developer_name: str, topics: List[str]) -> None:
        """
        Provide guided support to a new developer by sharing relevant prompts.

        Args:
            developer_name (str): The name of the developer.
            topics (List[str]): A list of topics related to the onboarding process.
        """
        logging.info(f"Starting onboarding for {developer_name}.")
        for topic in topics:
            prompt = self.get_prompt(topic)
            self.share_prompt(developer_name, prompt)

    def share_prompt(self, developer_name: str, prompt: str) -> None:
        """
        Simulate sharing a prompt with the developer.

        Args:
            developer_name (str): The name of the developer.
            prompt (str): The prompt to be shared.
        """
        logging.info(f"Sharing prompt with {developer_name}: {prompt}")

if __name__ == "__main__":
    # Example usage
    onboarding = OnboardingModule()
    developer = "Alice"
    topics_to_cover = ["Code Standards", "Version Control", "Testing Practices"]
    onboarding.guide_new_developer(developer, topics_to_cover)
```

### Sample `prompts.json` structure:
```json
{
    "Code Standards": "Always follow the PEP 8 style guide for Python.",
    "Version Control": "Use Git for version control and adhere to branching strategies.",
    "Testing Practices": "Write unit tests for your code using the unittest framework."
}
```
