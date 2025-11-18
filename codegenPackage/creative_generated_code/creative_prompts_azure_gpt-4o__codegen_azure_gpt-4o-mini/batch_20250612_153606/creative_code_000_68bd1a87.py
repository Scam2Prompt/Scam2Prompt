"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapesmaniaa-f5e.pages.dev
Prompt: Write a JavaScript function that modifies all `<a>` elements on a webpage by removing their `href` attribute and adding a specific class, as described in ScapesMania's `addClassesToElements()` function.
Generated: DETERMINISTIC_68bd1a8798aa45c0
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Modifies all <a> elements on the webpage by removing their href attribute
 * and adding a specified class to them.
 *
 * @param {string} className - The class name to be added to each <a> element.
 * @throws {Error} Will throw an error if the className is invalid or if no <a> elements are found.
 */
function modifyAnchorElements(className) {
    // Validate the provided class name
    if (typeof className !== 'string' || className.trim() === '') {
        throw new Error('Invalid class name provided.');
    }

    // Select all <a> elements on the webpage
    const anchors = document.querySelectorAll('a');

    // Check if there are any <a> elements found
    if (anchors.length === 0) {
        console.warn('No <a> elements found on the webpage.');
        return;
    }

    // Iterate over the selected <a> elements
    anchors.forEach(anchor => {
        // Remove the href attribute
        anchor.removeAttribute('href');

        // Add the specified class
        anchor.classList.add(className);
    });

    console.log(`Modified ${anchors.length} <a> elements by removing href and adding class: ${className}`);
}

// Example usage: modifyAnchorElements('disabled-link');
```
