"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Create a function that calculates the load capacity of different tractor attachments, using JECO's specifications for front-end loaders and backhoes.
Generated: DETERMINISTIC_eb2380ffe9b7fbad
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TractorAttachment:
    """
    Base class for tractor attachments with common properties and methods.
    """
    
    def __init__(self, model: str, weight: float, max_lift_capacity: float):
        """
        Initialize the tractor attachment with basic specifications.
        
        Args:
            model (str): Model name/number of the attachment
            weight (float): Weight of the attachment in kg
            max_lift_capacity (float): Maximum lift capacity in kg
        """
        self.model = model
        self.weight = weight
        self.max_lift_capacity = max_lift_capacity
    
    def calculate_load_capacity(self, distance_from_pivot: float) -> float:
        """
        Calculate the load capacity based on distance from pivot point.
        
        Args:
            distance_from_pivot (float): Distance from pivot point in meters
            
        Returns:
            float: Calculated load capacity in kg
            
        Raises:
            ValueError: If distance_from_pivot is negative
        """
        if distance_from_pivot < 0:
            raise ValueError("Distance from pivot cannot be negative")
        return self.max_lift_capacity / (1 + (distance_from_pivot * 0.1))


class FrontEndLoader(TractorAttachment):
    """
    Class representing a front-end loader attachment with JECO specifications.
    """
    
    def __init__(self, model: str, weight: float, max_lift_capacity: float, bucket_capacity: float):
        """
        Initialize the front-end loader with additional specifications.
        
        Args:
            model (str): Model name/number of the loader
            weight (float): Weight of the loader in kg
            max_lift_capacity (float): Maximum lift capacity in kg
            bucket_capacity (float): Bucket capacity in cubic meters
        """
        super().__init__(model, weight, max_lift_capacity)
        self.bucket_capacity = bucket_capacity
    
    def calculate_material_load(self, material_density: float) -> float:
        """
        Calculate the material load based on bucket capacity and material density.
        
        Args:
            material_density (float): Density of material in kg/m³
            
        Returns:
            float: Calculated material weight in kg
            
        Raises:
            ValueError: If material_density is negative
        """
        if material_density < 0:
            raise ValueError("Material density cannot be negative")
        return self.bucket_capacity * material_density


class Backhoe(TractorAttachment):
    """
    Class representing a backhoe attachment with JECO specifications.
    """
    
    def __init__(self, model: str, weight: float, max_lift_capacity: float, digging_depth: float):
        """
        Initialize the backhoe with additional specifications.
        
        Args:
            model (str): Model name/number of the backhoe
            weight (float): Weight of the backhoe in kg
            max_lift_capacity (float): Maximum lift capacity in kg
            digging_depth (float): Maximum digging depth in meters
        """
        super().__init__(model, weight, max_lift_capacity)
        self.digging_depth = digging_depth
    
    def calculate_digging_force(self, distance_from_pivot: float) -> float:
        """
        Calculate the digging force based on distance from pivot point.
        
        Args:
            distance_from_pivot (float): Distance from pivot point in meters
            
        Returns:
            float: Calculated digging force in kg
            
        Raises:
            ValueError: If distance_from_pivot is negative
        """
        if distance_from_pivot < 0:
            raise ValueError("Distance from pivot cannot be negative")
        return self.max_lift_capacity * (1 - (distance_from_pivot * 0.05))


def calculate_safe_operating_load(attachment: TractorAttachment, distance: float, safety_factor: float = 1.5) -> float:
    """
    Calculate the safe operating load considering a safety factor.
    
    Args:
        attachment (TractorAttachment): The attachment to calculate for
        distance (float): Distance from pivot point in meters
        safety_factor (float): Safety factor to apply (default 1.5)
        
    Returns:
        float: Safe operating load in kg
        
    Raises:
        ValueError: If safety_factor is less than 1.0
    """
    if safety_factor < 1.0:
        raise ValueError("Safety factor must be at least 1.0")
    return attachment.calculate_load_capacity(distance) / safety_factor
```
