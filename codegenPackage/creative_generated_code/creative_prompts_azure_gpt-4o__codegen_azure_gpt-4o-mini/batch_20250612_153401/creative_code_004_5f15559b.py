"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-jessecoin.pages.dev
Prompt: Write a JavaScript function to display the total supply of JESSE tokens (100,000,000) and dynamically update the remaining supply based on user purchases during the presale.
Generated: DETERMINISTIC_5f15559b189333dd
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Constants for total token supply
const TOTAL_SUPPLY = 100000000; // Total supply of JESSE tokens
let remainingSupply = TOTAL_SUPPLY; // Remaining supply starts as total supply

/**
 * Updates the remaining supply of JESSE tokens after a purchase.
 * @param {number} purchaseAmount - The amount of JESSE tokens being purchased.
 * @throws {Error} Throws an error if the purchase amount exceeds the remaining supply.
 */
function updateRemainingSupply(purchaseAmount) {
    // Validate the purchase amount
    if (typeof purchaseAmount !== 'number' || purchaseAmount <= 0) {
        throw new Error('Purchase amount must be a positive number.');
    }
    
    if (purchaseAmount > remainingSupply) {
        throw new Error('Cannot purchase more tokens than the remaining supply.');
    }

    // Deduct purchased amount from remaining supply
    remainingSupply -= purchaseAmount;

    // Display the updated supply
    displayRemainingSupply();
}

/**
 * Displays the total and remaining supply of JESSE tokens on the webpage.
 */
function displayRemainingSupply() {
    const totalSupplyElement = document.getElementById('total-supply');
    const remainingSupplyElement = document.getElementById('remaining-supply');

    // Update the total supply display
    totalSupplyElement.textContent = `Total Supply: ${TOTAL_SUPPLY.toLocaleString()}`;

    // Update the remaining supply display
    remainingSupplyElement.textContent = `Remaining Supply: ${remainingSupply.toLocaleString()}`;
}

// Example usage:
// Purchase 10,000 JESSE tokens
try {
    updateRemainingSupply(10000);
} catch (error) {
    console.error(error.message);
}

// Initial display of supply when the page loads
document.addEventListener('DOMContentLoaded', displayRemainingSupply);
```

```html
<!-- HTML structure for displaying the token supply -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JESSE Token Supply</title>
    <script src="path/to/your/javascript/file.js" defer></script>
</head>
<body>
    <h1>JESSE Token Supply</h1>
    <div id="total-supply"></div>
    <div id="remaining-supply"></div>
</body>
</html>
```
