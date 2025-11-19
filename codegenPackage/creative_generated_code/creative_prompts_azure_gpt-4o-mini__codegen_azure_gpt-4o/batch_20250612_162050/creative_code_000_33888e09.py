"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://textcounsellingonline.com.au
Prompt: How can I implement a text-based counselling service similar to the one offered at Text Counselling Online, focusing on user preferences for written communication?
Generated: DETERMINISTIC_33888e098fee5b52
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CounsellingService:
    """
    A text-based counselling service implementation.
    Allows users to send messages to counsellors and receive responses.
    """

    def __init__(self):
        # Initialize the service with empty user and counsellor message logs
        self.user_messages = []
        self.counsellor_responses = []

    def send_user_message(self, message: str):
        """
        Allows a user to send a message to the service.
        Stores the message with a timestamp.

        Args:
            message (str): The user's message.
        """
        if not message:
            raise ValueError("Message cannot be empty")
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = {"timestamp": timestamp, "message": message}
        self.user_messages.append(formatted_message)

    def get_user_messages(self):
        """
        Retrieves all user messages.

        Returns:
            list: A list of user messages with timestamps.
        """
        return self.user_messages

    def send_counsellor_response(self, response: str):
        """
        Allows a counsellor to send a response to the user.
        Stores the response with a timestamp.

        Args:
            response (str): The counsellor's response.
        """
        if not response:
            raise ValueError("Response cannot be empty")
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_response = {"timestamp": timestamp, "response": response}
        self.counsellor_responses.append(formatted_response)

    def get_counsellor_responses(self):
        """
        Retrieves all counsellor responses.

        Returns:
            list: A list of counsellor responses with timestamps.
        """
        return self.counsellor_responses

    def get_conversation_history(self):
        """
        Retrieves the full conversation history in chronological order.

        Returns:
            list: A list of conversation entries (messages and responses) with timestamps.
        """
        history = []

        # Combine user messages and counsellor responses into a single chronological list
        for user_msg, counsellor_resp in zip(self.user_messages, self.counsellor_responses):
            history.append({"type": "user", **user_msg})
            history.append({"type": "counsellor", **counsellor_resp})

        # Handle cases where the user or counsellor sends more messages
        if len(self.user_messages) > len(self.counsellor_responses):
            remaining = self.user_messages[len(self.counsellor_responses):]
            for msg in remaining:
                history.append({"type": "user", **msg})
        elif len(self.counsellor_responses) > len(self.user_messages):
            remaining = self.counsellor_responses[len(self.user_messages):]
            for resp in remaining:
                history.append({"type": "counsellor", **resp})

        return history


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the CounsellingService
        service = CounsellingService()

        # Send messages and responses
        service.send_user_message("I am feeling anxious lately.")
        service.send_counsellor_response("I understand. Can you tell me more about what’s causing your anxiety?")
        service.send_user_message("I have been stressed at work.")

        # Retrieve conversation history
        history = service.get_conversation_history()
        for entry in history:
            print(f"[{entry['timestamp']} - {entry['type'].capitalize()}] {entry.get('message') or entry.get('response')}")

    except Exception as e:
        print(f"Error: {e}")
```
