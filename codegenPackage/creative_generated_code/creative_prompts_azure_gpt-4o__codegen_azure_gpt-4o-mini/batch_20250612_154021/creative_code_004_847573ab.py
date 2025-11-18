"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectvox.pages.dev
Prompt: Write code to fetch and display the number of roles and whitelist approvals for a guild, similar to the statistics shown on the Guildhall webpage.
Generated: DETERMINISTIC_847573abec99438f
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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
import json

class GuildStatisticsFetcher:
    """
    A class to fetch and display statistics for a guild, including the number of roles
    and whitelist approvals.
    """

    def __init__(self, guild_id, api_base_url):
        """
        Initializes the GuildStatisticsFetcher with the guild ID and API base URL.

        :param guild_id: The ID of the guild to fetch statistics for.
        :param api_base_url: The base URL of the API to interact with.
        """
        self.guild_id = guild_id
        self.api_base_url = api_base_url

    def fetch_guild_data(self):
        """
        Fetches guild data from the API.

        :return: A dictionary with guild statistics.
        :raises Exception: If the API request fails or returns an unexpected response.
        """
        try:
            response = requests.get(f"{self.api_base_url}/guilds/{self.guild_id}/statistics")
            response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)

            data = response.json()
            if 'roles_count' not in data or 'whitelist_approvals' not in data:
                raise ValueError("Invalid data format received from API.")
            return data

        except requests.RequestException as e:
            raise Exception(f"Error fetching guild data: {e}")

    def display_statistics(self):
        """
        Fetches guild statistics and displays them in a readable format.
        """
        try:
            stats = self.fetch_guild_data()
            print(f"Guild ID: {self.guild_id}")
            print(f"Number of Roles: {stats['roles_count']}")
            print(f"Whitelist Approvals: {stats['whitelist_approvals']}")

        except Exception as e:
            print(f"Failed to display statistics: {e}")

if __name__ == "__main__":
    # Replace with your actual guild ID and API base URL
    GUILD_ID = "your_guild_id_here"
    API_BASE_URL = "https://api.example.com"

    guild_stats_fetcher = GuildStatisticsFetcher(GUILD_ID, API_BASE_URL)
    guild_stats_fetcher.display_statistics()
```
