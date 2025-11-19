"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: Provide a code snippet to list CloudFront distributions with jQuery and AJAX in a WordPress environment.
Generated: DETERMINISTIC_171aff44c09c85bb
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
 * JavaScript code to list AWS CloudFront distributions using jQuery and AJAX in a WordPress environment.
 * This assumes you have a custom WordPress REST API endpoint set up to interact with AWS SDK on the server-side.
 * The server-side endpoint should handle authentication and return the list of CloudFront distributions.
 */

jQuery(document).ready(function ($) {
    // Function to fetch CloudFront distributions
    function fetchCloudFrontDistributions() {
        // Show a loading message or spinner
        $('#cloudfront-distributions').html('<p>Loading CloudFront distributions...</p>');

        // AJAX request to the custom WordPress REST API endpoint
        $.ajax({
            url: '/wp-json/myplugin/v1/cloudfront-distributions', // Replace with your custom endpoint
            method: 'GET',
            dataType: 'json',
            success: function (response) {
                // Clear the loading message
                $('#cloudfront-distributions').empty();

                // Check if distributions are returned
                if (response && response.distributions && response.distributions.length > 0) {
                    // Create a list of distributions
                    const list = $('<ul></ul>');
                    response.distributions.forEach(function (distribution) {
                        const listItem = $('<li></li>').text(
                            `ID: ${distribution.Id}, Domain: ${distribution.DomainName}`
                        );
                        list.append(listItem);
                    });
                    $('#cloudfront-distributions').append(list);
                } else {
                    $('#cloudfront-distributions').html('<p>No CloudFront distributions found.</p>');
                }
            },
            error: function (xhr, status, error) {
                // Handle errors
                console.error('Error fetching CloudFront distributions:', error);
                $('#cloudfront-distributions').html('<p>Error fetching CloudFront distributions. Please try again later.</p>');
            },
        });
    }

    // Trigger the fetch function on page load or a button click
    $('#fetch-distributions-btn').on('click', function () {
        fetchCloudFrontDistributions();
    });

    // Optionally, fetch distributions on page load
    // fetchCloudFrontDistributions();
});
```

```php
<?php
/**
 * PHP code to create a custom WordPress REST API endpoint for fetching CloudFront distributions.
 * This uses the AWS SDK for PHP to interact with AWS CloudFront.
 * Ensure the AWS SDK is installed and properly configured in your WordPress environment.
 */

add_action('rest_api_init', function () {
    register_rest_route('myplugin/v1', '/cloudfront-distributions', [
        'methods'  => 'GET',
        'callback' => 'fetch_cloudfront_distributions',
        'permission_callback' => function () {
            return current_user_can('manage_options'); // Restrict access to admins
        },
    ]);
});

function fetch_cloudfront_distributions() {
    // Load AWS SDK
    if (!class_exists('Aws\Sdk')) {
        return new WP_Error('aws_sdk_not_found', 'AWS SDK not found.', ['status' => 500]);
    }

    // Initialize AWS SDK
    $aws = new Aws\Sdk([
        'region'  => 'us-east-1', // Replace with your AWS region
        'version' => 'latest',
    ]);

    $cloudFront = $aws->createCloudFront();

    try {
        // Fetch CloudFront distributions
        $result = $cloudFront->listDistributions();

        // Extract distribution details
        $distributions = [];
        if (!empty($result['DistributionList']['Items'])) {
            foreach ($result['DistributionList']['Items'] as $item) {
                $distributions[] = [
                    'Id'         => $item['Id'],
                    'DomainName' => $item['DomainName'],
                ];
            }
        }

        // Return the distributions as a JSON response
        return rest_ensure_response(['distributions' => $distributions]);
    } catch (Exception $e) {
        // Handle AWS SDK errors
        return new WP_Error('aws_error', $e->getMessage(), ['status' => 500]);
    }
}
?>
```

```html
<!-- HTML code to display the CloudFront distributions and trigger the AJAX request -->
<div id="cloudfront-distributions">
    <!-- CloudFront distributions will be loaded here -->
</div>
<button id="fetch-distributions-btn">Fetch CloudFront Distributions</button>
```
