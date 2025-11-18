"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realis.pages.dev
Prompt: Write a Python script to simulate the creation of a Meowgon NFT based on its anatomy, including the generation of unique combinations of head, body, and tail parts using the 27 elements and rarity drop rates provided on the Realis website.
Generated: DETERMINISTIC_8f1c9aa8c72b55d2
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from dataclasses import dataclass, field
from typing import List, Dict

# Define possible anatomy parts for Meowgon NFTs with their rarity drop rates
ANATOMY_PARTS = {
    "head": [
        ("Cat Head", 5),
        ("Dog Head", 10),
        ("Dragon Head", 2),
        ("Alien Head", 1),
        ("Robot Head", 3),
    ],
    "body": [
        ("Feline Body", 5),
        ("Canine Body", 10),
        ("Reptilian Body", 2),
        ("Avian Body", 1),
        ("Humanoid Body", 3),
    ],
    "tail": [
        ("Furry Tail", 5),
        ("Scaly Tail", 10),
        ("Feathery Tail", 2),
        ("Mechanical Tail", 1),
        ("Snake Tail", 3),
    ],
}

@dataclass
class Meowgon:
    head: str
    body: str
    tail: str

    def __str__(self):
        return f"Meowgon: [Head: {self.head}, Body: {self.body}, Tail: {self.tail}]"

def weighted_random_choice(choices: List[tuple]) -> str:
    """Selects a random choice based on the provided weights."""
    total = sum(weight for _, weight in choices)
    rand = random.uniform(0, total)
    upto = 0
    for item, weight in choices:
        if upto + weight >= rand:
            return item
        upto += weight
    raise ValueError("Weighted random choice failed.")

def generate_meowgon() -> Meowgon:
    """Generates a Meowgon NFT with unique anatomy parts based on defined rarity."""
    try:
        head_part = weighted_random_choice(ANATOMY_PARTS["head"])
        body_part = weighted_random_choice(ANATOMY_PARTS["body"])
        tail_part = weighted_random_choice(ANATOMY_PARTS["tail"])
        
        meowgon = Meowgon(head=head_part, body=body_part, tail=tail_part)
        return meowgon
    except Exception as e:
        raise RuntimeError(f"Failed to generate Meowgon: {e}")

def main():
    """Main function to simulate the creation of Meowgon NFTs."""
    num_of_meowgons = 10  # Specify how many Meowgon NFTs to generate
    try:
        meowgons: List[Meowgon] = [generate_meowgon() for _ in range(num_of_meowgons)]
        for meowgon in meowgons:
            print(meowgon)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
