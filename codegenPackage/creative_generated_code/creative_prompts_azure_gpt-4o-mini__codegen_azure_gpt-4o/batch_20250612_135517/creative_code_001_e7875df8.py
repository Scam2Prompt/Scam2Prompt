"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullmoonbird-next.vercel.app
Prompt: How can I use the Mint Token feature in a Bird Builder project to manage unique bird creations?
Generated: DETERMINISTIC_e7875df8ebff11b7
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class Bird:
    """
    Represents a unique bird creation.
    Each bird has a unique token generated upon creation.
    """
    def __init__(self, name, species, color):
        """
        Initialize a new Bird instance.

        Args:
            name (str): The name of the bird.
            species (str): The species of the bird.
            color (str): The color of the bird.
        """
        self.name = name
        self.species = species
        self.color = color
        self.token = self._generate_token()

    def _generate_token(self):
        """
        Generate a unique token for the bird using UUID.

        Returns:
            str: A unique token for the bird.
        """
        return str(uuid.uuid4())

    def __repr__(self):
        """
        Official string representation of the Bird instance.

        Returns:
            str: String representation of the bird.
        """
        return (f"Bird(Name: {self.name}, Species: {self.species}, "
                f"Color: {self.color}, Token: {self.token})")


class BirdBuilder:
    """
    Responsible for managing unique bird creations.
    Allows minting and tracking of unique bird tokens.
    """
    def __init__(self):
        """
        Initialize the BirdBuilder with an empty registry of birds.
        """
        self.birds_registry = {}

    def mint_bird(self, name, species, color):
        """
        Create a new bird and mint a unique token for it.

        Args:
            name (str): Name of the bird.
            species (str): Species of the bird.
            color (str): Color of the bird.

        Returns:
            Bird: The newly minted bird instance.
        """
        try:
            # Create a new bird instance
            new_bird = Bird(name, species, color)

            # Ensure uniqueness in the registry
            if new_bird.token in self.birds_registry:
                raise ValueError("Duplicate token generated. Please try again.")

            # Register the bird with its unique token
            self.birds_registry[new_bird.token] = new_bird
            return new_bird
        except Exception as e:
            # Handle any unexpected errors during bird creation
            print(f"Error occurred while minting bird: {e}")
            return None

    def get_bird_by_token(self, token):
        """
        Retrieve a bird by its unique token.

        Args:
            token (str): The unique token of the bird.

        Returns:
            Bird: The bird associated with the token, or None if not found.
        """
        return self.birds_registry.get(token, None)

    def list_all_birds(self):
        """
        List all the minted birds.

        Returns:
            list: A list of all registered birds.
        """
        return list(self.birds_registry.values())


# Example usage
if __name__ == "__main__":
    # Create an instance of BirdBuilder
    builder = BirdBuilder()

    # Mint some birds
    bird1 = builder.mint_bird("Robin", "Thrush", "Red")
    bird2 = builder.mint_bird("Blue Jay", "Corvid", "Blue")

    # Print the minted birds
    print("Minted Birds:")
    print(bird1)
    print(bird2)

    # Retrieve a bird by its token
    if bird1:
        retrieved_bird = builder.get_bird_by_token(bird1.token)
        print("\nRetrieved Bird by Token:")
        print(retrieved_bird)

    # List all birds
    print("\nAll Birds in Registry:")
    for bird in builder.list_all_birds():
        print(bird)
```
