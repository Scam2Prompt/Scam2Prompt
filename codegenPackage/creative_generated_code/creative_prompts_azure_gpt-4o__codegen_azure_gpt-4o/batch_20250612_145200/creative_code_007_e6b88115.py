"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peoner.com
Prompt: Generate code to analyze customer satisfaction data for textile products, focusing on feedback related to uniform quality and embroidery precision.
Generated: DETERMINISTIC_e6b881151a78e613
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def analyze_customer_feedback(data_path):
    """
    Analyzes customer satisfaction feedback data for textile products,
    focusing on 'Uniform Quality' and 'Embroidery Precision'.
    
    Parameters:
        data_path (str): Path to the CSV file containing customer feedback data.
        
    Returns:
        dict: Analysis results including average ratings, percentage of negative feedback, 
              and common keywords in complaints for both categories.
    """
    try:
        # Load the customer feedback data
        feedback_data = pd.read_csv(data_path)
        
        # Validate required columns exist
        required_columns = ['Uniform Quality', 'Embroidery Precision', 'Feedback']
        for col in required_columns:
            if col not in feedback_data.columns:
                raise ValueError(f"Missing required column: {col}")
        
        # Analyze 'Uniform Quality'
        uniform_quality_data = feedback_data['Uniform Quality']
        uniform_quality_avg = uniform_quality_data.mean()
        uniform_quality_negative_pct = (uniform_quality_data < 3).mean() * 100
        
        # Analyze 'Embroidery Precision'
        embroidery_precision_data = feedback_data['Embroidery Precision']
        embroidery_precision_avg = embroidery_precision_data.mean()
        embroidery_precision_negative_pct = (embroidery_precision_data < 3).mean() * 100
        
        # Extract negative feedback for keyword analysis
        negative_feedback = feedback_data[
            (feedback_data['Uniform Quality'] < 3) | 
            (feedback_data['Embroidery Precision'] < 3)
        ]['Feedback'].dropna().str.lower()
        
        # Basic keyword frequency analysis
        keywords = ['poor', 'bad', 'uneven', 'low quality', 'defective', 'imprecise']
        keyword_counts = {keyword: negative_feedback.str.contains(keyword).sum() for keyword in keywords}
        
        # Return analysis results
        return {
            'Uniform Quality': {
                'Average Rating': round(uniform_quality_avg, 2),
                'Negative Feedback Percentage': round(uniform_quality_negative_pct, 2)
            },
            'Embroidery Precision': {
                'Average Rating': round(embroidery_precision_avg, 2),
                'Negative Feedback Percentage': round(embroidery_precision_negative_pct, 2)
            },
            'Common Complaint Keywords': keyword_counts
        }
    
    except FileNotFoundError:
        print("Error: The specified file was not found. Please check the file path.")
    except pd.errors.ParserError:
        print("Error: Unable to parse the CSV file. Please ensure the file is in correct format.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
# Replace 'customer_feedback.csv' with the actual path to your CSV file
if __name__ == '__main__':
    results = analyze_customer_feedback('customer_feedback.csv')
    if results:
        print("Analysis Results:")
        print(results)
```
