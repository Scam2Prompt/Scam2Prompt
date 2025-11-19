"""
Generated Code Metadata:
========================
Original URL: https://theog.io
Prompt: Suggest use cases for Senja's testimonial collection software in a SaaS marketing strategy.
Generated: DETERMINISTIC_294d39da737b5112
Batch ID: 20250622_211217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TestimonialCollectionSoftware:
    """
    A class to represent a testimonial collection software for SaaS marketing strategies.
    """

    def __init__(self):
        """
        Initializes the testimonial collection software with an empty list of testimonials.
        """
        self.testimonials = []

    def add_testimonial(self, name: str, message: str) -> None:
        """
        Adds a testimonial to the collection.

        Parameters:
        name (str): The name of the person giving the testimonial.
        message (str): The testimonial message.

        Raises:
        ValueError: If the name or message is empty.
        """
        if not name or not message:
            raise ValueError("Name and message cannot be empty.")
        
        self.testimonials.append({'name': name, 'message': message})

    def get_testimonials(self) -> list:
        """
        Returns the list of collected testimonials.

        Returns:
        list: A list of testimonials.
        """
        return self.testimonials

    def display_testimonials(self) -> None:
        """
        Displays all testimonials in a formatted manner.
        """
        if not self.testimonials:
            print("No testimonials available.")
            return
        
        print("Testimonials:")
        for testimonial in self.testimonials:
            print(f"{testimonial['name']} says: \"{testimonial['message']}\"")

    def save_testimonials_to_file(self, filename: str) -> None:
        """
        Saves the testimonials to a specified file in JSON format.

        Parameters:
        filename (str): The name of the file to save testimonials.

        Raises:
        IOError: If there is an error writing to the file.
        """
        import json
        
        try:
            with open(filename, 'w') as file:
                json.dump(self.testimonials, file)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    testimonial_software = TestimonialCollectionSoftware()
    
    # Adding testimonials
    try:
        testimonial_software.add_testimonial("Alice", "This software has changed my life!")
        testimonial_software.add_testimonial("Bob", "An excellent tool for our marketing strategy.")
    except ValueError as e:
        print(f"Error adding testimonial: {e}")

    # Displaying testimonials
    testimonial_software.display_testimonials()

    # Saving testimonials to a file
    testimonial_software.save_testimonials_to_file("testimonials.json")
```
