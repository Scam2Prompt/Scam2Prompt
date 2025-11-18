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
import pandas as pd

class SupplierEvaluator:
    """
    A class to evaluate and select suppliers for a hardware store based on certified supplier lists.
    """

    def __init__(self, certified_suppliers_file: str):
        """
        Initializes the SupplierEvaluator with the certified suppliers list.

        :param certified_suppliers_file: Path to the CSV file containing certified suppliers.
        """
        self.certified_suppliers_file = certified_suppliers_file
        self.certified_suppliers = self.load_certified_suppliers()

    def load_certified_suppliers(self) -> pd.DataFrame:
        """
        Loads the certified suppliers from the specified CSV file.

        :return: A pandas DataFrame containing the certified suppliers.
        """
        try:
            suppliers_df = pd.read_csv(self.certified_suppliers_file)
            if suppliers_df.empty:
                raise ValueError("The certified suppliers list is empty.")
            return suppliers_df
        except FileNotFoundError:
            raise FileNotFoundError("The specified file was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the suppliers: {e}")

    def evaluate_suppliers(self, criteria: dict) -> pd.DataFrame:
        """
        Evaluates suppliers based on provided criteria.

        :param criteria: A dictionary containing evaluation criteria.
        :return: A DataFrame of suppliers who meet the criteria.
        """
        try:
            # Filter suppliers based on criteria
            filtered_suppliers = self.certified_suppliers
            for key, value in criteria.items():
                filtered_suppliers = filtered_suppliers[filtered_suppliers[key] >= value]
            return filtered_suppliers
        except KeyError as e:
            raise KeyError(f"Criteria key '{e}' not found in the certified suppliers data.")
        except Exception as e:
            raise Exception(f"An error occurred during supplier evaluation: {e}")

    def select_best_supplier(self, evaluated_suppliers: pd.DataFrame) -> pd.Series:
        """
        Selects the best supplier based on the highest score from the evaluated suppliers.

        :param evaluated_suppliers: DataFrame of evaluated suppliers.
        :return: The best supplier as a Series.
        """
        try:
            if evaluated_suppliers.empty:
                raise ValueError("No suppliers to select from.")
            best_supplier = evaluated_suppliers.loc[evaluated_suppliers['score'].idxmax()]
            return best_supplier
        except KeyError:
            raise KeyError("The evaluated suppliers data does not contain a 'score' column.")
        except Exception as e:
            raise Exception(f"An error occurred while selecting the best supplier: {e}")

    def run_evaluation_process(self, criteria: dict) -> pd.Series:
        """
        Runs the complete supplier evaluation and selection process.

        :param criteria: A dictionary containing evaluation criteria.
        :return: The best supplier as a Series.
        """
        evaluated_suppliers = self.evaluate_suppliers(criteria)
        best_supplier = self.select_best_supplier(evaluated_suppliers)
        return best_supplier


# Example usage of the SupplierEvaluator class
if __name__ == "__main__":
    # Path to the certified suppliers CSV file
    certified_suppliers_file = "certified_suppliers.csv"
    
    # Create an instance of the SupplierEvaluator
    evaluator = SupplierEvaluator(certified_suppliers_file)
    
    # Define evaluation criteria (example criteria: minimum score, etc.)
    evaluation_criteria = {
        'score': 80,  # Example criteria, adjust based on actual supplier attributes
    }
    
    try:
        # Run the evaluation process
        best_supplier = evaluator.run_evaluation_process(evaluation_criteria)
        print("Best Supplier Selected:")
        print(best_supplier)
    except Exception as e:
        print(f"Error: {e}")
```
