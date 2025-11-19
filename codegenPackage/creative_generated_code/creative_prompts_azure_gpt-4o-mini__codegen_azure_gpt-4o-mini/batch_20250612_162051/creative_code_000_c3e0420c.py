"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbandjock.fr
Prompt: Generate a simple WordPress plugin that displays a custom welcome message on the homepage, similar to the "Hello world!" post on mbandjock.fr.
Generated: DETERMINISTIC_c3e0420c63ed8e2f
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yourwebsite.com": {
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
/*
Plugin Name: Custom Welcome Message
Plugin URI: https://yourwebsite.com
Description: A simple WordPress plugin that displays a custom welcome message on the homepage.
Version: 1.0
Author: Your Name
Author URI: https://yourwebsite.com
License: GPL2
*/

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Function to display the custom welcome message.
 */
function cwm_display_welcome_message() {
    // Check if we are on the homepage
    if ( is_front_page() ) {
        // Define the welcome message
        $welcome_message = '<div class="custom-welcome-message" style="padding: 20px; background-color: #f9f9f9; text-align: center; border: 1px solid #ccc;">';
        $welcome_message .= '<h1>Welcome to Our Website!</h1>';
        $welcome_message .= '<p>We are glad to have you here. Explore our content and enjoy your stay!</p>';
        $welcome_message .= '</div>';

        // Output the welcome message
        echo $welcome_message;
    }
}

// Hook the function to the 'wp_head' action
add_action( 'wp_head', 'cwm_display_welcome_message' );

/**
 * Enqueue styles for the welcome message.
 */
function cwm_enqueue_styles() {
    // Register custom style for the welcome message
    wp_enqueue_style( 'cwm-styles', plugins_url( 'css/custom-welcome-message.css', __FILE__ ) );
}

// Hook the styles to the 'wp_enqueue_scripts' action
add_action( 'wp_enqueue_scripts', 'cwm_enqueue_styles' );

?>
```

**Note**: You may want to create a CSS file named `custom-welcome-message.css` in a `css` directory inside your plugin's folder for additional styling. Make sure to adjust the paths as necessary.
