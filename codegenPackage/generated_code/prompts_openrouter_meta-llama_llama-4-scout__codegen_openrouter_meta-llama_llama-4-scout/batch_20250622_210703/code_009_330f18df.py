"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Generate a report on the effectiveness of a community development program, such as "مهارات المستقبل" (Future Skills), using data from the organization's annual reports and surveys.
Generated: DETERMINISTIC_330f18df947da57e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Define a function to load data from annual reports and surveys
def load_data(annual_reports_file, surveys_file):
    """
    Load data from annual reports and surveys.

    Parameters:
    annual_reports_file (str): Path to the annual reports file.
    surveys_file (str): Path to the surveys file.

    Returns:
    tuple: A tuple containing two dataframes, one for annual reports and one for surveys.
    """
    try:
        # Load annual reports data
        annual_reports_df = pd.read_csv(annual_reports_file)
        
        # Load surveys data
        surveys_df = pd.read_csv(surveys_file)
        
        return annual_reports_df, surveys_df
    
    except FileNotFoundError:
        print("One or both of the files were not found.")
        return None, None
    except pd.errors.EmptyDataError:
        print("One or both of the files are empty.")
        return None, None
    except pd.errors.ParserError:
        print("Error parsing one or both of the files.")
        return None, None

# Define a function to merge and preprocess data
def preprocess_data(annual_reports_df, surveys_df):
    """
    Merge and preprocess data from annual reports and surveys.

    Parameters:
    annual_reports_df (pd.DataFrame): Dataframe containing annual reports data.
    surveys_df (pd.DataFrame): Dataframe containing surveys data.

    Returns:
    pd.DataFrame: A preprocessed dataframe.
    """
    try:
        # Merge dataframes on a common column (e.g., 'program_name')
        merged_df = pd.merge(annual_reports_df, surveys_df, on='program_name')
        
        # Handle missing values
        merged_df.fillna(merged_df.mean(), inplace=True)
        
        return merged_df
    
    except KeyError:
        print("The dataframes do not have a common column to merge on.")
        return None

# Define a function to analyze data and generate report
def generate_report(preprocessed_df):
    """
    Analyze data and generate a report on the effectiveness of the community development program.

    Parameters:
    preprocessed_df (pd.DataFrame): Preprocessed dataframe.

    Returns:
    dict: A dictionary containing the report's findings.
    """
    try:
        # Calculate key performance indicators (KPIs)
        kpi_participation_rate = preprocessed_df['participation_rate'].mean()
        kpi_satisfaction_rate = preprocessed_df['satisfaction_rate'].mean()
        
        # Perform linear regression to identify factors affecting program effectiveness
        X = preprocessed_df[['investment', 'resources']]
        y = preprocessed_df['effectiveness']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        
        model = LinearRegression()  
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        # Evaluate model performance
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        
        # Generate report
        report = {
            'kpi_participation_rate': kpi_participation_rate,
            'kpi_satisfaction_rate': kpi_satisfaction_rate,
            'factors_affecting_effectiveness': {
                'investment': model.coef_[0],
                'resources': model.coef_[1]
            },
            'model_performance': {
                'mae': mae,
                'rmse': rmse
            }
        }
        
        return report
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define a main function to execute the program
def main():
    annual_reports_file = 'annual_reports.csv'
    surveys_file = 'surveys.csv'
    
    annual_reports_df, surveys_df = load_data(annual_reports_file, surveys_file)
    
    if annual_reports_df is not None and surveys_df is not None:
        preprocessed_df = preprocess_data(annual_reports_df, surveys_df)
        
        if preprocessed_df is not None:
            report = generate_report(preprocessed_df)
            
            if report is not None:
                print("Report:")
                print(f"Participation Rate: {report['kpi_participation_rate']:.2f}")
                print(f"Satisfaction Rate: {report['kpi_satisfaction_rate']:.2f}")
                print("Factors Affecting Effectiveness:")
                print(f"Investment: {report['factors_affecting_effectiveness']['investment']:.2f}")
                print(f"Resources: {report['factors_affecting_effectiveness']['resources']:.2f}")
                print("Model Performance:")
                print(f"Mean Absolute Error (MAE): {report['model_performance']['mae']:.2f}")
                print(f"Root Mean Squared Error (RMSE): {report['model_performance']['rmse']:.2f}")

if __name__ == "__main__":
    main()
```
