"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bharatnews18.com
Prompt: Write code to create a WordPress plugin that mimics the functionality of the "Top 10 Contact Form Plugins" mentioned on BharatNews18, ensuring it supports customizable form fields and integrates with email services.
Generated: DETERMINISTIC_00298d72b98ba406
Batch ID: 20250612_145136
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
 * Plugin Name: Custom Contact Form
 * Description: A customizable contact form plugin that integrates with email services.
 * Version: 1.0
 * Author: Your Name
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

/**
 * Main Class for the Custom Contact Form Plugin
 */
class Custom_Contact_Form {

    // Constructor
    public function __construct() {
        // Register shortcode for the contact form
        add_shortcode( 'custom_contact_form', [ $this, 'render_form' ] );
        
        // Enqueue scripts and styles
        add_action( 'wp_enqueue_scripts', [ $this, 'enqueue_scripts' ] );
        
        // Handle form submission
        add_action( 'init', [ $this, 'handle_form_submission' ] );
    }

    /**
     * Enqueue necessary scripts and styles
     */
    public function enqueue_scripts() {
        wp_enqueue_style( 'custom-contact-form-style', plugins_url( '/css/style.css', __FILE__ ) );
        wp_enqueue_script( 'custom-contact-form-script', plugins_url( '/js/script.js', __FILE__ ), [ 'jquery' ], null, true );
    }

    /**
     * Render the contact form
     */
    public function render_form() {
        ob_start(); // Start output buffering
        ?>
        <form id="custom-contact-form" method="post">
            <label for="name">Name:</label>
            <input type="text" name="name" required>

            <label for="email">Email:</label>
            <input type="email" name="email" required>

            <label for="message">Message:</label>
            <textarea name="message" required></textarea>

            <input type="submit" name="submit" value="Send">
        </form>
        <?php
        return ob_get_clean(); // Return the buffered content
    }

    /**
     * Handle form submission
     */
    public function handle_form_submission() {
        if ( isset( $_POST['submit'] ) ) {
            // Validate nonce for security
            if ( ! check_admin_referer( 'custom_contact_form_nonce', 'nonce' ) ) {
                return; // Invalid nonce
            }

            // Sanitize and validate input
            $name = sanitize_text_field( $_POST['name'] );
            $email = sanitize_email( $_POST['email'] );
            $message = sanitize_textarea_field( $_POST['message'] );

            if ( ! is_email( $email ) ) {
                // Handle invalid email error
                wp_die( __( 'Invalid email address.', 'custom-contact-form' ) );
            }

            // Prepare the email
            $to = get_option( 'admin_email' );
            $subject = "New Contact Form Submission from $name";
            $body = "Name: $name\nEmail: $email\nMessage:\n$message";
            $headers = [ 'Content-Type: text/plain; charset=UTF-8' ];

            // Send the email
            $mail_sent = wp_mail( $to, $subject, $body, $headers );

            if ( ! $mail_sent ) {
                // Handle email sending error
                wp_die( __( 'Failed to send your message. Please try again later.', 'custom-contact-form' ) );
            }

            // Redirect to thank you page or show a success message
            wp_redirect( home_url( '/thank-you/' ) );
            exit;
        }
    }
}

// Initialize the plugin
new Custom_Contact_Form();
```

### Additional Notes:
- Ensure to create a `css/style.css` and `js/script.js` file in the plugin directory for styling and functionality.
- Implement a thank you page at `/thank-you/` to redirect upon successful submission.
- Properly handle translations if needed for multilingual support.
