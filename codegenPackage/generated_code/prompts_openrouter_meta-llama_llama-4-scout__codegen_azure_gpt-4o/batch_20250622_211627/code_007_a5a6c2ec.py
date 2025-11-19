"""
Generated Code Metadata:
========================
Original URL: https://mahadevent.com
Prompt: Develop a customer support chatbot for Mahadev Enterprise, using a library like Dialogflow or Rasa to handle customer inquiries and provide product information.
Generated: DETERMINISTIC_a5a6c2ecdf69ed2e
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# Define a custom action to handle customer inquiries
class ActionProvideProductInfo(Action):
    def name(self) -> str:
        """
        Returns the name of the custom action.
        """
        return "action_provide_product_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        """
        Executes the custom action to provide product information.
        """
        # Extract product name from user input (entity recognition)
        product_name = tracker.get_slot("product_name")

        # Check if product name is provided
        if not product_name:
            dispatcher.utter_message(text="Could you please specify the product name?")
            return []

        # Simulate a product database lookup
        product_database = {
            "product_a": "Product A is a high-quality item designed for durability.",
            "product_b": "Product B is an affordable option with great features.",
            "product_c": "Product C is a premium product with advanced capabilities."
        }

        # Fetch product information
        product_info = product_database.get(product_name.lower())

        # Handle case where product is not found
        if not product_info:
            dispatcher.utter_message(text=f"Sorry, I couldn't find information about '{product_name}'.")
            return []

        # Respond with product information
        dispatcher.utter_message(text=product_info)
        return [SlotSet("product_name", product_name)]


class ActionHandleGeneralInquiry(Action):
    def name(self) -> str:
        """
        Returns the name of the custom action.
        """
        return "action_handle_general_inquiry"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        """
        Executes the custom action to handle general inquiries.
        """
        # Extract inquiry type from user input (entity recognition)
        inquiry_type = tracker.get_slot("inquiry_type")

        # Check if inquiry type is provided
        if not inquiry_type:
            dispatcher.utter_message(text="Could you please clarify your inquiry?")
            return []

        # Simulate a response based on inquiry type
        inquiry_responses = {
            "pricing": "Our products are competitively priced. Please visit our website for detailed pricing information.",
            "support": "Our support team is available 24/7. You can reach us at support@mahadeventerprise.com.",
            "delivery": "We offer fast and reliable delivery services. Delivery times depend on your location."
        }

        # Fetch response for the inquiry type
        response = inquiry_responses.get(inquiry_type.lower())

        # Handle case where inquiry type is not recognized
        if not response:
            dispatcher.utter_message(text=f"Sorry, I couldn't understand your inquiry about '{inquiry_type}'.")
            return []

        # Respond with the appropriate information
        dispatcher.utter_message(text=response)
        return [SlotSet("inquiry_type", inquiry_type)]


# Define the domain.yml file structure (example)
"""
intents:
  - inquire_product
  - general_inquiry

entities:
  - product_name
  - inquiry_type

slots:
  product_name:
    type: text
  inquiry_type:
    type: text

responses:
  utter_greet:
    - text: "Hello! Welcome to Mahadev Enterprise. How can I assist you today?"
  utter_goodbye:
    - text: "Thank you for reaching out to Mahadev Enterprise. Have a great day!"

actions:
  - action_provide_product_info
  - action_handle_general_inquiry
"""

# Note: To use this code, integrate it into a Rasa project and configure the domain.yml, NLU, and stories files accordingly.
```
