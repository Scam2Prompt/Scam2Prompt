"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-52--gracious-swanson-bcc8c1.netlify.app
Prompt: Create a JavaScript function that toggles the visibility of a portfolio section in a front-end engineer's website, like the one Tim Mansell uses.
Generated: DETERMINISTIC_efd288dd87bd16ce
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Toggles the visibility of the portfolio section.
 * This function adds/removes the 'hidden' class to show or hide the portfolio.
 * 
 * @param {string} portfolioSelector - The CSS selector for the portfolio section.
 * @param {string} toggleButtonSelector - The CSS selector for the button that triggers the toggle.
 */
function togglePortfolioVisibility(portfolioSelector, toggleButtonSelector) {
    try {
        // Select the portfolio section and the toggle button
        const portfolio = document.querySelector(portfolioSelector);
        const toggleButton = document.querySelector(toggleButtonSelector);

        // Check if portfolio and button exist in the DOM
        if (!portfolio) {
            throw new Error(`Portfolio section not found: ${portfolioSelector}`);
        }
        if (!toggleButton) {
            throw new Error(`Toggle button not found: ${toggleButtonSelector}`);
        }

        // Define the function to toggle visibility
        const toggleVisibility = () => {
            portfolio.classList.toggle('hidden');
        };

        // Add click event listener to the toggle button
        toggleButton.addEventListener('click', toggleVisibility);
    } catch (error) {
        console.error('Error toggling portfolio visibility:', error.message);
    }
}

// Example usage
// Ensure you replace '.portfolio' and '.toggle-button' with the actual selectors used in your HTML
togglePortfolioVisibility('.portfolio', '.toggle-button');
```

```css
/* Add this to your CSS to hide the portfolio when the 'hidden' class is applied */
.hidden {
    display: none;
}
```
