"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: "Compare and contrast managed IT services, including monitoring, maintenance, and support, offered by different providers."
Generated: DETERMINISTIC_301083b2fe5a8eef
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ITServiceProvider:
    """
    Represents an IT service provider with details about their services.
    """
    def __init__(self, name, monitoring, maintenance, support):
        """
        Initialize the IT service provider with its offerings.

        :param name: Name of the provider
        :param monitoring: Description of monitoring services
        :param maintenance: Description of maintenance services
        :param support: Description of support services
        """
        self.name = name
        self.monitoring = monitoring
        self.maintenance = maintenance
        self.support = support

    def to_dict(self):
        """
        Convert the provider's details to a dictionary format.

        :return: Dictionary representation of the provider
        """
        return {
            "name": self.name,
            "monitoring": self.monitoring,
            "maintenance": self.maintenance,
            "support": self.support
        }


def compare_providers(providers):
    """
    Compare and contrast the services offered by different IT providers.

    :param providers: List of ITServiceProvider objects
    :return: JSON string summarizing the comparison
    """
    try:
        # Convert provider details to a list of dictionaries
        provider_data = [provider.to_dict() for provider in providers]

        # Generate a JSON string for easy comparison
        return json.dumps(provider_data, indent=4)
    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while comparing providers: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Create instances of ITServiceProvider
    provider1 = ITServiceProvider(
        name="Provider A",
        monitoring="24/7 network monitoring with real-time alerts.",
        maintenance="Regular software updates and hardware checks.",
        support="Dedicated support team available via phone and email."
    )

    provider2 = ITServiceProvider(
        name="Provider B",
        monitoring="Proactive monitoring with AI-driven insights.",
        maintenance="Monthly system audits and patch management.",
        support="24/7 live chat and on-site support for critical issues."
    )

    provider3 = ITServiceProvider(
        name="Provider C",
        monitoring="Basic monitoring with daily reports.",
        maintenance="On-demand maintenance services.",
        support="Email-based support with a 24-hour response time."
    )

    # Compare the providers
    comparison_result = compare_providers([provider1, provider2, provider3])

    # Print the comparison result
    print("Comparison of IT Service Providers:")
    print(comparison_result)
```
