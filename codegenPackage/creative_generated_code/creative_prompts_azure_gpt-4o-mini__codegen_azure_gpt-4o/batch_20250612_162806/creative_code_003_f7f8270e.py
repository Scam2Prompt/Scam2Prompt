"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msus.io
Prompt: Explain the potential issues with using `document.write()` after the page has loaded and suggest alternatives.
Generated: DETERMINISTIC_f7f8270ec3c21c1b
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to demonstrate the issues with `document.write()` and alternatives
(function () {
  // Issue: Using `document.write()` after the page has fully loaded will overwrite the entire document,
  // removing all existing content.
  try {
    // Example of using `document.write()` improperly after the page load
    document.write("<p>This will overwrite the entire document!</p>");
  } catch (error) {
    console.error("Error: Unable to use document.write() after page load.", error);
  }

  // Alternative: Use DOM manipulation via JavaScript for dynamic content updates
  function addContentSafely() {
    // Get the target element where new content will be added
    const targetElement = document.getElementById("content");

    // Ensure the target element exists
    if (!targetElement) {
      console.error("Error: Target element not found in the document.");
      return;
    }

    // Create a new paragraph element
    const newParagraph = document.createElement("p");
    newParagraph.textContent = "This is a safer way to add content dynamically.";

    // Append the new paragraph to the target element
    targetElement.appendChild(newParagraph);
  }

  // Execute the function to add content safely
  addContentSafely();

  // Alternative: Use innerHTML if content needs to be replaced, but be mindful of potential security risks
  function replaceContentSafely() {
    // Get the target element
    const targetElement = document.getElementById("content");

    // Ensure the target element exists
    if (!targetElement) {
      console.error("Error: Target element not found in the document.");
      return;
    }

    // Replace the inner HTML of the target element
    targetElement.innerHTML = "<p>This content has been replaced safely using innerHTML.</p>";

    // Note: Ensure any user-generated content is sanitized to prevent XSS attacks.
  }

  // Execute the function to replace content safely
  replaceContentSafely();
})();

/*
  HTML Structure for Testing:
  <div id="content">
    <p>Original content in the target element.</p>
  </div>
*/
```
