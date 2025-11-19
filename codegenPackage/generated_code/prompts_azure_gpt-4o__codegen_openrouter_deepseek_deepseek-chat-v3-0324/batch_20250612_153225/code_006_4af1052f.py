"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Develop a tool to assist users in selecting the most economical generator based on power needs and location, inspired by the "Güç ve Yer Tespiti" service on Birlik Jeneratör's website.
Generated: DETERMINISTIC_4af1052fea523f52
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pandas as pd
from typing import Dict, List, Optional, Tuple

class GeneratorSelector:
    """
    A tool to assist users in selecting the most economical generator based on power needs and location.
    """
    
    def __init__(self, generator_data_path: str = "generator_data.json"):
        """
        Initialize the GeneratorSelector with generator data.
        
        Args:
            generator_data_path (str): Path to JSON file containing generator specifications.
        """
        try:
            with open(generator_data_path, 'r') as f:
                self.generator_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Generator data file not found at {generator_data_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in generator data file")
            
        self.geolocator = Nominatim(user_agent="generator_selector")
        
    def get_location_coordinates(self, address: str) -> Tuple[float, float]:
        """
        Get latitude and longitude coordinates for a given address.
        
        Args:
            address (str): Physical address or location name
            
        Returns:
            Tuple[float, float]: (latitude, longitude)
            
        Raises:
            ValueError: If location cannot be geocoded
        """
        location = self.geolocator.geocode(address)
        if not location:
            raise ValueError(f"Could not geocode address: {address}")
        return (location.latitude, location.longitude)
    
    def calculate_distance(self, coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
        """
        Calculate distance in kilometers between two coordinates.
        
        Args:
            coord1 (Tuple[float, float]): (lat1, lon1)
            coord2 (Tuple[float, float]): (lat2, lon2)
            
        Returns:
            float: Distance in kilometers
        """
        return geodesic(coord1, coord2).kilometers
    
    def find_nearest_dealers(self, user_location: str, max_distance: float = 50.0) -> List[Dict]:
        """
        Find generator dealers nearest to the user's location.
        
        Args:
            user_location (str): User's address or location
            max_distance (float): Maximum distance in km to consider
            
        Returns:
            List[Dict]: List of nearby dealers with distance information
        """
        try:
            user_coords = self.get_location_coordinates(user_location)
        except ValueError as e:
            raise ValueError(f"Error processing location: {str(e)}")
            
        nearby_dealers = []
        for dealer in self.generator_data["dealers"]:
            try:
                dealer_coords = self.get_location_coordinates(dealer["address"])
                distance = self.calculate_distance(user_coords, dealer_coords)
                
                if distance <= max_distance:
                    dealer_info = dealer.copy()
                    dealer_info["distance_km"] = round(distance, 2)
                    nearby_dealers.append(dealer_info)
            except ValueError:
                continue
                
        return sorted(nearby_dealers, key=lambda x: x["distance_km"])
    
    def calculate_power_requirement(self, appliances: List[Dict]) -> float:
        """
        Calculate total power requirement based on appliances.
        
        Args:
            appliances (List[Dict]): List of appliances with power requirements
                Example: [{"name": "fridge", "power_w": 200, "quantity": 1}]
                
        Returns:
            float: Total power requirement in watts
        """
        total_power = 0.0
        for appliance in appliances:
            if "power_w" not in appliance or "quantity" not in appliance:
                raise ValueError("Each appliance must have 'power_w' and 'quantity' fields")
            total_power += appliance["power_w"] * appliance["quantity"]
        return total_power
    
    def recommend_generators(self, power_needed_w: float, budget: Optional[float] = None) -> pd.DataFrame:
        """
        Recommend suitable generators based on power needs and optional budget.
        
        Args:
            power_needed_w (float): Total power requirement in watts
            budget (Optional[float]): Maximum budget in local currency
            
        Returns:
            pd.DataFrame: DataFrame of recommended generators with specifications
        """
        suitable_generators = []
        
        for generator in self.generator_data["generators"]:
            if (generator["power_output_w"] >= power_needed_w and 
                (budget is None or generator["price"] <= budget)):
                suitable_generators.append(generator)
                
        if not suitable_generators:
            raise ValueError("No generators found matching the specified criteria")
            
        df = pd.DataFrame(suitable_generators)
        df = df.sort_values(by=["price", "power_output_w"])
        return df.reset_index(drop=True)
    
    def get_full_recommendation(self, appliances: List[Dict], location: str, 
                               budget: Optional[float] = None) -> Dict:
        """
        Get complete recommendation including power calculation, generator options, and nearby dealers.
        
        Args:
            appliances (List[Dict]): List of appliances with power requirements
            location (str): User's address or location
            budget (Optional[float]): Maximum budget in local currency
            
        Returns:
            Dict: Complete recommendation with all information
        """
        try:
            power_needed = self.calculate_power_requirement(appliances)
            generators = self.recommend_generators(power_needed, budget)
            dealers = self.find_nearest_dealers(location)
            
            return {
                "power_requirement_w": power_needed,
                "recommended_generators": generators.to_dict(orient="records"),
                "nearby_dealers": dealers
            }
        except Exception as e:
            return {
                "error": str(e),
                "success": False
            }

# Example usage
if __name__ == "__main__":
    try:
        selector = GeneratorSelector()
        
        # Sample appliance list
        appliances = [
            {"name": "Refrigerator", "power_w": 200, "quantity": 1},
            {"name": "TV", "power_w": 150, "quantity": 2},
            {"name": "Lights", "power_w": 50, "quantity": 10}
        ]
        
        # Get recommendation
        recommendation = selector.get_full_recommendation(
            appliances=appliances,
            location="Istanbul, Turkey",
            budget=5000
        )
        
        if "error" in recommendation:
            print(f"Error: {recommendation['error']}")
        else:
            print("Power Requirement (W):", recommendation["power_requirement_w"])
            print("\nRecommended Generators:")
            for gen in recommendation["recommended_generators"]:
                print(f"- {gen['model']} ({gen['power_output_w']}W): ${gen['price']}")
            
            print("\nNearby Dealers:")
            for dealer in recommendation["nearby_dealers"]:
                print(f"- {dealer['name']} ({dealer['distance_km']}km away)")
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
