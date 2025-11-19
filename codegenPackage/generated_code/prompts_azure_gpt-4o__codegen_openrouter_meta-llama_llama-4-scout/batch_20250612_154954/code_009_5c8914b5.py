"""
Generated Code Metadata:
========================
Original URL: https://phantom-extension.app
Prompt: Write a program to categorize online casinos by their mobile compatibility and user experience, referencing Rakoo and other platforms discussed on phantom-extension.app.
Generated: DETERMINISTIC_5c8914b5d58887b5
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# casino_categorizer.py

class Casino:
    """Represents an online casino with its mobile compatibility and user experience."""

    def __init__(self, name, mobile_compatible, user_experience):
        """
        Initializes a Casino object.

        Args:
            name (str): The name of the casino.
            mobile_compatible (bool): Whether the casino is mobile compatible.
            user_experience (str): The user experience of the casino (e.g., 'good', 'bad', 'average').
        """
        self.name = name
        self.mobile_compatible = mobile_compatible
        self.user_experience = user_experience

    def __str__(self):
        return f"{self.name} - Mobile Compatible: {self.mobile_compatible}, User Experience: {self.user_experience}"


class CasinoCategorizer:
    """Categorizes online casinos by their mobile compatibility and user experience."""

    def __init__(self):
        self.casinos = []

    def add_casino(self, casino):
        """
        Adds a casino to the categorizer.

        Args:
            casino (Casino): The casino to add.
        """
        self.casinos.append(casino)

    def categorize_by_mobile_compatibility(self):
        """
        Categorizes casinos by their mobile compatibility.

        Returns:
            dict: A dictionary with 'mobile_compatible' and 'not_mobile_compatible' as keys and lists of casinos as values.
        """
        categorized_casinos = {'mobile_compatible': [], 'not_mobile_compatible': []}
        for casino in self.casinos:
            if casino.mobile_compatible:
                categorized_casinos['mobile_compatible'].append(casino)
            else:
                categorized_casinos['not_mobile_compatible'].append(casino)
        return categorized_casinos

    def categorize_by_user_experience(self):
        """
        Categorizes casinos by their user experience.

        Returns:
            dict: A dictionary with user experience as keys and lists of casinos as values.
        """
        categorized_casinos = {}
        for casino in self.casinos:
            if casino.user_experience not in categorized_casinos:
                categorized_casinos[casino.user_experience] = []
            categorized_casinos[casino.user_experience].append(casino)
        return categorized_casinos


def main():
    try:
        categorizer = CasinoCategorizer()

        # Example casinos
        rakko = Casino('Rakoo', True, 'good')
        phantom_extension = Casino('Phantom Extension', False, 'average')
        example_casino = Casino('Example Casino', True, 'bad')

        # Add casinos to categorizer
        categorizer.add_casino(rakko)
        categorizer.add_casino(phantom_extension)
        categorizer.add_casino(example_casino)

        # Categorize by mobile compatibility
        mobile_compatibility_categories = categorizer.categorize_by_mobile_compatibility()
        print("Mobile Compatibility Categories:")
        print("Mobile Compatible:")
        for casino in mobile_compatibility_categories['mobile_compatible']:
            print(casino)
        print("Not Mobile Compatible:")
        for casino in mobile_compatibility_categories['not_mobile_compatible']:
            print(casino)

        # Categorize by user experience
        user_experience_categories = categorizer.categorize_by_user_experience()
        print("\nUser Experience Categories:")
        for experience, casinos in user_experience_categories.items():
            print(f"{experience.capitalize()}:")
            for casino in casinos:
                print(casino)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
