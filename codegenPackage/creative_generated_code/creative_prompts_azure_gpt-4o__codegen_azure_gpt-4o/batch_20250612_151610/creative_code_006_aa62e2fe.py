"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marufonlinebd.net
Prompt: Develop a customer support chatbot for MARUF ONLINE BD that integrates hotline numbers and email support for package inquiries.
Generated: DETERMINISTIC_aa62e2fe7245dfc9
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class CustomerSupportChatbot:
    """
    A Customer Support Chatbot for MARUF ONLINE BD.
    Provides hotline numbers and email support for package inquiries.
    """

    def __init__(self):
        # Hotline numbers and email configuration
        self.hotline_numbers = ["+880123456789", "+880987654321"]
        self.support_email = "support@marufonlinebd.com"

        # Predefined responses for package inquiries
        self.package_info = {
            "basic": "The Basic Package offers limited access for a low cost. Contact support for details.",
            "premium": "The Premium Package includes full access to all features. Contact support for details.",
            "pro": "The Pro Package is designed for professional use. Contact support for details."
        }

    def handle_user_input(self, user_input):
        """
        Process user input and return appropriate response.
        """
        try:
            # Normalize input
            user_input = user_input.strip().lower()

            # Check for package inquiries
            if "package" in user_input:
                return self._respond_to_package_inquiry(user_input)
            elif "hotline" in user_input:
                return self._provide_hotline_numbers()
            elif "email" in user_input:
                return self._provide_email_support()
            else:
                return "I'm sorry, I couldn't understand your request. Please specify 'package', 'hotline', or 'email'."
        except Exception as e:
            return f"An error occurred while processing your request. Please try again later. [Error: {str(e)}]"

    def _respond_to_package_inquiry(self, user_input):
        """
        Respond to package inquiries based on user input.
        """
        for package_name in self.package_info.keys():
            if re.search(fr"\b{package_name}\b", user_input):
                return self.package_info[package_name]
        return "We offer Basic, Premium, and Pro packages. Please specify which package you're inquiring about."

    def _provide_hotline_numbers(self):
        """
        Provide MARUF ONLINE BD hotline numbers.
        """
        return f"Our hotline numbers are: {', '.join(self.hotline_numbers)}"

    def _provide_email_support(self):
        """
        Provide MARUF ONLINE BD email support information.
        """
        return f"For email support, please contact us at: {self.support_email}"

# Initialize the chatbot
chatbot = CustomerSupportChatbot()

# Main loop for user interaction
if __name__ == "__main__":
    print("Welcome to MARUF ONLINE BD Customer Support Chatbot!")
    print("You can ask about 'package', 'hotline', or 'email'. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Thank you for using MARUF ONLINE BD Customer Support Chatbot. Goodbye!")
            break
        response = chatbot.handle_user_input(user_input)
        print(f"Chatbot: {response}")
```
