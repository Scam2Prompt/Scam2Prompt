"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinaeletrica.com.br
Prompt: Generate code to calculate the efficiency of Capina Elétrica's weed removal method over multiple applications, incorporating the duration of vegetation-free periods (30-45 days, 60-70 days, and up to 90 days) mentioned on the website.
Generated: DETERMINISTIC_f92076772050fb6e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

def calculate_efficiency(application_data):
    """
    Calculate the efficiency of weed removal based on vegetation-free periods.
    
    Args:
        application_data (list): A list of vegetation-free periods (in days) for multiple applications.
        
    Returns:
        dict: A dictionary containing average efficiency, standard deviation, and classification.
    """
    if not application_data or not all(isinstance(x, (int, float)) for x in application_data):
        raise ValueError("Invalid application data. Provide a list of numeric vegetation-free periods (in days).")
    
    # Constants for vegetation-free period ranges
    SHORT_PERIOD = (30, 45)  # Short vegetation-free period
    MEDIUM_PERIOD = (60, 70)  # Medium vegetation-free period
    LONG_PERIOD = (90, float('inf'))  # Long vegetation-free period (up to 90 or more)
    
    # Efficiency classification
    classification = {"Short": 0, "Medium": 0, "Long": 0}

    # Classify each vegetation-free period
    for duration in application_data:
        if SHORT_PERIOD[0] <= duration <= SHORT_PERIOD[1]:
            classification["Short"] += 1
        elif MEDIUM_PERIOD[0] <= duration <= MEDIUM_PERIOD[1]:
            classification["Medium"] += 1
        elif duration >= LONG_PERIOD[0]:
            classification["Long"] += 1
    
    # Calculate average vegetation-free period and standard deviation
    average_duration = statistics.mean(application_data)
    std_deviation = statistics.stdev(application_data) if len(application_data) > 1 else 0.0
    
    # Prepare the result
    result = {
        "average_duration": average_duration,
        "standard_deviation": std_deviation,
        "classification": classification
    }
    
    return result


def main():
    """
    Main function to demonstrate the efficiency calculation process.
    """
    # Example vegetation-free periods (in days) from multiple applications
    application_data = [35, 40, 65, 70, 90, 100, 45, 60, 85]
    
    try:
        # Calculate efficiency
        efficiency_results = calculate_efficiency(application_data)
        
        # Display results
        print("Efficiency Results:")
        print(f"Average Vegetation-Free Period: {efficiency_results['average_duration']:.2f} days")
        print(f"Standard Deviation: {efficiency_results['standard_deviation']:.2f} days")
        print("Classification:")
        for key, value in efficiency_results["classification"].items():
            print(f"  {key}: {value} applications")
    
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
