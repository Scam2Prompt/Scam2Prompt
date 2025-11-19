"""
Generated Code Metadata:
========================
Original URL: https://scapesmaniaa-f5e.pages.dev
Prompt: Write a JavaScript function to add a 'connectButton' class to all links and buttons on a webpage, except for those with specific classes, similar to the `addClassesToElements` function on the ScapesMania website.
Generated: DETERMINISTIC_1bf09e3ec595c672
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Adds the 'connectButton' class to all links (<a>) and buttons (<button>) on the webpage,
 * except for elements that already have specific classes to exclude.
 * 
 * @param {Array<string>} excludeClasses - An array of class names to exclude from modification.
 */
function addConnectButtonClass(excludeClasses = []) {
    try {
        // Validate input
        if (!Array.isArray(excludeClasses)) {
            throw new TypeError("excludeClasses must be an array of strings.");
        }

        // Combine links (<a>) and buttons (<button>) into a single NodeList
        const elements = document.querySelectorAll('a, button');

        elements.forEach(element => {
            // Check if the element has any of the excluded classes
            const hasExcludedClass = excludeClasses.some(excludeClass => 
                element.classList.contains(excludeClass)
            );

            // Add 'connectButton' class if no excluded class is found
            if (!hasExcludedClass) {
                element.classList.add('connectButton');
            }
        });
    } catch (error) {
        console.error("An error occurred while adding the 'connectButton' class:", error);
    }
}

// Example usage:
// Exclude elements with the classes 'no-connect' and 'special-button'
addConnectButtonClass(['no-connect', 'special-button']);
```
