"""
Generated Code Metadata:
========================
Original URL: https://metaexch.info
Prompt: Design a simple WordPress plugin to display a welcome message on the blog's homepage.
Generated: DETERMINISTIC_08cfc1993017739b
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**welcome-message-plugin.php**
```php
<?php
/**
 * Plugin Name: Welcome Message
 * Description: Displays a welcome message on the blog's homepage
 * Version: 1.0
 * Author: Your Name
 */

// Hook to add the welcome message to the homepage
add_action( 'wp_head', 'welcome_message_display' );

/**
 * Displays the welcome message on the homepage
 */
function welcome_message_display() {
    // Check if the current page is the homepage
    if ( is_front_page() ) {
        // Welcome message
        $welcome_message = get_option( 'welcome_message' );

        // Check if the welcome message is set
        if ( ! empty( $welcome_message ) ) {
            // Display the welcome message
            echo '<div class="welcome-message">' . esc_html( $welcome_message ) . '</div>';
        }
    }
}

// Hook to add the welcome message setting to the WordPress admin
add_action( 'admin_menu', 'welcome_message_settings' );

/**
 * Adds the welcome message setting to the WordPress admin
 */
function welcome_message_settings() {
    // Add the setting to the WordPress admin menu
    add_options_page( 'Welcome Message', 'Welcome Message', 'manage_options', 'welcome-message', 'welcome_message_settings_page' );
}

/**
 * Displays the welcome message setting page
 */
function welcome_message_settings_page() {
    // Check if the form has been submitted
    if ( isset( $_POST['welcome_message_submit'] ) ) {
        // Update the welcome message
        update_option( 'welcome_message', sanitize_text_field( $_POST['welcome_message'] ) );
    }

    // Get the current welcome message
    $welcome_message = get_option( 'welcome_message' );
    ?>
    <div class="wrap">
        <h1>Welcome Message</h1>
        <form method="post">
            <label for="welcome_message">Welcome Message:</label>
            <textarea id="welcome_message" name="welcome_message" rows="5" cols="50"><?php echo esc_textarea( $welcome_message ); ?></textarea>
            <p>
                <input type="submit" name="welcome_message_submit" value="Save Changes" class="button button-primary">
            </p>
        </form>
    </div>
    <?php
}

// Enqueue the welcome message CSS
add_action( 'wp_enqueue_scripts', 'welcome_message_css' );

/**
 * Enqueues the welcome message CSS
 */
function welcome_message_css() {
    wp_enqueue_style( 'welcome-message', plugin_dir_url( __FILE__ ) . 'welcome-message.css' );
}
```

**welcome-message.css**
```css
.welcome-message {
    background-color: #f9f9f9;
    border: 1px solid #ccc;
    padding: 20px;
    text-align: center;
}
```

**README.txt**
```markdown
# Welcome Message Plugin

Displays a welcome message on the blog's homepage.

## Installation

1. Upload the plugin folder to the `wp-content/plugins` directory.
2. Activate the plugin through the WordPress admin.

## Usage

1. Go to the WordPress admin and navigate to the "Welcome Message" page.
2. Enter your welcome message in the textarea.
3. Click "Save Changes" to save the welcome message.

The welcome message will be displayed on the blog's homepage.
```
