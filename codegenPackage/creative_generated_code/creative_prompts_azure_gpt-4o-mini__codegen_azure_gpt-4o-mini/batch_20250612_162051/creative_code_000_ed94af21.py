"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: How can I create an advertisement for a party service on Ifesty, including categories like decoration and catering?
Generated: DETERMINISTIC_ed94af21b8850c32
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Advertisement:
    """
    A class to represent an advertisement for a party service on Ifesty.
    
    Attributes
    ----------
    title : str
        The title of the advertisement.
    description : str
        A detailed description of the service offered.
    categories : list
        A list of categories that the advertisement falls under.
    contact_info : str
        Contact information for potential customers.
    """

    def __init__(self, title, description, categories, contact_info):
        """
        Initializes the Advertisement with the provided details.

        Parameters
        ----------
        title : str
            The title of the advertisement.
        description : str
            A detailed description of the service offered.
        categories : list
            A list of categories that the advertisement falls under.
        contact_info : str
            Contact information for potential customers.
        """
        self.title = title
        self.description = description
        self.categories = categories
        self.contact_info = contact_info

    def validate(self):
        """
        Validates the advertisement details.

        Returns
        -------
        bool
            True if all details are valid, raises ValueError otherwise.
        """
        if not self.title or not isinstance(self.title, str):
            raise ValueError("Invalid title: Must be a non-empty string.")
        if not self.description or not isinstance(self.description, str):
            raise ValueError("Invalid description: Must be a non-empty string.")
        if not isinstance(self.categories, list) or not self.categories:
            raise ValueError("Invalid categories: Must be a non-empty list.")
        if not self.contact_info or not isinstance(self.contact_info, str):
            raise ValueError("Invalid contact info: Must be a non-empty string.")
        return True

    def create_advertisement(self):
        """
        Creates the advertisement if all validations pass.

        Returns
        -------
        str
            A success message indicating that the advertisement has been created.
        """
        try:
            self.validate()
            # Here, you would typically integrate with the Ifesty API to post the advertisement.
            # For demonstration purposes, we'll just return a success message.
            return "Advertisement created successfully!"
        except ValueError as ve:
            return f"Error creating advertisement: {ve}"

# Example usage:
if __name__ == "__main__":
    try:
        ad = Advertisement(
            title="Delightful Party Services",
            description="We offer decoration and catering services for all types of parties.",
            categories=["Decoration", "Catering"],
            contact_info="info@delightfulparty.com"
        )
        result = ad.create_advertisement()
        print(result)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
