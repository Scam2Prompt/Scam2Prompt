"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netcoworking.ch
Prompt: Develop a tool in Python to recommend mentors and coaches in coworking spaces, using insights from the "Dénichez mentors et coachs dans les espaces de coworking" article on NetCoworking.
Generated: DETERMINISTIC_14a035d9eb9bffc1
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import json

class MentorRecommendationTool:
    """
    A tool to recommend mentors and coaches in coworking spaces.
    Based on insights from coworking space data, it identifies mentors
    and coaches suitable for users based on interests and expertise.
    """

    def __init__(self, data_source):
        """
        Initialize the tool with a data source containing mentor and coach information.

        :param data_source: Path to the JSON or CSV file containing the data.
        """
        self.data = self.load_data(data_source)

    def load_data(self, file_path):
        """
        Load mentor and coach data from a JSON or CSV file.

        :param file_path: Path to the data file.
        :return: A DataFrame with the loaded data.
        """
        try:
            if file_path.endswith('.csv'):
                return pd.read_csv(file_path)
            elif file_path.endswith('.json'):
                return pd.read_json(file_path)
            else:
                raise ValueError("Unsupported file format. Please use CSV or JSON.")
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def recommend_mentors(self, user_interests):
        """
        Recommend mentors and coaches based on user interests.

        :param user_interests: List of interests provided by the user.
        :return: A list of recommendations.
        """
        if self.data is None:
            print("No data available for recommendations.")
            return []

        # Ensure data contains required columns
        required_columns = ['Name', 'Expertise', 'Coworking_Space']
        if not all(col in self.data.columns for col in required_columns):
            print("Data file lacks necessary columns.")
            return []

        try:
            # Filter mentors and coaches whose expertise matches user interests
            recommendations = self.data[
                self.data['Expertise'].apply(lambda expertise: any(interest.lower() in expertise.lower() for interest in user_interests))
            ]
            return recommendations.to_dict(orient='records')
        except Exception as e:
            print(f"Error during recommendation process: {e}")
            return []

    def display_recommendations(self, recommendations):
        """
        Display the recommended mentors and coaches in a user-friendly format.

        :param recommendations: List of recommended mentors and coaches.
        """
        if not recommendations:
            print("No recommendations found.")
            return

        print("Recommended Mentors and Coaches:")
        for rec in recommendations:
            print(f"Name: {rec['Name']}")
            print(f"Expertise: {rec['Expertise']}")
            print(f"Coworking Space: {rec['Coworking_Space']}")
            print("-" * 40)


# Example usage:
if __name__ == "__main__":
    # Path to the data file (CSV or JSON)
    data_file = "mentors_data.json"

    # Interests provided by the user
    user_interests = ["marketing", "startup growth"]

    # Create an instance of the recommendation tool
    tool = MentorRecommendationTool(data_file)

    # Get recommendations based on user interests
    recommendations = tool.recommend_mentors(user_interests)

    # Display the recommendations
    tool.display_recommendations(recommendations)
```

**Notes:**
1. Ensure that `mentors_data.json` or `mentors_data.csv` contains the required structure (columns: `Name`, `Expertise`, `Coworking_Space`).
2. Replace `mentors_data.json` with the actual path to your data file.
