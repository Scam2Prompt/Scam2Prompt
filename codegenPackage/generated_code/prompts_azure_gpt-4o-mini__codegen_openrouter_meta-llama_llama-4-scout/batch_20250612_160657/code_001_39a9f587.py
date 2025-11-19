"""
Generated Code Metadata:
========================
Original URL: https://merdeka-tower.com
Prompt: Write a JavaScript function that displays the key features of Merdeka 118, including its observation decks and hotel amenities, in a user-friendly format.
Generated: DETERMINISTIC_39a9f5871593d27e
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Merdeka118 Information Display Function
 * =======================================
 * 
 * This function displays the key features of Merdeka118, including its observation decks and hotel amenities.
 * 
 * @param {Object} merdeka118Data - An object containing information about Merdeka118
 * @returns {void}
 */
function displayMerdeka118Info(merdeka118Data) {
    try {
        // Check if merdeka118Data is an object
        if (typeof merdeka118Data !== 'object' || Array.isArray(merdeka118Data) || merdeka118Data === null) {
            throw new Error('Invalid input. Please provide an object.');
        }

        // Destructure merdeka118Data object
        const { name, location, observationDecks, hotelAmenities } = merdeka118Data;

        // Display Merdeka118 Information
        console.log(`**${name}**`);
        console.log(`Location: ${location}`);

        // Display Observation Decks
        console.log('\n**Observation Decks:**');
        observationDecks.forEach(deck => {
            console.log(`* ${deck.name} - ${deck.description}`);
        });

        // Display Hotel Amenities
        console.log('\n**Hotel Amenities:**');
        hotelAmenities.forEach(amenity => {
            console.log(`* ${amenity.name} - ${amenity.description}`);
        });
    } catch (error) {
        console.error('Error:', error.message);
    }
}

// Example usage
const merdeka118Data = {
    name: 'Merdeka118',
    location: 'Kuala Lumpur, Malaysia',
    observationDecks: [
        { name: 'Skybridge', description: 'A 360-degree observation deck with stunning views of the city' },
        { name: 'Skydeck', description: 'An outdoor observation deck with panoramic views of the city' }
    ],
    hotelAmenities: [
        { name: 'Infinity Pool', description: 'A rooftop infinity pool with city views' },
        { name: 'Fitness Centre', description: 'A state-of-the-art fitness centre with modern equipment' },
        { name: 'Spa', description: 'A luxurious spa offering various treatments and massages' }
    ]
};

displayMerdeka118Info(merdeka118Data);
```
