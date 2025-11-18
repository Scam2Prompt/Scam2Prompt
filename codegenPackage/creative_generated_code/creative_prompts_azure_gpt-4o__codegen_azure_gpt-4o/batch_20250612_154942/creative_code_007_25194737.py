"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lucidmotorscae.rpdmnr.com
Prompt: Generate code to implement a custom machine learning pipeline in RapidMiner for use in the Altair AI Hub environment.
Generated: DETERMINISTIC_2519473731514362
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

RapidMiner uses a graphical interface for building pipelines, but Python scripts can be integrated for custom extensions. Below is an example of Python code that can be used in a RapidMiner Python operator to implement a custom machine learning pipeline. This script is designed to be production-ready and meets the outlined requirements.

```python
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.exceptions import NotFittedError

def rapidminer_entry_point():
    """
    Entry point for execution in RapidMiner's Python operator.
    Passes data from RapidMiner to this script, processes it, and returns results.
    """
    try:
        # Step 1: Load data from RapidMiner
        # RapidMiner passes input data as a pandas DataFrame
        input_data = rapidminer_in_data

        # Sanity check: Ensure the input data is not empty
        if input_data.empty:
            raise ValueError("The input data is empty. Please ensure data is passed correctly.")

        # Step 2: Preprocess the data
        # Assume the last column is the target variable
        target_column = input_data.columns[-1]
        X = input_data.drop(columns=[target_column])  # Features
        y = input_data[target_column]  # Target

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Step 3: Train a machine learning model
        # Use RandomForestClassifier for this example
        model = RandomForestClassifier(n_estimators=100, random_state=42)

        # Fit the model to the training data
        model.fit(X_train, y_train)

        # Step 4: Evaluate the model
        # Predict on the test set
        y_pred = model.predict(X_test)

        # Calculate accuracy and generate a classification report
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        # Step 5: Return results to RapidMiner
        # Return accuracy and classification report as output
        rapidminer_out_data = {
            "accuracy": accuracy,
            "classification_report": report,
        }

        return rapidminer_out_data

    except (ValueError, NotFittedError) as e:
        # Handle specific errors gracefully
        return {"error": str(e)}

    except Exception as e:
        # Catch all other exceptions and return a meaningful error message
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Call the entry point function
if __name__ == "__main__":
    result = rapidminer_entry_point()
    # Results will be passed back to the RapidMiner environment
```

### Notes:
- Replace `rapidminer_in_data` with the actual mechanism for passing data from RapidMiner into your Python script. Similarly, `rapidminer_out_data` should be structured to return data back to RapidMiner.
- This script assumes the use of RapidMiner's Python integration, where input and output are handled as pandas DataFrames.
- The code includes error handling for missing data and model training issues, ensuring robustness in production use.
