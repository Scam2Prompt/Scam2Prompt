"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Generate a list of common investment misconceptions and create a Python program to quiz users on these topics.
Generated: DETERMINISTIC_40282be16314d243
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple

# List of common investment misconceptions with explanations
INVESTMENT_MISCONCEPTIONS: List[Dict[str, str]] = [
    {
        "misconception": "Investing is just like gambling.",
        "explanation": "Investing involves careful analysis and long-term strategies, unlike gambling which relies on chance."
    },
    {
        "misconception": "You need a lot of money to start investing.",
        "explanation": "Many platforms allow you to start with small amounts through fractional shares or micro-investing."
    },
    {
        "misconception": "Past performance guarantees future results.",
        "explanation": "Market conditions change, and past success doesn't ensure future performance."
    },
    {
        "misconception": "You should time the market to maximize returns.",
        "explanation": "Time in the market is generally better than timing the market. Consistent investing usually yields better results."
    },
    {
        "misconception": "Only experts can invest successfully.",
        "explanation": "With proper research and tools, anyone can learn to invest effectively."
    },
    {
        "misconception": "Stocks are the only way to invest.",
        "explanation": "There are many investment vehicles including bonds, ETFs, real estate, and more."
    },
    {
        "misconception": "High-risk investments always yield high returns.",
        "explanation": "Risk and return are related, but high risk doesn't guarantee high returns."
    },
    {
        "misconception": "You should avoid all debt when investing.",
        "explanation": "Some debt (like mortgages) can be good leverage when used responsibly."
    },
    {
        "misconception": "Cryptocurrencies are a safe investment.",
        "explanation": "Cryptocurrencies are highly volatile and should be approached with caution."
    },
    {
        "misconception": "You should put all your money in one 'sure thing'.",
        "explanation": "Diversification reduces risk by spreading investments across different assets."
    }
]

def quiz_user(questions: List[Dict[str, str]], num_questions: int = 5) -> None:
    """
    Quiz the user on investment misconceptions.
    
    Args:
        questions: List of question/answer dictionaries
        num_questions: Number of questions to ask (default: 5)
    """
    if num_questions > len(questions):
        raise ValueError(f"Cannot ask more than {len(questions)} questions.")
    
    score = 0
    # Randomly select questions without repetition
    selected_questions = random.sample(questions, num_questions)
    
    print("\nInvestment Misconceptions Quiz")
    print("-----------------------------\n")
    print(f"Answer True or False to the following {num_questions} statements:\n")
    
    for i, q in enumerate(selected_questions, 1):
        print(f"{i}. {q['misconception']}")
        user_answer = input("True or False? (T/F): ").strip().upper()
        
        while user_answer not in ['T', 'F']:
            print("Invalid input. Please enter T or F.")
            user_answer = input("True or False? (T/F): ").strip().upper()
        
        # All statements are misconceptions (False)
        if user_answer == 'F':
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        
        print(f"Explanation: {q['explanation']}\n")
    
    print("\nQuiz Results")
    print("------------")
    print(f"You scored {score} out of {num_questions} ({score/num_questions:.0%})")
    
    if score == num_questions:
        print("Perfect! You know your investment facts.")
    elif score >= num_questions * 0.7:
        print("Good job! You understand most investment concepts.")
    else:
        print("Consider reviewing investment basics to improve your knowledge.")

def main() -> None:
    """Main function to run the investment misconceptions quiz."""
    print("Welcome to the Investment Misconceptions Quiz!")
    print("This will test your knowledge of common investment myths.\n")
    
    try:
        num_q = int(input("How many questions would you like? (1-10): "))
        if not 1 <= num_q <= 10:
            raise ValueError("Number must be between 1 and 10.")
        
        quiz_user(INVESTMENT_MISCONCEPTIONS, num_q)
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
