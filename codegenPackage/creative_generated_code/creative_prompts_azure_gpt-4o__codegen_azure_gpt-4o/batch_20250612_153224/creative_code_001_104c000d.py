"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masitsolutions.net
Prompt: Recommend cloud technology solutions for small businesses, specifically using Microsoft and Google Cloud services, as highlighted by MASIT Solutions.
Generated: DETERMINISTIC_104c000d976a959b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Cloud Technology Solutions Recommendation Tool

This script recommends cloud technology solutions for small businesses using 
Microsoft and Google Cloud services. It is designed to provide tailored 
recommendations based on specific needs provided by the user.

Dependencies:
    - Python 3.7+
"""

# Import necessary modules
import sys

def microsoft_cloud_recommendation():
    """
    Provides recommendations for Microsoft Cloud services based on common small business needs.
    """
    services = {
        "Collaboration and Productivity": "Microsoft 365 (includes Teams, SharePoint, OneDrive, Outlook, Word, Excel, etc.)",
        "Cloud Hosting and Computing": "Azure Virtual Machines, Azure App Service",
        "Data Storage and Backup": "Azure Blob Storage, Azure Backup",
        "Security and Compliance": "Azure Security Center, Microsoft Defender for Endpoint",
        "Business Intelligence": "Power BI"
    }
    return services


def google_cloud_recommendation():
    """
    Provides recommendations for Google Cloud services based on common small business needs.
    """
    services = {
        "Collaboration and Productivity": "Google Workspace (includes Gmail, Google Drive, Docs, Sheets, Meet, etc.)",
        "Cloud Hosting and Computing": "Google Compute Engine, Google App Engine",
        "Data Storage and Backup": "Google Cloud Storage",
        "Security and Compliance": "Google Cloud Security Command Center",
        "Business Intelligence": "Google Looker"
    }
    return services


def recommend_cloud_services(provider):
    """
    Recommends cloud services based on the provider specified.

    Args:
        provider (str): The cloud provider ("Microsoft" or "Google").

    Returns:
        dict: A dictionary of recommended services.
    """
    if provider.lower() == "microsoft":
        return microsoft_cloud_recommendation()
    elif provider.lower() == "google":
        return google_cloud_recommendation()
    else:
        raise ValueError("Invalid provider specified. Choose 'Microsoft' or 'Google'.")


def main():
    """
    Main function to interact with the user and provide cloud service recommendations.
    """
    print("Welcome to the Cloud Technology Solutions Recommendation Tool!")
    print("Please choose a provider: Microsoft or Google")

    try:
        provider = input("Enter your choice: ").strip()

        # Get recommendations for the chosen provider
        recommendations = recommend_cloud_services(provider)

        # Display recommendations
        print(f"\nRecommended services for {provider} Cloud:")
        for category, service in recommendations.items():
            print(f"- {category}: {service}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Run the program if executed directly
if __name__ == "__main__":
    main()
```
