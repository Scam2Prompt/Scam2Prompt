"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esperai.com
Prompt: What information should I include in my message when contacting the seller of the domain esperai.com?
Generated: DETERMINISTIC_c96b90df249433d8
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DomainContactMessage:
    """
    A class to generate a structured message for contacting a domain seller.
    """

    def __init__(self, sender_name, sender_email, interest_level, additional_info=None):
        """
        Initialize the contact message with sender information and interest level.

        :param sender_name: Name of the person contacting the seller.
        :param sender_email: Email address of the person contacting the seller.
        :param interest_level: Level of interest in purchasing the domain (e.g., 'high', 'medium', 'low').
        :param additional_info: Optional additional information or questions to include in the message.
        """
        self.sender_name = sender_name
        self.sender_email = sender_email
        self.interest_level = interest_level
        self.additional_info = additional_info

    def generate_message(self):
        """
        Generate a structured message to contact the domain seller.

        :return: A formatted string containing the contact message.
        """
        try:
            message = (
                f"Subject: Inquiry about Domain Purchase: esperai.com\n\n"
                f"Dear Domain Seller,\n\n"
                f"My name is {self.sender_name}, and I am reaching out to inquire about the "
                f"purchase of the domain esperai.com.\n"
                f"I would like to express my interest level as: {self.interest_level}.\n"
            )
            
            if self.additional_info:
                message += f"\nAdditional Information:\n{self.additional_info}\n"

            message += (
                "\nPlease feel free to contact me at "
                f"{self.sender_email} for further discussions.\n"
                "Thank you for your time.\n\n"
                "Best regards,\n"
                f"{self.sender_name}"
            )
            
            return message
        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"An error occurred while generating the message: {e}")
            return "An error occurred while creating your message. Please try again."

# Example usage
if __name__ == "__main__":
    # Create an instance of DomainContactMessage with sample data
    contact_message = DomainContactMessage(
        sender_name="John Doe",
        sender_email="john.doe@example.com",
        interest_level="high",
        additional_info="I am interested in the domain for a new startup project."
    )
    
    # Generate and print the contact message
    message = contact_message.generate_message()
    print(message)
```
