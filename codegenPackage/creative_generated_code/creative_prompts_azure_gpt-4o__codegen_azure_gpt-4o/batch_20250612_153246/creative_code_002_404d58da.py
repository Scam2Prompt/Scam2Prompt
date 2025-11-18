"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Generate a step-by-step guide in code to automate supplier evaluation and selection for a hardware store, referencing the "Listas de Proveedores Certificados" section from Aula Ferretera.
Generated: DETERMINISTIC_404d58da991dac64
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Supplier Evaluation and Selection Automation Script
This script automates the evaluation and selection process for hardware store suppliers
using the data from the "Listas de Proveedores Certificados" section.
"""

import pandas as pd
import json

# Step 1: Load supplier data
def load_supplier_data(file_path: str):
    """
    Loads supplier data from the specified file path.
    Supports CSV and JSON formats.

    Args:
        file_path (str): Path to the supplier data file.

    Returns:
        pd.DataFrame: DataFrame containing supplier data.
    """
    try:
        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        elif file_path.endswith(".json"):
            return pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or JSON.")
    except Exception as e:
        print(f"Error loading supplier data: {e}")
        raise

# Step 2: Define evaluation criteria
def evaluate_supplier(supplier_row):
    """
    Evaluates a supplier based on predefined criteria.

    Args:
        supplier_row (pd.Series): A row from the supplier DataFrame.

    Returns:
        dict: Evaluation results for the supplier.
    """
    try:
        evaluation_results = {
            "SupplierID": supplier_row["SupplierID"],
            "Name": supplier_row["Name"],
            "QualityScore": supplier_row["QualityScore"],
            "DeliveryReliability": supplier_row["DeliveryReliability"],
            "PricingScore": supplier_row["PricingScore"],
            "TotalScore": (supplier_row["QualityScore"] * 0.4) +
                          (supplier_row["DeliveryReliability"] * 0.4) +
                          (supplier_row["PricingScore"] * 0.2),
            "Selected": False
        }
        return evaluation_results
    except KeyError as e:
        print(f"Missing required field in supplier data: {e}")
        raise
    except Exception as e:
        print(f"Error evaluating supplier: {e}")
        raise

# Step 3: Evaluate all suppliers
def evaluate_all_suppliers(supplier_data: pd.DataFrame):
    """
    Evaluate all suppliers in the DataFrame.

    Args:
        supplier_data (pd.DataFrame): DataFrame containing supplier data.

    Returns:
        pd.DataFrame: DataFrame with evaluation results.
    """
    try:
        evaluations = [evaluate_supplier(row) for _, row in supplier_data.iterrows()]
        return pd.DataFrame(evaluations)
    except Exception as e:
        print(f"Error evaluating all suppliers: {e}")
        raise

# Step 4: Select the best suppliers based on TotalScore
def select_best_suppliers(evaluations: pd.DataFrame, threshold: float):
    """
    Select suppliers whose TotalScore exceeds the given threshold.

    Args:
        evaluations (pd.DataFrame): DataFrame containing evaluation results.
        threshold (float): Minimum score for supplier selection.

    Returns:
        pd.DataFrame: DataFrame of selected suppliers.
    """
    try:
        evaluations["Selected"] = evaluations["TotalScore"] >= threshold
        return evaluations[evaluations["Selected"]]
    except Exception as e:
        print(f"Error selecting best suppliers: {e}")
        raise

# Step 5: Save the selected suppliers to a file
def save_selected_suppliers(selected_suppliers: pd.DataFrame, output_path: str):
    """
    Saves the selected suppliers to the specified file path.

    Args:
        selected_suppliers (pd.DataFrame): DataFrame of selected suppliers.
        output_path (str): Path to the output file.

    Raises:
        ValueError: If an unsupported file format is specified.
    """
    try:
        if output_path.endswith(".csv"):
            selected_suppliers.to_csv(output_path, index=False)
        elif output_path.endswith(".json"):
            selected_suppliers.to_json(output_path, orient="records")
        else:
            raise ValueError("Unsupported file format. Please use CSV or JSON.")
        print(f"Selected suppliers successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving selected suppliers: {e}")
        raise

# Main function to automate supplier evaluation and selection
def main():
    try:
        # File paths
        input_file = "supplier_data.csv"  # Replace with your input file path
        output_file = "selected_suppliers.csv"  # Replace with your output file path

        # Load supplier data
        supplier_data = load_supplier_data(input_file)

        # Evaluate suppliers
        evaluation_results = evaluate_all_suppliers(supplier_data)

        # Select best suppliers with threshold of 80 (replace with desired threshold)
        selected_suppliers = select_best_suppliers(evaluation_results, threshold=80)

        # Save the selected suppliers to file
        save_selected_suppliers(selected_suppliers, output_file)

    except Exception as e:
        print(f"Error in supplier evaluation and selection process: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
