"""
Generated Code Metadata:
========================
Original URL: https://africarisesafaris.com
Prompt: Develop a script that recommends the best time to visit Tanzania for a Serengeti Migration Safari, considering factors like weather and wildlife activity.
Generated: DETERMINISTIC_3271ddc70c2755fd
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def recommend_best_time_to_visit():
    """
    Recommends the best time to visit Tanzania for a Serengeti Migration Safari
    based on weather and wildlife activity.
    
    Returns:
        str: A recommendation message with the best months to visit.
    """
    try:
        # Define the migration patterns and weather conditions
        migration_schedule = {
            "January": "Great time to see the migration in the southern Serengeti.",
            "February": "Calving season in the southern Serengeti; excellent for wildlife viewing.",
            "March": "End of calving season; still good for southern Serengeti.",
            "April": "Rainy season; migration starts moving northward.",
            "May": "Migration continues north; lush landscapes but wet conditions.",
            "June": "Dry season begins; migration in western Serengeti.",
            "July": "Peak migration crossing the Grumeti River; excellent viewing.",
            "August": "Migration moves to northern Serengeti; river crossings continue.",
            "September": "Migration in northern Serengeti; great for Mara River crossings.",
            "October": "Migration starts returning south; northern Serengeti still active.",
            "November": "Short rains; migration moves to central Serengeti.",
            "December": "Migration in southern Serengeti; good for wildlife viewing."
        }

        # Define the best months for safari based on migration activity and weather
        best_months = ["January", "February", "June", "July", "August", "September"]

        # Get the current month
        current_month = datetime.datetime.now().strftime("%B")

        # Generate recommendation
        if current_month in best_months:
            recommendation = f"{current_month} is one of the best months to visit Tanzania for a Serengeti Migration Safari. {migration_schedule[current_month]}"
        else:
            recommendation = f"{current_month} is not the peak season for a Serengeti Migration Safari. Consider visiting during one of these months: {', '.join(best_months)}."

        return recommendation

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the recommendation: {str(e)}"


if __name__ == "__main__":
    # Run the script and display the recommendation
    print(recommend_best_time_to_visit())
```
