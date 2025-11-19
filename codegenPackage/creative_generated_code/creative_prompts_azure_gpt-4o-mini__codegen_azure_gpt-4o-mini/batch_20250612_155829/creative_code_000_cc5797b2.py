"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getrise.pro
Prompt: Generate a JavaScript code snippet to enable RainBNB functionality on a web application.
Generated: DETERMINISTIC_cc5797b229daed6d
Batch ID: 20250612_155829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * RainBNB Class to handle RainBNB functionality
 */
class RainBNB {
    constructor() {
        this.locations = []; // Array to hold available locations
    }

    /**
     * Adds a new location to the RainBNB listings.
     * @param {Object} location - The location object containing details.
     * @throws {Error} Will throw an error if the location is invalid.
     */
    addLocation(location) {
        if (!this.validateLocation(location)) {
            throw new Error("Invalid location: Please provide a valid location object.");
        }
        this.locations.push(location);
        console.log("Location added successfully:", location);
    }

    /**
     * Validates the location object.
     * @param {Object} location - The location object to validate.
     * @returns {boolean} True if valid, otherwise false.
     */
    validateLocation(location) {
        return location && typeof location.name === 'string' && typeof location.price === 'number';
    }

    /**
     * Searches for available locations based on price range.
     * @param {number} minPrice - Minimum price for search.
     * @param {number} maxPrice - Maximum price for search.
     * @returns {Array} Array of found locations within the price range.
     */
    searchLocations(minPrice, maxPrice) {
        if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
            throw new Error("Invalid price range: Please provide valid numbers.");
        }
        return this.locations.filter(location => location.price >= minPrice && location.price <= maxPrice);
    }

    /**
     * Displays all available locations in the console.
     */
    displayLocations() {
        if (this.locations.length === 0) {
            console.log("No locations available.");
            return;
        }
        console.log("Available Locations:");
        this.locations.forEach((location, index) => {
            console.log(`${index + 1}: ${location.name} - $${location.price}`);
        });
    }
}

// Example usage
try {
    const rainBNB = new RainBNB();
    
    // Adding locations
    rainBNB.addLocation({ name: "Beach House", price: 150 });
    rainBNB.addLocation({ name: "Mountain Cabin", price: 120 });

    // Displaying locations
    rainBNB.displayLocations();

    // Searching locations within a price range
    const affordableLocations = rainBNB.searchLocations(100, 150);
    console.log("Affordable Locations:", affordableLocations);
} catch (error) {
    console.error("Error:", error.message);
}
```
