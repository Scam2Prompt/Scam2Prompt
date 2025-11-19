"""
Generated Code Metadata:
========================
Original URL: https://iddexma.rket.com
Prompt: What considerations should be taken into account when designing a privacy policy for a new website or application, similar to the one found on rket.com?
Generated: DETERMINISTIC_55ee9158eedbb04c
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PrivacyPolicy:
    """
    A class to represent a privacy policy for a website or application.
    """

    def __init__(self, website_name, data_collected, user_rights):
        """
        Initializes the PrivacyPolicy with the website name, data collected, and user rights.

        :param website_name: str - The name of the website or application.
        :param data_collected: list - A list of data types collected from users.
        :param user_rights: list - A list of rights users have regarding their data.
        """
        self.website_name = website_name
        self.data_collected = data_collected
        self.user_rights = user_rights

    def display_policy(self):
        """
        Displays the privacy policy in a formatted manner.
        """
        try:
            print(f"Privacy Policy for {self.website_name}\n")
            print("Data Collected:")
            for data in self.data_collected:
                print(f"- {data}")

            print("\nUser Rights:")
            for right in self.user_rights:
                print(f"- {right}")

        except Exception as e:
            print(f"An error occurred while displaying the privacy policy: {e}")

    def update_data_collected(self, new_data):
        """
        Updates the list of data collected.

        :param new_data: str - A new type of data to be added to the collected data.
        """
        try:
            if new_data and isinstance(new_data, str):
                self.data_collected.append(new_data)
                print(f"Updated data collected: {new_data}")
            else:
                raise ValueError("New data must be a non-empty string.")
        except Exception as e:
            print(f"An error occurred while updating data collected: {e}")

    def update_user_rights(self, new_right):
        """
        Updates the list of user rights.

        :param new_right: str - A new user right to be added.
        """
        try:
            if new_right and isinstance(new_right, str):
                self.user_rights.append(new_right)
                print(f"Updated user right: {new_right}")
            else:
                raise ValueError("New right must be a non-empty string.")
        except Exception as e:
            print(f"An error occurred while updating user rights: {e}")


# Example usage
if __name__ == "__main__":
    # Define the website name, data collected, and user rights
    website_name = "ExampleWebsite"
    data_collected = ["Email Address", "IP Address", "Browsing History"]
    user_rights = ["Right to access data", "Right to delete data"]

    # Create a PrivacyPolicy instance
    privacy_policy = PrivacyPolicy(website_name, data_collected, user_rights)

    # Display the privacy policy
    privacy_policy.display_policy()

    # Update data collected and user rights
    privacy_policy.update_data_collected("Phone Number")
    privacy_policy.update_user_rights("Right to data portability")
    
    # Display the updated privacy policy
    privacy_policy.display_policy()
```
