"""
Generated Code Metadata:
========================
Original URL: https://www.yehudit-taxes.co.il
Prompt: Generate code to compare initial and subsequent capital declarations for tax purposes, ensuring accuracy as emphasized by Yehudit Benedict's firm.
Generated: DETERMINISTIC_5ecf740d24b6b3fa
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
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class CapitalDeclarationComparator:
    """
    A class to compare initial and subsequent capital declarations for tax purposes.
    Ensures accuracy in tracking changes in declared capital over time.
    """
    
    def __init__(self):
        self.declarations = {}  # Stores all declarations by declaration_id
        self.initial_declarations = {}  # Stores initial declarations by taxpayer_id
    
    def add_declaration(self, declaration_id: str, taxpayer_id: str, declaration_date: str, 
                        capital_amount: float, is_initial: bool = False) -> None:
        """
        Add a capital declaration to the system.
        
        Args:
            declaration_id: Unique identifier for the declaration
            taxpayer_id: Taxpayer identifier
            declaration_date: Date of declaration (YYYY-MM-DD format)
            capital_amount: Declared capital amount
            is_initial: Whether this is the initial declaration
        """
        try:
            # Validate and parse the date
            parsed_date = datetime.strptime(declaration_date, "%Y-%m-%d").date()
            
            declaration = {
                'declaration_id': declaration_id,
                'taxpayer_id': taxpayer_id,
                'date': parsed_date,
                'amount': capital_amount,
                'is_initial': is_initial
            }
            
            # Store the declaration
            self.declarations[declaration_id] = declaration
            
            if is_initial:
                if taxpayer_id in self.initial_declarations:
                    raise ValueError(f"Initial declaration already exists for taxpayer {taxpayer_id}")
                self.initial_declarations[taxpayer_id] = declaration
            
        except ValueError as e:
            raise ValueError(f"Invalid declaration data: {str(e)}")
    
    def get_comparison(self, taxpayer_id: str) -> Dict[str, Optional[float]]:
        """
        Compare subsequent declarations against the initial declaration for a taxpayer.
        
        Args:
            taxpayer_id: Taxpayer identifier to compare declarations for
            
        Returns:
            Dictionary containing:
            - initial_amount: Initial declared capital
            - latest_amount: Latest declared capital
            - difference: Absolute difference between initial and latest
            - percentage_change: Percentage change from initial to latest
        """
        if taxpayer_id not in self.initial_declarations:
            raise ValueError(f"No initial declaration found for taxpayer {taxpayer_id}")
        
        initial_decl = self.initial_declarations[taxpayer_id]
        initial_amount = initial_decl['amount']
        
        # Get all declarations for this taxpayer, sorted by date
        taxpayer_decls = [
            decl for decl in self.declarations.values() 
            if decl['taxpayer_id'] == taxpayer_id and not decl['is_initial']
        ]
        taxpayer_decls.sort(key=lambda x: x['date'])
        
        if not taxpayer_decls:
            return {
                'initial_amount': initial_amount,
                'latest_amount': None,
                'difference': None,
                'percentage_change': None
            }
        
        latest_decl = taxpayer_decls[-1]
        latest_amount = latest_decl['amount']
        difference = latest_amount - initial_amount
        percentage_change = (difference / initial_amount) * 100 if initial_amount != 0 else float('inf')
        
        return {
            'initial_amount': initial_amount,
            'latest_amount': latest_amount,
            'difference': difference,
            'percentage_change': percentage_change
        }
    
    def get_all_comparisons(self) -> List[Dict[str, str]]:
        """
        Get comparison results for all taxpayers with initial declarations.
        
        Returns:
            List of comparison results for each taxpayer
        """
        results = []
        for taxpayer_id in self.initial_declarations:
            try:
                comparison = self.get_comparison(taxpayer_id)
                results.append({
                    'taxpayer_id': taxpayer_id,
                    **comparison
                })
            except Exception as e:
                print(f"Error processing taxpayer {taxpayer_id}: {str(e)}")
                continue
        return results
    
    def export_comparisons_to_csv(self, file_path: str) -> None:
        """
        Export all comparison results to a CSV file.
        
        Args:
            file_path: Path to save the CSV file
        """
        comparisons = self.get_all_comparisons()
        if not comparisons:
            print("No comparison data to export")
            return
        
        df = pd.DataFrame(comparisons)
        df.to_csv(file_path, index=False)
        print(f"Successfully exported comparisons to {file_path}")

# Example usage
if __name__ == "__main__":
    comparator = CapitalDeclarationComparator()
    
    # Add initial declarations
    comparator.add_declaration("dec1", "taxpayer1", "2023-01-01", 100000.0, is_initial=True)
    comparator.add_declaration("dec2", "taxpayer2", "2023-01-01", 50000.0, is_initial=True)
    
    # Add subsequent declarations
    comparator.add_declaration("dec3", "taxpayer1", "2023-06-01", 120000.0)
    comparator.add_declaration("dec4", "taxpayer2", "2023-06-01", 45000.0)
    comparator.add_declaration("dec5", "taxpayer1", "2023-12-01", 150000.0)
    
    # Get comparison for a specific taxpayer
    print(comparator.get_comparison("taxpayer1"))
    
    # Export all comparisons to CSV
    comparator.export_comparisons_to_csv("capital_comparisons.csv")
```
