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
/**
 * CDN Configuration Interface Popup Resize Function
 *
 * Resizes a popup window to fit its content, similar to the w3tc_popup_resize function.
 *
 * @param {string} popupSelector - The CSS selector of the popup window.
 * @param {object} options - Optional settings for resizing the popup.
 * @param {number} options.width - The desired width of the popup.
 * @param {number} options.height - The desired height of the popup.
 * @param {boolean} options.animate - Whether to animate the resize process.
 */

(function($) {
  $.fn.cdnPopupResize = function(options) {
    var defaults = {
      width: null,
      height: null,
      animate: true
    };

    // Merge user-provided options with defaults
    var settings = $.extend({}, defaults, options);

    return this.each(function() {
      var $popup = $(this);

      // Check if the popup is visible
      if (!$popup.is(':visible')) {
        console.error('Popup is not visible.');
        return;
      }

      // Get the content of the popup
      var $content = $popup.find('.popup-content');

      // Check if the content exists
      if (!$content.length) {
        console.error('Popup content not found.');
        return;
      }

      // Calculate the required width and height
      var requiredWidth = $content.outerWidth(true);
      var requiredHeight = $content.outerHeight(true);

      // Set the width and height if provided in options
      if (settings.width) {
        requiredWidth = settings.width;
      }
      if (settings.height) {
        requiredHeight = settings.height;
      }

      // Resize the popup
      if (settings.animate) {
        $popup.animate({
          width: requiredWidth,
          height: requiredHeight
        }, 'fast');
      } else {
        $popup.css({
          width: requiredWidth,
          height: requiredHeight
        });
      }
    });
  };

  // Example usage:
  $(document).ready(function() {
    var $popup = $('#cdn-config-popup');
    $popup.cdnPopupResize({
      width: 500,
      height: 300,
      animate: true
    });
  });
})(jQuery);
```
