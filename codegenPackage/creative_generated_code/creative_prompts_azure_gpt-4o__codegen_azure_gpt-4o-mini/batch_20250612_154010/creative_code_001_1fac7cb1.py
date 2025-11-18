"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaxfaupth.pages.dev
Prompt: Generate code for exploring and interacting with verified guilds, referencing the roles and categories such as "Migration," "Recovery," and "Airdrop" mentioned on the page.
Generated: DETERMINISTIC_1fac7cb1fec109ab
Batch ID: 20250612_154010
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/guilds": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class GuildExplorer:
    """A class to explore and interact with verified guilds."""

    def __init__(self, api_url):
        """
        Initializes the GuildExplorer with the API URL.

        Args:
            api_url (str): The base URL of the guild API.
        """
        self.api_url = api_url

    def fetch_verified_guilds(self):
        """
        Fetches the list of verified guilds from the API.

        Returns:
            list: A list of verified guilds.
        """
        try:
            response = requests.get(f"{self.api_url}/verified_guilds")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response as a list
        except requests.exceptions.RequestException as e:
            print(f"Error fetching verified guilds: {e}")
            return []

    def filter_guilds_by_category(self, guilds, category):
        """
        Filters guilds by a specified category.

        Args:
            guilds (list): The list of guilds to filter.
            category (str): The category to filter guilds by.

        Returns:
            list: Filtered list of guilds in the specified category.
        """
        return [guild for guild in guilds if category in guild.get('categories', [])]

    def display_guilds(self, guilds):
        """
        Displays the information of the guilds.

        Args:
            guilds (list): The list of guilds to display.
        """
        if not guilds:
            print("No guilds to display.")
            return

        for guild in guilds:
            print(f"Guild Name: {guild['name']}")
            print(f"Description: {guild.get('description', 'No description available')}")
            print(f"Categories: {', '.join(guild.get('categories', []))}")
            print('-' * 40)

    def run(self, category):
        """
        Executes the guild exploration process.

        Args:
            category (str): The category to filter guilds by.
        """
        print(f"Fetching verified guilds in the '{category}' category...\n")
        guilds = self.fetch_verified_guilds()
        filtered_guilds = self.filter_guilds_by_category(guilds, category)
        self.display_guilds(filtered_guilds)

# Example usage
if __name__ == "__main__":
    # Define the base API URL for guilds
    GUILD_API_URL = "https://api.example.com/guilds"
    
    # Create an instance of GuildExplorer
    explorer = GuildExplorer(GUILD_API_URL)
    
    # Run the explorer for the specified category
    explorer.run("Migration")  # Replace "Migration" with "Recovery" or "Airdrop" as needed
```
