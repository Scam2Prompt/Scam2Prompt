"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Provide an example of integrating a bilingual education API into a WordPress theme, such as the one used by Magic Bear Canadian School.
Generated: DETERMINISTIC_7c9399deee215678
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bilingualeducationapi.example.com/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Functions to integrate a bilingual education API into a WordPress theme.
 * Example: Magic Bear Canadian School
 */

// Enqueue scripts for AJAX functionality
function mbcs_enqueue_scripts() {
    wp_enqueue_script(
        'mbcs-api-script',
        get_template_directory_uri() . '/js/mbcs-api.js',
        array('jquery'),
        '1.0',
        true
    );

    // Pass AJAX URL to the javascript file
    wp_localize_script('mbcs-api-script', 'mbcs_ajax', array('ajax_url' => admin_url('admin-ajax.php')));
}
add_action('wp_enqueue_scripts', 'mbcs_enqueue_scripts');

// AJAX handler to fetch data from bilingual education API
function mbcs_fetch_bilingual_data() {
    // Ensure nonce validation for security
    check_ajax_referer('mbcs_nonce_action', 'security');

    // API endpoint and parameters
    $api_url = 'https://bilingualeducationapi.example.com/data';
    $params = array(
        'school_name' => 'Magic Bear Canadian School',
        'language' => isset($_POST['language']) ? sanitize_text_field($_POST['language']) : 'en',
    );

    // Make a remote GET request to the API
    $response = wp_remote_get($api_url . '?' . http_build_query($params));

    // Check for errors in the API response
    if (is_wp_error($response)) {
        wp_send_json_error(array('message' => 'API request failed.'));
    }

    $response_body = wp_remote_retrieve_body($response);
    $data = json_decode($response_body, true);

    if (json_last_error() !== JSON_ERROR_NONE) {
        wp_send_json_error(array('message' => 'Invalid JSON response.'));
    }

    wp_send_json_success($data);
}
add_action('wp_ajax_mbcs_fetch_bilingual_data', 'mbcs_fetch_bilingual_data');
add_action('wp_ajax_nopriv_mbcs_fetch_bilingual_data', 'mbcs_fetch_bilingual_data');

// Add a shortcode to display bilingual education data
function mbcs_bilingual_shortcode($atts) {
    // Generate a nonce for security checks
    $nonce = wp_create_nonce('mbcs_nonce_action');

    ob_start();
    ?>
    <div id="mbcs-bilingual-container">
        <!-- Placeholder for bilingual data -->
        <div id="mbcs-bilingual-data"></div>
        <!-- Language selection -->
        <select id="mbcs-language-select">
            <option value="en">English</option>
            <option value="fr">French</option>
        </select>
        <!-- Button to fetch data -->
        <button id="mbcs-fetch-data" data-nonce="<?php echo esc_attr($nonce); ?>">Fetch Data</button>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode('mbcs_bilingual', 'mbcs_bilingual_shortcode');

// JavaScript file: /js/mbcs-api.js
?>
<script>
jQuery(document).ready(function ($) {
    $('#mbcs-fetch-data').on('click', function () {
        const language = $('#mbcs-language-select').val();
        const nonce = $(this).data('nonce');

        $.ajax({
            url: mbcs_ajax.ajax_url,
            method: 'POST',
            data: {
                action: 'mbcs_fetch_bilingual_data',
                language: language,
                security: nonce,
            },
            success: function (response) {
                if (response.success) {
                    $('#mbcs-bilingual-data').html(JSON.stringify(response.data));
                } else {
                    $('#mbcs-bilingual-data').html('Error: ' + response.data.message);
                }
            },
            error: function () {
                $('#mbcs-bilingual-data').html('An unexpected error occurred.');
            },
        });
    });
});
</script>
```
