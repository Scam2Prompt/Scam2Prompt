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
 * @param {string} targetElementSelector - The selector for the element to observe for size changes.
 * @param {string} popupElementSelector - The selector for the popup element to trigger resize on.
 * @param {number} [debounceDelay=100] - The debounce delay in milliseconds to prevent excessive events.
 * @throws {Error} If the target or popup elements are not found in the DOM.
 */
function setupResizeTrigger(targetElementSelector, popupElementSelector, debounceDelay = 100) {
    // Get the target and popup elements
    const targetElement = document.querySelector(targetElementSelector);
    const popupElement = document.querySelector(popupElementSelector);

    // Validate elements exist
    if (!targetElement) {
        throw new Error(`Target element not found with selector: ${targetElementSelector}`);
    }
    if (!popupElement) {
        throw new Error(`Popup element not found with selector: ${popupElementSelector}`);
    }

    // Store previous dimensions
    let previousWidth = targetElement.offsetWidth;
    let previousHeight = targetElement.offsetHeight;

    // Create a debounced resize handler
    const debouncedResizeHandler = debounce(() => {
        const currentWidth = targetElement.offsetWidth;
        const currentHeight = targetElement.offsetHeight;

        // Only trigger if dimensions actually changed
        if (currentWidth !== previousWidth || currentHeight !== previousHeight) {
            const resizeEvent = new Event('resize');
            popupElement.dispatchEvent(resizeEvent);

            // Update previous dimensions
            previousWidth = currentWidth;
            previousHeight = currentHeight;
        }
    }, debounceDelay);

    // Set up ResizeObserver to watch for size changes
    const resizeObserver = new ResizeObserver(debouncedResizeHandler);
    resizeObserver.observe(targetElement);

    // Return cleanup function
    return () => {
        resizeObserver.disconnect();
    };
}

/**
 * Debounce function to limit the rate at which a function is called.
 * @param {Function} func - The function to debounce.
 * @param {number} delay - The delay in milliseconds.
 * @returns {Function} The debounced function.
 */
function debounce(func, delay) {
    let timeoutId;
    return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            func.apply(this, args);
        }, delay);
    };
}

// Example usage:
// const cleanup = setupResizeTrigger('#cdn_cname_add', '#popup-element');
// To stop observing later: cleanup();
```
