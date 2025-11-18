"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: Provide code examples for using the OpenAI Assistant API to build a chatbot that can search files and answer user queries in real-time.
Generated: DETERMINISTIC_f6e881d165aefaba
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import openai
import json

# Set the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

class Chatbot:
    def __init__(self, file_paths):
        """
        Initializes the Chatbot with a list of file paths to search.

        Args:
            file_paths (list): A list of file paths to be searched.
        """
        self.file_paths = file_paths

    def search_files(self, query):
        """
        Searches for the query in the specified files and returns the results.

        Args:
            query (str): The search query.

        Returns:
            str: The content found in the files related to the query.
        """
        results = []
        for file_path in self.file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if query.lower() in content.lower():
                        results.append(content)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
        return results

    def ask_openai(self, query):
        """
        Sends a query to the OpenAI API and retrieves a response.

        Args:
            query (str): The user query.

        Returns:
            str: The response from the OpenAI API.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": query}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error with OpenAI API: {e}")
            return "I'm having trouble accessing the information right now."

    def handle_query(self, user_query):
        """
        Handles a user query by searching files and querying OpenAI.

        Args:
            user_query (str): The user's query.

        Returns:
            str: The result from searching files or the response from OpenAI.
        """
        search_results = self.search_files(user_query)
        if search_results:
            return "\n".join(search_results)
        else:
            return self.ask_openai(user_query)

if __name__ == "__main__":
    # List of files to search
    files_to_search = ['file1.txt', 'file2.txt', 'file3.txt']  # Update with actual file paths
    
    # Initialize the chatbot
    chatbot = Chatbot(files_to_search)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot.handle_query(user_input)
        print(f"Chatbot: {response}")
```

Make sure to:
1. Set your OpenAI API key in the environment variable `OPENAI_API_KEY`.
2. Update the `files_to_search` list with the actual paths to the text files you want to search.
3. Install the `openai` Python package if you haven't already: `pip install openai`.
