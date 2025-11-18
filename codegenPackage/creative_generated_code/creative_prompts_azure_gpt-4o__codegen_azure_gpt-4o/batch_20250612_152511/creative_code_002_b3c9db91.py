"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qna3ai.web.app
Prompt: Generate code to analyze the voting trends for questions on the QnA3 platform, including calculating the total votes and identifying the top-voted question.
Generated: DETERMINISTIC_b3c9db91c60247b7
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def analyze_voting_trends(data):
    """
    Analyze voting trends for questions on the QnA3 platform.

    Parameters:
    - data (list of dict): A list where each dictionary represents a question and contains:
        - 'id' (str): Unique identifier for the question.
        - 'title' (str): Title of the question.
        - 'votes' (int): Number of votes the question received.

    Returns:
    - dict: A dictionary containing:
        - 'total_votes' (int): Total number of votes across all questions.
        - 'top_voted_question' (dict): The question with the highest number of votes.
    """
    try:
        # Validate input data structure
        if not isinstance(data, list) or any(
            not isinstance(question, dict) or 'votes' not in question for question in data
        ):
            raise ValueError("Invalid input data format. Expected a list of dictionaries with 'votes' key.")

        # Calculate total votes
        total_votes = sum(question.get('votes', 0) for question in data)

        # Find the top-voted question
        top_voted_question = max(data, key=lambda q: q.get('votes', 0), default=None)

        return {
            'total_votes': total_votes,
            'top_voted_question': top_voted_question
        }
    except Exception as e:
        # Log and handle unexpected errors
        print(f"An error occurred: {e}")
        return {
            'total_votes': 0,
            'top_voted_question': None
        }

if __name__ == '__main__':
    # Example usage
    # Mock data representing questions and their votes
    example_data = [
        {"id": "q1", "title": "How to learn Python?", "votes": 120},
        {"id": "q2", "title": "Best practices for web development?", "votes": 150},
        {"id": "q3", "title": "What is machine learning?", "votes": 200},
        {"id": "q4", "title": "Understanding databases", "votes": 90}
    ]

    # Analyze the voting trends
    result = analyze_voting_trends(example_data)

    # Print the results
    print(json.dumps(result, indent=4))
```
