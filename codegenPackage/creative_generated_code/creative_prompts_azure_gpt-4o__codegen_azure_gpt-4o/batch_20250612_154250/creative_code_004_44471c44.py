"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://statapk.com
Prompt: Write code to implement a search functionality that mimics APKMabbu's search feature, allowing users to find APKs by name, category, or version.
Generated: DETERMINISTIC_44471c44a61f6101
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class APKSearchEngine:
    def __init__(self):
        """
        Initializes the APKSearchEngine with an empty list of APK data.
        """
        self.apks = []

    def load_apk_data(self, file_path):
        """
        Loads APK data from a JSON file into the search engine.
        
        Args:
            file_path (str): Path to the JSON file containing APK data.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not a valid JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                self.apks = json.load(file)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            raise
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode JSON file - {e}")
            raise

    def search_by_name(self, name):
        """
        Searches for APKs by name.
        
        Args:
            name (str): The name of the APK to search for.
            
        Returns:
            list: A list of APKs that match the name.
        """
        return [apk for apk in self.apks if name.lower() in apk['name'].lower()]

    def search_by_category(self, category):
        """
        Searches for APKs by category.
        
        Args:
            category (str): The category of APKs to search for.
            
        Returns:
            list: A list of APKs that match the category.
        """
        return [apk for apk in self.apks if category.lower() in apk['category'].lower()]

    def search_by_version(self, version):
        """
        Searches for APKs by version.
        
        Args:
            version (str): The version of APKs to search for.
            
        Returns:
            list: A list of APKs that match the version.
        """
        return [apk for apk in self.apks if version.lower() == apk['version'].lower()]

    def search(self, name=None, category=None, version=None):
        """
        Performs a search based on one or more criteria: name, category, and/or version.
        
        Args:
            name (str, optional): The name of the APK to search for.
            category (str, optional): The category of APKs to search for.
            version (str, optional): The version of APKs to search for.
            
        Returns:
            list: A list of APKs that match the given criteria.
        """
        results = self.apks
        if name:
            results = [apk for apk in results if name.lower() in apk['name'].lower()]
        if category:
            results = [apk for apk in results if category.lower() in apk['category'].lower()]
        if version:
            results = [apk for apk in results if version.lower() == apk['version'].lower()]
        return results


if __name__ == "__main__":
    # Example usage of APKSearchEngine
    apk_search_engine = APKSearchEngine()
    
    try:
        # Load APK data from a JSON file
        apk_search_engine.load_apk_data("apks.json")
        
        # Perform searches
        print("Search by Name:")
        print(apk_search_engine.search_by_name("WhatsApp"))
        
        print("\nSearch by Category:")
        print(apk_search_engine.search_by_category("Social"))
        
        print("\nSearch by Version:")
        print(apk_search_engine.search_by_version("2.3.4"))

        print("\nSearch by Multiple Criteria:")
        print(apk_search_engine.search(name="WhatsApp", category="Social"))
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code implements a search functionality for APKs using Python, allowing searches by name, category, and version. It assumes there is a JSON file (`apks.json`) with a list of APKs, each represented as dictionaries with `name`, `category`, and `version` keys.
