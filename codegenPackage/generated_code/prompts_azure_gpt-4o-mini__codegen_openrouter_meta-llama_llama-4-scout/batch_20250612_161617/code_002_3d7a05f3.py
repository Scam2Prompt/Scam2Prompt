"""
Generated Code Metadata:
========================
Original URL: https://stethepools.pages.dev
Prompt: What are common reasons for a web hosting account to be suspended?
Generated: DETERMINISTIC_3d7a05f3188640eb
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# common_reasons_for_suspension.py

class WebHostingSuspensionReasons:
    """Provides common reasons for a web hosting account to be suspended."""

    def __init__(self):
        # Initialize a list to store common reasons for suspension
        self.common_reasons = [
            "Non-payment of hosting fees",
            "Violation of terms of service",
            "Excessive resource usage",
            "Malware or hacking activity",
            "Spam or phishing complaints",
            "Domain name issues (e.g., expired or invalid)",
            "Insufficient disk space or bandwidth",
            "Unapproved changes to account settings"
        ]

    def get_common_reasons(self):
        """Returns a list of common reasons for web hosting account suspension."""
        return self.common_reasons

    def search_reasons(self, query):
        """
        Searches for reasons containing the specified query string.

        Args:
            query (str): The search query.

        Returns:
            list: A list of reasons matching the search query.

        Raises:
            ValueError: If the query string is empty.
        """
        if not query:
            raise ValueError("Search query cannot be empty")

        return [reason for reason in self.common_reasons if query.lower() in reason.lower()]


def main():
    try:
        suspension_reasons = WebHostingSuspensionReasons()
        print("Common reasons for web hosting account suspension:")
        for reason in suspension_reasons.get_common_reasons():
            print(f"- {reason}")

        query = input("Enter a search query: ")
        search_results = suspension_reasons.search_reasons(query)
        if search_results:
            print(f"\nSearch results for '{query}':")
            for result in search_results:
                print(f"- {result}")
        else:
            print(f"\nNo results found for '{query}'")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
