"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: How do I set up a jQuery click event to configure a CloudFront distribution using W3TC?
Generated: DETERMINISTIC_fd83e78063cc1ff9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Ensure jQuery is loaded and document is ready
(function($) {
    $(document).ready(function() {
        // Handle click event for configuring CloudFront distribution
        $('#configure-cloudfront').on('click', function(e) {
            e.preventDefault();
            
            // Show loading indicator
            var $button = $(this);
            $button.prop('disabled', true).text('Configuring...');
            
            // AJAX request to configure CloudFront
            $.ajax({
                url: ajaxurl, // WordPress AJAX URL
                type: 'POST',
                dataType: 'json',
                data: {
                    action: 'w3tc_configure_cloudfront',
                    _wpnonce: $('#_wpnonce').val() // Security nonce
                },
                success: function(response) {
                    if (response.success) {
                        // Show success message
                        $('#cloudfront-message').html(
                            '<div class="notice notice-success"><p>' + 
                            response.data.message + 
                            '</p></div>'
                        );
                    } else {
                        // Show error message
                        $('#cloudfront-message').html(
                            '<div class="notice notice-error"><p>' + 
                            response.data.message + 
                            '</p></div>'
                        );
                    }
                },
                error: function(xhr, status, error) {
                    // Show AJAX error message
                    $('#cloudfront-message').html(
                        '<div class="notice notice-error"><p>' +
                        'An error occurred while configuring CloudFront: ' + 
                        error + 
                        '</p></div>'
                    );
                },
                complete: function() {
                    // Reset button state
                    $button.prop('disabled', false).text('Configure CloudFront');
                }
            });
        });
    });
})(jQuery);
```
