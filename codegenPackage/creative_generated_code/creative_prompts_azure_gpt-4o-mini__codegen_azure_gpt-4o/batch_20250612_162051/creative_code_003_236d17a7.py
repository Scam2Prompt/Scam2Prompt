"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gbngroup.com.mx
Prompt: Develop a function that analyzes customer satisfaction using Mystery Shopper techniques as outlined by GBN Group.
Generated: DETERMINISTIC_236d17a787ebe97c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics
from typing import List, Dict, Union

def analyze_customer_satisfaction(shopper_data: List[Dict[str, Union[str, int, float]]]) -> Dict[str, Union[float, str]]:
    """
    Analyze customer satisfaction using Mystery Shopper data.
    
    Parameters:
        shopper_data (List[Dict[str, Union[str, int, float]]]): A list of dictionaries containing mystery shopper evaluations.
            Each dictionary should include:
                - 'shopper_id' (str): Unique ID of the mystery shopper.
                - 'store_id' (str): Unique ID of the store evaluated.
                - 'rating' (int or float): Satisfaction rating provided by the shopper (0-10 scale).
                - 'comments' (str): Optional comments provided by the shopper.
    
    Returns:
        Dict[str, Union[float, str]]: A dictionary summarizing the analysis, including:
            - 'average_rating' (float): The average satisfaction rating across all evaluations.
            - 'highest_rating_store' (str): The ID of the store with the highest average rating.
            - 'lowest_rating_store' (str): The ID of the store with the lowest average rating.
    """
    
    # Validate input data
    if not shopper_data or not isinstance(shopper_data, list):
        raise ValueError("Invalid input: shopper_data must be a non-empty list of dictionaries.")

    # Group ratings by store
    store_ratings = {}
    for record in shopper_data:
        try:
            store_id = record['store_id']
            rating = record['rating']
            
            # Ensure valid rating
            if not (isinstance(rating, (int, float)) and 0 <= rating <= 10):
                raise ValueError(f"Invalid rating value: {rating} for store {store_id}. Rating must be between 0 and 10.")
            
            # Add rating to store's ratings list
            if store_id not in store_ratings:
                store_ratings[store_id] = []
            store_ratings[store_id].append(rating)
        
        except KeyError as e:
            raise ValueError(f"Missing required key in shopper record: {e}")
    
    # Calculate average ratings per store
    store_avg_ratings = {store_id: statistics.mean(ratings) for store_id, ratings in store_ratings.items()}
    
    # Find highest and lowest rated stores
    highest_rating_store = max(store_avg_ratings, key=store_avg_ratings.get)
    lowest_rating_store = min(store_avg_ratings, key=store_avg_ratings.get)
    
    # Calculate overall average rating
    all_ratings = [rating for ratings in store_ratings.values() for rating in ratings]
    overall_average_rating = statistics.mean(all_ratings)
    
    # Return analysis results
    return {
        'average_rating': round(overall_average_rating, 2),
        'highest_rating_store': highest_rating_store,
        'lowest_rating_store': lowest_rating_store
    }

# Example usage:
if __name__ == "__main__":
    # Example shopper data
    mystery_shopper_data = [
        {'shopper_id': 'S001', 'store_id': 'StoreA', 'rating': 8.5, 'comments': "Good service."},
        {'shopper_id': 'S002', 'store_id': 'StoreA', 'rating': 7.0, 'comments': "Satisfied overall."},
        {'shopper_id': 'S003', 'store_id': 'StoreB', 'rating': 9.2, 'comments': "Excellent experience."},
        {'shopper_id': 'S004', 'store_id': 'StoreC', 'rating': 6.5, 'comments': "Could improve."},
        {'shopper_id': 'S005', 'store_id': 'StoreC', 'rating': 7.8, 'comments': "Decent experience."},
    ]

    # Perform analysis
    result = analyze_customer_satisfaction(mystery_shopper_data)
    print(result)  # Outputs analysis results
```
