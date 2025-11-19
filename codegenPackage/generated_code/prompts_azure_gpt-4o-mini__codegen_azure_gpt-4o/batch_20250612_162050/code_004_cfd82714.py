"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: Generate a jQuery function that handles the resizing of a lightbox for CDN configuration in WordPress.
Generated: DETERMINISTIC_cfd8271426d0699c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// jQuery function to handle the resizing of a lightbox for CDN configuration in WordPress
(function($) {
    'use strict';

    // Document ready function to ensure DOM is fully loaded
    $(document).ready(function() {
        // Function to resize the lightbox dynamically
        function resizeLightbox() {
            try {
                // Select the lightbox element
                var $lightbox = $('.lightbox');

                // Ensure the lightbox exists before proceeding
                if ($lightbox.length === 0) {
                    console.warn('Lightbox element not found.');
                    return;
                }

                // Get the viewport dimensions
                var viewportWidth = $(window).width();
                var viewportHeight = $(window).height();

                // Calculate new dimensions for the lightbox
                var lightboxWidth = Math.min(viewportWidth * 0.8, 800); // Max width: 800px or 80% of viewport
                var lightboxHeight = Math.min(viewportHeight * 0.8, 600); // Max height: 600px or 80% of viewport

                // Apply the new dimensions to the lightbox
                $lightbox.css({
                    width: lightboxWidth + 'px',
                    height: lightboxHeight + 'px',
                    'margin-left': -(lightboxWidth / 2) + 'px', // Center horizontally
                    'margin-top': -(lightboxHeight / 2) + 'px' // Center vertically
                });

                console.log('Lightbox resized to:', lightboxWidth, 'x', lightboxHeight);
            } catch (error) {
                // Log any errors that occur during resizing
                console.error('Error resizing lightbox:', error);
            }
        }

        // Bind the resizeLightbox function to the window resize event
        $(window).on('resize', function() {
            resizeLightbox();
        });

        // Trigger the resizeLightbox function on page load
        resizeLightbox();
    });
})(jQuery);
```
