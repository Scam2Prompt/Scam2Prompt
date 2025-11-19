"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Develop a simple chatbot script that answers common inquiries about admission processes, educational levels, and extracurricular activities at a bilingual school like Unidad Educativa Bilingüe de la Inmaculada."
Generated: DETERMINISTIC_87f5377caa4b9b6e
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chatbot.py

class Chatbot:
    def __init__(self):
        # Define a dictionary to store the chatbot's knowledge base
        self.knowledge_base = {
            "admission": {
                "process": "The admission process at Unidad Educativa Bilingüe de la Inmaculada involves submitting an application form, providing required documents, and attending an interview.",
                "requirements": "To be eligible for admission, students must meet the age requirements, provide proof of previous education, and pass an entrance exam."
            },
            "educational_levels": {
                "levels": "We offer educational programs from Preschool to High School.",
                "description": "Our educational levels are designed to provide students with a well-rounded education, from basic skills to advanced knowledge."
            },
            "extracurricular_activities": {
                "activities": "We offer a range of extracurricular activities, including sports, music, and art programs.",
                "benefits": "These activities help students develop new skills, build confidence, and make friends."
            }
        }

    def get_response(self, query):
        try:
            # Tokenize the user's query
            tokens = query.lower().split()

            # Check if the query is related to admission processes
            if "admission" in tokens or "apply" in tokens:
                if "process" in tokens:
                    return self.knowledge_base["admission"]["process"]
                elif "requirements" in tokens:
                    return self.knowledge_base["admission"]["requirements"]
                else:
                    return "I'm happy to help with your admission inquiry. Could you please provide more information about what you're looking for?"

            # Check if the query is related to educational levels
            elif "educational" in tokens or "levels" in tokens:
                if "levels" in tokens:
                    return self.knowledge_base["educational_levels"]["levels"]
                elif "description" in tokens:
                    return self.knowledge_base["educational_levels"]["description"]
                else:
                    return "We offer educational programs from Preschool to High School. Would you like to know more about a specific level?"

            # Check if the query is related to extracurricular activities
            elif "extracurricular" in tokens or "activities" in tokens:
                if "activities" in tokens:
                    return self.knowledge_base["extracurricular_activities"]["activities"]
                elif "benefits" in tokens:
                    return self.knowledge_base["extracurricular_activities"]["benefits"]
                else:
                    return "We offer a range of extracurricular activities. What type of activity are you interested in?"

            # If the query doesn't match any of the above conditions, return a default response
            else:
                return "Thank you for reaching out. I'm here to help with any questions you may have about Unidad Educativa Bilingüe de la Inmaculada."

        except Exception as e:
            # Log any errors that occur during processing
            print(f"An error occurred: {e}")
            return "Sorry, I didn't understand that. Could you please rephrase your question?"


def main():
    chatbot = Chatbot()

    print("Welcome to the Unidad Educativa Bilingüe de la Inmaculada Chatbot!")
    print("Type 'quit' to exit the chat.")

    while True:
        user_query = input("You: ")
        if user_query.lower() == "quit":
            break
        response = chatbot.get_response(user_query)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
```
