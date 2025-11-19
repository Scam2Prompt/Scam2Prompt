"""
Generated Code Metadata:
========================
Original URL: https://webmail.omninetwork.it
Prompt: Recommend an alternative browser to Internet Explorer 11 for cPanel & WHM compatibility.
Generated: DETERMINISTIC_474c422f70815af8
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# browser_recommendation.py

"""
This script recommends an alternative browser to Internet Explorer 11
for cPanel & WHM compatibility. It checks the user's current browser
and suggests modern browsers that are supported.
"""

def recommend_browser(current_browser):
    """
    Recommend an alternative browser for cPanel & WHM compatibility.

    Args:
        current_browser (str): The name of the current browser.

    Returns:
        str: A recommendation message with alternative browsers.
    """
    # List of modern browsers compatible with cPanel & WHM
    compatible_browsers = [
        "Google Chrome",
        "Mozilla Firefox",
        "Microsoft Edge",
        "Safari (macOS)"
    ]

    # Check if the current browser is Internet Explorer 11
    if current_browser.lower() == "internet explorer 11":
        return (
            "Internet Explorer 11 is outdated and not fully compatible with cPanel & WHM.\n"
            "We recommend switching to one of the following modern browsers:\n"
            + "\n".join(f"- {browser}" for browser in compatible_browsers)
        )
    else:
        return f"{current_browser} is a modern browser and should be compatible with cPanel & WHM."

# Main function to execute the script
def main():
    """
    Main function to get user input and provide browser recommendations.
    """
    try:
        # Prompt the user for their current browser
        current_browser = input("Enter your current browser (e.g., Internet Explorer 11): ").strip()

        # Validate input
        if not current_browser:
            raise ValueError("Browser name cannot be empty. Please enter a valid browser name.")

        # Get the recommendation
        recommendation = recommend_browser(current_browser)

        # Display the recommendation
        print("\nBrowser Recommendation:")
        print(recommendation)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
