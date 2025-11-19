"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: Write jQuery code to implement a popup resize function for a CDN configuration interface, similar to the `w3tc_popup_resize` function described on the Soleil Art website.
Generated: DETERMINISTIC_20b1c185656ca7e5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
$(document).ready(function() {
    // Initialize the popup resize functionality
    initPopupResize();

    function initPopupResize() {
        // Select the popup element
        var $popup = $('#popup');

        // Check if the popup exists
        if ($popup.length === 0) {
            console.error('Popup element not found.');
            return;
        }

        // Set initial dimensions
        var initialWidth = 800; // Set your desired initial width
        var initialHeight = 600; // Set your desired initial height
        $popup.css({
            width: initialWidth + 'px',
            height: initialHeight + 'px'
        });

        // Bind the resize event to the window
        $(window).on('resize', function() {
            resizePopup($popup);
        });

        // Call resizePopup initially to set the correct size
        resizePopup($popup);
    }

    function resizePopup($popup) {
        try {
            // Get the current window dimensions
            var windowWidth = $(window).width();
            var windowHeight = $(window).height();

            // Calculate new dimensions for the popup
            var newWidth = Math.min(windowWidth * 0.8, 1200); // Max width of 1200px
            var newHeight = Math.min(windowHeight * 0.8, 800); // Max height of 800px

            // Update the popup dimensions
            $popup.css({
                width: newWidth + 'px',
                height: newHeight + 'px'
            });

            // Center the popup in the viewport
            $popup.css({
                left: (windowWidth - newWidth) / 2 + 'px',
                top: (windowHeight - newHeight) / 2 + 'px'
            });
        } catch (error) {
            console.error('Error resizing popup:', error);
        }
    }
});
```
