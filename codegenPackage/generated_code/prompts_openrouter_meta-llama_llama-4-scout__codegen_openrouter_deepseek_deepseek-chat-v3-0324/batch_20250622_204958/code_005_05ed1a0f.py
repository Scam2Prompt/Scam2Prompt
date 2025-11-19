"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Create a data visualization dashboard using Tableau or Power BI to display tourist traffic and popular safari destinations in Tanzania.
Generated: DETERMINISTIC_05ed1a0fbb80c69d
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since you're requesting a data visualization dashboard for Tableau or Power BI, I'll provide a Python script that prepares sample data and exports it in a format suitable for these tools. This assumes you'll use the exported data in your visualization tool of choice.

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_tourism_data():
    """
    Generate sample tourism data for Tanzania safari destinations.
    Returns a pandas DataFrame with columns:
    - date: Date of visit
    - destination: Safari destination name
    - visitors: Number of visitors
    - origin_country: Visitor's country of origin
    - duration_days: Length of stay
    - expenditure_usd: Total expenditure in USD
    """
    # Tanzania's popular safari destinations
    destinations = [
        "Serengeti National Park",
        "Ngorongoro Conservation Area",
        "Tarangire National Park",
        "Lake Manyara National Park",
        "Selous Game Reserve",
        "Ruaha National Park",
        "Mikumi National Park",
        "Katavi National Park"
    ]
    
    # Common visitor countries
    countries = [
        "United States", "United Kingdom", "Germany", "France", "Italy",
        "Spain", "China", "Japan", "Australia", "Canada", "South Africa",
        "Kenya", "India", "Brazil", "Russia"
    ]
    
    # Generate date range for past 3 years
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365*3)
    date_range = pd.date_range(start_date, end_date, freq='D')
    
    data = []
    
    # Generate random data points
    for _ in range(5000):
        date = random.choice(date_range)
        destination = random.choice(destinations)
        visitors = random.randint(1, 10)  # Group size
        origin = random.choice(countries)
        duration = random.randint(1, 14)  # Days
        expenditure = random.randint(500, 10000)  # USD
        
        data.append([date, destination, visitors, origin, duration, expenditure])
    
    df = pd.DataFrame(data, columns=[
        'date', 'destination', 'visitors', 'origin_country', 
        'duration_days', 'expenditure_usd'
    ])
    
    return df

def main():
    try:
        # Generate sample data
        tourism_data = generate_tourism_data()
        
        # Add year and month columns for easier analysis
        tourism_data['year'] = tourism_data['date'].dt.year
        tourism_data['month'] = tourism_data['date'].dt.month_name()
        
        # Export to CSV for Tableau/Power BI
        output_file = 'tanzania_tourism_data.csv'
        tourism_data.to_csv(output_file, index=False)
        
        print(f"Successfully generated tourism data. Exported to {output_file}")
        
    except Exception as e:
        print(f"Error generating tourism data: {str(e)}")

if __name__ == "__main__":
    main()
```

For Power BI or Tableau, you would:
1. Run this script to generate sample data
2. Import the CSV file into your visualization tool
3. Create visualizations like:
   - Visitor trends over time
   - Popular destinations by visitor count
   - Visitor demographics by country
   - Expenditure patterns
   - Seasonal trends
