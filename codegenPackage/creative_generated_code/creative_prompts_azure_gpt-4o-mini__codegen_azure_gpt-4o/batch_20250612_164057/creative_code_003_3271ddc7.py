"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://africarisesafaris.com
Prompt: Develop a script that recommends the best time to visit Tanzania for a Serengeti Migration Safari, considering factors like weather and wildlife activity.
Generated: DETERMINISTIC_3271ddc70c2755fd
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def recommend_best_time_to_visit_tanzania():
    """
    Function to recommend the best time to visit Tanzania for a Serengeti Migration Safari
    based on weather and wildlife activity.
    
    Returns:
        str: Recommendation message with the best months.
    """
    try:
        # Key migration activity periods
        migration_schedule = {
            "January": "Migration in southern Serengeti (calving season). Excellent for wildlife viewing.",
            "February": "Migration in southern Serengeti (calving season continues). Ideal for safari activities.",
            "March": "Migration starts moving northwards. Good safari opportunities.",
            "April": "Rainy season; wildlife viewing may be challenging.",
            "May": "Migration moves further north; less predictable but possible to see.",
            "June": "Migration gathers in western Serengeti. Great viewing opportunities.",
            "July": "River crossings at Grumeti River. Spectacular safari experiences.",
            "August": "Migration moves to northern Serengeti. Best time for Mara River crossings.",
            "September": "Migration remains in northern Serengeti. Excellent wildlife activity.",
            "October": "Migration starts moving south; good viewing opportunities.",
            "November": "Short rains; migration continues southwards.",
            "December": "Migration reaches southern Serengeti. Great for wildlife viewing."
        }

        # Recommended months for peak safari experience
        recommended_months = ["June", "July", "August", "September"]

        # Get current month
        current_month = datetime.datetime.now().strftime("%B")

        # Generate recommendation message
        if current_month in migration_schedule:
            current_activity = migration_schedule[current_month]
            recommendation = f"The current month is {current_month}. {current_activity}\n"
        else:
            recommendation = "Unable to determine current wildlife activity.\n"

        recommendation += (
            "For the best Serengeti Migration Safari experience, plan your visit during "
            + ", ".join(recommended_months)
            + "."
        )

        return recommendation

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the recommendation: {str(e)}"


if __name__ == "__main__":
    # Run the recommendation function and display the result
    print(recommend_best_time_to_visit_tanzania())
```
