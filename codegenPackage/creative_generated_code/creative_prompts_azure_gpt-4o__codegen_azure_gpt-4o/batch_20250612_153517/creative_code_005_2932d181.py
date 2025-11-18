"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fsromain.com
Prompt: Create code to automate the process of generating press releases for social media campaigns, inspired by the press relations services on fsromain.com.
Generated: DETERMINISTIC_2932d181d08bd18e
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import os

def validate_input(campaign_name, target_audience, key_message, social_platforms):
    """
    Validates the input data for generating a press release.
    """
    if not campaign_name or not isinstance(campaign_name, str):
        raise ValueError("Campaign name must be a non-empty string.")
    if not target_audience or not isinstance(target_audience, str):
        raise ValueError("Target audience must be a non-empty string.")
    if not key_message or not isinstance(key_message, str):
        raise ValueError("Key message must be a non-empty string.")
    if not social_platforms or not isinstance(social_platforms, list) or not all(isinstance(p, str) for p in social_platforms):
        raise ValueError("Social platforms must be a list of non-empty strings.")

def generate_press_release(campaign_name, target_audience, key_message, social_platforms):
    """
    Generates a press release for a social media campaign.

    Args:
        campaign_name (str): Name of the campaign.
        target_audience (str): Description of the target audience.
        key_message (str): Key message of the campaign.
        social_platforms (list): List of social media platforms.

    Returns:
        str: A formatted press release.
    """
    # Validate inputs
    validate_input(campaign_name, target_audience, key_message, social_platforms)

    # Generate press release content
    release_date = datetime.date.today().strftime('%B %d, %Y')
    platforms = ", ".join(social_platforms)
    press_release = f"""\
Press Release
--------------
Date: {release_date}

Introducing Our Latest Social Media Campaign: "{campaign_name}"

We are thrilled to announce the launch of our newest social media campaign: "{campaign_name}". This campaign is designed to engage and inspire our target audience: {target_audience}.

Our key message for this campaign is:
"{key_message}"

Stay tuned as we roll out this campaign across the following platforms: {platforms}. We believe these channels will help us effectively reach our audience and make a lasting impact.

For more information, please contact us at press@yourcompany.com.

Thank you for your support,
The YourCompany Team
"""
    return press_release

def save_press_release_to_file(press_release, file_path):
    """
    Saves a press release to a file.

    Args:
        press_release (str): The press release content.
        file_path (str): The path to save the file.

    Raises:
        IOError: If there is an issue saving the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(press_release)
    except IOError as e:
        raise IOError(f"Failed to save press release to file: {e}")

def main():
    """
    Main function to run the press release automation.
    """
    # Example campaign details
    campaign_name = "Eco-Friendly Living"
    target_audience = "Environmentally conscious individuals"
    key_message = "Small changes lead to big impacts. Join us in creating a sustainable future!"
    social_platforms = ["Facebook", "Twitter", "Instagram"]

    # Generate press release
    try:
        press_release = generate_press_release(campaign_name, target_audience, key_message, social_platforms)
        print("Press release generated successfully!")
        print(press_release)

        # Save press release to file
        file_path = os.path.join(os.getcwd(), f"{campaign_name.replace(' ', '_').lower()}_press_release.txt")
        save_press_release_to_file(press_release, file_path)
        print(f"Press release saved to: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
