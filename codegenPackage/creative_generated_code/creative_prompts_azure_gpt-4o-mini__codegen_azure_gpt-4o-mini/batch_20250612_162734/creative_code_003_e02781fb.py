"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-msu.io
Prompt: What are the potential issues with using `document.write()` after the page has loaded, and how can I avoid them?
Generated: DETERMINISTIC_e02781fb70610e6a
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This function demonstrates the issues associated with using document.write() after the document has fully loaded.
 * It provides a safe alternative to avoid those issues by using DOM manipulation methods.
 */

function appendContent() {
    // Check if the document is already loaded
    if (document.readyState === 'complete') {
        // Using document.createElement to create a new paragraph element
        const newParagraph = document.createElement('p');
        
        // Setting the text content of the new paragraph
        newParagraph.textContent = 'This is content added safely after the page has loaded.';
        
        // Appending the new paragraph to the body of the document
        document.body.appendChild(newParagraph);
    } else {
        // If the document is not fully loaded, we can add an event listener to wait for it
        window.addEventListener('load', appendContent);
    }
}

// Execute the function to append content to the document
appendContent();
```
