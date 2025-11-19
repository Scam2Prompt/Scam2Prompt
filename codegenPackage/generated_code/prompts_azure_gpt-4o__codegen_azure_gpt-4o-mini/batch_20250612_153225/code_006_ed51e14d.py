"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: Create a JavaScript function that triggers a resize event for a popup element when a specific DOM element changes size, similar to the `#cdn_cname_add` event listener described on the Soleil Art site.
Generated: DETERMINISTIC_ed51e14d55bd47d5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Triggers a resize event for a popup element when a specific DOM element changes size.
 * 
 * @param {string} targetSelector - The CSS selector for the target element to observe.
 * @param {string} popupSelector - The CSS selector for the popup element to resize.
 */
function observeElementResize(targetSelector, popupSelector) {
    // Select the target element and the popup element
    const targetElement = document.querySelector(targetSelector);
    const popupElement = document.querySelector(popupSelector);

    // Check if the target element and popup element exist
    if (!targetElement || !popupElement) {
        console.error('Target or popup element not found.');
        return;
    }

    // Create a ResizeObserver to monitor size changes of the target element
    const resizeObserver = new ResizeObserver(() => {
        // Trigger a custom resize event on the popup element
        const resizeEvent = new Event('resize');
        popupElement.dispatchEvent(resizeEvent);
    });

    // Start observing the target element for size changes
    resizeObserver.observe(targetElement);

    // Optional: Clean up the observer when the popup is closed or no longer needed
    const cleanupObserver = () => {
        resizeObserver.unobserve(targetElement);
        resizeObserver.disconnect();
        popupElement.removeEventListener('close', cleanupObserver);
    };

    // Listen for a custom 'close' event on the popup to clean up the observer
    popupElement.addEventListener('close', cleanupObserver);
}

// Example usage
// observeElementResize('#targetElement', '#popupElement');
```
