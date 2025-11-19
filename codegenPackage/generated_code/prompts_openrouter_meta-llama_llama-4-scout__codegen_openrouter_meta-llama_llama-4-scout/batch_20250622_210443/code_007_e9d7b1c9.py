"""
Generated Code Metadata:
========================
Original URL: https://villapanorea.com
Prompt: Generate a sample webpage content for a similar vacation rental property, including descriptions of accommodations and amenities, using Markdown formatting.
Generated: DETERMINISTIC_e9d7b1c900779c49
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```markdown
# Welcome to Coastal Getaway

## Property Description

Escape to serenity with our stunning coastal vacation rental, perfect for a relaxing getaway. Our property, **Coastal Getaway**, offers breathtaking ocean views, spacious accommodations, and top-notch amenities.

## Accommodations

### Main House

* **3 Bedrooms**: 2 King, 1 Queen
* **2.5 Bathrooms**: 1 en-suite with ocean views
* **Living Area**: 40" Smart TV, comfortable seating for 8
* **Kitchen**: Fully equipped with stainless steel appliances, dishwasher, and microwave

### Guest Cottage

* **1 Bedroom**: Queen
* **1 Bathroom**
* **Private Patio**: Enjoy your morning coffee with ocean views

## Amenities

* **Private Beach Access**: Unwind on our secluded beach
* **Outdoor Pool**: Refreshing saltwater pool with sun loungers
* **Fitness Center**: State-of-the-art equipment and free weights
* **Game Room**: Pool table, ping-pong, and board games
* **Wi-Fi**: Fast and reliable internet throughout the property

## Additional Features

* **Parking**: Ample parking for up to 5 vehicles
* **Pet-Friendly**: Welcome your furry friends (additional fees apply)
* **Laundry Facilities**: Washer and dryer on site

## Rates

* **Seasonal Rates**:
	+ Peak (June 15 - August 31): $500/night
	+ Off-Peak (September 1 - June 14): $350/night
* **Minimum Stay**: 3 nights

## Policies

* **Cancellation Policy**: 30-day notice required for cancellations
* **House Rules**: Please respect our home and neighbors

## Booking Information

Ready to book your dream vacation? Contact us at [coastalgoaway@example.com](mailto:coastalgoaway@example.com) or call (555) 123-4567.

## Photos

[Insert photos of the property, accommodations, and amenities]
```

```python
# For a python script to generate the above markdown content programmatically

import markdown

def generate_markdown_content(property_name, description, accommodations, amenities, rates, policies):
    content = f"# Welcome to {property_name}\n\n## Property Description\n\n{description}\n\n"
    
    content += "## Accommodations\n\n"
    for accommodation, details in accommodations.items():
        content += f"### {accommodation}\n"
        for key, value in details.items():
            content += f"* **{key}**: {value}\n"
    
    content += "\n## Amenities\n\n"
    for amenity in amenities:
        content += f"* {amenity}\n"
    
    content += "\n## Rates\n\n"
    for rate_type, rate in rates.items():
        content += f"* **{rate_type}**: {rate}\n"
    
    content += "\n## Policies\n\n"
    for policy, description in policies.items():
        content += f"* **{policy}**: {description}\n"
    
    return content

def main():
    property_name = "Coastal Getaway"
    description = "Escape to serenity with our stunning coastal vacation rental, perfect for a relaxing getaway."
    accommodations = {
        "Main House": {
            "Bedrooms": "3 (2 King, 1 Queen)",
            "Bathrooms": "2.5 (1 en-suite with ocean views)",
            "Living Area": "40\" Smart TV, comfortable seating for 8",
            "Kitchen": "Fully equipped with stainless steel appliances, dishwasher, and microwave"
        },
        "Guest Cottage": {
            "Bedroom": "1 (Queen)",
            "Bathroom": "1",
            "Private Patio": "Enjoy your morning coffee with ocean views"
        }
    }
    amenities = [
        "Private Beach Access",
        "Outdoor Pool",
        "Fitness Center",
        "Game Room",
        "Wi-Fi"
    ]
    rates = {
        "Peak (June 15 - August 31)": "$500/night",
        "Off-Peak (September 1 - June 14)": "$350/night"
    }
    policies = {
        "Cancellation Policy": "30-day notice required for cancellations",
        "House Rules": "Please respect our home and neighbors"
    }
    
    markdown_content = generate_markdown_content(property_name, description, accommodations, amenities, rates, policies)
    print(markdown_content)

if __name__ == "__main__":
    main()
```
