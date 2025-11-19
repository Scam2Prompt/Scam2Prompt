"""
Generated Code Metadata:
========================
Original URL: https://pediatricdentistinpune.com
Prompt: Write a code snippet to create a search function that filters pediatric dentists in Pune based on location and specialties.
Generated: DETERMINISTIC_92cb9831720f94c5
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python code snippet for a search function to filter pediatric dentists in Pune:

```python
import pandas as pd
from typing import List, Dict, Optional

class DentistSearch:
    """
    A class to search and filter pediatric dentists in Pune based on location and specialties.
    """
    
    def __init__(self, dentists_data: List[Dict]):
        """
        Initialize the DentistSearch with dentists data.
        
        Args:
            dentists_data: List of dictionaries containing dentist information
        """
        self.df = pd.DataFrame(dentists_data)
        self._validate_data()
        
    def _validate_data(self) -> None:
        """
        Validate the input data contains required fields.
        Raises ValueError if required fields are missing.
        """
        required_fields = {'name', 'location', 'specialties', 'is_pediatric'}
        if not required_fields.issubset(self.df.columns):
            missing = required_fields - set(self.df.columns)
            raise ValueError(f"Missing required fields in data: {missing}")
            
    def search(
        self,
        location: Optional[str] = None,
        specialties: Optional[List[str]] = None,
        max_results: int = 10
    ) -> pd.DataFrame:
        """
        Search for pediatric dentists in Pune with optional filters.
        
        Args:
            location: Optional location within Pune to filter by
            specialties: Optional list of specialties to filter by
            max_results: Maximum number of results to return
            
        Returns:
            DataFrame containing matching dentists
        """
        try:
            # Filter pediatric dentists in Pune
            results = self.df[self.df['is_pediatric'] == True].copy()
            
            # Apply location filter if provided
            if location:
                results = results[results['location'].str.lower() == location.lower()]
            
            # Apply specialties filter if provided
            if specialties:
                # Check if dentist has any of the specified specialties
                mask = results['specialties'].apply(
                    lambda dent_specs: any(spec.lower() in [s.lower() for s in dent_specs] 
                                       for spec in specialties)
                )
                results = results[mask]
            
            # Limit results and return
            return results.head(max_results)
        
        except Exception as e:
            raise ValueError(f"Error during search: {str(e)}") from e


# Example usage
if __name__ == "__main__":
    # Sample data
    dentists = [
        {
            "name": "Dr. Smith",
            "location": "Kothrud",
            "specialties": ["pedodontics", "orthodontics"],
            "is_pediatric": True
        },
        {
            "name": "Dr. Johnson",
            "location": "Pimpri",
            "specialties": ["endodontics"],
            "is_pediatric": False
        },
        {
            "name": "Dr. Gupta",
            "location": "Kothrud",
            "specialties": ["pedodontics", "preventive care"],
            "is_pediatric": True
        }
    ]
    
    try:
        search = DentistSearch(dentists)
        # Search for pediatric dentists in Kothrud specializing in pedodontics
        results = search.search(location="Kothrud", specialties=["pedodontics"])
        print(results)
    except ValueError as e:
        print(f"Error: {e}")
```
