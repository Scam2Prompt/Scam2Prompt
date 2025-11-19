"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: "Develop a code to assess the effectiveness of a leadership development program using Matter's expertise in talent development and evaluation."
Generated: DETERMINISTIC_60477062af0e0440
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leadership_development_program_evaluator.py

import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class LeadershipDevelopmentProgramEvaluator:
    """
    Evaluates the effectiveness of a leadership development program.

    Attributes:
    -----------
    participant_data : pandas.DataFrame
        Participant data, including demographics and program engagement metrics.
    pre_post_assessment_data : pandas.DataFrame
        Pre- and post-program assessment data for participants.

    Methods:
    --------
    load_participant_data(file_path)
        Loads participant data from a CSV file.
    load_pre_post_assessment_data(file_path)
        Loads pre- and post-program assessment data from a CSV file.
    calculate_program_effectiveness()
        Calculates the effectiveness of the leadership development program.
    """

    def __init__(self, participant_data_file, pre_post_assessment_data_file):
        """
        Initializes the LeadershipDevelopmentProgramEvaluator.

        Parameters:
        -----------
        participant_data_file : str
            File path to participant data CSV file.
        pre_post_assessment_data_file : str
            File path to pre- and post-program assessment data CSV file.
        """
        self.participant_data = self.load_participant_data(participant_data_file)
        self.pre_post_assessment_data = self.load_pre_post_assessment_data(pre_post_assessment_data_file)

    def load_participant_data(self, file_path):
        """
        Loads participant data from a CSV file.

        Parameters:
        -----------
        file_path : str
            File path to participant data CSV file.

        Returns:
        --------
        pandas.DataFrame
            Participant data.
        """
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except pd.errors.EmptyDataError:
            print(f"Error: File '{file_path}' is empty.")
            return None
        except pd.errors.ParserError:
            print(f"Error: Failed to parse file '{file_path}'.")
            return None

    def load_pre_post_assessment_data(self, file_path):
        """
        Loads pre- and post-program assessment data from a CSV file.

        Parameters:
        -----------
        file_path : str
            File path to pre- and post-program assessment data CSV file.

        Returns:
        --------
        pandas.DataFrame
            Pre- and post-program assessment data.
        """
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except pd.errors.EmptyDataError:
            print(f"Error: File '{file_path}' is empty.")
            return None
        except pd.errors.ParserError:
            print(f"Error: Failed to parse file '{file_path}'.")
            return None

    def calculate_program_effectiveness(self):
        """
        Calculates the effectiveness of the leadership development program.

        Returns:
        --------
        dict
            Program effectiveness metrics.
        """
        # Merge participant and assessment data
        merged_data = pd.merge(self.participant_data, self.pre_post_assessment_data, on='participant_id')

        # Define features (X) and target (y)
        X = merged_data[['program_engagement', 'demographics_age', 'demographics_experience']]
        y = merged_data['post_assessment_score']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train linear regression model
        model = LinearRegression()  
        model.fit(X_train, y_train)

        # Make predictions on test set
        y_pred = model.predict(X_test)

        # Evaluate model performance
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = mse ** 0.5

        # Return program effectiveness metrics
        return {
            'mean_absolute_error': mae,
            'mean_squared_error': mse,
            'root_mean_squared_error': rmse
        }

def main():
    evaluator = LeadershipDevelopmentProgramEvaluator('participant_data.csv', 'pre_post_assessment_data.csv')
    program_effectiveness = evaluator.calculate_program_effectiveness()
    print("Program Effectiveness Metrics:")
    for metric, value in program_effectiveness.items():
        print(f"{metric}: {value:.2f}")

if __name__ == "__main__":
    main()
```
