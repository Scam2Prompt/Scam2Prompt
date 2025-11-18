"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miniapp.starsbot.xyz
Prompt: Create a JavaScript function that dynamically updates the price of stars and TON equivalent based on user input, similar to the StarsBot interface.
Generated: DETERMINISTIC_305e5a3e3ef7a869
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to update the price of stars and TON equivalent based on user input
function updatePrice() {
    // Get the user input for the number of stars
    const starsInput = document.getElementById('starsInput');
    const tonPriceInput = document.getElementById('tonPriceInput');
    
    // Validate the user inputs
    if (!starsInput || !tonPriceInput) {
        console.error('Input elements not found in the DOM');
        return;
    }

    const stars = parseFloat(starsInput.value);
    const tonPrice = parseFloat(tonPriceInput.value);

    // Check if the parsed values are valid numbers
    if (isNaN(stars) || isNaN(tonPrice) || stars < 0 || tonPrice < 0) {
        console.error('Invalid input: Please enter positive numbers for stars and TON price');
        return;
    }

    // Update the price display for stars and TON equivalent
    const starsPrice = stars * tonPrice; // Calculate total price in TON
    const tonEquivalent = stars / tonPrice; // Calculate equivalent stars for a given TON price

    // Update the DOM with the calculated values
    document.getElementById('starsPriceDisplay').innerText = `Price in TON: ${starsPrice.toFixed(2)} TON`;
    document.getElementById('tonEquivalentDisplay').innerText = `Equivalent Stars: ${tonEquivalent.toFixed(2)} Stars`;
}

// Event listeners to trigger updatePrice function on input change
document.getElementById('starsInput').addEventListener('input', updatePrice);
document.getElementById('tonPriceInput').addEventListener('input', updatePrice);
```

```html
<!-- HTML Structure for input fields -->
<div>
    <label for="starsInput">Enter number of stars:</label>
    <input type="number" id="starsInput" min="0" step="0.01" />
</div>
<div>
    <label for="tonPriceInput">Enter TON price:</label>
    <input type="number" id="tonPriceInput" min="0" step="0.01" />
</div>
<div>
    <p id="starsPriceDisplay">Price in TON: 0.00 TON</p>
    <p id="tonEquivalentDisplay">Equivalent Stars: 0.00 Stars</p>
</div>
```
