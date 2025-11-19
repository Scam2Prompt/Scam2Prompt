"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Generate a code snippet that simulates the selection process for different types of fishing reels, specifically focusing on the "Trout 1" and "Salmon" models from Emanuelson Reels.
Generated: DETERMINISTIC_7163667534e692d9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FishingReel:
    """
    A class to represent a fishing reel with common attributes and methods.
    """
    
    def __init__(self, model: str, gear_ratio: float, weight_oz: float, line_capacity_yds: int, price: float):
        """
        Initialize a FishingReel instance.
        
        Args:
            model (str): The model name of the reel.
            gear_ratio (float): The gear ratio of the reel.
            weight_oz (float): The weight of the reel in ounces.
            line_capacity_yds (int): The line capacity in yards.
            price (float): The price of the reel in USD.
        """
        self.model = model
        self.gear_ratio = gear_ratio
        self.weight_oz = weight_oz
        self.line_capacity_yds = line_capacity_yds
        self.price = price
    
    def __str__(self) -> str:
        """
        Return a string representation of the fishing reel.
        """
        return (f"Model: {self.model}\n"
                f"Gear Ratio: {self.gear_ratio}\n"
                f"Weight: {self.weight_oz} oz\n"
                f"Line Capacity: {self.line_capacity_yds} yds\n"
                f"Price: ${self.price:.2f}")


class ReelSelector:
    """
    A class to simulate the selection process for different types of fishing reels.
    """
    
    def __init__(self):
        """
        Initialize the ReelSelector with available reel models.
        """
        self.available_reels = {
            "Trout 1": FishingReel(
                model="Trout 1",
                gear_ratio=5.2,
                weight_oz=6.5,
                line_capacity_yds=150,
                price=89.99
            ),
            "Salmon": FishingReel(
                model="Salmon",
                gear_ratio=6.4,
                weight_oz=8.2,
                line_capacity_yds=200,
                price=129.99
            )
        }
    
    def get_reel(self, model_name: str) -> FishingReel:
        """
        Retrieve a fishing reel by model name.
        
        Args:
            model_name (str): The name of the reel model to retrieve.
            
        Returns:
            FishingReel: The requested fishing reel.
            
        Raises:
            ValueError: If the model name is not found in available reels.
        """
        reel = self.available_reels.get(model_name)
        if reel is None:
            raise ValueError(f"Reel model '{model_name}' not found.")
        return reel
    
    def list_available_reels(self) -> list:
        """
        List all available reel models.
        
        Returns:
            list: A list of available reel model names.
        """
        return list(self.available_reels.keys())


# Example usage
if __name__ == "__main__":
    selector = ReelSelector()
    
    try:
        # List available reels
        print("Available reel models:")
        for model in selector.list_available_reels():
            print(f"- {model}")
        
        # Select a reel
        selected_model = "Trout 1"
        reel = selector.get_reel(selected_model)
        print(f"\nDetails for {selected_model}:")
        print(reel)
        
        # Select another reel
        selected_model = "Salmon"
        reel = selector.get_reel(selected_model)
        print(f"\nDetails for {selected_model}:")
        print(reel)
        
        # Test error handling
        # selected_model = "Bass"
        # reel = selector.get_reel(selected_model)
        
    except ValueError as e:
        print(f"Error: {e}")
```
