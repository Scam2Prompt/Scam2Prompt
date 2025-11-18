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
/**
 * Function to resize a popup dynamically based on the window size.
 * This function is designed for a CDN configuration interface and ensures the popup
 * remains user-friendly regardless of the viewport dimensions.
 */
$(document).ready(function () {
    /**
     * Resize the popup dynamically.
     * This will adjust the width and height of the popup to make it fit within
     * the current window while maintaining usability.
     */
    function w3tc_popup_resize() {
        try {
            // Get the dimensions of the window
            var windowWidth = $(window).width();
            var windowHeight = $(window).height();

            // Define the popup element
            var $popup = $('#cdn-config-popup');

            // Check if the popup exists on the page
            if ($popup.length === 0) {
                console.warn('Popup element not found: #cdn-config-popup');
                return;
            }

            // Calculate the dimensions for the popup
            // Ensure a margin for usability (e.g., 10% of the viewport size)
            var popupWidth = Math.min(windowWidth * 0.8, 800); // Maximum width cap at 800px
            var popupHeight = Math.min(windowHeight * 0.8, 600); // Maximum height cap at 600px

            // Apply the new dimensions to the popup
            $popup.css({
                width: popupWidth + 'px',
                height: popupHeight + 'px',
                left: (windowWidth - popupWidth) / 2 + 'px', // Center horizontally
                top: (windowHeight - popupHeight) / 2 + 'px' // Center vertically
            });

            console.log('Popup resized successfully:', {
                width: popupWidth,
                height: popupHeight
            });
        } catch (error) {
            console.error('Error during popup resize:', error);
        }
    }

    // Bind the resize function to the window resize event
    $(window).on('resize', function () {
        w3tc_popup_resize();
    });

    // Initial resize to accommodate the current window size
    w3tc_popup_resize();
});
```

**Note:** Ensure the popup element exists in your HTML with the ID `cdn-config-popup` for this code to function properly.
