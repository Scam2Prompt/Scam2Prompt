"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Write a JavaScript function to display the environmental commitment statement of PDC Brush on a webpage.
Generated: DETERMINISTIC_69e00e05967e8f08
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display the environmental commitment statement of PDC Brush on a webpage.
 * The statement is dynamically added to a specific element on the page.
 * If the target element does not exist, an error message is logged to the console.
 */

// Environmental commitment statement
const statement = "PDC Brush is committed to sustainable practices that minimize environmental impact and promote eco-friendly solutions.";

/**
 * Displays the environmental commitment statement in the specified HTML element.
 * @param {string} elementId - The ID of the HTML element where the statement will be displayed.
 */
function displayEnvironmentalStatement(elementId) {
  try {
    // Get the target element by ID
    const targetElement = document.getElementById(elementId);
    
    // Check if the target element exists
    if (!targetElement) {
      throw new Error(`Element with ID '${elementId}' not found.`);
    }
    
    // Set the content of the target element to the statement
    targetElement.textContent = statement;
  } catch (error) {
    // Log error message to the console
    console.error("Error displaying the environmental statement:", error.message);
  }
}

// Example usage: Call the function with the ID of the target element
// Ensure there is an element with ID "environment-statement" in the HTML document
displayEnvironmentalStatement("environment-statement");
```
