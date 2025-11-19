"""
Generated Code Metadata:
========================
Original URL: https://msus.io
Prompt: Explain the potential issues with using `document.write()` after the page has loaded and suggest alternatives.
Generated: DETERMINISTIC_f7f8270ec3c21c1b
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Write Example</title>
</head>
<body>
    <h1 id="header">Initial Header</h1>
    <script src="script.js" defer></script>
</body>
</html>
```

```javascript
// script.js
/**
 * Demonstrates the potential issues with using document.write() after the page has loaded.
 * 
 * @author [Your Name]
 */

// Function to demonstrate document.write() issues
function demonstrateDocumentWriteIssues() {
    try {
        // Attempt to use document.write() after page load
        document.write("<h2>Injected Header</h2>");
    } catch (error) {
        console.error("Error using document.write():", error);
    }
}

// Function to suggest alternatives to document.write()
function suggestAlternatives() {
    // Using innerHTML to inject content
    const headerElement = document.getElementById("header");
    headerElement.innerHTML = "Updated Header";

    // Using createElement and appendChild to inject content
    const injectedHeader = document.createElement("h2");
    injectedHeader.textContent = "Injected Header";
    document.body.appendChild(injectedHeader);
}

// Call the functions
document.addEventListener("DOMContentLoaded", () => {
    console.log("Page has finished loading.");
    demonstrateDocumentWriteIssues();
    suggestAlternatives();
});
```
