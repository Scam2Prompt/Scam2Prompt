"""
Generated Code Metadata:
========================
Original URL: https://dappchainweb.rf.gd
Prompt: Generate a simple web hosting plan comparison between iFastNet Web Hosting and another popular hosting service, highlighting features like cPanel, SSL support, and email accounts.
Generated: DETERMINISTIC_e7ae5b41fc505f25
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from prettytable import PrettyTable

def compare_web_hosting_plans():
    """
    Function to compare web hosting plans between iFastNet and Bluehost.
    Displays a table with features like cPanel, SSL support, and email accounts.
    """
    try:
        # Define hosting plan features for iFastNet
        ifastnet_features = {
            "Provider": "iFastNet",
            "cPanel": "Yes",
            "SSL Support": "Free SSL Certificates",
            "Email Accounts": "Unlimited"
        }

        # Define hosting plan features for Bluehost
        bluehost_features = {
            "Provider": "Bluehost",
            "cPanel": "Yes",
            "SSL Support": "Free SSL Certificates",
            "Email Accounts": "5 (Basic Plan)"
        }

        # Create a table to display the comparison
        table = PrettyTable()
        table.field_names = ["Feature", "iFastNet", "Bluehost"]

        # Add rows to the table
        table.add_row(["cPanel", ifastnet_features["cPanel"], bluehost_features["cPanel"]])
        table.add_row(["SSL Support", ifastnet_features["SSL Support"], bluehost_features["SSL Support"]])
        table.add_row(["Email Accounts", ifastnet_features["Email Accounts"], bluehost_features["Email Accounts"]])

        # Print the table
        print("Web Hosting Plan Comparison:")
        print(table)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the comparison: {e}")

# Entry point for the script
if __name__ == "__main__":
    compare_web_hosting_plans()
```

### Requirements:
1. Install the `prettytable` library to run this script:
   ```
   pip install prettytable
   ```
2. Run the script in a Python environment to see the hosting plan comparison table.
