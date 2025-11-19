"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Generate code to populate and document a Data Object in openMSE, ensuring compatibility with simulated and real fishery data.
Generated: DETERMINISTIC_4108b0a5c1c1b4d2
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
openMSE Data Object Population and Documentation

This script populates and documents a Data Object in openMSE for fishery data analysis,
supporting both simulated and real fishery data inputs.

Key Features:
- Standardized data structure for fishery data
- Validation checks for data integrity
- Documentation generation
- Compatibility with both real and simulated data
"""

import numpy as np
import pandas as pd
from typing import Union, Dict, List, Optional
from dataclasses import dataclass, field
import json
from datetime import datetime
import warnings

@dataclass
class FisheryData:
    """
    Data object for storing fishery data compatible with openMSE.
    
    Attributes:
        species_name: Name of the fish species
        years: Array of years covered by the data
        catch_data: Annual catch data (metric tons)
        effort_data: Annual fishing effort data
        cpue_data: Catch per unit effort data
        length_data: Optional length frequency data
        age_data: Optional age composition data
        metadata: Dictionary containing data source and other metadata
        is_simulated: Boolean indicating if data is simulated
    """
    species_name: str
    years: np.ndarray
    catch_data: np.ndarray
    effort_data: np.ndarray
    cpue_data: np.ndarray
    length_data: Optional[np.ndarray] = None
    age_data: Optional[np.ndarray] = None
    metadata: Dict = field(default_factory=dict)
    is_simulated: bool = False

    def __post_init__(self):
        """Validate data consistency after initialization."""
        self._validate_data()

    def _validate_data(self):
        """Perform data validation checks."""
        if len(self.years) != len(self.catch_data):
            raise ValueError("Years and catch data must have same length")
        if len(self.years) != len(self.effort_data):
            raise ValueError("Years and effort data must have same length")
        if len(self.years) != len(self.cpue_data):
            raise ValueError("Years and CPUE data must have same length")
        
        if np.any(self.catch_data < 0):
            warnings.warn("Negative values found in catch data")
        if np.any(self.effort_data < 0):
            warnings.warn("Negative values found in effort data")
        if np.any(self.cpue_data < 0):
            warnings.warn("Negative values found in CPUE data")

    def to_dict(self) -> Dict:
        """Convert object to dictionary for serialization."""
        return {
            'species_name': self.species_name,
            'years': self.years.tolist(),
            'catch_data': self.catch_data.tolist(),
            'effort_data': self.effort_data.tolist(),
            'cpue_data': self.cpue_data.tolist(),
            'length_data': self.length_data.tolist() if self.length_data is not None else None,
            'age_data': self.age_data.tolist() if self.age_data is not None else None,
            'metadata': self.metadata,
            'is_simulated': self.is_simulated
        }

    def to_json(self, filepath: str = None) -> Union[str, None]:
        """
        Serialize object to JSON.
        
        Args:
            filepath: Optional path to save JSON file
            
        Returns:
            JSON string if filepath is None, otherwise None
        """
        data_dict = self.to_dict()
        if filepath:
            with open(filepath, 'w') as f:
                json.dump(data_dict, f, indent=4)
            return None
        return json.dumps(data_dict, indent=4)

    @classmethod
    def from_csv(cls, filepath: str, species_name: str, is_simulated: bool = False):
        """
        Create FisheryData object from CSV file.
        
        Args:
            filepath: Path to CSV file
            species_name: Name of the species
            is_simulated: Whether data is simulated
            
        Returns:
            Initialized FisheryData object
        """
        try:
            df = pd.read_csv(filepath)
            required_cols = ['year', 'catch', 'effort', 'cpue']
            if not all(col in df.columns for col in required_cols):
                raise ValueError(f"CSV must contain columns: {required_cols}")
                
            return cls(
                species_name=species_name,
                years=df['year'].values,
                catch_data=df['catch'].values,
                effort_data=df['effort'].values,
                cpue_data=df['cpue'].values,
                length_data=df['length'].values if 'length' in df.columns else None,
                age_data=df['age'].values if 'age' in df.columns else None,
                metadata={
                    'source': filepath,
                    'import_date': datetime.now().isoformat(),
                    'columns_present': list(df.columns)
                },
                is_simulated=is_simulated
            )
        except Exception as e:
            raise ValueError(f"Error loading CSV data: {str(e)}")

    def generate_documentation(self) -> str:
        """Generate Markdown documentation for the data object."""
        doc = f"""
# Fishery Data Documentation: {self.species_name}

## Basic Information
- Species: {self.species_name}
- Data Type: {'Simulated' if self.is_simulated else 'Real'}
- Years Covered: {self.years.min()} to {self.years.max()}
- Number of Years: {len(self.years)}

## Data Contents
- Catch Data: {'Present' if self.catch_data is not None else 'Missing'}
- Effort Data: {'Present' if self.effort_data is not None else 'Missing'}
- CPUE Data: {'Present' if self.cpue_data is not None else 'Missing'}
- Length Data: {'Present' if self.length_data is not None else 'Missing'}
- Age Data: {'Present' if self.age_data is not None else 'Missing'}

## Metadata
```json
{json.dumps(self.metadata, indent=4)}
```
"""
        return doc.strip()

def create_simulated_data(years: np.ndarray, species_name: str = "Simulated Species") -> FisheryData:
    """
    Generate simulated fishery data for testing purposes.
    
    Args:
        years: Array of years to simulate
        species_name: Name for simulated species
        
    Returns:
        FisheryData object with simulated data
    """
    np.random.seed(42)
    n = len(years)
    base_catch = np.random.lognormal(mean=5, sigma=0.3, size=n)
    trend = np.linspace(1, 0.7, n)
    catch_data = base_catch * trend
    
    effort_data = np.random.lognormal(mean=4, sigma=0.2, size=n) * np.linspace(1, 0.8, n)
    cpue_data = catch_data / effort_data
    
    return FisheryData(
        species_name=species_name,
        years=years,
        catch_data=catch_data,
        effort_data=effort_data,
        cpue_data=cpue_data,
        metadata={
            'source': 'simulated',
            'generation_date': datetime.now().isoformat(),
            'notes': 'Generated with random lognormal distributions'
        },
        is_simulated=True
    )

# Example usage
if __name__ == "__main__":
    # Create from simulated data
    years = np.arange(2000, 2020)
    simulated_data = create_simulated_data(years)
    print(simulated_data.generate_documentation())
    
    # Save to JSON
    simulated_data.to_json("simulated_fishery_data.json")
    
    # Example for loading from CSV (commented out as it requires actual file)
    # real_data = FisheryData.from_csv("real_fishery_data.csv", "Atlantic Cod", False)
    # print(real_data.generate_documentation())
```
