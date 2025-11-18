"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe.com.se
Prompt: Recommend libraries or tools compatible with Plesk for managing mail services securely via its GUI.
Generated: DETERMINISTIC_87c3224ace0f937c
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script recommends libraries/tools compatible with Plesk for managing mail services securely.
It uses a dictionary to dynamically return tools based on user selection.
Designed for production use with error handling in place.
"""

# Function to recommend libraries/tools compatible with Plesk
def recommend_mail_tools(service_type):
    """
    Recommends libraries or tools for managing mail services securely via Plesk.

    :param service_type: The type of mail service (e.g., "security", "management").
    :type service_type: str
    :return: List of recommended libraries/tools.
    :rtype: list
    """
    # Available recommendations for mail services with Plesk
    recommendations = {
        "security": [
            "Let's Encrypt Extension (SSL Certificates)",
            "SpamAssassin for spam filtering",
            "DKIM/DMARC configurator for email security",
        ],
        "management": [
            "Postfix integration",
            "MailEnable for Windows hosting",
            "Horde or Roundcube Webmail for GUI-based management",
        ],
    }

    try:
        # Attempt to fetch the recommendations for the given service type
        tools = recommendations.get(service_type.lower())
        if tools:
            return tools
        else:
            raise ValueError(f"Invalid service type: {service_type}. "
                             f"Available types are: {', '.join(recommendations.keys())}.")
    except Exception as e:
        # Log the error and provide feedback
        print(f"Error: {e}")
        return []

# Main block to execute the function
if __name__ == "__main__":
    try:
        # Get user input for the type of mail service
        user_input = input("Enter the type of mail service (security/management): ").strip()
        
        # Fetch tools based on user input
        recommended_tools = recommend_mail_tools(user_input)
        
        if recommended_tools:
            print("\nRecommended tools/libraries compatible with Plesk:\n")
            for tool in recommended_tools:
                print(f"- {tool}")
        else:
            print("\nNo recommendations found. Please try again.")
    except KeyboardInterrupt:
        # Handle user interrupt gracefully
        print("\nProcess interrupted by user. Exiting...")
    except Exception as e:
        # Catch unexpected exceptions
        print(f"An unexpected error occurred: {e}")
```
