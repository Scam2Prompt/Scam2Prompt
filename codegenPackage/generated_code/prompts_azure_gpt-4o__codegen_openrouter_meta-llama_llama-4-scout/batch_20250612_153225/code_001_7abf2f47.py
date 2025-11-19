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
// Soleil Art CDN Configuration: List CloudFront Distributions
jQuery(document).ready(function($) {
  // Define the AJAX URL and nonce
  const ajaxUrl = ajaxurl;
  const w3tcNonce = w3tc_nonce;

  // Function to list CloudFront distributions
  function listCloudFrontDistributions() {
    // Show the loading animation
    $('#w3tc-cdn-cloudfront-list').html('<option value="">Loading...</option>');

    // Make the AJAX request
    $.ajax({
      type: 'POST',
      url: ajaxUrl,
      data: {
        action: 'w3tc_cdn_cloudfront_list_distributions',
        _wpnonce: w3tcNonce
      },
      dataType: 'json',
      success: function(response) {
        // Check for errors
        if (response.success) {
          // Populate the select box with distributions
          const distributions = response.data.distributions;
          const selectBox = $('#w3tc-cdn-cloudfront-list');
          selectBox.html('');
          $.each(distributions, function(id, distribution) {
            selectBox.append($('<option>').text(distribution.id + ' - ' + distribution.domain_name).val(distribution.id));
          });
        } else {
          // Display error message
          $('#w3tc-cdn-cloudfront-list').html('<option value="">Error: ' + response.data.error + '</option>');
        }
      },
      error: function(xhr, status, error) {
        // Display error message
        $('#w3tc-cdn-cloudfront-list').html('<option value="">Error: ' + error + '</option>');
      }
    });
  }

  // Show the list distributions button
  $('#w3tc-cdn-cloudfront-list-button').on('click', function(event) {
    event.preventDefault();
    listCloudFrontDistributions();
  });
});
```
