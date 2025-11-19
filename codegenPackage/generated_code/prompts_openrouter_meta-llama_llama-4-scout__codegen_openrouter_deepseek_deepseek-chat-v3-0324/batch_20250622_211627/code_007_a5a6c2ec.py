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
import logging
from typing import Dict, Any, Optional
from rasa.core.agent import Agent
from rasa.shared.constants import DEFAULT_SERVER_PORT
from rasa.core.channels.socketio import SocketIOInput
from rasa.core.utils import AvailableEndpoints
from sanic import Sanic
from sanic.response import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

class MahadevEnterpriseChatbot:
    """
    Customer support chatbot for Mahadev Enterprise.
    Handles customer inquiries and provides product information.
    """

    def __init__(self, model_path: str = "models"):
        """
        Initialize the chatbot with a trained Rasa model.
        
        Args:
            model_path: Path to the trained Rasa model directory.
        """
        self.agent = self._load_agent(model_path)

    def _load_agent(self, model_path: str) -> Agent:
        """
        Load the Rasa agent from the specified model path.
        
        Args:
            model_path: Path to the trained Rasa model directory.
            
        Returns:
            Loaded Rasa agent.
            
        Raises:
            FileNotFoundError: If model files are not found.
            Exception: For other loading errors.
        """
        try:
            endpoints = AvailableEndpoints()
            agent = Agent.load(model_path, endpoints=endpoints)
            logger.info("Rasa agent loaded successfully")
            return agent
        except FileNotFoundError as e:
            logger.error(f"Model files not found: {e}")
            raise
        except Exception as e:
            logger.error(f"Error loading Rasa agent: {e}")
            raise

    async def handle_message(self, message: str, sender_id: str) -> Dict[str, Any]:
        """
        Process an incoming message and return the chatbot's response.
        
        Args:
            message: The user's message text.
            sender_id: Unique identifier for the user/session.
            
        Returns:
            Dictionary containing the bot's response.
        """
        try:
            response = await self.agent.handle_text(message, sender_id=sender_id)
            return {"response": response}
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            return {"error": "Sorry, I encountered an error processing your request."}

def create_app(model_path: str = "models") -> Sanic:
    """
    Create and configure a Sanic application for the chatbot API.
    
    Args:
        model_path: Path to the trained Rasa model directory.
        
    Returns:
        Configured Sanic application.
    """
    app = Sanic("MahadevEnterpriseChatbot")
    chatbot = MahadevEnterpriseChatbot(model_path)

    @app.route("/webhook", methods=["POST"])
    async def webhook(request):
        """
        Webhook endpoint for processing messages.
        """
        try:
            data = request.json
            message = data.get("message", "")
            sender_id = data.get("sender_id", "default")
            
            if not message:
                return json({"error": "Message is required"}, status=400)
                
            response = await chatbot.handle_message(message, sender_id)
            return json(response)
        except Exception as e:
            logger.error(f"Error in webhook: {e}")
            return json({"error": "Internal server error"}, status=500)

    return app

def run_chatbot_server(
    model_path: str = "models",
    port: int = DEFAULT_SERVER_PORT,
    cors: Optional[str] = None,
):
    """
    Run the chatbot server with SocketIO input channel.
    
    Args:
        model_path: Path to the trained Rasa model directory.
        port: Port to run the server on.
        cors: CORS origin to allow (optional).
    """
    app = create_app(model_path)
    input_channel = SocketIOInput(
        # You can customize the SocketIO configuration here
        user_message_evt="user_uttered",
        bot_message_evt="bot_uttered",
        namespace=None,
        cors_origins=cors,
    )

    app.agent = MahadevEnterpriseChatbot(model_path).agent
    app.agent.handle_channels([input_channel], http_port=port)
    logger.info(f"Chatbot server running on port {port}")
    app.run(port=port)

if __name__ == "__main__":
    # Example usage
    run_chatbot_server()
```
