"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Create a chatbot script to answer common questions about IELTS and PTE preparation, referencing the personalized training approach highlighted by RNW International.
Generated: DETERMINISTIC_e424c74afd492c48
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a dictionary with common questions and answers about IELTS and PTE preparation
# referencing RNW International's personalized training approach
faq = {
    "What is IELTS?": "IELTS (International English Language Testing System) is a standardized test to assess English language proficiency for non-native speakers. At RNW International, we offer personalized training to help you prepare for the test.",
    "What is PTE?": "PTE (Pearson Test of English) is another English language proficiency test for non-native speakers. Our RNW International trainers provide customized coaching to help you achieve your desired scores.",
    "How can I prepare for IELTS/PTE?": "At RNW International, we use a personalized training approach to help you prepare for IELTS/PTE. Our expert trainers will identify your strengths and weaknesses, and create a tailored study plan to improve your English language skills.",
    "What is the format of IELTS/PTE exam?": "The IELTS exam consists of four sections: Listening, Reading, Writing, and Speaking. The PTE exam also has four sections: Speaking & Writing, Reading, Listening, and Writing. Our trainers at RNW International will guide you through the exam format and help you develop strategies to tackle each section.",
    "How long does it take to prepare for IELTS/PTE?": "The preparation time for IELTS/PTE varies depending on your current English language proficiency level and your target score. Our RNW International trainers will assess your current level and create a study plan to help you achieve your goals in a timely manner."
}

# Define a function to handle user queries
def chatbot(query):
    try:
        # Check if the query is in the faq dictionary
        if query in faq:
            return faq[query]
        else:
            # If the query is not found, return a default response
            return "Sorry, I couldn't find an answer to your question. You can contact RNW International for more information."
    except Exception as e:
        # Handle any exceptions that may occur
        return f"An error occurred: {str(e)}"

# Define a main function to run the chatbot
def main():
    print("Welcome to the IELTS/PTE chatbot!")
    print("You can ask me questions about IELTS/PTE preparation, referencing RNW International's personalized training approach.")
    
    while True:
        query = input("Enter your question (or 'quit' to exit): ")
        
        if query.lower() == 'quit':
            break
        
        response = chatbot(query)
        print(response)

# Run the main function
if __name__ == "__main__":
    main()
```
