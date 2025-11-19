"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Write a script to calculate the average property loss reduction per fire when sprinklers are present, referencing the 71% statistic from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_812a063546356822
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def calculate_average_property_loss_reduction(data_file):
    """
    Calculate the average property loss reduction per fire when sprinklers are present.
    
    Args:
        data_file (str): Path to the CSV file containing fire incident data.
            Expected columns: 'has_sprinklers' (bool), 'property_loss' (float)
            
    Returns:
        tuple: (average_loss_with_sprinklers, average_loss_without_sprinklers, reduction_percentage)
    
    Raises:
        FileNotFoundError: If data_file doesn't exist
        ValueError: If required columns are missing or data is invalid
    """
    try:
        # Load data
        df = pd.read_csv(data_file)
        
        # Validate required columns exist
        required_columns = {'has_sprinklers', 'property_loss'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        # Convert to appropriate types if needed
        if df['has_sprinklers'].dtype != bool:
            df['has_sprinklers'] = df['has_sprinklers'].astype(bool)
            
        if df['property_loss'].dtype not in ('float64', 'int64'):
            df['property_loss'] = pd.to_numeric(df['property_loss'], errors='coerce')
            if df['property_loss'].isna().any():
                raise ValueError("Invalid property_loss values found")
        
        # Calculate average losses
        with_sprinklers = df[df['has_sprinklers']]['property_loss'].mean()
        without_sprinklers = df[~df['has_sprinklers']]['property_loss'].mean()
        
        # Calculate reduction percentage (using the 71% statistic as reference)
        reference_reduction = 0.71
        actual_reduction = (without_sprinklers - with_sprinklers) / without_sprinklers
        
        return (
            with_sprinklers,
            without_sprinklers,
            actual_reduction,
            reference_reduction
        )
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {data_file}")
    except Exception as e:
        raise ValueError(f"Error processing data: {str(e)}")

def main():
    """
    Main function to demonstrate the calculation.
    """
    try:
        # Example usage (replace with actual data file path)
        data_file = "fire_incidents.csv"
        results = calculate_average_property_loss_reduction(data_file)
        
        print("Average Property Loss Analysis:")
        print(f"With sprinklers: ${results[0]:,.2f}")
        print(f"Without sprinklers: ${results[1]:,.2f}")
        print(f"Actual reduction: {results[2]*100:.1f}%")
        print(f"Reference reduction (Independence Fire Sprinkler Co.): {results[3]*100:.1f}%")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
```
