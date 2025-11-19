"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hotchipilin.com
Prompt: Provide a code example for setting up a WordPress site with a custom welcome message using PHP.
Generated: DETERMINISTIC_4cfa3789aa0f5012
Batch ID: 20250612_162051
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
 * Plugin Name: Custom Welcome Message
 * Description: A simple WordPress plugin to display a custom welcome message on the homepage.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Function to display a custom welcome message
 */
function cwm_display_welcome_message() {
    // Check if we are on the homepage
    if ( is_front_page() ) {
        // Define the custom welcome message
        $welcome_message = '<h2>Welcome to My Custom WordPress Site!</h2>';
        $welcome_message .= '<p>We are glad to have you here. Enjoy exploring our content!</p>';

        // Output the welcome message
        echo '<div class="custom-welcome-message" style="text-align: center; margin: 20px 0;">' . $welcome_message . '</div>';
    }
}

// Hook the function to the 'wp_head' action to ensure it runs in the head section
add_action( 'wp_head', 'cwm_display_welcome_message' );

/**
 * Function to enqueue custom styles for the welcome message
 */
function cwm_enqueue_styles() {
    // Enqueue custom stylesheet for the welcome message
    wp_enqueue_style( 'cwm-styles', plugin_dir_url( __FILE__ ) . 'css/custom-welcome-message.css' );
}

// Hook the enqueue function to 'wp_enqueue_scripts'
add_action( 'wp_enqueue_scripts', 'cwm_enqueue_styles' );

/**
 * Activation hook to ensure proper setup when the plugin is activated
 */
function cwm_activate() {
    // Code to run during plugin activation (if necessary)
    // E.g., setting default options or creating database tables
}
register_activation_hook( __FILE__, 'cwm_activate' );

/**
 * Deactivation hook to clean up when the plugin is deactivated
 */
function cwm_deactivate() {
    // Code to run during plugin deactivation (if necessary)
    // E.g., cleaning up database options
}
register_deactivation_hook( __FILE__, 'cwm_deactivate' );
?>
```

**Note:** To make this code functional, you need to create a directory for your plugin and save this file as `custom-welcome-message.php`. Additionally, if you wish to add custom styles, create a `css` directory inside your plugin directory and create a `custom-welcome-message.css` file for styling.
