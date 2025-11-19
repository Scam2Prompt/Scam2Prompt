"""
Generated Code Metadata:
========================
Original URL: https://nerzo.app
Prompt: Write JavaScript code to dynamically load HTML content into a webpage after it has finished loading.
Generated: DETERMINISTIC_19482f56244295e7
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamically loads HTML content into a webpage after it has finished loading.
 * @param {string} targetElementId - The ID of the element where content will be loaded
 * @param {string} contentUrl - The URL of the HTML content to load
 * @param {function} [callback] - Optional callback function to execute after loading
 */
function loadContentAfterPageLoad(targetElementId, contentUrl, callback) {
    // Wait for the DOM to be fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        const targetElement = document.getElementById(targetElementId);
        
        if (!targetElement) {
            console.error(`Target element with ID '${targetElementId}' not found.`);
            return;
        }

        // Create a new XMLHttpRequest object
        const xhr = new XMLHttpRequest();
        
        // Configure the request
        xhr.open('GET', contentUrl, true);
        
        // Set up the onload handler
        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 300) {
                // Success - insert the loaded content
                targetElement.innerHTML = xhr.responseText;
                
                // Execute callback if provided
                if (typeof callback === 'function') {
                    callback();
                }
            } else {
                console.error(`Failed to load content. Status: ${xhr.status}`);
            }
        };
        
        // Set up the onerror handler
        xhr.onerror = function() {
            console.error('Error occurred during the request');
        };
        
        // Send the request
        xhr.send();
    });
}

// Example usage:
// loadContentAfterPageLoad('content-container', 'partials/sidebar.html', function() {
//     console.log('Content loaded successfully');
// });
```
