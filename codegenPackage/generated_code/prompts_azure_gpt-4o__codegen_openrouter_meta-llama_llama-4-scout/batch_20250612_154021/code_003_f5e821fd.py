"""
Generated Code Metadata:
========================
Original URL: https://projectvox.pages.dev
Prompt: Implement a feature to display and filter guilds by categories such as "featured" and "newest," inspired by the Guildhall website's guild exploration tools.
Generated: DETERMINISTIC_f5e821fdda9ae7e5
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# guild_filter.py

from enum import Enum
from typing import List, Dict

class GuildCategory(str, Enum):
    """Guild category types."""
    FEATURED = "featured"
    NEWEST = "newest"

class Guild:
    """Represents a guild with its properties."""
    def __init__(self, id: int, name: str, category: GuildCategory):
        self.id = id
        self.name = name
        self.category = category

class GuildFilter:
    """Filters guilds by categories."""
    def __init__(self, guilds: List[Guild]):
        self.guilds = guilds

    def filter_by_category(self, category: GuildCategory) -> List[Guild]:
        """Filters guilds by a specific category."""
        return [guild for guild in self.guilds if guild.category == category]

    def get_categories(self) -> List[GuildCategory]:
        """Gets all unique categories of guilds."""
        return list(set(guild.category for guild in self.guilds))

def main():
    try:
        # Example guilds
        guilds = [
            Guild(1, "Guild 1", GuildCategory.FEATURED),
            Guild(2, "Guild 2", GuildCategory.NEWEST),
            Guild(3, "Guild 3", GuildCategory.FEATURED),
            Guild(4, "Guild 4", GuildCategory.NEWEST),
        ]

        filter = GuildFilter(guilds)

        print("Available categories:")
        for category in filter.get_categories():
            print(category)

        category = input("Enter a category to filter by (featured/newest): ")
        try:
            category = GuildCategory(category)
        except ValueError:
            print("Invalid category. Exiting.")
            return

        filtered_guilds = filter.filter_by_category(category)

        print(f"\nGuilds in category '{category.value}':")
        for guild in filtered_guilds:
            print(f"ID: {guild.id}, Name: {guild.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
