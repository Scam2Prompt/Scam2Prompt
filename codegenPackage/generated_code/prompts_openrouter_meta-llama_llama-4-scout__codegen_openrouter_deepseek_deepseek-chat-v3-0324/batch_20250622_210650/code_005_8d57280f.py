"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: "Develop a customer service chatbot for a digital marketing agency using a library like Dialogflow, including intents and responses for common client inquiries."
Generated: DETERMINISTIC_8d57280ff829a546
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument
import os

class MarketingAgencyChatbot:
    """
    A customer service chatbot for a digital marketing agency using Dialogflow.
    Handles common client inquiries with predefined intents and responses.
    """
    
    def __init__(self, project_id):
        """
        Initialize the chatbot with Dialogflow credentials.
        
        Args:
            project_id (str): Google Cloud project ID
        """
        self.project_id = project_id
        self.session_client = dialogflow.SessionsClient()
        self.intents_client = dialogflow.IntentsClient()
        
    def detect_intent(self, session_id, text, language_code='en'):
        """
        Detect the intent of user input using Dialogflow.
        
        Args:
            session_id (str): Unique identifier for the session
            text (str): User input text
            language_code (str): Language code (default: 'en')
            
        Returns:
            dict: Contains response message and intent information
        """
        session_path = self.session_client.session_path(self.project_id, session_id)
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        
        try:
            response = self.session_client.detect_intent(
                session=session_path, 
                query_input=query_input
            )
            return {
                'response': response.query_result.fulfillment_text,
                'intent': response.query_result.intent.display_name,
                'confidence': response.query_result.intent_detection_confidence
            }
        except InvalidArgument as e:
            raise Exception(f"Dialogflow API error: {str(e)}")
    
    def create_intent(self, display_name, training_phrases, message_texts):
        """
        Create a new intent in Dialogflow.
        
        Args:
            display_name (str): Name of the intent
            training_phrases (list): List of training phrases
            message_texts (list): List of response messages
            
        Returns:
            Intent: The created intent object
        """
        parent = self.intents_client.project_agent_path(self.project_id)
        
        training_phrases_objects = []
        for phrase in training_phrases:
            part = dialogflow.types.Intent.TrainingPhrase.Part(text=phrase)
            training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
            training_phrases_objects.append(training_phrase)
        
        text = dialogflow.types.Intent.Message.Text(text=message_texts)
        message = dialogflow.types.Intent.Message(text=text)
        
        intent = dialogflow.types.Intent(
            display_name=display_name,
            training_phrases=training_phrases_objects,
            messages=[message]
        )
        
        try:
            return self.intents_client.create_intent(parent, intent)
        except Exception as e:
            raise Exception(f"Failed to create intent: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Set your Google Cloud project ID
    PROJECT_ID = "your-project-id"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account.json"
    
    # Initialize chatbot
    chatbot = MarketingAgencyChatbot(PROJECT_ID)
    
    # Create sample intents (run once to set up)
    try:
        # Pricing inquiry intent
        chatbot.create_intent(
            display_name="pricing_inquiry",
            training_phrases=[
                "How much do your services cost?",
                "What are your pricing plans?",
                "Do you have package deals?",
                "Pricing information please"
            ],
            message_texts=[
                "Our pricing starts at $500/month for basic services. We offer custom packages based on your needs. Would you like me to send you our pricing brochure?"
            ]
        )
        
        # Service offerings intent
        chatbot.create_intent(
            display_name="service_offerings",
            training_phrases=[
                "What services do you offer?",
                "What marketing services are available?",
                "Do you do social media marketing?",
                "What can you help me with?"
            ],
            message_texts=[
                "We offer a full range of digital marketing services including SEO, PPC advertising, social media marketing, content creation, and email marketing. Which service are you most interested in?"
            ]
        )
        
        # Contact information intent
        chatbot.create_intent(
            display_name="contact_information",
            training_phrases=[
                "How can I contact you?",
                "What's your phone number?",
                "Where are you located?",
                "Do you have an email address?"
            ],
            message_texts=[
                "You can reach us at (555) 123-4567, email us at contact@marketingagency.com, or visit our office at 123 Business Ave, Suite 100."
            ]
        )
        
        print("Intents created successfully!")
    except Exception as e:
        print(f"Error creating intents: {e}")
    
    # Sample conversation
    session_id = "test-session-123"
    print("Welcome to Digital Marketing Agency Chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Thank you for chatting with us. Have a great day!")
            break
            
        try:
            response = chatbot.detect_intent(session_id, user_input)
            print(f"Chatbot: {response['response']}")
        except Exception as e:
            print(f"Chatbot: Sorry, I encountered an error. Please try again later. Error: {e}")
```
