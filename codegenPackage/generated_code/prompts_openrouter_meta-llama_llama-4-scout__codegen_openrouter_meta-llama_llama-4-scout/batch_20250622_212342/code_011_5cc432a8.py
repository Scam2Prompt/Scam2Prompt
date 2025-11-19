"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Create a quiz to assess a user's social media follower list strategy, using questions and topics discussed on fearlessnetpreneur.com.
Generated: DETERMINISTIC_5cc432a83d3d6f91
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# social_media_quiz.py

class SocialMediaQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the primary goal of having a social media presence?",
                "options": [
                    "To share personal updates",
                    "To promote products or services",
                    "To engage with influencers",
                    "To build a community"
                ],
                "correct_answer": 2,
                "topic": "social media strategy"
            },
            {
                "question": "How often should you post on social media?",
                "options": [
                    "Daily",
                    "Weekly",
                    "Monthly",
                    "As needed"
                ],
                "correct_answer": 1,
                "topic": "content calendar"
            },
            {
                "question": "What is the ideal engagement rate on social media?",
                "options": [
                    "1-2%",
                    "5-10%",
                    "10-20%",
                    "20-50%"
                ],
                "correct_answer": 0,
                "topic": "engagement metrics"
            },
            {
                "question": "How can you grow your social media followers?",
                "options": [
                    "By buying followers",
                    "By engaging with your audience",
                    "By posting irrelevant content",
                    "By ignoring comments"
                ],
                "correct_answer": 1,
                "topic": "follower growth"
            },
            {
                "question": "What is the importance of monitoring social media analytics?",
                "options": [
                    "To track engagement metrics",
                    "To ignore negative feedback",
                    "To compare with competitors",
                    "To adjust your strategy"
                ],
                "correct_answer": 3,
                "topic": "analytics"
            }
        ]

    def run_quiz(self):
        score = 0
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i+1}: {question['question']}")
            for j, option in enumerate(question['options']):
                print(f"{j+1}. {option}")
            try:
                user_answer = int(input("Enter your answer (1-4): ")) - 1
                if user_answer == question['correct_answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {question['options'][question['correct_answer']]}")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")
        print(f"\nQuiz complete! Your final score is {score}/{len(self.questions)}")

    def get_topics(self):
        topics = set(question['topic'] for question in self.questions)
        return topics

def main():
    quiz = SocialMediaQuiz()
    print("Welcome to the social media quiz!")
    while True:
        print("\n1. Take the quiz")
        print("2. View topics")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                quiz.run_quiz()
            elif choice == 2:
                topics = quiz.get_topics()
                print("Topics:")
                for topic in topics:
                    print(topic)
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
```
