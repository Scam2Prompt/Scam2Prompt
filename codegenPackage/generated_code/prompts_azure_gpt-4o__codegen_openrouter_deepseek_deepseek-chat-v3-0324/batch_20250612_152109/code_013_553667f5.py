"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Write code to generate a comparison chart of Caja China models based on their dimensions, weight, and meat capacity, using data from Meat Master.
Generated: DETERMINISTIC_553667f5a6607906
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict

class CajaChinaModel:
    """Represents a Caja China model with its specifications."""
    
    def __init__(self, model_name: str, length: float, width: float, height: float, weight: float, meat_capacity: float):
        """
        Initialize a Caja China model with its specifications.
        
        Args:
            model_name (str): Name of the model
            length (float): Length in inches
            width (float): Width in inches
            height (float): Height in inches
            weight (float): Weight in pounds
            meat_capacity (float): Meat capacity in pounds
        """
        self.model_name = model_name
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.meat_capacity = meat_capacity
    
    def get_volume(self) -> float:
        """Calculate and return the volume in cubic inches."""
        return self.length * self.width * self.height

def load_meat_master_data() -> List[CajaChinaModel]:
    """
    Load Caja China models data from Meat Master (simulated).
    
    Returns:
        List[CajaChinaModel]: List of Caja China models with their specifications
    """
    # Simulated data - in a real scenario, this would come from an API or database
    return [
        CajaChinaModel("La Caja China Model #1", 30.5, 18.5, 15.75, 35, 70),
        CajaChinaModel("La Caja China Model #2", 37.5, 23.5, 16, 50, 100),
        CajaChinaModel("La Caja China Mini", 24, 16, 12, 25, 40),
        CajaChinaModel("La Caja China Pro", 42, 26, 18, 65, 150)
    ]

def create_comparison_dataframe(models: List[CajaChinaModel]) -> pd.DataFrame:
    """
    Create a pandas DataFrame for comparison of Caja China models.
    
    Args:
        models (List[CajaChinaModel]): List of Caja China models
        
    Returns:
        pd.DataFrame: DataFrame containing comparison data
    """
    data = []
    for model in models:
        data.append({
            'Model': model.model_name,
            'Length (in)': model.length,
            'Width (in)': model.width,
            'Height (in)': model.height,
            'Volume (cu in)': model.get_volume(),
            'Weight (lbs)': model.weight,
            'Meat Capacity (lbs)': model.meat_capacity
        })
    
    return pd.DataFrame(data)

def generate_comparison_chart(df: pd.DataFrame, output_file: str = None):
    """
    Generate a comparison chart of Caja China models.
    
    Args:
        df (pd.DataFrame): DataFrame containing comparison data
        output_file (str, optional): Path to save the chart. If None, displays the chart.
    """
    # Set up the figure and axes
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))
    fig.suptitle('Caja China Models Comparison', fontsize=16)
    
    # Plot 1: Dimensions comparison
    dimensions = df[['Model', 'Length (in)', 'Width (in)', 'Height (in)']]
    dimensions.set_index('Model').plot(kind='bar', ax=axes[0, 0], rot=45)
    axes[0, 0].set_title('Dimensions Comparison (inches)')
    axes[0, 0].set_ylabel('Inches')
    
    # Plot 2: Volume comparison
    df.set_index('Model')['Volume (cu in)'].plot(kind='bar', ax=axes[0, 1], rot=45, color='green')
    axes[0, 1].set_title('Volume Comparison (cubic inches)')
    axes[0, 1].set_ylabel('Cubic Inches')
    
    # Plot 3: Weight comparison
    df.set_index('Model')['Weight (lbs)'].plot(kind='bar', ax=axes[1, 0], rot=45, color='orange')
    axes[1, 0].set_title('Weight Comparison (pounds)')
    axes[1, 0].set_ylabel('Pounds')
    
    # Plot 4: Meat capacity comparison
    df.set_index('Model')['Meat Capacity (lbs)'].plot(kind='bar', ax=axes[1, 1], rot=45, color='red')
    axes[1, 1].set_title('Meat Capacity Comparison (pounds)')
    axes[1, 1].set_ylabel('Pounds')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save or display the chart
    if output_file:
        plt.savefig(output_file, bbox_inches='tight')
        plt.close()
    else:
        plt.show()

def main():
    """Main function to generate the comparison chart."""
    try:
        # Load data
        models = load_meat_master_data()
        
        # Create comparison DataFrame
        df = create_comparison_dataframe(models)
        
        # Print the comparison table
        print("Caja China Models Comparison Table:")
        print(df.to_string(index=False))
        print("\n")
        
        # Generate and display the comparison chart
        generate_comparison_chart(df)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
