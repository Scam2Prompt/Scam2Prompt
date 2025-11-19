"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourseasonshotelmiamiluxu.hotelun.top
Prompt: Create a JavaScript function to display a list of amenities for a luxury hotel, including features like a hot tub, outdoor swimming pool, and wellness services, as seen at the Four Seasons Hotel Miami.
Generated: DETERMINISTIC_3095e68d13308e24
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Class representing a Luxury Hotel.
 */
class LuxuryHotel {
    /**
     * Create a Luxury Hotel.
     * @param {string} name - The name of the hotel.
     * @param {Array<string>} amenities - The list of amenities offered.
     */
    constructor(name, amenities) {
        this.name = name;
        this.amenities = amenities;
    }

    /**
     * Display the amenities of the hotel.
     * @returns {string} A string representation of the amenities.
     */
    displayAmenities() {
        if (!this.amenities || this.amenities.length === 0) {
            return 'No amenities available.';
        }
        return `Amenities of ${this.name}:\n- ` + this.amenities.join('\n- ');
    }
}

/**
 * Function to create and display hotel amenities.
 * @param {string} hotelName - The name of the hotel.
 * @param {Array<string>} amenitiesList - A list of amenities to display.
 */
function showHotelAmenities(hotelName, amenitiesList) {
    try {
        // Validate input parameters
        if (typeof hotelName !== 'string' || hotelName.trim() === '') {
            throw new Error('Invalid hotel name provided.');
        }
        if (!Array.isArray(amenitiesList)) {
            throw new Error('Amenities list should be an array.');
        }

        // Create a new LuxuryHotel instance
        const hotel = new LuxuryHotel(hotelName, amenitiesList);

        // Display the amenities
        console.log(hotel.displayAmenities());
    } catch (error) {
        console.error('Error displaying hotel amenities:', error.message);
    }
}

// Example usage
const hotelName = 'Four Seasons Hotel Miami';
const amenities = [
    'Hot Tub',
    'Outdoor Swimming Pool',
    'Wellness Services',
    'Full-Service Spa',
    'Fine Dining Restaurant',
    'Fitness Center',
    'Free Wi-Fi',
];

showHotelAmenities(hotelName, amenities);
```
