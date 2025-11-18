"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Develop a code snippet for categorizing users as "Ancien client" or "Nouveau client" based on their input, similar to the classification system mentioned on the Proximus client page.
Generated: DETERMINISTIC_a943903752b84d18
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ClientCategorizer:
    """
    A class to categorize clients based on their input.
    Clients are classified as 'Ancien client' (existing clients)
    or 'Nouveau client' (new clients).
    """

    def __init__(self):
        """Initialize the categorizer."""
        self.categories = {
            "ancien": "Ancien client",
            "nouveau": "Nouveau client"
        }

    def categorize_client(self, client_input):
        """
        Categorize a client based on their input.

        Args:
            client_input (str): The input provided by the client.

        Returns:
            str: The category of the client.

        Raises:
            ValueError: If the input is not recognized.
        """
        # Normalize input to lowercase for consistent comparison
        normalized_input = client_input.lower()

        # Check if the input matches known categories
        if normalized_input in self.categories:
            return self.categories[normalized_input]
        else:
            raise ValueError(f"Input '{client_input}' is not valid. Expected 'ancien' or 'nouveau'.")

def main():
    """
    Main function to execute the client categorization.
    It handles user input and displays the corresponding category.
    """
    categorizer = ClientCategorizer()

    # Get user input
    client_input = input("Please enter your status (ancien/nouveau): ")

    try:
        # Categorize the client and print the result
        category = categorizer.categorize_client(client_input)
        print(f"You are categorized as: {category}")
    except ValueError as ve:
        # Handle invalid input error
        print(ve)

if __name__ == "__main__":
    main()
```
