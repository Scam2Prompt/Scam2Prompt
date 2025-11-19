"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stargate.fund
Prompt: How can I use Elementor for hosting a private site similar to Stargate Fund?
Generated: DETERMINISTIC_28b06443dcae1caf
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Private Site Elementor Setup
 * Description: A simple plugin to set up a private site using Elementor.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Create a private page with Elementor template.
 */
function create_private_elementor_page() {
    // Check if the Elementor plugin is active
    if ( ! class_exists( 'Elementor\Plugin' ) ) {
        return; // Elementor is not active, exit the function
    }

    // Create a new page
    $page_title = 'Private Stargate Fund Site';
    $page_content = '[elementor-template id="123"]'; // Replace with your Elementor template ID

    // Create the page
    $page_id = wp_insert_post( array(
        'post_title'   => $page_title,
        'post_content' => $page_content,
        'post_status'  => 'private', // Set the page status to private
        'post_type'    => 'page'
    ));

    // Check for errors in page creation
    if ( is_wp_error( $page_id ) ) {
        error_log( 'Error creating page: ' . $page_id->get_error_message() ); // Log error
        return; // Exit if there was an error
    }

    // Optionally set the page template
    update_post_meta( $page_id, '_elementor_template_type', 'page' );
}

add_action( 'init', 'create_private_elementor_page' );

/**
 * Restrict access to private pages for non-logged-in users.
 */
function restrict_private_page_access() {
    if ( is_page() && ! is_user_logged_in() ) {
        wp_redirect( wp_login_url() ); // Redirect to login page
        exit; // Always exit after redirecting
    }
}

add_action( 'template_redirect', 'restrict_private_page_access' );
?>
```
