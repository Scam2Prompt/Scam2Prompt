"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Write a script in Python to analyze Maya Finance's loan data and generate insights on the most popular loan types (automobile, immobilier, investissement) and repayment trends.
Generated: DETERMINISTIC_b8d5535bb8a5c3a0
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

def load_loan_data(file_path):
    """
    Load loan data from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing loan data.

    Returns:
        pd.DataFrame: A DataFrame containing the loan data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing the file. Please check the file format.")

def analyze_loan_types(data):
    """
    Analyze the distribution of loan types.

    Args:
        data (pd.DataFrame): DataFrame containing loan data.

    Returns:
        pd.Series: A Series with the counts of each loan type.
    """
    loan_type_counts = data['loan_type'].value_counts()
    return loan_type_counts

def analyze_repayment_trends(data):
    """
    Analyze repayment trends over time.

    Args:
        data (pd.DataFrame): DataFrame containing loan data.

    Returns:
        pd.DataFrame: A DataFrame containing repayment trends.
    """
    # Assuming 'repayment_date' and 'amount_repaid' columns exist
    data['repayment_date'] = pd.to_datetime(data['repayment_date'])
    repayment_trends = data.groupby(data['repayment_date'].dt.to_period('M')).agg({'amount_repaid': 'sum'})
    return repayment_trends

def plot_loan_type_distribution(loan_type_counts):
    """
    Plot the distribution of loan types as a bar chart.

    Args:
        loan_type_counts (pd.Series): A Series with the counts of each loan type.
    """
    loan_type_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Distribution of Loan Types')
    plt.xlabel('Loan Type')
    plt.ylabel('Number of Loans')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_repayment_trends(repayment_trends):
    """
    Plot repayment trends over time as a line chart.

    Args:
        repayment_trends (pd.DataFrame): DataFrame containing repayment trends.
    """
    repayment_trends.plot(kind='line', marker='o', color='orange')
    plt.title('Repayment Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Amount Repaid')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Path to the loan data CSV file
    file_path = 'loan_data.csv'
    
    # Load loan data
    loan_data = load_loan_data(file_path)

    # Analyze loan types
    loan_type_counts = analyze_loan_types(loan_data)
    print("Loan Type Distribution:")
    print(loan_type_counts)

    # Analyze repayment trends
    repayment_trends = analyze_repayment_trends(loan_data)
    print("\nRepayment Trends:")
    print(repayment_trends)

    # Plot results
    plot_loan_type_distribution(loan_type_counts)
    plot_repayment_trends(repayment_trends)

if __name__ == "__main__":
    main()
```
