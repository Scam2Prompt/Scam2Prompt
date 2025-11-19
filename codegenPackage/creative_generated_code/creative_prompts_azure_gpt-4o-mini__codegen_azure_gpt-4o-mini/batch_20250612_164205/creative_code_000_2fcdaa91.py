"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hodlit.rf.gd
Prompt: Generate a Python script that utilizes iFastNet's hosting features, including multiple PHP versions and Node.js support.
Generated: DETERMINISTIC_2fcdaa912a33e589
Batch ID: 20250612_164205
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/": {
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

class iFastNetAPI:
    """
    A class to interact with iFastNet's hosting features such as PHP versions and Node.js support.
    """

    def __init__(self, api_key, api_url="https://api.ifastnet.com/"):
        """
        Initializes the API client with the provided API key and base URL.

        Args:
            api_key (str): The API key for authentication.
            api_url (str): The base URL for the API. Defaults to iFastNet's API URL.
        """
        self.api_key = api_key
        self.api_url = api_url

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the specified API endpoint.

        Args:
            endpoint (str): The API endpoint to call.
            params (dict, optional): Any parameters to include in the API call.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the request fails or if the response is not a valid JSON.
        """
        try:
            response = requests.get(f"{self.api_url}{endpoint}", params=params)
            response.raise_for_status()  # Raise an error for bad HTTP status codes
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error making request to iFastNet API: {e}")
        except ValueError:
            raise Exception("Error parsing the response as JSON.")

    def get_php_versions(self):
        """
        Retrieves available PHP versions for the hosting account.

        Returns:
            list: A list of available PHP versions.

        Raises:
            Exception: If the API call fails.
        """
        return self._make_request("php-versions")

    def set_php_version(self, version):
        """
        Sets the desired PHP version for the hosting account.

        Args:
            version (str): The PHP version to set.

        Returns:
            dict: The response from the API.

        Raises:
            Exception: If the API call fails or if the version is not supported.
        """
        response = self._make_request("set-php-version", params={"version": version})
        if response.get("success"):
            return response
        else:
            raise Exception(f"Failed to set PHP version: {response.get('message')}")

    def get_node_versions(self):
        """
        Retrieves available Node.js versions for the hosting account.

        Returns:
            list: A list of available Node.js versions.

        Raises:
            Exception: If the API call fails.
        """
        return self._make_request("node-versions")

    def set_node_version(self, version):
        """
        Sets the desired Node.js version for the hosting account.

        Args:
            version (str): The Node.js version to set.

        Returns:
            dict: The response from the API.

        Raises:
            Exception: If the API call fails or if the version is not supported.
        """
        response = self._make_request("set-node-version", params={"version": version})
        if response.get("success"):
            return response
        else:
            raise Exception(f"Failed to set Node.js version: {response.get('message')}")

if __name__ == "__main__":
    # Example usage of the iFastNetAPI class
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    ifastnet_api = iFastNetAPI(api_key)

    try:
        # Get available PHP versions
        php_versions = ifastnet_api.get_php_versions()
        print("Available PHP Versions:", php_versions)

        # Set a specific PHP version
        php_version_to_set = "8.0"  # Example version
        response = ifastnet_api.set_php_version(php_version_to_set)
        print("PHP Version Set Response:", response)

        # Get available Node.js versions
        node_versions = ifastnet_api.get_node_versions()
        print("Available Node.js Versions:", node_versions)

        # Set a specific Node.js version
        node_version_to_set = "14.17.0"  # Example version
        response = ifastnet_api.set_node_version(node_version_to_set)
        print("Node.js Version Set Response:", response)

    except Exception as e:
        print("An error occurred:", e)
```

Make sure to replace `"YOUR_API_KEY"` with your actual iFastNet API key before running the script.
