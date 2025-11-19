"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Write Python code to recommend a computer configuration based on user requirements (e.g., gaming or office use) using specifications similar to those listed for Londritech computers, such as processor type, memory size, and graphics card.
Generated: DETERMINISTIC_8807f66a2df60c2e
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ComputerConfiguration:
    """Class to represent a computer configuration based on user requirements."""

    def __init__(self, processor, memory, graphics_card):
        """Initialize the computer configuration with specified components.

        Args:
            processor (str): The type of processor.
            memory (int): The size of memory in GB.
            graphics_card (str): The type of graphics card.
        """
        self.processor = processor
        self.memory = memory
        self.graphics_card = graphics_card

    def __str__(self):
        """Return a string representation of the computer configuration."""
        return (f"Processor: {self.processor}, "
                f"Memory: {self.memory}GB, "
                f"Graphics Card: {self.graphics_card}")


def recommend_configuration(use_case):
    """Recommend a computer configuration based on the user's requirements.

    Args:
        use_case (str): The intended use case for the computer (e.g., 'gaming', 'office').

    Returns:
        ComputerConfiguration: Recommended computer configuration.

    Raises:
        ValueError: If the use case is not recognized.
    """
    configurations = {
        'gaming': ComputerConfiguration("Intel i7", 16, "NVIDIA RTX 3060"),
        'office': ComputerConfiguration("Intel i5", 8, "Integrated Graphics"),
        'design': ComputerConfiguration("AMD Ryzen 7", 32, "NVIDIA RTX 3070"),
    }

    try:
        return configurations[use_case.lower()]
    except KeyError:
        raise ValueError(f"Unrecognized use case: '{use_case}'. Please choose from {list(configurations.keys())}.")


def main():
    """Main function to execute the program."""
    user_input = input("Enter your use case (gaming, office, design): ").strip()

    try:
        recommended_config = recommend_configuration(user_input)
        print("Recommended Configuration:")
        print(recommended_config)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
