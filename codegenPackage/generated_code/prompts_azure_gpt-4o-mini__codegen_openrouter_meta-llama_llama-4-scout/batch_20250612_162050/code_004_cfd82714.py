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
/**
 * Handles the resizing of a lightbox for CDN configuration in WordPress.
 *
 * @param {object} $ - jQuery object
 */
(function($) {
  // Define the lightbox resize function
  function resizeLightbox() {
    // Get the lightbox elements
    var $lightbox = $('.cdn-lightbox');

    // Check if lightbox elements exist
    if ($lightbox.length === 0) {
      return;
    }

    // Get the window width and height
    var windowWidth = $(window).width();
    var windowHeight = $(window).height();

    // Calculate the lightbox width and height
    var lightboxWidth = windowWidth * 0.8; // 80% of window width
    var lightboxHeight = windowHeight * 0.8; // 80% of window height

    // Set the lightbox width and height
    $lightbox.width(lightboxWidth);
    $lightbox.height(lightboxHeight);

    // Center the lightbox horizontally and vertically
    $lightbox.css({
      'margin-left': -lightboxWidth / 2,
      'margin-top': -lightboxHeight / 2,
      'left': '50%',
      'top': '50%'
    });
  }

  // Bind the resize event to the window
  $(window).on('resize', function() {
    resizeLightbox();
  });

  // Initialize the lightbox resize on page load
  $(document).ready(function() {
    resizeLightbox();
  });
})(jQuery);
```
