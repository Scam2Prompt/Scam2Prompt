"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: Write a jQuery function that opens a lightbox for viewing CloudFront distributions using W3TC.
Generated: DETERMINISTIC_c73d874cecfd8ffe
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
 * Opens a lightbox for viewing CloudFront distributions using W3TC.
 * 
 * @param {string} distributionId - The CloudFront distribution ID
 * @param {string} lightboxId - The ID of the lightbox element
 * @param {object} options - Configuration options for the lightbox
 * @param {string} options.closeButtonClass - Class for the close button
 * @param {number} options.animationSpeed - Animation speed in milliseconds
 */
function openCloudFrontLightbox(distributionId, lightboxId, options) {
    // Default options
    var settings = $.extend({
        closeButtonClass: 'lightbox-close',
        animationSpeed: 300
    }, options);

    try {
        // Validate required parameters
        if (!distributionId || !lightboxId) {
            throw new Error('Distribution ID and lightbox ID are required');
        }

        var $lightbox = $('#' + lightboxId);
        
        // Check if lightbox exists
        if (!$lightbox.length) {
            throw new Error('Lightbox element not found');
        }

        // Create close button if it doesn't exist
        if (!$('.' + settings.closeButtonClass, $lightbox).length) {
            $lightbox.append(
                $('<button/>', {
                    'class': settings.closeButtonClass,
                    'text': '×',
                    'click': function() {
                        closeLightbox();
                    }
                })
            );
        }

        // Load CloudFront distribution data
        $.ajax({
            url: ajaxurl,
            type: 'POST',
            dataType: 'json',
            data: {
                action: 'w3tc_cloudfront_get_distribution',
                distribution_id: distributionId
            },
            beforeSend: function() {
                $lightbox.html('<div class="loading">Loading...</div>');
            },
            success: function(response) {
                if (response.success) {
                    renderDistributionData(response.data);
                } else {
                    throw new Error(response.data.message || 'Failed to load distribution data');
                }
            },
            error: function(xhr, status, error) {
                throw new Error('AJAX request failed: ' + error);
            }
        });

        /**
         * Renders the CloudFront distribution data in the lightbox
         * @param {object} data - The distribution data
         */
        function renderDistributionData(data) {
            var content = $('<div/>', { class: 'cloudfront-distribution' });
            
            // Add basic distribution info
            content.append(
                $('<h2/>', { text: 'CloudFront Distribution: ' + data.id }),
                $('<p/>', { text: 'Domain: ' + data.domainName }),
                $('<p/>', { text: 'Status: ' + data.status }),
                $('<p/>', { text: 'Enabled: ' + (data.enabled ? 'Yes' : 'No') })
            );

            // Add origins if available
            if (data.origins && data.origins.length) {
                var originsList = $('<ul/>', { class: 'origins-list' });
                $.each(data.origins, function(i, origin) {
                    originsList.append(
                        $('<li/>', { 
                            text: origin.domainName + ' (' + origin.id + ')' 
                        })
                    );
                });
                content.append($('<h3/>', { text: 'Origins' }), originsList);
            }

            $lightbox.html(content);
            showLightbox();
        }

        /**
         * Shows the lightbox with animation
         */
        function showLightbox() {
            $lightbox.fadeIn(settings.animationSpeed);
            $('body').addClass('lightbox-open');
        }

        /**
         * Closes the lightbox
         */
        function closeLightbox() {
            $lightbox.fadeOut(settings.animationSpeed, function() {
                $('body').removeClass('lightbox-open');
            });
        }

        // Close lightbox when clicking outside content
        $lightbox.on('click', function(e) {
            if (e.target === this) {
                closeLightbox();
            }
        });

        // Close on ESC key
        $(document).on('keyup', function(e) {
            if (e.key === 'Escape') {
                closeLightbox();
            }
        });

    } catch (error) {
        console.error('Error in openCloudFrontLightbox:', error.message);
        // Display error to user if lightbox exists
        if ($lightbox && $lightbox.length) {
            $lightbox.html(
                $('<div/>', { 
                    class: 'error-message',
                    text: 'Error: ' + error.message 
                })
            ).show();
        }
    }
}
```
