"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Create a script to model the influence of local media coverage on voter turnout in McHenry County, Illinois, using the examples provided by Fair Maps Illinois.
Generated: DETERMINISTIC_0c7e90aa7597a6e9
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Constants for the script
DATA_FILE = "mchenry_voter_turnout.csv"  # Replace with actual data file path
MEDIA_COVERAGE_FILE = "local_media_coverage.csv"  # Replace with actual data file path

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: File {file_path} is empty.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while loading the file: {str(e)}")
        exit(1)

def preprocess_data(voter_data, media_data):
    """
    Preprocess and merge voter turnout data with media coverage data.

    Args:
        voter_data (pd.DataFrame): Voter turnout data.
        media_data (pd.DataFrame): Media coverage data.

    Returns:
        pd.DataFrame: Merged and preprocessed data.
    """
    try:
        # Ensure columns are aligned for merging
        voter_data = voter_data.rename(columns={"date": "Date", "turnout": "VoterTurnout"})
        media_data = media_data.rename(columns={"date": "Date", "coverage": "MediaCoverage"})

        # Convert 'Date' column to datetime for proper merging
        voter_data['Date'] = pd.to_datetime(voter_data['Date'])
        media_data['Date'] = pd.to_datetime(media_data['Date'])

        # Merge data on 'Date'
        merged_data = pd.merge(voter_data, media_data, on="Date")

        # Drop any rows with missing values
        merged_data = merged_data.dropna()
        return merged_data
    except KeyError as e:
        print(f"Error: Missing expected column - {str(e)}")
        exit(1)
    except Exception as e:
        print(f"An error occurred during preprocessing: {str(e)}")
        exit(1)

def model_voter_turnout(data):
    """
    Model voter turnout based on local media coverage using linear regression.

    Args:
        data (pd.DataFrame): Data containing voter turnout and media coverage.

    Returns:
        None
    """
    try:
        # Features and target variable
        X = data[['MediaCoverage']].values
        y = data['VoterTurnout'].values

        # Initialize and fit the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Predict voter turnout
        predictions = model.predict(X)

        # Compute model evaluation metrics
        mse = mean_squared_error(y, predictions)
        r2 = r2_score(y, predictions)

        # Display results
        print("Linear Regression Model")
        print("-----------------------")
        print(f"Coefficient (Media Coverage): {model.coef_[0]:.4f}")
        print(f"Intercept: {model.intercept_:.4f}")
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"R-Squared: {r2:.4f}")

        # Plot actual vs predicted turnout
        plt.figure(figsize=(10, 6))
        plt.scatter(X, y, color='blue', label='Actual Turnout')
        plt.plot(X, predictions, color='red', label='Predicted Turnout')
        plt.title('Voter Turnout vs Media Coverage')
        plt.xlabel('Media Coverage')
        plt.ylabel('Voter Turnout')
        plt.legend()
        plt.grid()
        plt.show()
    except Exception as e:
        print(f"An error occurred during modeling: {str(e)}")
        exit(1)

def main():
    """
    Main function to execute the script.
    """
    # Load voter turnout and media coverage data
    voter_data = load_data(DATA_FILE)
    media_data = load_data(MEDIA_COVERAGE_FILE)

    # Preprocess and merge data
    merged_data = preprocess_data(voter_data, media_data)

    # Model voter turnout based on media coverage
    model_voter_turnout(merged_data)

if __name__ == "__main__":
    main()
```
