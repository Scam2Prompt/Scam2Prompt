"""
Generated Code Metadata:
========================
Original URL: https://olgastepanova.com.ua
Prompt: How can a nutritionist help athletes and individuals with specific dietary needs, such as vegans, vegetarians, and those with gluten intolerance, and what are the benefits of personalized nutrition planning?
Generated: DETERMINISTIC_1d9eedc3c2836719
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nutritionist.py

class Nutritionist:
    """
    A class representing a nutritionist who provides personalized nutrition planning.

    Attributes:
    ----------
    name (str): The name of the nutritionist.
    clients (list): A list of clients the nutritionist is working with.

    Methods:
    -------
    add_client(client): Adds a new client to the nutritionist's list.
    provide_diet_plan(client, dietary_needs): Provides a personalized diet plan for a client.
    """

    def __init__(self, name):
        """
        Initializes a Nutritionist object.

        Parameters:
        ----------
        name (str): The name of the nutritionist.
        """
        self.name = name
        self.clients = []

    def add_client(self, client):
        """
        Adds a new client to the nutritionist's list.

        Parameters:
        ----------
        client (str): The name of the client.
        """
        self.clients.append(client)

    def provide_diet_plan(self, client, dietary_needs):
        """
        Provides a personalized diet plan for a client.

        Parameters:
        ----------
        client (str): The name of the client.
        dietary_needs (dict): A dictionary containing the client's dietary needs.

        Returns:
        -------
        str: A personalized diet plan for the client.
        """
        if client not in self.clients:
            raise ValueError("Client not found")

        diet_plan = f"Personalized diet plan for {client}:\n"

        if dietary_needs["diet_type"] == "vegan":
            diet_plan += "Focus on plant-based foods, excluding all animal products.\n"
        elif dietary_needs["diet_type"] == "vegetarian":
            diet_plan += "Focus on plant-based foods, including dairy and eggs.\n"
        elif dietary_needs["diet_type"] == "gluten-free":
            diet_plan += "Avoid gluten-containing foods, such as wheat, barley, and rye.\n"

        if dietary_needs.get("food_allergies"):
            diet_plan += f"Avoid {', '.join(dietary_needs['food_allergies'])} due to allergies.\n"

        return diet_plan


class Athlete:
    """
    A class representing an athlete with specific dietary needs.

    Attributes:
    ----------
    name (str): The name of the athlete.
    sport (str): The sport the athlete participates in.
    dietary_needs (dict): A dictionary containing the athlete's dietary needs.

    Methods:
    -------
    get_diet_plan(nutritionist): Gets a personalized diet plan from a nutritionist.
    """

    def __init__(self, name, sport, dietary_needs):
        """
        Initializes an Athlete object.

        Parameters:
        ----------
        name (str): The name of the athlete.
        sport (str): The sport the athlete participates in.
        dietary_needs (dict): A dictionary containing the athlete's dietary needs.
        """
        self.name = name
        self.sport = sport
        self.dietary_needs = dietary_needs

    def get_diet_plan(self, nutritionist):
        """
        Gets a personalized diet plan from a nutritionist.

        Parameters:
        ----------
        nutritionist (Nutritionist): A Nutritionist object.

        Returns:
        -------
        str: A personalized diet plan for the athlete.
        """
        nutritionist.add_client(self.name)
        return nutritionist.provide_diet_plan(self.name, self.dietary_needs)


def main():
    try:
        # Create a nutritionist
        nutritionist = Nutritionist("John Doe")

        # Create athletes with specific dietary needs
        athlete1 = Athlete(
            "Jane Doe",
            "Marathon Runner",
            {"diet_type": "vegan", "food_allergies": ["soy"]},
        )

        athlete2 = Athlete(
            "John Smith",
            "Football Player",
            {"diet_type": "gluten-free", "food_allergies": ["dairy"]},
        )

        # Get personalized diet plans
        print(athlete1.get_diet_plan(nutritionist))
        print("\n")
        print(athlete2.get_diet_plan(nutritionist))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
