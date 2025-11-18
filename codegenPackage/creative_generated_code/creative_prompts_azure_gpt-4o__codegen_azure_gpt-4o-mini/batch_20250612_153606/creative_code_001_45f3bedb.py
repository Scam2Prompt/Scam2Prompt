"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapesmaniaa-f5e.pages.dev
Prompt: Generate code to periodically execute a function every 300 milliseconds that adds a specific class to `<div>` elements, excluding certain classes, similar to the functionality described on the ScapesMania website.
Generated: DETERMINISTIC_45f3bedbd02c59f0
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to periodically add a specific class to <div> elements
// while excluding certain classes
(function() {
    // Class to be added
    const classToAdd = 'highlight';
    // Classes to exclude
    const excludedClasses = ['exclude-this', 'do-not-add', 'another-exclude'];

    // Function to add class to eligible <div> elements
    function addClassToDivs() {
        // Select all <div> elements on the page
        const divElements = document.querySelectorAll('div');

        // Iterate through each <div> element
        divElements.forEach(div => {
            // Check if the <div> does not have any excluded classes
            const hasExcludedClass = excludedClasses.some(excludedClass =>
                div.classList.contains(excludedClass)
            );

            // If the <div> does not have excluded classes, add the new class
            if (!hasExcludedClass) {
                div.classList.add(classToAdd);
            }
        });
    }

    // Setting an interval to execute the function every 300 milliseconds
    const interval = 300;

    // Execute the function initially
    addClassToDivs();

    // Use setInterval to run the function periodically
    const intervalId = setInterval(() => {
        try {
            addClassToDivs();
        } catch (error) {
            console.error('Error executing addClassToDivs:', error);
            // Clear the interval on error to prevent further execution
            clearInterval(intervalId);
        }
    }, interval);

    // Clean up the interval when no longer needed (optional)
    // You can call clearInterval(intervalId) when appropriate in your code
})();
```
