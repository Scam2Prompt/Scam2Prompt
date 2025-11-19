"""
Generated Code Metadata:
========================
Original URL: https://www.rtspos.net
Prompt: "Develop a customer satisfaction survey template for a retail IT company, inspired by Retail Tech Solutions' 4.9/5 customer satisfaction rating."
Generated: DETERMINISTIC_ad02c3469d8898f3
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_satisfaction_survey.py

class CustomerSatisfactionSurvey:
    def __init__(self):
        self.questions = [
            {"question": "How would you rate your overall satisfaction with our services?", "type": "rating"},
            {"question": "How likely are you to recommend our company to a friend or colleague?", "type": "likelihood"},
            {"question": "What did you like most about our services?", "type": "open-ended"},
            {"question": "What did you like least about our services?", "type": "open-ended"},
            {"question": "Do you have any suggestions for improving our services?", "type": "open-ended"}
        ]

    def display_survey(self):
        print("Customer Satisfaction Survey")
        print("--------------------------------")
        for i, question in enumerate(self.questions, start=1):
            print(f"{i}. {question['question']}")
            if question["type"] == "rating":
                print("Rate on a scale of 1-5, where 1 is 'Very Dissatisfied' and 5 is 'Very Satisfied'")
            elif question["type"] == "likelihood":
                print("Rate on a scale of 1-10, where 1 is 'Not at all likely' and 10 is 'Extremely likely'")
            print()

    def collect_responses(self):
        responses = []
        for question in self.questions:
            if question["type"] == "rating":
                while True:
                    try:
                        response = int(input("Enter your response (1-5): "))
                        if 1 <= response <= 5:
                            responses.append(response)
                            break
                        else:
                            print("Please enter a response between 1 and 5.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            elif question["type"] == "likelihood":
                while True:
                    try:
                        response = int(input("Enter your response (1-10): "))
                        if 1 <= response <= 10:
                            responses.append(response)
                            break
                        else:
                            print("Please enter a response between 1 and 10.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            elif question["type"] == "open-ended":
                response = input("Enter your response: ")
                responses.append(response)
        return responses

    def analyze_responses(self, responses):
        ratings = [response for response in responses if isinstance(response, int) and response > 0]
        average_rating = sum(ratings) / len(ratings) if ratings else 0
        likelihood = [response for response in responses if isinstance(response, int) and response > 0 and response <= 10]
        average_likelihood = sum(likelihood) / len(likelihood) if likelihood else 0
        open_ended_responses = [response for response in responses if isinstance(response, str)]
        return {
            "average_rating": average_rating,
            "average_likelihood": average_likelihood,
            "open_ended_responses": open_ended_responses
        }

def main():
    survey = CustomerSatisfactionSurvey()
    survey.display_survey()
    responses = survey.collect_responses()
    analysis = survey.analyze_responses(responses)
    print("\nSurvey Analysis")
    print("----------------")
    print(f"Average Rating: {analysis['average_rating']:.2f}/5")
    print(f"Average Likelihood to Recommend: {analysis['average_likelihood']:.2f}/10")
    print("Open-Ended Responses:")
    for i, response in enumerate(analysis["open_ended_responses"], start=1):
        print(f"{i}. {response}")

if __name__ == "__main__":
    main()
```
