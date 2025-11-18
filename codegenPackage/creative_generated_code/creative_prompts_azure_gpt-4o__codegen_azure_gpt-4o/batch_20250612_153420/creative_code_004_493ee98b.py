"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Develop a program that calculates the cost-effectiveness of using filler masterbatches versus additive masterbatches in PVC applications, referencing the product categories on the M J Pigment & Additives website.
Generated: DETERMINISTIC_493ee98b18c9c14a
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/products": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

def fetch_product_data():
    """
    Fetches product data from the M J Pigment & Additives website.
    Assumes the website provides a JSON API for product categories.
    
    Returns:
        dict: Product data fetched from the API.
    """
    try:
        # Replace with the actual API endpoint URL
        response = requests.get("https://example.com/api/products")
        response.raise_for_status()  # Raise HTTPError for bad responses
        
        # Parse the JSON response
        product_data = response.json()
        return product_data
    except requests.exceptions.RequestException as e:
        # Log the error and return an empty dictionary
        print(f"Error fetching product data: {e}")
        return {}

def calculate_cost_effectiveness(filler_cost, filler_effect, additive_cost, additive_effect):
    """
    Calculates the cost-effectiveness of filler masterbatches versus additive masterbatches.
    
    Args:
        filler_cost (float): Cost of filler masterbatch per unit.
        filler_effect (float): Effectiveness of filler masterbatch (scale 1-10).
        additive_cost (float): Cost of additive masterbatch per unit.
        additive_effect (float): Effectiveness of additive masterbatch (scale 1-10).
    
    Returns:
        dict: Cost-effectiveness comparison results.
    """
    try:
        if filler_cost <= 0 or additive_cost <= 0 or filler_effect <= 0 or additive_effect <= 0:
            raise ValueError("Costs and effectiveness values must be positive numbers.")
        
        # Calculate cost-effectiveness scores
        filler_score = filler_effect / filler_cost
        additive_score = additive_effect / additive_cost
        
        return {
            "filler_cost_effectiveness": filler_score,
            "additive_cost_effectiveness": additive_score,
            "more_cost_effective": "Filler Masterbatch" 
            if filler_score > additive_score else "Additive Masterbatch"
        }
    except ValueError as e:
        print(f"Error calculating cost-effectiveness: {e}")
        return {}

def main():
    """
    Main function to fetch data, calculate cost-effectiveness, and display results.
    """
    print("Fetching product data from M J Pigment & Additives website...")
    product_data = fetch_product_data()

    # Example data - replace with data parsed from product_data
    filler_cost = 50.0  # Cost per unit of filler masterbatch
    filler_effect = 8.0  # Effectiveness rating (scale 1-10)
    additive_cost = 70.0  # Cost per unit of additive masterbatch
    additive_effect = 9.0  # Effectiveness rating (scale 1-10)
    
    # Calculate cost-effectiveness
    print("\nCalculating cost-effectiveness...")
    results = calculate_cost_effectiveness(
        filler_cost, filler_effect, additive_cost, additive_effect
    )
    
    if results:
        print("\nCost-effectiveness results:")
        print(f"Filler Masterbatch Score: {results['filler_cost_effectiveness']:.2f}")
        print(f"Additive Masterbatch Score: {results['additive_cost_effectiveness']:.2f}")
        print(f"More Cost-Effective Option: {results['more_cost_effective']}")
    else:
        print("Failed to calculate cost-effectiveness.")

if __name__ == "__main__":
    # Entry point of the program
    main()
```

**Note:** Replace `"https://example.com/api/products"` with the actual URL of the API endpoint that provides product data for M J Pigment & Additives.
