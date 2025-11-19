"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Write Python code to simulate a polygraph test questionnaire for pre-employment screening, including questions about integrity and background checks, as described on the Euro Poligraf Center website.
Generated: DETERMINISTIC_be0e219b917d648c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# polygraph_test.py

class PolygraphTest:
    def __init__(self):
        self.questions = {
            "Have you ever been convicted of a crime?": True,
            "Have you ever been dishonest with an employer?": True,
            "Have you ever used a fake identity?": True,
            "Have you ever been involved in a financial crime?": True,
            "Have you ever lied under oath?": True,
            "Do you have any skeletons in your closet that could harm your future employer?": True,
            "Have you ever cheated on a test or exam?": True,
            "Have you ever been fired from a job?": True,
            "Have you ever been involved in a violent crime?": True,
            "Have you ever used someone else's work without permission?": True,
        }
        self.user_answers = {}

    def administer_test(self):
        print("Polygraph Test Questionnaire")
        print("--------------------------------")
        for question, is_sensitive in self.questions.items():
            while True:
                try:
                    answer = input(question + " (yes/no): ")
                    if answer.lower() not in ["yes", "no"]:
                        raise ValueError
                    self.user_answers[question] = answer.lower() == "yes"
                    break
                except ValueError:
                    print("Invalid input. Please enter 'yes' or 'no'.")

    def evaluate_test(self):
        print("\nTest Results")
        print("-------------")
        for question, answer in self.user_answers.items():
            print(f"{question}: {'Yes' if answer else 'No'}")
        self.background_check()

    def background_check(self):
        print("\nBackground Check")
        print("-----------------")
        # Simulate a background check
        import random
        background_check_result = random.choice(["Passed", "Failed"])
        print(f"Background check result: {background_check_result}")
        if background_check_result == "Failed":
            print("Further investigation is required.")

    def integrity_assessment(self):
        print("\nIntegrity Assessment")
        print("--------------------")
        integrity_score = 0
        for question, answer in self.user_answers.items():
            if answer:
                integrity_score += 1
        print(f"Integrity score: {integrity_score}/{len(self.user_answers)}")
        if integrity_score > 3:
            print("Candidate's integrity is a concern.")
        else:
            print("Candidate's integrity appears to be satisfactory.")

def main():
    try:
        polygraph_test = PolygraphTest()
        polygraph_test.administer_test()
        polygraph_test.evaluate_test()
        polygraph_test.integrity_assessment()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
