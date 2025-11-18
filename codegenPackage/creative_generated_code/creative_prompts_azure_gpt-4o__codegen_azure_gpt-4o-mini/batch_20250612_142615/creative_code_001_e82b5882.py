"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbi-apps.teachable.com
Prompt: Generate a script that uses an API to filter and sort products on an online course platform, referencing features like "import_export" and "hide_source."
Generated: DETERMINISTIC_e82b5882f2fe2920
Batch ID: 20250612_142615
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.onlinecourseplatform.com": {
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

class CoursePlatformAPI:
    """
    A class to interact with an online course platform's API for fetching,
    filtering, and sorting products.
    """
    
    def __init__(self, base_url, api_key):
        """
        Initializes the CoursePlatformAPI with the base URL and API key.
        
        :param base_url: str - The base URL of the API.
        :param api_key: str - API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_products(self, filter_params=None, sort_by=None):
        """
        Fetches products from the API, with optional filtering and sorting.

        :param filter_params: dict - Dictionary containing filtering parameters.
        :param sort_by: str - Parameter to sort the products by.
        :return: list - List of products from the API.
        """
        url = f"{self.base_url}/products"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        # Prepare query parameters
        params = {}
        if filter_params:
            params.update(filter_params)
        if sort_by:
            params['sort'] = sort_by

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json().get('products', [])
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        return []

def filter_and_sort_courses(api_instance, import_export=None, hide_source=None, sort_by='name'):
    """
    Filters and sorts courses based on specified criteria.

    :param api_instance: CoursePlatformAPI - An instance of the CoursePlatformAPI class.
    :param import_export: bool - Filter for products with import/export feature.
    :param hide_source: bool - Filter for products that hide the source.
    :param sort_by: str - The field to sort the results by.
    :return: list - The filtered and sorted list of courses.
    """
    filter_params = {}
    if import_export is not None:
        filter_params['import_export'] = import_export
    if hide_source is not None:
        filter_params['hide_source'] = hide_source

    # Fetch products using the API and return the filtered and sorted list
    return api_instance.get_products(filter_params=filter_params, sort_by=sort_by)

if __name__ == "__main__":
    # Initialize API instance with your API credentials
    BASE_URL = "https://api.onlinecourseplatform.com"
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    api = CoursePlatformAPI(BASE_URL, API_KEY)
    
    # Example usage: Filter for products with import/export feature and hide source, sorted by name
    courses = filter_and_sort_courses(api, import_export=True, hide_source=False, sort_by='name')
    
    # Print the filtered and sorted courses
    for course in courses:
        print(course)
```
