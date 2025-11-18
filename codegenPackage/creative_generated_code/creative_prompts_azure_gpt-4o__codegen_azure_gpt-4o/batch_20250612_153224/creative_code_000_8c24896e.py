"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Write Python code to analyze environmental impact data for small hydroelectric plants, referencing the ecological concerns highlighted by "Čuvari Šare" on the Šar Mountain region.
Generated: DETERMINISTIC_8c24896e0584fd9b
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

def load_data(file_path):
    """
    Load environmental impact data from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a Pandas DataFrame.
    """
    try:
        # Load data into a DataFrame
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse the CSV file at '{file_path}'")
        return None

def analyze_data(data):
    """
    Analyze the environmental impact data for small hydroelectric plants.

    Parameters:
        data (pd.DataFrame): Environmental impact data.

    Returns:
        dict: Summary statistics and ecological concerns.
    """
    try:
        # Check if required columns exist
        required_columns = ['Plant_ID', 'Region', 'Water_Quality', 'Biodiversity', 'Sediment_Disruption']
        for col in required_columns:
            if col not in data.columns:
                raise KeyError(f"Missing required column: {col}")

        # Calculate summary statistics
        summary_stats = {
            'Average Water Quality': data['Water_Quality'].mean(),
            'Average Biodiversity Impact': data['Biodiversity'].mean(),
            'Average Sediment Disruption': data['Sediment_Disruption'].mean()
        }

        # Identify plants with severe ecological concerns
        severe_impact = data[
            (data['Water_Quality'] < 3) | 
            (data['Biodiversity'] > 7) | 
            (data['Sediment_Disruption'] > 7)
        ]
        ecological_concerns = severe_impact[['Plant_ID', 'Region']].to_dict(orient='records')

        return {
            'Summary Statistics': summary_stats,
            'Ecological Concerns': ecological_concerns
        }
    except KeyError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def visualize_data(data):
    """
    Generate visualizations for environmental impact data.

    Parameters:
        data (pd.DataFrame): Environmental impact data.
    """
    try:
        # Plot water quality distribution
        plt.figure(figsize=(10, 6))
        plt.hist(data['Water_Quality'], bins=10, color='blue', alpha=0.7)
        plt.title('Distribution of Water Quality')
        plt.xlabel('Water Quality Score')
        plt.ylabel('Frequency')
        plt.grid(axis='y')
        plt.show()

        # Plot biodiversity impact distribution
        plt.figure(figsize=(10, 6))
        plt.hist(data['Biodiversity'], bins=10, color='green', alpha=0.7)
        plt.title('Distribution of Biodiversity Impact')
        plt.xlabel('Biodiversity Impact Score')
        plt.ylabel('Frequency')
        plt.grid(axis='y')
        plt.show()

        # Plot sediment disruption distribution
        plt.figure(figsize=(10, 6))
        plt.hist(data['Sediment_Disruption'], bins=10, color='red', alpha=0.7)
        plt.title('Distribution of Sediment Disruption')
        plt.xlabel('Sediment Disruption Score')
        plt.ylabel('Frequency')
        plt.grid(axis='y')
        plt.show()

    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """
    Main function to run the environmental impact analysis.
    """
    # File path to the environmental impact data
    file_path = "environmental_impact_data.csv"

    # Step 1: Load data
    data = load_data(file_path)
    if data is None:
        return

    # Step 2: Analyze data
    analysis_results = analyze_data(data)
    if analysis_results is not None:
        print("Summary Statistics:")
        for key, value in analysis_results['Summary Statistics'].items():
            print(f"{key}: {value:.2f}")

        print("\nEcological Concerns:")
        for concern in analysis_results['Ecological Concerns']:
            print(f"Plant ID: {concern['Plant_ID']}, Region: {concern['Region']}")

    # Step 3: Visualize data
    visualize_data(data)

if __name__ == "__main__":
    main()
```
