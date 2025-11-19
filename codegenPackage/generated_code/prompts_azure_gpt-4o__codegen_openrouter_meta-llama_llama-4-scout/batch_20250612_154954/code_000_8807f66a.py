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
from enum import Enum
from typing import Dict

class ComputerUse(Enum):
    """Enum for computer use cases"""
    GAMING = 1
    OFFICE = 2
    VIDEO_EDITING = 3

class ComputerConfig:
    """Class to hold computer configuration"""
    def __init__(self, processor: str, memory: int, graphics_card: str, storage: int):
        self.processor = processor
        self.memory = memory
        self.graphics_card = graphics_card
        self.storage = storage

    def __str__(self):
        return f"Processor: {self.processor}, Memory: {self.memory} GB, Graphics Card: {self.graphics_card}, Storage: {self.storage} GB"

class ComputerRecommender:
    """Class to recommend computer configuration"""
    def __init__(self):
        self.configs: Dict[ComputerUse, ComputerConfig] = {
            ComputerUse.GAMING: ComputerConfig("Intel Core i9", 16, "NVIDIA GeForce RTX 3080", 512),
            ComputerUse.OFFICE: ComputerConfig("Intel Core i5", 8, "Integrated Graphics", 256),
            ComputerUse.VIDEO_EDITING: ComputerConfig("Intel Core i7", 32, "NVIDIA GeForce RTX 3070", 1024),
        }

    def recommend(self, use_case: ComputerUse) -> ComputerConfig:
        """Recommend computer configuration based on use case"""
        return self.configs.get(use_case)

def main():
    try:
        recommender = ComputerRecommender()
        print("Computer Use Cases:")
        for i, use_case in enumerate(ComputerUse):
            print(f"{i+1}. {use_case.name}")

        choice = int(input("Enter the number of your use case: "))
        use_case = list(ComputerUse)[choice - 1]
        config = recommender.recommend(use_case)

        if config:
            print("\nRecommended Computer Configuration:")
            print(config)
        else:
            print("Invalid use case")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
