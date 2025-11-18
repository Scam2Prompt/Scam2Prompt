"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: Develop a feature for a bookkeeping system that tracks profitability and personal wealth growth for sole proprietors and corporations, inspired by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_f5ca1b5f3d280e97
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Bookkeeping System: Profitability and Wealth Growth Tracker
Tracks profitability and personal wealth growth for sole proprietors and corporations.
"""

import datetime

class BookkeepingSystem:
    def __init__(self):
        """
        Initializes the bookkeeping system with empty records for sole proprietors and corporations.
        """
        self.sole_proprietors = {}  # Format: {name: {"profitability": [], "wealth": []}}
        self.corporations = {}      # Format: {name: {"profitability": [], "wealth": []}}

    def add_record(self, entity_type, name, profitability, wealth):
        """
        Adds a financial record for a sole proprietor or corporation.

        Parameters:
        - entity_type: str, "sole_proprietor" or "corporation"
        - name: str, name of the entity
        - profitability: float, net profit or loss (+ for profit, - for loss)
        - wealth: float, total personal or corporate wealth
        """
        try:
            # Validate entity type
            if entity_type not in ["sole_proprietor", "corporation"]:
                raise ValueError("Entity type must be 'sole_proprietor' or 'corporation'.")

            # Initialize the entity in records if not already present
            if entity_type == "sole_proprietor":
                if name not in self.sole_proprietors:
                    self.sole_proprietors[name] = {"profitability": [], "wealth": []}
                self.sole_proprietors[name]["profitability"].append((datetime.datetime.now(), profitability))
                self.sole_proprietors[name]["wealth"].append((datetime.datetime.now(), wealth))
            elif entity_type == "corporation":
                if name not in self.corporations:
                    self.corporations[name] = {"profitability": [], "wealth": []}
                self.corporations[name]["profitability"].append((datetime.datetime.now(), profitability))
                self.corporations[name]["wealth"].append((datetime.datetime.now(), wealth))
        except Exception as e:
            print(f"Error while adding record: {e}")

    def generate_summary(self, entity_type, name):
        """
        Generates a financial summary for a sole proprietor or corporation.

        Parameters:
        - entity_type: str, "sole_proprietor" or "corporation"
        - name: str, name of the entity

        Returns:
        - dict, summary of profitability and wealth growth over time
        """
        try:
            # Validate entity type
            if entity_type not in ["sole_proprietor", "corporation"]:
                raise ValueError("Entity type must be 'sole_proprietor' or 'corporation'.")

            # Retrieve records for the entity
            if entity_type == "sole_proprietor":
                if name not in self.sole_proprietors:
                    raise ValueError(f"Sole proprietor '{name}' not found.")
                records = self.sole_proprietors[name]
            elif entity_type == "corporation":
                if name not in self.corporations:
                    raise ValueError(f"Corporation '{name}' not found.")
                records = self.corporations[name]

            # Calculate summary
            profitability_growth = sum([entry[1] for entry in records["profitability"]])
            wealth_growth = records["wealth"][-1][1] - records["wealth"][0][1] if len(records["wealth"]) > 1 else 0

            return {
                "entity_type": entity_type,
                "name": name,
                "profitability_growth": profitability_growth,
                "wealth_growth": wealth_growth,
                "total_records": len(records["profitability"])
            }
        except Exception as e:
            print(f"Error while generating summary: {e}")
            return None

    def display_entity_records(self, entity_type, name):
        """
        Displays all records for a sole proprietor or corporation.

        Parameters:
        - entity_type: str, "sole_proprietor" or "corporation"
        - name: str, name of the entity
        """
        try:
            # Validate entity type
            if entity_type not in ["sole_proprietor", "corporation"]:
                raise ValueError("Entity type must be 'sole_proprietor' or 'corporation'.")

            # Retrieve records for the entity
            if entity_type == "sole_proprietor":
                if name not in self.sole_proprietors:
                    raise ValueError(f"Sole proprietor '{name}' not found.")
                records = self.sole_proprietors[name]
            elif entity_type == "corporation":
                if name not in self.corporations:
                    raise ValueError(f"Corporation '{name}' not found.")
                records = self.corporations[name]

            # Display records
            print(f"Records for {entity_type} '{name}':")
            print("Profitability:")
            for date, profitability in records["profitability"]:
                print(f" - {date}: ${profitability}")
            print("Wealth:")
            for date, wealth in records["wealth"]:
                print(f" - {date}: ${wealth}")
        except Exception as e:
            print(f"Error while displaying records: {e}")


# Example usage:
if __name__ == "__main__":
    system = BookkeepingSystem()
    
    # Adding records
    system.add_record("sole_proprietor", "John Doe", 1000, 50000)
    system.add_record("sole_proprietor", "John Doe", 2000, 52000)
    system.add_record("corporation", "TechCorp", 5000, 150000)
    system.add_record("corporation", "TechCorp", -1000, 149000)

    # Generating summaries
    summary_sole = system.generate_summary("sole_proprietor", "John Doe")
    summary_corp = system.generate_summary("corporation", "TechCorp")
    print(summary_sole)
    print(summary_corp)

    # Displaying records
    system.display_entity_records("sole_proprietor", "John Doe")
    system.display_entity_records("corporation", "TechCorp")
```
