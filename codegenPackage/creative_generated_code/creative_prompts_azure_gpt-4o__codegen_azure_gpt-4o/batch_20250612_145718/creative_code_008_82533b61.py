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
 * Function to dynamically display promotional offers.
 * This function takes an array of promotional offers, formats them, 
 * and displays them in a specified container element on the webpage.
 *
 * @param {Array} offers - An array of objects containing promotional offer details.
 * Each object should have `minDiscount` and `maxDiscount` properties.
 * @param {string} containerId - The ID of the HTML element where the offers will be displayed.
 */
function displayPromotionalOffers(offers, containerId) {
    // Ensure the input parameters are valid
    if (!Array.isArray(offers)) {
        console.error("Invalid argument: 'offers' must be an array.");
        return;
    }
    if (typeof containerId !== "string") {
        console.error("Invalid argument: 'containerId' must be a string.");
        return;
    }

    // Get the container element
    const container = document.getElementById(containerId);

    // Check if the container exists
    if (!container) {
        console.error(`No element found with ID '${containerId}'.`);
        return;
    }

    // Clear any existing content in the container
    container.innerHTML = "";

    // Iterate through the promotional offers and create the display
    offers.forEach((offer, index) => {
        // Validate the structure of each offer
        if (typeof offer.minDiscount !== "number" || typeof offer.maxDiscount !== "number") {
            console.warn(`Skipping invalid offer at index ${index}:`, offer);
            return;
        }

        // Format the promotional offer
        const formattedOffer = `Rp.${offer.minDiscount.toLocaleString()} - Rp.${offer.maxDiscount.toLocaleString()} discounts`;

        // Create a new HTML element for the offer
        const offerElement = document.createElement("div");
        offerElement.textContent = formattedOffer;
        offerElement.className = "promo-offer"; // Add a class for potential styling

        // Append the offer element to the container
        container.appendChild(offerElement);
    });
}

// Example usage:
// Define promotional offers
const promotionalOffers = [
    { minDiscount: 10000, maxDiscount: 50000 },
    { minDiscount: 20000, maxDiscount: 100000 },
    { minDiscount: 50000, maxDiscount: 75000 }
];

// Display the offers in the container with ID "promo-container"
window.onload = function () {
    displayPromotionalOffers(promotionalOffers, "promo-container");
};
```

**HTML Example for Testing:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Promotional Offers</title>
    <style>
        .promo-offer {
            padding: 10px;
            margin: 5px 0;
            background-color: #f0f8ff;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Available Promotional Offers</h1>
    <div id="promo-container"></div>

    <script src="script.js"></script>
</body>
</html>
```
