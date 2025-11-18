"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Write JavaScript code to dynamically update product prices on an e-commerce website based on selected options, as seen on MorevaCare's product pages.
Generated: DETERMINISTIC_2aa9e9f957a5e91f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ProductPriceUpdater class to handle dynamic price updates
class ProductPriceUpdater {
    constructor(priceElementId, options) {
        this.priceElement = document.getElementById(priceElementId);
        this.options = options;

        // Bind the updatePrice method to the current context
        this.updatePrice = this.updatePrice.bind(this);
        
        // Initialize event listeners
        this.initEventListeners();
    }

    // Initialize event listeners for option changes
    initEventListeners() {
        const optionElements = document.querySelectorAll('.product-option');
        optionElements.forEach(option => {
            option.addEventListener('change', this.updatePrice);
        });
    }

    // Update the product price based on selected options
    updatePrice() {
        try {
            let totalPrice = this.options.basePrice; // Start with the base price
            let selectedOptions = this.getSelectedOptions();

            // Calculate new price based on selected options
            selectedOptions.forEach(option => {
                const optionPrice = this.options.prices[option];
                if (optionPrice) {
                    totalPrice += optionPrice; // Add the price of the selected option
                }
            });

            // Update the price display on the page
            this.priceElement.textContent = this.formatPrice(totalPrice);
        } catch (error) {
            console.error('Error updating price:', error);
            this.priceElement.textContent = 'Error loading price'; // Fallback message
        }
    }

    // Get selected options from the form elements
    getSelectedOptions() {
        const selectedOptions = [];
        const optionElements = document.querySelectorAll('.product-option:checked');

        optionElements.forEach(option => {
            selectedOptions.push(option.value);
        });

        return selectedOptions;
    }

    // Format the price for display
    formatPrice(price) {
        return `$${price.toFixed(2)}`; // Format as currency
    }
}

// Example usage of the ProductPriceUpdater class
document.addEventListener('DOMContentLoaded', () => {
    const options = {
        basePrice: 29.99, // Base price of the product
        prices: {
            sizeSmall: 0,    // No extra charge for small size
            sizeMedium: 5,   // Extra charge for medium size
            sizeLarge: 10,    // Extra charge for large size
            colorRed: 0,     // No extra charge for red color
            colorBlue: 3,    // Extra charge for blue color
            // Add more options and their prices as needed
        }
    };

    // Initialize the ProductPriceUpdater
    new ProductPriceUpdater('product-price', options);
});
```

**HTML Structure** (for context, not included in the original request):
```html
<div>
    <h1>Product Title</h1>
    <div>
        <h2 id="product-price">$29.99</h2> <!-- Price element -->
    </div>
    <div>
        <label>
            <input type="radio" class="product-option" name="size" value="sizeSmall" checked> Small
        </label>
        <label>
            <input type="radio" class="product-option" name="size" value="sizeMedium"> Medium (+$5)
        </label>
        <label>
            <input type="radio" class="product-option" name="size" value="sizeLarge"> Large (+$10)
        </label>
    </div>
    <div>
        <label>
            <input type="radio" class="product-option" name="color" value="colorRed" checked> Red
        </label>
        <label>
            <input type="radio" class="product-option" name="color" value="colorBlue"> Blue (+$3)
        </label>
    </div>
</div>
```
