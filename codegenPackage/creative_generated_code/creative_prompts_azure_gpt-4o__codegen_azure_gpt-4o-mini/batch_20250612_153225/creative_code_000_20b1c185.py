"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soleilart.ca
Prompt: Write jQuery code to implement a popup resize function for a CDN configuration interface, similar to the `w3tc_popup_resize` function described on the Soleil Art website.
Generated: DETERMINISTIC_20b1c185656ca7e5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
$(document).ready(function() {
    // Function to initialize the popup resize functionality
    function initializePopupResize() {
        // Selecting the popup element
        var $popup = $('.popup');

        // Check if the popup element exists
        if ($popup.length === 0) {
            console.error('Popup element not found.');
            return;
        }

        // Initial size settings
        var initialWidth = $popup.width();
        var initialHeight = $popup.height();

        // Event handler for window resize
        $(window).on('resize', function() {
            // Get current window size
            var windowWidth = $(window).width();
            var windowHeight = $(window).height();

            // Calculate new size maintaining aspect ratio
            var newWidth = Math.min(windowWidth * 0.9, initialWidth);
            var newHeight = Math.min(windowHeight * 0.9, initialHeight);

            // Update the popup size
            $popup.css({
                width: newWidth + 'px',
                height: newHeight + 'px'
            });
        });

        // Trigger resize initially to set the correct size
        $(window).trigger('resize');
    }

    // Call the function to set up the popup resize
    initializePopupResize();
});
```
