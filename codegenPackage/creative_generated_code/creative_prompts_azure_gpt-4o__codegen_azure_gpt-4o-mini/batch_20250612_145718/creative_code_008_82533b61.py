"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aakashapps.org
Prompt: Write a JavaScript function to display promotional offers dynamically, such as "Rp.10,000 - Rp.100,000 discounts," as mentioned on the website.
Generated: DETERMINISTIC_82533b61e9d5f8bc
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display promotional offers dynamically.
 * This function generates a list of discount offers and displays them in the specified HTML element.
 * 
 * @param {HTMLElement} displayElement - The HTML element where the offers will be displayed.
 * @param {Array<{min: number, max: number}>} offers - Array of offers, each with a minimum and maximum discount.
 * @throws Will throw an error if the displayElement is not a valid HTMLElement.
 */
function displayPromotionalOffers(displayElement, offers) {
    // Validate that displayElement is a valid HTMLElement
    if (!(displayElement instanceof HTMLElement)) {
        throw new Error('Invalid display element. Must be a valid HTMLElement.');
    }
    
    // Clear previous offers
    displayElement.innerHTML = '';

    // Check if offers array is valid
    if (!Array.isArray(offers) || offers.length === 0) {
        displayElement.innerHTML = '<p>No promotional offers available.</p>';
        return;
    }

    // Iterate through the offers and create HTML elements to display them
    offers.forEach(offer => {
        // Validate each offer object
        if (typeof offer.min !== 'number' || typeof offer.max !== 'number' || offer.min < 0 || offer.max < offer.min) {
            console.warn('Invalid offer detected:', offer);
            return; // Skip invalid offers
        }

        // Create offer string
        const offerString = `Rp.${offer.min.toLocaleString()} - Rp.${offer.max.toLocaleString()} discounts`;
        
        // Create a new paragraph element for the offer
        const offerElement = document.createElement('p');
        offerElement.textContent = offerString;

        // Append the offer element to the display element
        displayElement.appendChild(offerElement);
    });
}

// Example usage:
const offers = [
    { min: 10000, max: 100000 },
    { min: 20000, max: 50000 },
    { min: 50000, max: 100000 },
];

// Assuming there is an HTML element with the id of 'promotions'
const promotionsContainer = document.getElementById('promotions');
displayPromotionalOffers(promotionsContainer, offers);
```
