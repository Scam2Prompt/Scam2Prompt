"""
Generated Code Metadata:
========================
Original URL: https://claim-msu.io
Prompt: What are the potential issues with using `document.write()` after the page has loaded, and how can I avoid them?
Generated: DETERMINISTIC_e02781fb70610e6a
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a JavaScript code snippet demonstrating alternatives to `document.write()` with proper error handling:

```javascript
/**
 * Safe alternatives to document.write() for dynamic content injection
 */

// Method 1: Using DOM manipulation
function appendContentSafely(content) {
    try {
        const element = document.createElement('div');
        element.innerHTML = content;
        document.body.appendChild(element);
    } catch (error) {
        console.error('Error appending content:', error);
    }
}

// Method 2: Using textContent for text-only injection
function appendTextSafely(text) {
    try {
        const element = document.createElement('p');
        element.textContent = text;
        document.body.appendChild(element);
    } catch (error) {
        console.error('Error appending text:', error);
    }
}

// Method 3: Using insertAdjacentHTML for more control over position
function insertHTMLSafely(position, elementId, html) {
    try {
        const container = document.getElementById(elementId);
        if (!container) {
            throw new Error(`Element with ID ${elementId} not found`);
        }
        container.insertAdjacentHTML(position, html);
    } catch (error) {
        console.error('Error inserting HTML:', error);
    }
}

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
    // Using DOM manipulation
    appendContentSafely('<h1>Safe Content Injection</h1>');
    
    // Using textContent
    appendTextSafely('This text was added safely after page load.');
    
    // Using insertAdjacentHTML
    insertHTMLSafely('beforeend', 'some-container', '<div>Inserted at end of container</div>');
});
```
