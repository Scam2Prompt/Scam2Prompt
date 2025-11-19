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
 * This function dynamically adjusts the lightbox dimensions based on the window size
 * and ensures proper display of CDN configuration content.
 * 
 * @param {string} lightboxSelector - The CSS selector for the lightbox element.
 * @param {string} contentSelector - The CSS selector for the content container inside the lightbox.
 * @param {object} options - Configuration options for the lightbox.
 * @param {number} [options.minWidth=300] - Minimum width of the lightbox in pixels.
 * @param {number} [options.minHeight=200] - Minimum height of the lightbox in pixels.
 * @param {number} [options.maxWidth=800] - Maximum width of the lightbox in pixels.
 * @param {number} [options.maxHeight=600] - Maximum height of the lightbox in pixels.
 * @param {number} [options.padding=20] - Padding around the content in pixels.
 */
function handleLightboxResize(lightboxSelector, contentSelector, options) {
    // Default options
    const defaults = {
        minWidth: 300,
        minHeight: 200,
        maxWidth: 800,
        maxHeight: 600,
        padding: 20
    };
    
    // Merge user options with defaults
    const settings = $.extend({}, defaults, options);
    
    // Cache selectors
    const $lightbox = $(lightboxSelector);
    const $content = $(contentSelector);
    
    // Check if elements exist
    if (!$lightbox.length || !$content.length) {
        console.error('Lightbox or content element not found');
        return;
    }
    
    /**
     * Calculates and applies the appropriate dimensions to the lightbox.
     */
    function resizeLightbox() {
        try {
            // Get window dimensions
            const windowWidth = $(window).width();
            const windowHeight = $(window).height();
            
            // Calculate content dimensions
            const contentWidth = $content.outerWidth(true);
            const contentHeight = $content.outerHeight(true);
            
            // Calculate lightbox dimensions with padding
            let lightboxWidth = contentWidth + (settings.padding * 2);
            let lightboxHeight = contentHeight + (settings.padding * 2);
            
            // Apply min/max constraints
            lightboxWidth = Math.max(settings.minWidth, Math.min(lightboxWidth, settings.maxWidth, windowWidth - 40));
            lightboxHeight = Math.max(settings.minHeight, Math.min(lightboxHeight, settings.maxHeight, windowHeight - 40));
            
            // Set lightbox dimensions
            $lightbox.css({
                'width': lightboxWidth + 'px',
                'height': lightboxHeight + 'px',
                'margin-left': -(lightboxWidth / 2) + 'px',
                'margin-top': -(lightboxHeight / 2) + 'px'
            });
            
            // Center content within lightbox
            $content.css({
                'margin': settings.padding + 'px'
            });
        } catch (error) {
            console.error('Error resizing lightbox:', error);
        }
    }
    
    // Initialize lightbox dimensions
    resizeLightbox();
    
    // Bind resize event
    $(window).on('resize.lightbox', $.throttle(250, resizeLightbox));
    
    // Cleanup function to remove event listeners
    return function cleanup() {
        $(window).off('resize.lightbox');
    };
}

// Example usage:
// $(document).ready(function() {
//     const cleanup = handleLightboxResize(
//         '#cdn-lightbox', 
//         '.lightbox-content',
//         {
//             minWidth: 400,
//             minHeight: 300,
//             maxWidth: 900,
//             padding: 30
//         }
//     );
//     
//     // When you need to clean up:
//     // cleanup();
// });
```
