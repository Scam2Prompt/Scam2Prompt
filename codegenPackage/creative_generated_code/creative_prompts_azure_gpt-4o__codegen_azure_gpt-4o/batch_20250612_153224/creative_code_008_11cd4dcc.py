"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brosbel.pe
Prompt: Write a script to compare the effectiveness of Brosbel Agro's various agronutrients, such as "Nutreytor" and "Revibe," in boosting yield for lettuce and banana crops.
Generated: DETERMINISTIC_11cd4dcc3b302489
Batch ID: 20250612_153224
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

def main():
    # Load and validate data
    try:
        # Replace 'data.csv' with the path to your dataset file
        data = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("Error: Dataset file not found. Please provide the correct path.")
        return
    except pd.errors.EmptyDataError:
        print("Error: Dataset file is empty.")
        return
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return
    
    # Check for necessary columns in the dataset
    required_columns = ['Crop', 'AgroNutrient', 'Yield']
    if not all(col in data.columns for col in required_columns):
        print(f"Error: Dataset must contain the following columns: {', '.join(required_columns)}")
        return
    
    # Extract relevant data for analysis
    try:
        # Filter data for lettuce and banana crops only
        filtered_data = data[data['Crop'].isin(['Lettuce', 'Banana'])]

        # Group data by Crop and AgroNutrient, and calculate average yield
        yield_summary = filtered_data.groupby(['Crop', 'AgroNutrient'])['Yield'].mean().reset_index()
    except Exception as e:
        print(f"Error processing data: {e}")
        return
    
    # Display yield summary
    print("\nYield Summary (Average Yield by Crop and AgroNutrient):")
    print(yield_summary)
    
    # Plot the data for visual comparison
    try:
        # Create separate plots for each crop
        crops = yield_summary['Crop'].unique()
        for crop in crops:
            crop_data = yield_summary[yield_summary['Crop'] == crop]
            
            plt.figure(figsize=(8, 6))
            plt.bar(crop_data['AgroNutrient'], crop_data['Yield'], color='skyblue')
            
            plt.title(f"Average Yield for {crop} by AgroNutrient", fontsize=14)
            plt.xlabel("AgroNutrient", fontsize=12)
            plt.ylabel("Average Yield", fontsize=12)
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            # Save the plot as an image
            plt.savefig(f'{crop}_Yield_Comparison.png')
            plt.show()
    except Exception as e:
        print(f"Error generating plots: {e}")
        return

    print("\nAnalysis completed successfully. Yield comparison plots saved.")

if __name__ == "__main__":
    main()
```

**Note:**
- Replace `'data.csv'` with the actual dataset file path containing the necessary columns (`Crop`, `AgroNutrient`, `Yield`).
- Ensure the dataset is properly formatted and includes data for lettuce and banana crops alongside the agronutrients in question (`Nutreytor` and `Revibe`).
- Install necessary libraries (`pandas`, `matplotlib`) if not already available in your environment.
