"""
Generated Code Metadata:
========================
Original URL: https://westbengalrealestates.com
Prompt: "Create a JavaScript function to calculate the affordability of a property based on factors like price, location, and amenities, using data from a website like westbengalrealestates.com."
Generated: DETERMINISTIC_298bfb1106bda3d8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the affordability of a property based on its price, location, and amenities.
 * 
 * @param {Object} propertyData - The data of the property.
 * @param {number} propertyData.price - The price of the property.
 * @param {string} propertyData.location - The location of the property.
 * @param {Array<string>} propertyData.amenities - The amenities of the property.
 * @returns {Object} An object containing the affordability score and a message.
 */

function calculateAffordability(propertyData) {
    try {
        // Check if propertyData is an object
        if (typeof propertyData !== 'object' || Array.isArray(propertyData) || propertyData === null) {
            throw new Error('Property data must be an object');
        }

        // Check if required properties exist
        if (!('price' in propertyData) || !('location' in propertyData) || !('amenities' in propertyData)) {
            throw new Error('Property data must contain price, location, and amenities');
        }

        // Define location scores
        const locationScores = {
            'kolkata': 1,
            'dhanbad': 0.8,
            'siliguri': 0.7,
            // Add more locations as needed
        };

        // Define amenity scores
        const amenityScores = {
            'gym': 0.05,
            'swimming pool': 0.03,
            'security': 0.02,
            'park': 0.01,
            // Add more amenities as needed
        };

        // Calculate location score
        let locationScore = locationScores[propertyData.location.toLowerCase()] || 0;

        // Calculate amenity score
        let amenityScore = propertyData.amenities.reduce((acc, amenity) => acc + (amenityScores[amenity.toLowerCase()] || 0), 0);

        // Calculate affordability score
        let affordabilityScore = propertyData.price * (1 - locationScore - amenityScore);

        // Determine affordability message
        let affordabilityMessage;
        if (affordabilityScore < 0) {
            affordabilityMessage = 'Very affordable';
        } else if (affordabilityScore < 500000) {
            affordabilityMessage = 'Affordable';
        } else if (affordabilityScore < 1000000) {
            affordabilityMessage = 'Moderately priced';
        } else {
            affordabilityMessage = 'Expensive';
        }

        // Return affordability data
        return {
            affordabilityScore,
            affordabilityMessage,
        };
    } catch (error) {
        // Log and rethrow error
        console.error('Error calculating affordability:', error);
        throw error;
    }
}

// Example usage:
const propertyData = {
    price: 750000,
    location: 'Kolkata',
    amenities: ['gym', 'security', 'park'],
};

const affordabilityData = calculateAffordability(propertyData);
console.log(affordabilityData);
```
