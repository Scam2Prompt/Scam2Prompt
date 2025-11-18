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
 * Modifies all <a> elements on the webpage.
 * - Removes the `href` attribute from each <a> element.
 * - Adds a specific class to each <a> element.
 *
 * @param {string} className - The class name to add to each <a> element.
 */
function addClassesToElements(className) {
  try {
    // Validate the input
    if (typeof className !== 'string' || className.trim() === '') {
      throw new Error('Invalid class name. Please provide a non-empty string.');
    }

    // Select all <a> elements on the page
    const anchorElements = document.querySelectorAll('a');

    // Iterate through each <a> element and modify it
    anchorElements.forEach(anchor => {
      // Remove the 'href' attribute
      anchor.removeAttribute('href');

      // Add the specified class
      anchor.classList.add(className);
    });
  } catch (error) {
    // Log any errors encountered during execution
    console.error('Error modifying <a> elements:', error.message);
  }
}
```

Usage example:
```javascript
// Call the function to modify all <a> elements, adding the class "disabled-link"
addClassesToElements('disabled-link');
```
