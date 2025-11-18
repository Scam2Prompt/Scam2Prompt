"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ungleder.no
Prompt: Generate code to build a chatbot that answers questions based on the FAQ section of ungLeder.no using GPT-3 or GPT-4.
Generated: DETERMINISTIC_c21e36b4aa3b507c
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import requests

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

class FAQChatbot:
    def __init__(self, faq_url):
        """
        Initializes the FAQChatbot with the URL of the FAQ section.
        
        Parameters:
            faq_url (str): The URL where the FAQ content is located.
        """
        self.faq_url = faq_url
        self.faq_data = self.fetch_faq_data()

    def fetch_faq_data(self):
        """
        Fetches the FAQ data from the provided URL.
        
        Returns:
            str: The FAQ data as a string.
        Raises:
            Exception: If there is an error fetching or parsing the data.
        """
        try:
            response = requests.get(self.faq_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text  # Assumes FAQ is in plain text format
        except requests.RequestException as e:
            raise Exception(f"Error fetching FAQ data: {e}")

    def get_answer(self, question):
        """
        Gets an answer to a question using OpenAI's GPT model.
        
        Parameters:
            question (str): The question to be answered.
        
        Returns:
            str: The answer from the model.
        Raises:
            Exception: If there is an error during the API call.
        """
        try:
            prompt = f"Based on the following FAQ, answer the question:\n\n{self.faq_data}\n\nQuestion: {question}\nAnswer:"
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            raise Exception(f"Error getting answer from OpenAI: {e}")

def main():
    """
    Main function to run the FAQ chatbot.
    Replace 'YOUR_FAQ_URL' with the actual URL of the FAQ section.
    """
    faq_url = 'YOUR_FAQ_URL'  # Replace with the FAQ URL
    chatbot = FAQChatbot(faq_url)
    
    print("Welcome to the FAQ Chatbot! Type 'exit' to quit.")
    while True:
        user_question = input("You: ")
        if user_question.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            answer = chatbot.get_answer(user_question)
            print(f"Chatbot: {answer}")
        except Exception as e:
            print(f"Chatbot error: {e}")

if __name__ == "__main__":
    main()
```

Make sure to replace `'YOUR_OPENAI_API_KEY'` and `'YOUR_FAQ_URL'` with your actual OpenAI API key and the FAQ URL.
