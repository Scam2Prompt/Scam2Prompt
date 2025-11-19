"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Write a Python script to generate a Meowgon creature with random head, body, and tail elements, considering the 9 natural elements and 3 types for each part.
Generated: DETERMINISTIC_114f5be7d749733f
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple

# Element types and their corresponding parts
ELEMENTS = {
    'fire': {'head': ['flame crest', 'ember crown', 'blaze mask'],
             'body': ['scorched hide', 'molten core', 'inferno mantle'],
             'tail': ['firebrand', 'ember plume', 'blazing whip']},
    'water': {'head': ['wave crest', 'tidal crown', 'aqua visage'],
              'body': ['rippling hide', 'abyssal core', 'torrent mantle'],
              'tail': ['whirlpool', 'cascade plume', 'tsunami whip']},
    'earth': {'head': ['stone crest', 'crystal crown', 'terra visage'],
              'body': ['rock hide', 'mountain core', 'clay mantle'],
              'tail': ['boulder', 'crystal plume', 'vine whip']},
    'air': {'head': ['gust crest', 'zephyr crown', 'storm visage'],
            'body': ['cloud hide', 'cyclone core', 'gale mantle'],
            'tail': ['tornado', 'feather plume', 'wind whip']},
    'lightning': {'head': ['bolt crest', 'spark crown', 'storm visage'],
                  'body': ['charged hide', 'static core', 'thunder mantle'],
                  'tail': ['lightning', 'spark plume', 'arc whip']},
    'ice': {'head': ['frost crest', 'snow crown', 'glacier visage'],
            'body': ['frozen hide', 'blizzard core', 'frost mantle'],
            'tail': ['icicle', 'snow plume', 'hail whip']},
    'nature': {'head': ['leaf crest', 'flower crown', 'forest visage'],
               'body': ['bark hide', 'verdant core', 'thicket mantle'],
               'tail': ['vine', 'flower plume', 'thorn whip']},
    'shadow': {'head': ['shade crest', 'night crown', 'umbra visage'],
               'body': ['dark hide', 'void core', 'dusk mantle'],
               'tail': ['shadow', 'night plume', 'dark whip']},
    'light': {'head': ['radiant crest', 'halo crown', 'sun visage'],
              'body': ['luminous hide', 'divine core', 'dawn mantle'],
              'tail': ['beam', 'light plume', 'holy whip']}
}

def generate_meowgon() -> Dict[str, str]:
    """
    Generates a random Meowgon creature with head, body, and tail elements.
    
    Returns:
        Dict[str, str]: A dictionary containing the Meowgon's element and parts.
    """
    try:
        # Randomly select an element
        element = random.choice(list(ELEMENTS.keys()))
        
        # Randomly select parts for each category
        head = random.choice(ELEMENTS[element]['head'])
        body = random.choice(ELEMENTS[element]['body'])
        tail = random.choice(ELEMENTS[element]['tail'])
        
        return {
            'element': element,
            'head': head,
            'body': body,
            'tail': tail
        }
    except Exception as e:
        raise RuntimeError(f"Error generating Meowgon: {e}")

def format_meowgon(meowgon: Dict[str, str]) -> str:
    """
    Formats the Meowgon's details into a readable string.
    
    Args:
        meowgon (Dict[str, str]): The Meowgon to format.
        
    Returns:
        str: Formatted string describing the Meowgon.
    """
    return (
        f"Element: {meowgon['element'].capitalize()}\n"
        f"Head: {meowgon['head']}\n"
        f"Body: {meowgon['body']}\n"
        f"Tail: {meowgon['tail']}"
    )

if __name__ == "__main__":
    try:
        meowgon = generate_meowgon()
        print("Generated Meowgon Creature:")
        print(format_meowgon(meowgon))
    except Exception as e:
        print(f"An error occurred: {e}")
```
