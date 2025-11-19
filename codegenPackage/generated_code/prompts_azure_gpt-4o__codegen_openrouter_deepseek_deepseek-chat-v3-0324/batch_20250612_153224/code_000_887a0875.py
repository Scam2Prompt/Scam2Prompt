"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Write Python code to calculate excavation depth and bucket volume for Yanmar mini excavators, using specifications like those of the ViO12, ViO17, ViO25, ViO35, and SV100 models.
Generated: DETERMINISTIC_887a087590e7aa20
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class YanmarMiniExcavator:
    """
    A class to calculate excavation depth and bucket volume for Yanmar mini excavators.
    Supported models: ViO12, ViO17, ViO25, ViO35, SV100.
    """
    
    def __init__(self):
        # Model specifications: (max_depth (m), bucket_volume_range (m³))
        self.model_specs = {
            'ViO12': (2.5, (0.02, 0.05)),
            'ViO17': (2.8, (0.03, 0.07)),
            'ViO25': (3.2, (0.04, 0.10)),
            'ViO35': (3.8, (0.05, 0.15)),
            'SV100': (4.5, (0.08, 0.25))
        }
    
    def get_max_depth(self, model: str) -> float:
        """
        Get maximum excavation depth for a given model.
        
        Args:
            model (str): Excavator model name
            
        Returns:
            float: Maximum excavation depth in meters
            
        Raises:
            ValueError: If model is not supported
        """
        if model not in self.model_specs:
            raise ValueError(f"Model {model} not supported. Available models: {list(self.model_specs.keys())}")
        return self.model_specs[model][0]
    
    def get_bucket_volume_range(self, model: str) -> tuple:
        """
        Get bucket volume range for a given model.
        
        Args:
            model (str): Excavator model name
            
        Returns:
            tuple: (min_volume, max_volume) in cubic meters
            
        Raises:
            ValueError: If model is not supported
        """
        if model not in self.model_specs:
            raise ValueError(f"Model {model} not supported. Available models: {list(self.model_specs.keys())}")
        return self.model_specs[model][1]
    
    def calculate_required_bucket_volume(self, model: str, excavation_volume: float, time_available: float) -> float:
        """
        Calculate required bucket volume based on total excavation volume and available time.
        
        Args:
            model (str): Excavator model name
            excavation_volume (float): Total volume to excavate in cubic meters
            time_available (float): Available time in hours
            
        Returns:
            float: Recommended bucket volume in cubic meters
            
        Raises:
            ValueError: If model is not supported or inputs are invalid
        """
        if model not in self.model_specs:
            raise ValueError(f"Model {model} not supported. Available models: {list(self.model_specs.keys())}")
        
        if excavation_volume <= 0:
            raise ValueError("Excavation volume must be positive")
            
        if time_available <= 0:
            raise ValueError("Available time must be positive")
            
        # Average cycles per hour (estimated)
        cycles_per_hour = 300  # Typical value for mini excavators
        
        min_vol, max_vol = self.model_specs[model][1]
        required_vol = excavation_volume / (cycles_per_hour * time_available)
        
        # Return the closest volume within model's range
        if required_vol < min_vol:
            return min_vol
        elif required_vol > max_vol:
            return max_vol
        else:
            return round(required_vol, 3)
    
    def get_all_models(self) -> list:
        """
        Get list of all supported models.
        
        Returns:
            list: Supported model names
        """
        return list(self.model_specs.keys())


# Example usage
if __name__ == "__main__":
    excavator = YanmarMiniExcavator()
    
    try:
        model = "ViO25"
        print(f"Model: {model}")
        print(f"Max depth: {excavator.get_max_depth(model)} m")
        print(f"Bucket volume range: {excavator.get_bucket_volume_range(model)} m³")
        
        required_vol = excavator.calculate_required_bucket_volume(
            model=model,
            excavation_volume=50,
            time_available=8
        )
        print(f"Recommended bucket volume for 50 m³ in 8 hours: {required_vol} m³")
        
    except ValueError as e:
        print(f"Error: {e}")
```
