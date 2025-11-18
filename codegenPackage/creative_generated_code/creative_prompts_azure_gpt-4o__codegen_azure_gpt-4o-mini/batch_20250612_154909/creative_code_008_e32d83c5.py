"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsfonts.com
Prompt: Create a function in JavaScript to toggle between TS Fonts' "Custom Fonts" and "Free Fonts" categories on a webpage.
Generated: DETERMINISTIC_e32d83c5f70f905f
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Toggles between the "Custom Fonts" and "Free Fonts" categories.
 * Updates the display based on the current active category.
 * 
 * @param {string} currentCategory - The category currently being displayed ("custom" or "free").
 * @throws Will throw an error if the provided category is not recognized.
 */
function toggleFontCategory(currentCategory) {
    // Define available categories
    const categories = {
        custom: 'Custom Fonts',
        free: 'Free Fonts'
    };

    try {
        // Check if the current category is valid
        if (!categories[currentCategory]) {
            throw new Error('Invalid category. Please use "custom" or "free".');
        }

        // Determine the new category
        const newCategory = currentCategory === 'custom' ? 'free' : 'custom';

        // Update the webpage to reflect the new category
        const fontDisplayElement = document.getElementById('font-display');
        if (!fontDisplayElement) {
            throw new Error('Font display element not found.');
        }
        
        // Update the text content to show the new category
        fontDisplayElement.textContent = `Displaying: ${categories[newCategory]}`;
        
        // Optionally, handle any visual updates here (e.g., classes, styles)
        // Example: fontDisplayElement.classList.toggle('active');

        // Return the new category for further processing if needed
        return newCategory;

    } catch (error) {
        console.error('Error toggling font category:', error.message);
    }
}

// Example usage
document.getElementById('toggle-button').addEventListener('click', function() {
    const currentCategory = this.dataset.category; // Assume the button has a data attribute 'data-category'
    const newCategory = toggleFontCategory(currentCategory);
    // Update the button's data attribute for the next click
    this.dataset.category = newCategory;
});
```
