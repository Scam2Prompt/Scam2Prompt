"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soleilart.ca
Prompt: Generate a jQuery function that handles the resizing of a lightbox for CDN configuration in WordPress.
Generated: DETERMINISTIC_cfd8271426d0699c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * jQuery function to handle resizing of a lightbox for CDN configuration in WordPress.
 * Ensures the lightbox adjusts dynamically based on the window size.
 */
(function ($) {
    'use strict';

    // Wait for the DOM to fully load
    $(document).ready(function () {
        /**
         * Function to resize the lightbox dynamically based on the window size.
         */
        function resizeLightbox() {
            try {
                // Select the lightbox element
                var $lightbox = $('.lightbox');

                // Ensure the lightbox exists on the page
                if ($lightbox.length === 0) {
                    console.warn('Lightbox element not found.');
                    return;
                }

                // Get the current window dimensions
                var windowWidth = $(window).width();
                var windowHeight = $(window).height();

                // Calculate new dimensions for the lightbox
                var lightboxWidth = Math.min(windowWidth * 0.8, 800); // Max width: 800px, or 80% of window width
                var lightboxHeight = Math.min(windowHeight * 0.8, 600); // Max height: 600px, or 80% of window height

                // Apply the new dimensions to the lightbox
                $lightbox.css({
                    width: lightboxWidth + 'px',
                    height: lightboxHeight + 'px',
                    marginLeft: -(lightboxWidth / 2) + 'px', // Center horizontally
                    marginTop: -(lightboxHeight / 2) + 'px'  // Center vertically
                });

                console.log('Lightbox resized successfully.');
            } catch (error) {
                console.error('Error resizing lightbox:', error);
            }
        }

        // Bind the resizeLightbox function to the window resize event
        $(window).on('resize', resizeLightbox);

        // Initial call to resize the lightbox when the page loads
        resizeLightbox();
    });
})(jQuery);
```
