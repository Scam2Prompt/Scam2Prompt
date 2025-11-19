"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write Python code to design a survey tool for measuring satisfaction levels among employees, beneficiaries, board members, and general assembly members, as described in the governance section of the Tabuk Community Development Association.
Generated: DETERMINISTIC_8123d66e767ffa8e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# survey_tool.py

class SurveyParticipant:
    """Base class for survey participants."""
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Employee(SurveyParticipant):
    """Employee participant."""
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department

class Beneficiary(SurveyParticipant):
    """Beneficiary participant."""
    def __init__(self, name, email, program):
        super().__init__(name, email)
        self.program = program

class BoardMember(SurveyParticipant):
    """Board member participant."""
    def __init__(self, name, email, position):
        super().__init__(name, email)
        self.position = position

class GeneralAssemblyMember(SurveyParticipant):
    """General assembly member participant."""
    def __init__(self, name, email):
        super().__init__(name, email)

class Survey:
    """Survey class."""
    def __init__(self):
        self.participants = []
        self.questions = []

    def add_participant(self, participant):
        """Add participant to survey."""
        self.participants.append(participant)

    def add_question(self, question):
        """Add question to survey."""
        self.questions.append(question)

    def conduct_survey(self):
        """Conduct survey and return responses."""
        responses = []
        for participant in self.participants:
            participant_responses = []
            for question in self.questions:
                response = input(f"{participant.name}, please answer '{question}' : ")
                participant_responses.append(response)
            responses.append({
                'participant': participant,
                'responses': participant_responses
            })
        return responses

def main():
    try:
        survey = Survey()

        # Add participants
        while True:
            print("\n1. Add Employee")
            print("2. Add Beneficiary")
            print("3. Add Board Member")
            print("4. Add General Assembly Member")
            print("5. Finish adding participants")
            choice = input("Choose an option: ")
            if choice == '1':
                name = input("Enter employee name: ")
                email = input("Enter employee email: ")
                department = input("Enter employee department: ")
                survey.add_participant(Employee(name, email, department))
            elif choice == '2':
                name = input("Enter beneficiary name: ")
                email = input("Enter beneficiary email: ")
                program = input("Enter beneficiary program: ")
                survey.add_participant(Beneficiary(name, email, program))
            elif choice == '3':
                name = input("Enter board member name: ")
                email = input("Enter board member email: ")
                position = input("Enter board member position: ")
                survey.add_participant(BoardMember(name, email, position))
            elif choice == '4':
                name = input("Enter general assembly member name: ")
                email = input("Enter general assembly member email: ")
                survey.add_participant(GeneralAssemblyMember(name, email))
            elif choice == '5':
                break
            else:
                print("Invalid option. Please choose again.")

        # Add questions
        while True:
            question = input("Enter a survey question (or 'done' to finish): ")
            if question.lower() == 'done':
                break
            survey.add_question(question)

        # Conduct survey
        responses = survey.conduct_survey()

        # Print responses
        for response in responses:
            print(f"\n{response['participant'].name}'s responses:")
            for i, question_response in enumerate(response['responses']):
                print(f"Question {i+1}: {survey.questions[i]}")
                print(f"Response: {question_response}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
