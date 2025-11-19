"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: What are the steps to condition an operating model with data in openMSE, and how does it differ for data-moderate conditions?
Generated: DETERMINISTIC_a8df15a363e00028
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openmse
import pandas as pd
import numpy as np
from typing import Dict, Union, Optional

class OperatingModelConditioner:
    """
    A class to condition operating models in openMSE with different data scenarios.
    """
    
    def __init__(self, om: openmse.OperatingModel):
        """
        Initialize the conditioner with an openMSE operating model.
        
        Args:
            om: An openMSE OperatingModel instance
        """
        self.om = om
        self._validate_om()
        
    def _validate_om(self) -> None:
        """Validate the operating model meets minimum requirements."""
        if not isinstance(self.om, openmse.OperatingModel):
            raise ValueError("Input must be an openMSE OperatingModel instance")
            
    def condition_with_data(
        self,
        data: Dict[str, Union[pd.DataFrame, np.ndarray]],
        data_type: str = "data-rich",
        **kwargs
    ) -> openmse.OperatingModel:
        """
        Condition the operating model with provided data.
        
        Args:
            data: Dictionary containing data components
            data_type: Type of data scenario ("data-rich" or "data-moderate")
            **kwargs: Additional parameters for specific conditioning
            
        Returns:
            Conditioned operating model
        """
        try:
            if data_type == "data-rich":
                return self._condition_data_rich(data, **kwargs)
            elif data_type == "data-moderate":
                return self._condition_data_moderate(data, **kwargs)
            else:
                raise ValueError("Invalid data_type. Must be 'data-rich' or 'data-moderate'")
        except Exception as e:
            raise RuntimeError(f"Error conditioning operating model: {str(e)}")
    
    def _condition_data_rich(
        self,
        data: Dict[str, Union[pd.DataFrame, np.ndarray]],
        **kwargs
    ) -> openmse.OperatingModel:
        """
        Condition operating model with data-rich scenario.
        
        Args:
            data: Dictionary containing all required data components
            **kwargs: Additional parameters for data-rich conditioning
            
        Returns:
            Conditioned operating model
        """
        # Data-rich conditioning steps
        self.om.set_catch_data(data['catch'])
        self.om.set_index_data(data['index'])
        self.om.set_length_data(data['length'])
        self.om.set_age_data(data['age'])
        
        # Additional data-rich specific conditioning
        if 'environmental' in data:
            self.om.set_environmental_data(data['environmental'])
            
        return self.om
    
    def _condition_data_moderate(
        self,
        data: Dict[str, Union[pd.DataFrame, np.ndarray]],
        **kwargs
    ) -> openmse.OperatingModel:
        """
        Condition operating model with data-moderate scenario.
        
        Args:
            data: Dictionary containing available data components
            **kwargs: Additional parameters for data-moderate conditioning
            
        Returns:
            Conditioned operating model
        """
        # Data-moderate conditioning steps (with fewer data requirements)
        required_data = ['catch', 'index']
        for key in required_data:
            if key not in data:
                raise ValueError(f"Missing required data for data-moderate: {key}")
                
        self.om.set_catch_data(data['catch'])
        self.om.set_index_data(data['index'])
        
        # Optional data components
        if 'length' in data:
            self.om.set_length_data(data['length'])
            
        # Data-moderate specific adjustments
        self.om.adjust_for_data_limitations(
            catch_cv=kwargs.get('catch_cv', 0.2),
            index_cv=kwargs.get('index_cv', 0.3)
        )
        
        return self.om
    
    def save_conditioned_model(
        self,
        file_path: str,
        format: str = "json"
    ) -> None:
        """
        Save the conditioned operating model to file.
        
        Args:
            file_path: Path to save the model
            format: File format ("json" or "binary")
        """
        try:
            if format == "json":
                self.om.to_json(file_path)
            elif format == "binary":
                self.om.to_binary(file_path)
            else:
                raise ValueError("Invalid format. Must be 'json' or 'binary'")
        except Exception as e:
            raise RuntimeError(f"Error saving conditioned model: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize an operating model
    om = openmse.OperatingModel()
    
    # Create sample data
    data = {
        'catch': pd.DataFrame(...),
        'index': pd.DataFrame(...),
        'length': pd.DataFrame(...)
    }
    
    # Condition the model
    conditioner = OperatingModelConditioner(om)
    
    # Data-rich conditioning
    rich_om = conditioner.condition_with_data(data, data_type="data-rich")
    
    # Data-moderate conditioning
    moderate_om = conditioner.condition_with_data(
        data,
        data_type="data-moderate",
        catch_cv=0.25,
        index_cv=0.35
    )
    
    # Save the models
    rich_om.save_conditioned_model("rich_model.json")
    moderate_om.save_conditioned_model("moderate_model.json")
```
