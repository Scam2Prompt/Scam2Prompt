"""
Generated Code Metadata:
========================
Original URL: https://molinahealthcareinc.com
Prompt: Create a clinical practice guideline database using a library like pandas in Python, inspired by MHC Inc's approach to patient care.
Generated: DETERMINISTIC_af4edf1fafefe01a
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class ClinicalPracticeGuidelineDB:
    """
    A class to manage a clinical practice guideline database using pandas.
    """

    def __init__(self):
        """
        Initializes the ClinicalPracticeGuidelineDB with an empty DataFrame.
        """
        self.guidelines = pd.DataFrame(columns=['ID', 'Title', 'Description', 'Date', 'Category'])

    def add_guideline(self, guideline_id, title, description, date, category):
        """
        Adds a new clinical practice guideline to the database.

        Parameters:
        guideline_id (int): Unique identifier for the guideline.
        title (str): Title of the guideline.
        description (str): Description of the guideline.
        date (str): Date of publication in 'YYYY-MM-DD' format.
        category (str): Category of the guideline.
        """
        try:
            new_guideline = {
                'ID': guideline_id,
                'Title': title,
                'Description': description,
                'Date': pd.to_datetime(date),
                'Category': category
            }
            self.guidelines = self.guidelines.append(new_guideline, ignore_index=True)
            print(f"Guideline '{title}' added successfully.")
        except Exception as e:
            print(f"Error adding guideline: {e}")

    def get_guideline(self, guideline_id):
        """
        Retrieves a guideline by its ID.

        Parameters:
        guideline_id (int): Unique identifier for the guideline.

        Returns:
        dict: The guideline details if found, else None.
        """
        try:
            guideline = self.guidelines[self.guidelines['ID'] == guideline_id]
            if not guideline.empty:
                return guideline.to_dict(orient='records')[0]
            else:
                print(f"No guideline found with ID: {guideline_id}")
                return None
        except Exception as e:
            print(f"Error retrieving guideline: {e}")
            return None

    def update_guideline(self, guideline_id, title=None, description=None, date=None, category=None):
        """
        Updates an existing clinical practice guideline.

        Parameters:
        guideline_id (int): Unique identifier for the guideline.
        title (str): New title of the guideline (optional).
        description (str): New description of the guideline (optional).
        date (str): New date of publication in 'YYYY-MM-DD' format (optional).
        category (str): New category of the guideline (optional).
        """
        try:
            index = self.guidelines[self.guidelines['ID'] == guideline_id].index
            if not index.empty:
                if title:
                    self.guidelines.at[index[0], 'Title'] = title
                if description:
                    self.guidelines.at[index[0], 'Description'] = description
                if date:
                    self.guidelines.at[index[0], 'Date'] = pd.to_datetime(date)
                if category:
                    self.guidelines.at[index[0], 'Category'] = category
                print(f"Guideline with ID {guideline_id} updated successfully.")
            else:
                print(f"No guideline found with ID: {guideline_id}")
        except Exception as e:
            print(f"Error updating guideline: {e}")

    def delete_guideline(self, guideline_id):
        """
        Deletes a guideline from the database.

        Parameters:
        guideline_id (int): Unique identifier for the guideline.
        """
        try:
            index = self.guidelines[self.guidelines['ID'] == guideline_id].index
            if not index.empty:
                self.guidelines = self.guidelines.drop(index)
                print(f"Guideline with ID {guideline_id} deleted successfully.")
            else:
                print(f"No guideline found with ID: {guideline_id}")
        except Exception as e:
            print(f"Error deleting guideline: {e}")

    def list_guidelines(self):
        """
        Lists all clinical practice guidelines in the database.

        Returns:
        DataFrame: A DataFrame containing all guidelines.
        """
        return self.guidelines

# Example usage
if __name__ == "__main__":
    db = ClinicalPracticeGuidelineDB()
    db.add_guideline(1, "Hypertension Management", "Guideline for managing hypertension.", "2023-01-15", "Cardiology")
    db.add_guideline(2, "Diabetes Care", "Guideline for diabetes management.", "2023-02-20", "Endocrinology")
    
    print(db.list_guidelines())
    print(db.get_guideline(1))
    db.update_guideline(1, description="Updated guideline for managing hypertension.")
    db.delete_guideline(2)
    print(db.list_guidelines())
```
