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

class CareerAdviceChatbot:
    """
    A chatbot that provides career advice, including earning potential analysis
    and job market demand insights.
    """

    def __init__(self):
        # Career data with sample earning potential and job market demand insights
        self.career_data = {
            "Software Engineer": {
                "earning_potential": "$80,000 - $150,000 annually",
                "job_market_demand": "Very high demand due to the growth of tech industry."
            },
            "Data Scientist": {
                "earning_potential": "$90,000 - $170,000 annually",
                "job_market_demand": "High demand due to increasing use of data analytics."
            },
            "Digital Marketer": {
                "earning_potential": "$50,000 - $100,000 annually",
                "job_market_demand": "Growing demand as businesses expand their online presence."
            },
            "Cybersecurity Analyst": {
                "earning_potential": "$75,000 - $130,000 annually",
                "job_market_demand": "Critical demand due to increasing cybersecurity threats."
            },
            "Mechanical Engineer": {
                "earning_potential": "$70,000 - $120,000 annually",
                "job_market_demand": "Steady demand across industries like manufacturing and aerospace."
            },
        }

    def greet_user(self):
        """
        Greets the user and introduces the chatbot.
        """
        print("Hello! I'm your Career Advice Chatbot.")
        print("I can provide insights on earning potential and job market demand for various careers.")

    def list_available_careers(self):
        """
        Lists the careers available in the chatbot database.
        """
        print("\nHere are some careers I can provide advice on:")
        for career in self.career_data.keys():
            print(f"- {career}")

    def provide_career_advice(self, career_name):
        """
        Provides advice for the selected career.
        :param career_name: The name of the career to provide advice on.
        """
        # Error handling for invalid career names
        if career_name not in self.career_data:
            print("\nSorry, I don't have information about this career. Please try another.")
            return
        
        # Fetching and displaying career information
        advice = self.career_data[career_name]
        print(f"\nCareer: {career_name}")
        print(f"Earning Potential: {advice['earning_potential']}")
        print(f"Job Market Demand: {advice['job_market_demand']}")

    def random_career_advice(self):
        """
        Provides advice for a random career.
        """
        career_name = random.choice(list(self.career_data.keys()))
        print("\nHere's advice for a randomly selected career:")
        self.provide_career_advice(career_name)

    def run_chatbot(self):
        """
        Main method to run the chatbot interaction loop.
        """
        self.greet_user()
        
        # Interaction loop
        while True:
            print("\nOptions:")
            print("1. List available careers")
            print("2. Get advice for a specific career")
            print("3. Get advice for a random career")
            print("4. Exit")
            
            try:
                user_input = int(input("\nEnter your choice (1-4): "))
                
                if user_input == 1:
                    self.list_available_careers()
                elif user_input == 2:
                    career_name = input("\nEnter the name of the career: ").strip()
                    self.provide_career_advice(career_name)
                elif user_input == 3:
                    self.random_career_advice()
                elif user_input == 4:
                    print("\nThank you for using the Career Advice Chatbot. Goodbye!")
                    break
                else:
                    print("\nInvalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

# Create an instance of the chatbot
chatbot = CareerAdviceChatbot()

# Run the chatbot
if __name__ == "__main__":
    chatbot.run_chatbot()
```
