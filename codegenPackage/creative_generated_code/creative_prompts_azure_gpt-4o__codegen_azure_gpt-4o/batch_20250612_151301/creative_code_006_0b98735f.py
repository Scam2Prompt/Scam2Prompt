"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Develop a Python script to analyze patient appointment data for a gastroenterology clinic, including metrics for exams like elastografia hepática and supercrescimento bacteriano.
Generated: DETERMINISTIC_0b98735fe75bc673
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd


# Define constants for metrics
EXAM_TYPES = ["elastografia hepática", "supercrescimento bacteriano"]


def load_data(file_path):
    """
    Load patient appointment data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing appointment data.
    
    Returns:
        pd.DataFrame: DataFrame with loaded data.
    """
    try:
        # Load data from CSV
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        exit(1)
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        exit(1)


def analyze_exams(data, exam_types):
    """
    Analyze the appointment data for specific exams.
    
    Args:
        data (pd.DataFrame): DataFrame containing appointment data.
        exam_types (list): List of exam types to analyze.
    
    Returns:
        dict: Dictionary containing metrics for each exam type.
    """
    metrics = {}
    
    for exam in exam_types:
        try:
            # Filter rows for the specific exam
            exam_data = data[data['exam_type'] == exam]
            
            # Calculate metrics
            total_appointments = len(exam_data)
            completed_appointments = len(exam_data[exam_data['status'] == 'completed'])
            canceled_appointments = len(exam_data[exam_data['status'] == 'canceled'])
            
            # Store metrics in dictionary
            metrics[exam] = {
                'total_appointments': total_appointments,
                'completed_appointments': completed_appointments,
                'canceled_appointments': canceled_appointments
            }
        except KeyError as e:
            print(f"Error: Missing expected column '{str(e)}' in data.")
            exit(1)
        except Exception as e:
            print(f"Error analyzing exam '{exam}': {str(e)}")
            exit(1)
    
    return metrics


def save_metrics(metrics, output_path):
    """
    Save metrics to a CSV file.
    
    Args:
        metrics (dict): Dictionary containing metrics for each exam type.
        output_path (str): Path to the output CSV file.
    """
    try:
        # Convert metrics dictionary to DataFrame
        metrics_df = pd.DataFrame.from_dict(metrics, orient='index')
        
        # Save DataFrame to CSV
        metrics_df.to_csv(output_path)
        print(f"Metrics successfully saved to '{output_path}'.")
    except Exception as e:
        print(f"Error saving metrics: {str(e)}")
        exit(1)


def main():
    """
    Main function to orchestrate the analysis of patient appointment data.
    """
    # Input file path
    input_file = "appointments.csv"  # Replace with your actual file path
    
    # Output file path
    output_file = "exam_metrics.csv"
    
    # Load appointment data
    data = load_data(input_file)
    
    # Analyze exam data
    metrics = analyze_exams(data, EXAM_TYPES)
    
    # Print metrics to console for review
    print("Exam Metrics:")
    for exam, values in metrics.items():
        print(f"{exam}: {values}")
    
    # Save metrics to CSV
    save_metrics(metrics, output_file)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
