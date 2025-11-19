"""
Generated Code Metadata:
========================
Original URL: https://exelade.eu
Prompt: Generate code to integrate WP Guardian with a WordPress site hosted outside of Plesk, ensuring visibility into site health and enabling flexible updates management.
Generated: DETERMINISTIC_a6b7fb0d18443650
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * WP Guardian Integration for WordPress
 * 
 * This script integrates WP Guardian with a WordPress site hosted outside of Plesk.
 * It ensures visibility into site health and enables flexible updates management.
 * 
 * @package WP_Guardian_Integration
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Class WP_Guardian_Integration
 * 
 * Handles the integration with WP Guardian.
 */
class WP_Guardian_Integration {

    /**
     * Constructor to initialize the integration.
     */
    public function __construct() {
        // Hook into WordPress actions
        add_action( 'init', array( $this, 'initialize_wp_guardian' ) );
        add_action( 'wp_ajax_wp_guardian_update', array( $this, 'handle_update_request' ) );
    }

    /**
     * Initialize WP Guardian settings.
     */
    public function initialize_wp_guardian() {
        // Check if WP Guardian is enabled
        if ( get_option( 'wp_guardian_enabled' ) ) {
            // Load necessary scripts and styles
            wp_enqueue_script( 'wp-guardian-script', plugin_dir_url( __FILE__ ) . 'js/wp-guardian.js', array( 'jquery' ), '1.0', true );
            wp_localize_script( 'wp-guardian-script', 'wpGuardian', array(
                'ajax_url' => admin_url( 'admin-ajax.php' ),
                'nonce'    => wp_create_nonce( 'wp_guardian_nonce' ),
            ) );
        }
    }

    /**
     * Handle update requests from WP Guardian.
     */
    public function handle_update_request() {
        // Verify nonce for security
        check_ajax_referer( 'wp_guardian_nonce', 'nonce' );

        // Check user capabilities
        if ( ! current_user_can( 'update_plugins' ) ) {
            wp_send_json_error( 'Insufficient permissions', 403 );
        }

        // Perform the update logic
        try {
            // Example: Update plugins
            $this->update_plugins();
            wp_send_json_success( 'Plugins updated successfully.' );
        } catch ( Exception $e ) {
            // Handle exceptions and send error response
            wp_send_json_error( 'Update failed: ' . $e->getMessage(), 500 );
        }
    }

    /**
     * Update plugins logic.
     */
    private function update_plugins() {
        // Fetch the list of plugins to update
        $updatable_plugins = get_site_transient( 'update_plugins' );

        if ( ! empty( $updatable_plugins->response ) ) {
            foreach ( $updatable_plugins->response as $plugin_slug => $plugin_data ) {
                // Update each plugin
                $result = wp_update_plugin( $plugin_slug );
                if ( is_wp_error( $result ) ) {
                    throw new Exception( 'Error updating plugin: ' . $result->get_error_message() );
                }
            }
        } else {
            throw new Exception( 'No plugins available for update.' );
        }
    }
}

// Initialize the WP Guardian Integration
new WP_Guardian_Integration();
```

```javascript
// js/wp-guardian.js
jQuery(document).ready(function($) {
    $('#update-button').on('click', function() {
        $.ajax({
            url: wpGuardian.ajax_url,
            type: 'POST',
            data: {
                action: 'wp_guardian_update',
                nonce: wpGuardian.nonce
            },
            success: function(response) {
                if (response.success) {
                    alert(response.data);
                } else {
                    alert('Error: ' + response.data);
                }
            },
            error: function(xhr, status, error) {
                alert('AJAX Error: ' + error);
            }
        });
    });
});
```

```php
// Add settings to enable WP Guardian in the WordPress admin
function wp_guardian_settings() {
    add_option( 'wp_guardian_enabled', false );
    register_setting( 'general', 'wp_guardian_enabled' );
    add_settings_field( 'wp_guardian_enabled', '<label for="wp_guardian_enabled">Enable WP Guardian</label>', 'wp_guardian_enabled_html', 'general' );
}

function wp_guardian_enabled_html() {
    $checked = get_option( 'wp_guardian_enabled' ) ? 'checked' : '';
    echo '<input type="checkbox" id="wp_guardian_enabled" name="wp_guardian_enabled" value="1" ' . $checked . ' />';
}

add_action( 'admin_init', 'wp_guardian_settings' );
```

This code provides a complete integration of WP Guardian with a WordPress site, including JavaScript for handling AJAX requests and settings for enabling the integration in the WordPress admin.
