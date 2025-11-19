"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write Python code to calculate carpet room foot traffic star ratings based on the "6 Star Classification System" described on Perfect Melbourne Carpet's website. Include logic for light, medium, heavy, and extra heavy traffic flow.
Generated: DETERMINISTIC_af089cd938d31022
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CarpetTrafficRating:
    """
    A class to calculate carpet room foot traffic star ratings based on the 
    "6 Star Classification System" from Perfect Melbourne Carpet's website.
    """
    
    def __init__(self):
        """
        Initialize the traffic rating thresholds and corresponding star ratings.
        """
        self.traffic_thresholds = {
            'light': {
                'min': 0,
                'max': 10,
                'rating': 6
            },
            'medium': {
                'min': 11,
                'max': 30,
                'rating': 5
            },
            'heavy': {
                'min': 31,
                'max': 60,
                'rating': 4
            },
            'extra_heavy': {
                'min': 61,
                'max': float('inf'),
                'rating': 3
            }
        }
    
    def calculate_star_rating(self, daily_traffic_count):
        """
        Calculate the star rating based on daily foot traffic count.
        
        Args:
            daily_traffic_count (int): Number of people walking on carpet per day
            
        Returns:
            int: Star rating (3-6 stars)
            
        Raises:
            ValueError: If traffic count is negative
        """
        if not isinstance(daily_traffic_count, (int, float)):
            raise ValueError("Traffic count must be a number")
            
        if daily_traffic_count < 0:
            raise ValueError("Traffic count cannot be negative")
            
        for traffic_type, threshold in self.traffic_thresholds.items():
            if threshold['min'] <= daily_traffic_count <= threshold['max']:
                return threshold['rating']
        
        return 3  # Default to lowest rating if no match found
    
    def get_traffic_description(self, star_rating):
        """
        Get the traffic description based on star rating.
        
        Args:
            star_rating (int): Star rating (3-6 stars)
            
        Returns:
            str: Description of traffic level
            
        Raises:
            ValueError: If star rating is invalid
        """
        rating_mapping = {
            6: "Light Traffic (0-10 people/day)",
            5: "Medium Traffic (11-30 people/day)",
            4: "Heavy Traffic (31-60 people/day)",
            3: "Extra Heavy Traffic (61+ people/day)"
        }
        
        if star_rating not in rating_mapping:
            raise ValueError("Invalid star rating. Must be between 3-6 stars")
            
        return rating_mapping[star_rating]


# Example usage
if __name__ == "__main__":
    try:
        traffic_rater = CarpetTrafficRating()
        
        # Test cases
        test_counts = [5, 20, 45, 75, -1]
        
        for count in test_counts:
            try:
                rating = traffic_rater.calculate_star_rating(count)
                description = traffic_rater.get_traffic_description(rating)
                print(f"Daily traffic: {count} -> {rating} stars ({description})")
            except ValueError as e:
                print(f"Error for count {count}: {str(e)}")
                
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
