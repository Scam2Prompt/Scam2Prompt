"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Write code to create a chatbot for a digital marketing agency like MoOve Marketing that can handle inquiries about services such as video production, web design, and social media management.
Generated: DETERMINISTIC_b59dc43f0f579cba
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chatbot.py

class Service:
    def __init__(self, name, description):
        """
        Initialize a Service object.

        Args:
            name (str): The name of the service.
            description (str): A brief description of the service.
        """
        self.name = name
        self.description = description

class Chatbot:
    def __init__(self):
        """
        Initialize a Chatbot object.

        Attributes:
            services (dict): A dictionary of services offered by the agency.
        """
        self.services = {
            "video production": Service("Video Production", "We create high-quality videos for your brand."),
            "web design": Service("Web Design", "We design and develop responsive websites for your business."),
            "social media management": Service("Social Media Management", "We manage your social media presence and create engaging content.")
        }

    def handle_inquiry(self, inquiry):
        """
        Handle an inquiry about a service.

        Args:
            inquiry (str): The user's inquiry.

        Returns:
            str: A response to the user's inquiry.
        """
        inquiry = inquiry.lower()

        if inquiry in self.services:
            service = self.services[inquiry]
            return f"Our {service.name} service {service.description} Would you like to know more?"
        else:
            return "Sorry, we don't offer that service. Please try again!"

    def get_service_info(self, service_name):
        """
        Get more information about a service.

        Args:
            service_name (str): The name of the service.

        Returns:
            str: More information about the service.
        """
        service_name = service_name.lower()

        if service_name in self.services:
            service = self.services[service_name]
            return f"Our {service.name} service includes:\n- {service.description}\n- Customized solutions for your business.\n- Professional team with years of experience."
        else:
            return "Sorry, we don't offer that service. Please try again!"

def main():
    chatbot = Chatbot()

    print("Welcome to MoOve Marketing Chatbot!")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("User: ")
        user_input = user_input.strip()

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = chatbot.handle_inquiry(user_input)

        if "more" in user_input.lower():
            service_name = user_input.lower().replace("more about ", "").replace("what's more about ", "")
            response = chatbot.get_service_info(service_name)

        print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
