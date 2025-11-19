"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Write a Python script to manage customer satisfaction surveys for a computer repair service like Geeks on Repair.
Generated: DETERMINISTIC_db544ee3ef00e008
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class SurveyManager:
    """
    A class to manage customer satisfaction surveys for a computer repair service.
    """

    def __init__(self, data_file="surveys.json"):
        """
        Initializes the SurveyManager with a file to store survey data.

        :param data_file: Path to the JSON file where survey data will be stored.
        """
        self.data_file = data_file
        self.surveys = self._load_surveys()

    def _load_surveys(self):
        """
        Loads survey data from the JSON file. If the file doesn't exist, initializes an empty list.

        :return: List of surveys.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading survey data. Starting with an empty list.")
                return []
        return []

    def _save_surveys(self):
        """
        Saves the current survey data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.surveys, file, indent=4)
        except IOError as e:
            print(f"Error saving survey data: {e}")

    def add_survey(self, customer_name, rating, comments):
        """
        Adds a new survey to the list.

        :param customer_name: Name of the customer.
        :param rating: Satisfaction rating (1-5).
        :param comments: Additional comments from the customer.
        """
        if not (1 <= rating <= 5):
            print("Error: Rating must be between 1 and 5.")
            return

        survey = {
            "customer_name": customer_name,
            "rating": rating,
            "comments": comments
        }
        self.surveys.append(survey)
        self._save_surveys()
        print("Survey added successfully.")

    def view_surveys(self):
        """
        Displays all surveys in a readable format.
        """
        if not self.surveys:
            print("No surveys available.")
            return

        for idx, survey in enumerate(self.surveys, start=1):
            print(f"Survey #{idx}")
            print(f"Customer Name: {survey['customer_name']}")
            print(f"Rating: {survey['rating']}")
            print(f"Comments: {survey['comments']}")
            print("-" * 40)

    def average_rating(self):
        """
        Calculates and returns the average satisfaction rating.

        :return: Average rating as a float, or None if no surveys exist.
        """
        if not self.surveys:
            print("No surveys available to calculate average rating.")
            return None

        total_rating = sum(survey["rating"] for survey in self.surveys)
        avg_rating = total_rating / len(self.surveys)
        return round(avg_rating, 2)


def main():
    """
    Main function to interact with the SurveyManager.
    """
    manager = SurveyManager()

    while True:
        print("\nCustomer Satisfaction Survey Manager")
        print("1. Add a new survey")
        print("2. View all surveys")
        print("3. Calculate average rating")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_name = input("Enter customer name: ")
            try:
                rating = int(input("Enter satisfaction rating (1-5): "))
            except ValueError:
                print("Error: Rating must be a number between 1 and 5.")
                continue
            comments = input("Enter additional comments: ")
            manager.add_survey(customer_name, rating, comments)
        elif choice == "2":
            manager.view_surveys()
        elif choice == "3":
            avg_rating = manager.average_rating()
            if avg_rating is not None:
                print(f"Average Satisfaction Rating: {avg_rating}")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
