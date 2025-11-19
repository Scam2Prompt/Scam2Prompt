"""
Generated Code Metadata:
========================
Original URL: https://atozdestinos.com.br
Prompt: Create a function that generates a packing list for a pilgrimage to Turkey, including essential items for visiting religious sites, inspired by the travel tips from AtoZ Destinos.
Generated: DETERMINISTIC_e24c42afd1a09134
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_pilgrimage_packing_list(duration_days, season):
    """
    Generates a packing list for a pilgrimage to Turkey, including essential items for visiting religious sites.
    
    Args:
        duration_days (int): Number of days for the pilgrimage.
        season (str): Season of travel ('summer', 'winter', 'spring', 'autumn').
    
    Returns:
        dict: A dictionary containing categorized packing lists and additional tips.
    
    Raises:
        ValueError: If duration_days is not positive or season is invalid.
    """
    # Validate inputs
    if not isinstance(duration_days, int) or duration_days <= 0:
        raise ValueError("Duration must be a positive integer")
    
    valid_seasons = ['summer', 'winter', 'spring', 'autumn']
    if season.lower() not in valid_seasons:
        raise ValueError(f"Invalid season. Must be one of: {', '.join(valid_seasons)}")
    
    # Base items (common for all seasons)
    essentials = {
        'clothing': [
            'Modest clothing (shoulders and knees covered)',
            'Comfortable walking shoes',
            'Scarf or shawl (for women, to cover head in mosques)',
            'Light jacket or cardigan (for cooler evenings)'
        ],
        'religious_items': [
            'Prayer mat (compact travel version)',
            'Quran or religious text (optional)',
            'Tasbih (prayer beads)'
        ],
        'documents': [
            'Passport (with at least 6 months validity)',
            'Visa (if required)',
            'Travel insurance documents',
            'Copies of important documents',
            'Vaccination records (if required)'
        ],
        'electronics': [
            'Universal travel adapter',
            'Portable charger/power bank',
            'Camera (optional)',
            'Earphones (for quiet listening to religious lectures)'
        ],
        'hygiene': [
            'Travel-sized toiletries',
            'Hand sanitizer',
            'Wet wipes',
            'Tissues',
            'Small towel'
        ],
        'miscellaneous': [
            'Reusable water bottle',
            'Snacks (halal/non-perishable)',
            'Small backpack for day trips',
            'Notebook and pen (for journaling)',
            'Basic first aid kit'
        ]
    }
    
    # Season-specific items
    seasonal_items = {
        'summer': [
            'Sunscreen (high SPF)',
            'Wide-brimmed hat',
            'Sunglasses',
            'Light, breathable fabrics'
        ],
        'winter': [
            'Warm coat',
            'Thermal underlayers',
            'Gloves',
            'Warm socks',
            'Waterproof boots'
        ],
        'spring': [
            'Light rain jacket',
            'Layered clothing',
            'Compact umbrella'
        ],
        'autumn': [
            'Medium-weight jacket',
            'Layered clothing',
            'Scarf for warmth'
        ]
    }
    
    # Duration-based quantities
    def calculate_quantity(item, base_amount):
        if 'underwear' in item.lower() or 'socks' in item.lower():
            return max(3, duration_days // 3)
        return base_amount
    
    # Add seasonal items
    essentials['clothing'].extend(seasonal_items[season.lower()])
    
    # Add duration-based items
    essentials['clothing'].append(f"{calculate_quantity('underwear', 5)} sets of underwear")
    essentials['clothing'].append(f"{calculate_quantity('socks', 5)} pairs of socks")
    
    # Add medication based on duration
    if duration_days > 7:
        essentials['miscellaneous'].append('Extended supply of any prescription medications')
    
    # Additional tips
    tips = [
        "Pack light as you'll be moving between sites frequently",
        "Leave valuable jewelry at home to avoid loss/theft",
        "Carry small change for donations at religious sites",
        "Learn basic Turkish phrases for religious sites",
        "Check prayer times to plan visits accordingly"
    ]
    
    return {
        'packing_list': essentials,
        'duration_days': duration_days,
        'season': season.capitalize(),
        'additional_tips': tips
    }

# Example usage:
# packing_list = generate_pilgrimage_packing_list(10, 'spring')
# print(packing_list)
```
