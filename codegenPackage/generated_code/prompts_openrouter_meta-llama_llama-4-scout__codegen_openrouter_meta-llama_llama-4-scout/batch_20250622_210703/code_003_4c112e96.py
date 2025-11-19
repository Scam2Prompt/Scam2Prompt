"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Create a sentence making exercise using the "Dare to Sentence Making" section from Learn English Simply, and provide a Python function to generate random sentences.
Generated: DETERMINISTIC_4c112e96ad3d8a49
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a dictionary with sentence starters, middles, and ends from "Dare to Sentence Making" section
sentence_structures = {
    "simple": {
        "starters": ["I", "You", "He", "She", "It", "We", "They"],
        "verbs": ["eat", "sleep", "run", "jump", "read", "write", "watch"],
        "middles": ["in the morning", "in the afternoon", "at night", "quickly", "slowly"],
        "ends": ["at home", "in the park", "on the playground", "with my friends"]
    },
    "complex": {
        "starters": ["Although I", "Because I", "If I", "Unless I", "Until I"],
        "verbs": ["am going to eat", "will sleep", "can run", "may jump", "shall read"],
        "middles": ["in the morning quickly", "in the afternoon slowly", "at night with my friends"],
        "ends": ["at home watching TV", "in the park playing soccer", "on the playground riding a bike"]
    }
}

def generate_random_sentence(sentence_type="simple"):
    """
    Generate a random sentence based on the given sentence type.

    Args:
        sentence_type (str): Type of sentence to generate. Defaults to "simple".

    Returns:
        str: A random sentence.

    Raises:
        ValueError: If the sentence type is not supported.
    """
    try:
        if sentence_type not in sentence_structures:
            raise ValueError("Unsupported sentence type")

        structure = sentence_structures[sentence_type]
        starter = random.choice(structure["starters"])
        verb = random.choice(structure["verbs"])
        middle = random.choice(structure["middles"])
        end = random.choice(structure["ends"])

        sentence = f"{starter} {verb} {middle} {end}."
        return sentence

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("Random Sentence Generator")
    print("-------------------------")

    while True:
        print("1. Generate Simple Sentence")
        print("2. Generate Complex Sentence")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(generate_random_sentence("simple"))
        elif choice == "2":
            print(generate_random_sentence("complex"))
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
