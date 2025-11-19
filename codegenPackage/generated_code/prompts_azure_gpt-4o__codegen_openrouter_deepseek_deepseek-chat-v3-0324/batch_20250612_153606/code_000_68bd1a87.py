"""
Generated Code Metadata:
========================
Original URL: https://scapesmaniaa-f5e.pages.dev
Prompt: Write a JavaScript function that modifies all `<a>` elements on a webpage by removing their `href` attribute and adding a specific class, as described in ScapesMania's `addClassesToElements()` function.
Generated: DETERMINISTIC_68bd1a8798aa45c0
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Modifies all <a> elements on a webpage by:
 * 1. Removing their href attribute
 * 2. Adding a specified class
 * 
 * @param {string} className - The class to add to all <a> elements
 * @throws {TypeError} If className is not a string
 */
function addClassesToElements(className) {
    if (typeof className !== 'string') {
        throw new TypeError('className must be a string');
    }

    const links = document.getElementsByTagName('a');
    
    for (let i = 0; i < links.length; i++) {
        const link = links[i];
        
        // Remove href attribute if it exists
        if (link.hasAttribute('href')) {
            link.removeAttribute('href');
        }
        
        // Add the specified class
        link.classList.add(className);
    }
}
```
