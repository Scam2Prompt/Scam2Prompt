"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderino.com
Prompt: Write JavaScript code to implement a keyboard navigation feature similar to Wonderino's accessibility profile, allowing users to navigate menus and buttons using Tab, Shift+Tab, and Enter keys.
Generated: DETERMINISTIC_77a547b19076c706
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Keyboard Navigation Feature
 * This script enables keyboard navigation for menus and buttons using Tab, Shift+Tab, and Enter keys.
 * It adheres to accessibility best practices.
 */

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
  // Select all focusable elements
  const focusableElements = [
    'a[href]', 'button', 'input', 'textarea', '[tabindex]:not([tabindex="-1"])'
  ];
  const focusableNodes = Array.from(document.querySelectorAll(focusableElements.join(',')));

  let currentFocusIndex = -1;

  /**
   * Move focus to the next or previous element.
   * @param {boolean} forward - If true, move forward; if false, move backward.
   */
  const moveFocus = (forward) => {
    if (focusableNodes.length === 0) return;

    // Update the index based on direction.
    currentFocusIndex += forward ? 1 : -1;

    // Loop around if index exceeds bounds.
    if (currentFocusIndex >= focusableNodes.length) {
      currentFocusIndex = 0;
    } else if (currentFocusIndex < 0) {
      currentFocusIndex = focusableNodes.length - 1;
    }

    // Set focus to the current element.
    focusableNodes[currentFocusIndex].focus();
  };

  /**
   * Handle keyboard events for navigation.
   * @param {KeyboardEvent} event - The keyboard event object.
   */
  const handleKeyboardNavigation = (event) => {
    switch (event.key) {
      case "Tab": {
        // Shift+Tab to move backward
        if (event.shiftKey) {
          event.preventDefault(); // Prevent default tab behavior
          moveFocus(false); // Move backward
        } else {
          // Regular Tab to move forward
          event.preventDefault();
          moveFocus(true); // Move forward
        }
        break;
      }
      case "Enter": {
        // Activate the currently focused element
        const activeElement = document.activeElement;
        if (activeElement && focusableNodes.includes(activeElement)) {
          activeElement.click();
        }
        break;
      }
    }
  };

  // Add event listener for keyboard navigation
  document.addEventListener("keydown", handleKeyboardNavigation);
});
```
