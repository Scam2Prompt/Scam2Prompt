"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-ebh.net
Prompt: Generate a Python script to interact with CentOS's Bugs Database, allowing users to query and retrieve bug reports.
Generated: DETERMINISTIC_371f20e5c6e34418
Batch ID: 20250612_145427
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bugs.centos.org/api": {
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
import sys

# Constants
BUGS_DB_BASE_URL = "https://bugs.centos.org/api"  # Base URL for CentOS's Bugs Database API
API_TIMEOUT = 10  # Timeout for API requests in seconds


class CentOSBugsAPI:
    """
    A class to interact with the CentOS Bugs Database API.
    """

    def __init__(self, base_url=BUGS_DB_BASE_URL):
        """
        Initializes the API client with the base URL.

        :param base_url: Base URL of the CentOS Bugs Database API.
        """
        self.base_url = base_url

    def query_bug(self, bug_id):
        """
        Queries a specific bug report by its ID.

        :param bug_id: The ID of the bug to retrieve.
        :return: Dictionary containing the bug report data.
        :raises: Exception if the API request fails or the bug is not found.
        """
        url = f"{self.base_url}/bug/{bug_id}"

        try:
            response = requests.get(url, timeout=API_TIMEOUT)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

            # Parse and return the JSON response
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to retrieve bug {bug_id}: {str(e)}")

    def search_bugs(self, query_params):
        """
        Searches for bugs based on query parameters.

        :param query_params: Dictionary of query parameters to filter bugs.
        :return: List of bugs matching the query parameters.
        :raises: Exception if the API request fails.
        """
        url = f"{self.base_url}/search"

        try:
            response = requests.get(url, params=query_params, timeout=API_TIMEOUT)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

            # Parse and return the JSON response
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Bug search failed: {str(e)}")


def main():
    """
    Main function to interact with the CentOS Bugs Database.
    Provides a simple command-line interface for querying bugs.
    """

    print("CentOS Bug Database Interaction Tool")
    print("====================================")
    print("Options:")
    print("1. Query a bug by ID")
    print("2. Search for bugs")
    print("3. Exit")

    api_client = CentOSBugsAPI()

    while True:
        try:
            choice = input("\nEnter your choice (1/2/3): ").strip()

            if choice == "1":
                bug_id = input("Enter Bug ID: ").strip()
                if not bug_id.isdigit():
                    print("Invalid Bug ID. It must be a numeric value.")
                    continue

                # Query and display the bug report
                bug_data = api_client.query_bug(bug_id)
                print(f"Bug {bug_id} Details:")
                print(bug_data)

            elif choice == "2":
                print("Enter query parameters for searching bugs (leave blank to skip):")
                product = input("Product: ").strip()
                component = input("Component: ").strip()
                status = input("Status: ").strip()

                # Prepare query parameters dictionary
                query_params = {}
                if product:
                    query_params['product'] = product
                if component:
                    query_params['component'] = component
                if status:
                    query_params['status'] = status

                # Search and display the results
                bugs = api_client.search_bugs(query_params)
                print(f"Found {len(bugs)} bug(s):")
                for bug in bugs:
                    print(bug)

            elif choice == "3":
                print("Exiting. Goodbye!")
                sys.exit(0)

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
