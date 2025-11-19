"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perezbernalte.com
Prompt: Draft a client intake questionnaire for a law firm, including questions that align with the services provided by Pérez Bernalte Abogados in Barcelona.
Generated: DETERMINISTIC_c539b9c281baf02c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# client_intake_questionnaire.py

class ClientIntakeQuestionnaire:
    """
    A class to represent a client intake questionnaire for Pérez Bernalte Abogados in Barcelona.
    """

    def __init__(self):
        self.questions = [
            "1. Full Name:",
            "2. Contact Information (Email and Phone Number):",
            "3. Preferred Method of Communication (Email/Phone):",
            "4. Briefly describe your legal issue:",
            "5. Which of our services are you interested in? (e.g., Family Law, Immigration, Business Law, etc.):",
            "6. Have you previously worked with a lawyer? If yes, please provide details:",
            "7. How did you hear about Pérez Bernalte Abogados?",
            "8. Do you have any specific concerns or questions for us?",
            "9. Please provide any relevant documents or evidence related to your legal issue:",
            "10. What is your preferred schedule for a consultation?"
        ]

    def display_questionnaire(self):
        """
        Displays the client intake questionnaire.
        """
        print("Client Intake Questionnaire for Pérez Bernalte Abogados\n")
        for question in self.questions:
            print(question)

    def collect_answers(self):
        """
        Collects answers from the client.
        Returns a dictionary of responses.
        """
        responses = {}
        print("\nPlease answer the following questions:\n")
        for question in self.questions:
            answer = input(question + " ")
            responses[question] = answer
        return responses

    def save_to_file(self, responses, filename="client_responses.txt"):
        """
        Saves the collected responses to a text file.
        
        :param responses: A dictionary containing the questions and client responses.
        :param filename: The name of the file to save responses.
        """
        try:
            with open(filename, 'w') as file:
                for question, answer in responses.items():
                    file.write(f"{question} {answer}\n")
            print(f"\nResponses successfully saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while trying to save responses: {e}")

if __name__ == "__main__":
    questionnaire = ClientIntakeQuestionnaire()
    questionnaire.display_questionnaire()
    
    client_responses = questionnaire.collect_answers()
    questionnaire.save_to_file(client_responses)
```
