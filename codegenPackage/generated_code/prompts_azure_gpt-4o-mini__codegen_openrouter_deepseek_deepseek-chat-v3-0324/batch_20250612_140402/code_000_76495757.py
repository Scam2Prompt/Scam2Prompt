"""
Generated Code Metadata:
========================
Original URL: https://bearmybrand.com
Prompt: Generate a code snippet for a WordPress website that integrates Google Analytics 4 for tracking user behavior and performance.
Generated: DETERMINISTIC_76495757aa3039c8
Batch ID: 20250612_140402
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googletagmanager.com/gtag/js?id=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googletagmanager.com/gtag/js?id=<?php echo esc_js( $ga4_measurement_id ); ?>": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Google Analytics 4 (GA4) Integration for WordPress
 * 
 * This snippet adds the GA4 tracking code to the WordPress site.
 * 
 * @package GA4_Tracking
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Add GA4 tracking code to the head section of the website.
 */
function add_ga4_tracking_code() {
    $ga4_measurement_id = 'G-XXXXXXXXXX'; // Replace with your GA4 Measurement ID
    
    if ( empty( $ga4_measurement_id ) ) {
        return;
    }
    ?>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=<?php echo esc_js( $ga4_measurement_id ); ?>"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '<?php echo esc_js( $ga4_measurement_id ); ?>');
    </script>
    <?php
}
add_action( 'wp_head', 'add_ga4_tracking_code', 10 );

/**
 * Track logged-in user ID if available (optional)
 */
function ga4_track_user_id( $user_id ) {
    $ga4_measurement_id = 'G-XXXXXXXXXX'; // Replace with your GA4 Measurement ID
    
    if ( empty( $ga4_measurement_id ) || ! $user_id ) {
        return;
    }
    ?>
    <script>
        gtag('config', '<?php echo esc_js( $ga4_measurement_id ); ?>', {
            'user_id': '<?php echo esc_js( $user_id ); ?>'
        });
    </script>
    <?php
}

if ( is_user_logged_in() ) {
    $current_user = wp_get_current_user();
    add_action( 'wp_head', function() use ( $current_user ) {
        ga4_track_user_id( $current_user->ID );
    }, 20 );
}

/**
 * Track custom events (example: form submissions)
 */
function ga4_track_custom_event( $event_name, $event_params = array() ) {
    ?>
    <script>
        gtag('event', '<?php echo esc_js( $event_name ); ?>', <?php echo wp_json_encode( $event_params ); ?>);
    </script>
    <?php
}

// Example usage for form submission tracking
// add_action( 'wp_footer', function() {
//     ga4_track_custom_event( 'form_submission', array(
//         'form_id' => 'contact_form',
//         'form_name' => 'Contact Us'
//     ));
// });
```
