"""
Generated Code Metadata:
========================
Original URL: https://olas-network.pages.dev
Prompt: What are the key modules of the Olas protocol, and how do they enhance the functionality of crypto projects on different chains?
Generated: DETERMINISTIC_23587a93952f4ba3
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# olas_protocol.py

from typing import Dict

class OlasProtocol:
    """
    The Olas protocol is a modular framework designed to enhance the functionality of crypto projects on different chains.
    """

    def __init__(self):
        # Initialize the key modules of the Olas protocol
        self.modules: Dict[str, str] = {
            "prediction": "enables prediction markets",
            "voting": "enables on-chain voting",
            "oracle": "provides external data to smart contracts",
            "autopilot": "automates complex decision-making processes",
            "reserve": "manages reserve funds for crypto projects"
        }

    def get_modules(self) -> Dict[str, str]:
        """
        Returns a dictionary of key modules in the Olas protocol and their descriptions.

        Returns:
            Dict[str, str]: A dictionary of Olas protocol modules
        """
        return self.modules

    def enable_module(self, module_name: str, chain: str) -> str:
        """
        Enables a specific module for a crypto project on a given chain.

        Args:
            module_name (str): The name of the module to enable
            chain (str): The chain on which to enable the module

        Returns:
            str: A success message or an error message if the module does not exist

        Raises:
            ValueError: If the module does not exist
        """
        if module_name in self.modules:
            # Simulate enabling the module on the given chain
            return f"Enabled {module_name} module on {chain} chain"
        else:
            raise ValueError(f"Module {module_name} does not exist")

def main():
    olas = OlasProtocol()
    print("Key Modules of Olas Protocol:")
    for module, description in olas.get_modules().items():
        print(f"- {module}: {description}")

    # Example usage: Enable a module on a specific chain
    try:
        print(olas.enable_module("prediction", "Ethereum"))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
