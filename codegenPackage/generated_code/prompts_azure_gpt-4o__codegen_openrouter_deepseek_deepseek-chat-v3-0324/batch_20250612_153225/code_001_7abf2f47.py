"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: Generate JavaScript code that uses `ajaxurl` and `w3tc_nonce` to list CloudFront distributions via a popup form, as shown in the Soleil Art CDN configuration example.
Generated: DETERMINISTIC_7abf2f47b946e146
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
 * CloudFront Distribution Lister
 * 
 * This script handles the AJAX request to list CloudFront distributions
 * using the provided nonce and ajaxurl for security.
 */

(function($) {
    'use strict';

    // Cache DOM elements
    var $popupTrigger = $('#cdn-cloudfront-popup-trigger');
    var $popupContainer = $('#cdn-cloudfront-popup');
    var $popupContent = $('#cdn-cloudfront-popup-content');
    var $loadingIndicator = $('#cdn-cloudfront-loading');
    var $errorContainer = $('#cdn-cloudfront-error');

    /**
     * Initialize the CloudFront distribution lister
     */
    function init() {
        bindEvents();
    }

    /**
     * Bind event handlers
     */
    function bindEvents() {
        $popupTrigger.on('click', function(e) {
            e.preventDefault();
            showPopup();
            fetchDistributions();
        });

        $(document).on('click', '.cdn-cloudfront-close', function() {
            hidePopup();
        });
    }

    /**
     * Show the popup container
     */
    function showPopup() {
        $popupContainer.fadeIn();
        $popupContent.html('');
        $errorContainer.hide();
    }

    /**
     * Hide the popup container
     */
    function hidePopup() {
        $popupContainer.fadeOut();
    }

    /**
     * Fetch CloudFront distributions via AJAX
     */
    function fetchDistributions() {
        $loadingIndicator.show();

        $.ajax({
            url: ajaxurl,
            type: 'POST',
            dataType: 'json',
            data: {
                action: 'w3tc_cloudfront_list_distributions',
                _wpnonce: w3tc_nonce
            },
            success: function(response) {
                $loadingIndicator.hide();
                
                if (response.success) {
                    renderDistributions(response.data);
                } else {
                    showError(response.error || 'Unknown error occurred');
                }
            },
            error: function(xhr, status, error) {
                $loadingIndicator.hide();
                showError('AJAX request failed: ' + error);
            }
        });
    }

    /**
     * Render distributions in the popup
     * @param {Array} distributions - Array of distribution objects
     */
    function renderDistributions(distributions) {
        if (!distributions || distributions.length === 0) {
            $popupContent.html('<p>No distributions found.</p>');
            return;
        }

        var html = '<div class="cdn-cloudfront-distributions">';
        html += '<h3>Available Distributions</h3>';
        html += '<ul class="cdn-cloudfront-list">';

        distributions.forEach(function(dist) {
            html += '<li>';
            html += '<strong>' + dist.DomainName + '</strong>';
            html += '<span class="cdn-cloudfront-id">' + dist.Id + '</span>';
            html += '</li>';
        });

        html += '</ul>';
        html += '</div>';

        $popupContent.html(html);
    }

    /**
     * Show error message in popup
     * @param {string} message - Error message to display
     */
    function showError(message) {
        $errorContainer.text(message).show();
    }

    // Initialize on DOM ready
    $(document).ready(init);

})(jQuery);
```
