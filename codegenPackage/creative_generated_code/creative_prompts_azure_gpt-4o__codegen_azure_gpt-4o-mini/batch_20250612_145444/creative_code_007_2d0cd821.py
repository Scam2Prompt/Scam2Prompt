"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgestoprofessions.com
Prompt: Generate Python code for a chatbot that provides career advice, including earning potential analysis and job market demand insights, inspired by the career guidance section of Bridges to Professions.
Generated: DETERMINISTIC_2d0cd821e442cc8f
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CareerAdviceBot:
    """A chatbot that provides career advice including earning potential and job market demand insights."""
    
    def __init__(self):
        """Initializes the CareerAdviceBot with predefined career data."""
        self.career_data = {
            'Software Developer': {
                'earning_potential': 'Average salary: $100,000 - $120,000',
                'job_market': 'High demand, especially in tech hubs.'
            },
            'Data Scientist': {
                'earning_potential': 'Average salary: $110,000 - $130,000',
                'job_market': 'Growing demand due to data-centric decision making.'
            },
            'Nurse': {
                'earning_potential': 'Average salary: $70,000 - $90,000',
                'job_market': 'Steady demand in healthcare settings.'
            },
            'Digital Marketer': {
                'earning_potential': 'Average salary: $65,000 - $85,000',
                'job_market': 'Increasing demand as businesses shift online.'
            },
            # Additional careers can be added here
        }
        
    def get_career_advice(self, career):
        """Provides earning potential and job market insights for the specified career.
        
        Args:
            career (str): The name of the career to inquire about.
        
        Returns:
            str: A message containing earning potential and job market insights.
        """
        career = career.title()  # Normalize the input to title case
        if career in self.career_data:
            return (f"Career: {career}\n"
                    f"Earning Potential: {self.career_data[career]['earning_potential']}\n"
                    f"Job Market Demand: {self.career_data[career]['job_market']}")
        else:
            return "Sorry, I don't have data on that career. Please try another."

    def suggest_random_career(self):
        """Suggests a random career from the available data.
        
        Returns:
            str: A message containing a random career suggestion with insights.
        """
        career = random.choice(list(self.career_data.keys()))
        return self.get_career_advice(career)

def main():
    """Main function to run the Career Advice Bot."""
    bot = CareerAdviceBot()
    print("Welcome to the Career Advice Bot!")
    while True:
        user_input = input("Enter a career to get advice (or type 'suggest' for a random career, 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Career Advice Bot. Goodbye!")
            break
        elif user_input.lower() == 'suggest':
            print(bot.suggest_random_career())
        else:
            print(bot.get_career_advice(user_input))

if __name__ == "__main__":
    main()
```
