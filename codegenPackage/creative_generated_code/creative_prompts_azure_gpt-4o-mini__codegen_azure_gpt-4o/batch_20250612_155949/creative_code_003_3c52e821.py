"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamamaski.azurewebsites.net
Prompt: What are the supported programming languages for web apps on Microsoft Azure App Service?
Generated: DETERMINISTIC_3c52e82110dd5188
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script lists the supported programming languages for web applications hosted on Microsoft Azure App Service.
It uses the Azure SDK to retrieve the runtime stack information.
"""

# Required imports
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient

def list_supported_languages():
    """
    Fetches and prints the supported programming languages for Azure App Service Web Apps.
    """
    try:
        # Authenticate using DefaultAzureCredential (Make sure to set up Azure credentials beforehand)
        credential = DefaultAzureCredential()
        
        # Replace with your Azure subscription ID
        subscription_id = "your_subscription_id"

        # Initialize the WebSiteManagementClient
        client = WebSiteManagementClient(credential, subscription_id)
        
        # Fetch the available runtime stacks
        runtime_stacks = client.provider.get_available_stacks(stack_os_type="Linux", detailed=True)
        
        # Print the supported programming languages
        print("Supported Programming Languages for Azure App Service Web Apps:")
        for stack in runtime_stacks.value:
            print(f"Language: {stack.display_name}")
            print("Versions Supported:")
            for version in stack.major_versions:
                print(f"  - {version.display_version}")
            print("-" * 40)
    except Exception as e:
        # Handle exceptions and print error messages
        print(f"An error occurred while fetching the supported languages: {e}")

if __name__ == "__main__":
    # Entry point for the script
    list_supported_languages()
```

### Notes:
- Replace `"your_subscription_id"` with your Azure subscription ID.
- Ensure all necessary Azure credentials are set up (e.g., environment variables for `DefaultAzureCredential`).
- Install required libraries using `pip install azure-identity azure-mgmt-web` before running the script.
