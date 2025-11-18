"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Write JavaScript code to display casino bonus offers dynamically, including wagering requirements and free spins, similar to the format used on Santa Claus Casino.
Generated: DETERMINISTIC_7cfbea12a1951be6
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a class to represent a Casino Bonus Offer
class CasinoBonusOffer {
    constructor(name, wageringRequirements, freeSpins, expirationDate) {
        this.name = name; // Name of the bonus offer
        this.wageringRequirements = wageringRequirements; // Wagering requirements in times
        this.freeSpins = freeSpins; // Number of free spins
        this.expirationDate = new Date(expirationDate); // Expiration date of the offer
    }

    // Method to check if the offer is still valid
    isValid() {
        const today = new Date();
        return today < this.expirationDate; // Returns true if the offer is still valid
    }

    // Method to format the bonus offer details as a string
    formatOffer() {
        if (!this.isValid()) {
            return `${this.name} - Expired`;
        }
        return `${this.name}: ${this.wageringRequirements}x wagering, ${this.freeSpins} free spins. Expires on: ${this.expirationDate.toLocaleDateString()}`;
    }
}

// Function to display bonus offers dynamically on the web page
function displayBonusOffers(bonusOffers) {
    const offersContainer = document.getElementById('bonus-offers'); // Container to display offers
    if (!offersContainer) {
        console.error("Offers container not found in the document.");
        return; // Exit if the container is not found
    }
    
    // Clear any existing offers
    offersContainer.innerHTML = '';

    // Loop through the bonus offers and create HTML elements for each
    bonusOffers.forEach(offer => {
        const offerElement = document.createElement('div'); // Create a div for each offer
        offerElement.className = 'bonus-offer'; // Assign a class for styling
        offerElement.textContent = offer.formatOffer(); // Set the text content
        offersContainer.appendChild(offerElement); // Append the offer to the container
    });
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    // Sample bonus offers data
    const bonusOffersData = [
        new CasinoBonusOffer('Welcome Bonus', 35, 50, '2023-12-31'),
        new CasinoBonusOffer('No Deposit Bonus', 20, 20, '2023-11-15'),
        new CasinoBonusOffer('Weekend Reload Bonus', 25, 30, '2023-10-30'),
    ];

    try {
        displayBonusOffers(bonusOffersData); // Call function to display the offers
    } catch (error) {
        console.error("An error occurred while displaying bonus offers:", error);
    }
});
```

```html
<!-- HTML structure for displaying bonus offers -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casino Bonus Offers</title>
    <style>
        .bonus-offer {
            border: 1px solid #ccc;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Casino Bonus Offers</h1>
    <div id="bonus-offers"></div>
    <script src="path/to/your/script.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
