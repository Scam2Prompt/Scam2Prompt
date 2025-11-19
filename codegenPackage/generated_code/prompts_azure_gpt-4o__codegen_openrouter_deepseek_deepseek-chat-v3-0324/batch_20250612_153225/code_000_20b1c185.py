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
 * Resizes a popup window to fit its content dynamically
 * @param {Object} options - Configuration options for the popup
 * @param {string} options.popupId - The ID of the popup element
 * @param {number} [options.minWidth=300] - Minimum width of the popup
 * @param {number} [options.minHeight=200] - Minimum height of the popup
 * @param {number} [options.padding=20] - Padding around the content
 * @param {boolean} [options.center=true] - Whether to center the popup after resize
 */
function w3tc_popup_resize(options) {
    // Default options
    const defaults = {
        popupId: '',
        minWidth: 300,
        minHeight: 200,
        padding: 20,
        center: true
    };

    // Merge user options with defaults
    const config = $.extend({}, defaults, options);

    // Validate required parameters
    if (!config.popupId) {
        console.error('Popup ID is required');
        return;
    }

    const $popup = $('#' + config.popupId);
    if (!$popup.length) {
        console.error('Popup element not found');
        return;
    }

    try {
        // Calculate content dimensions
        const $content = $popup.find('.popup-content');
        if (!$content.length) {
            console.error('Popup content not found');
            return;
        }

        const contentWidth = $content.outerWidth(true);
        const contentHeight = $content.outerHeight(true);

        // Calculate new dimensions with padding
        let newWidth = Math.max(contentWidth + (config.padding * 2), config.minWidth);
        let newHeight = Math.max(contentHeight + (config.padding * 2), config.minHeight);

        // Apply new dimensions
        $popup.css({
            'width': newWidth + 'px',
            'height': newHeight + 'px'
        });

        // Center popup if requested
        if (config.center) {
            const windowWidth = $(window).width();
            const windowHeight = $(window).height();

            const left = (windowWidth - newWidth) / 2;
            const top = (windowHeight - newHeight) / 2;

            $popup.css({
                'left': left + 'px',
                'top': top + 'px'
            });
        }

        // Trigger custom event after resize
        $popup.trigger('w3tc_popup_resized', [newWidth, newHeight]);
    } catch (error) {
        console.error('Error resizing popup:', error);
    }
}

// Example usage:
// $(document).ready(function() {
//     w3tc_popup_resize({
//         popupId: 'cdn-config-popup',
//         minWidth: 400,
//         minHeight: 300,
//         padding: 30
//     });
// });
```
