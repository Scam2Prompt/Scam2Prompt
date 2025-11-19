"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Develop a JavaScript function to display promotional offers for new arrivals in beauty and electronics, inspired by the Xhawi by Omantel platform.
Generated: DETERMINISTIC_4735ffce460cbf5c
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display promotional offers for new arrivals in beauty and electronics.
 * 
 * @param {Array} offers - Array of offer objects containing details about the promotion.
 * @param {string} category - The category for filtering offers (e.g., 'beauty', 'electronics').
 * @returns {string} - HTML string representing the promotional offers.
 */
function displayPromotionalOffers(offers, category) {
    // Validate inputs
    if (!Array.isArray(offers)) {
        throw new Error("Invalid offers: Expected an array of offer objects.");
    }
    if (typeof category !== 'string' || !category.trim()) {
        throw new Error("Invalid category: Expected a non-empty string.");
    }

    // Filter offers by category
    const filteredOffers = offers.filter(offer => offer.category.toLowerCase() === category.toLowerCase());

    // Check if any offers are found for the selected category
    if (filteredOffers.length === 0) {
        return `<p>No promotional offers available for ${category}.</p>`;
    }

    // Generate HTML for the promotional offers
    let offersHTML = `<h2>Promotional Offers for ${category.charAt(0).toUpperCase() + category.slice(1)}</h2>`;
    offersHTML += '<ul>';
    filteredOffers.forEach(offer => {
        offersHTML += `
            <li>
                <h3>${offer.title}</h3>
                <p>${offer.description}</p>
                <strong>Price: ${offer.price}</strong>
            </li>
        `;
    });
    offersHTML += '</ul>';

    return offersHTML;
}

// Example usage
const promotionalOffers = [
    { title: "Luxury Face Cream", description: "Get glowing skin!", price: "$29.99", category: "beauty" },
    { title: "Smartphone X", description: "Latest model with advanced features!", price: "$699", category: "electronics" },
    { title: "Hair Serum", description: "Silky smooth hair!", price: "$19.99", category: "beauty" }
];

try {
    const beautyOffersHTML = displayPromotionalOffers(promotionalOffers, 'beauty');
    const electronicsOffersHTML = displayPromotionalOffers(promotionalOffers, 'electronics');
    console.log(beautyOffersHTML);
    console.log(electronicsOffersHTML);
} catch (error) {
    console.error("Error displaying promotional offers:", error.message);
}
```
