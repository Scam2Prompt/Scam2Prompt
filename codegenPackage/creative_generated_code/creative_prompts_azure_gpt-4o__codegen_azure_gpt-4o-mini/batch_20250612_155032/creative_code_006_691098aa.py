"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinnbase.ltd
Prompt: Create a WordPress shortcode for embedding a contact form on a webpage, ensuring proper error handling for undefined array keys.
Generated: DETERMINISTIC_691098aac261e0f9
Batch ID: 20250612_155032
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
 * Plugin Name: Custom Contact Form Shortcode
 * Description: A simple shortcode to embed a contact form in WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Shortcode function to display a contact form
 *
 * @param array $atts Attributes passed to the shortcode
 * @return string HTML output of the contact form
 */
function custom_contact_form_shortcode( $atts ) {
    // Shortcode attributes, with default values
    $atts = shortcode_atts(
        array(
            'to' => get_option( 'admin_email' ), // Default recipient is the admin email
        ), 
        $atts, 
        'contact_form'
    );

    // Initialize output variable
    $output = '';

    // Check if the form is submitted
    if ( $_SERVER['REQUEST_METHOD'] === 'POST' ) {
        // Sanitize and validate input
        $name    = isset( $_POST['name'] ) ? sanitize_text_field( $_POST['name'] ) : '';
        $email   = isset( $_POST['email'] ) ? sanitize_email( $_POST['email'] ) : '';
        $message = isset( $_POST['message'] ) ? sanitize_textarea_field( $_POST['message'] ) : '';

        // Validate the email address
        if ( ! is_email( $email ) ) {
            $output .= '<div class="error">Please enter a valid email address.</div>';
        } elseif ( empty( $name ) || empty( $message ) ) {
            $output .= '<div class="error">Please fill in all fields.</div>';
        } else {
            // Prepare and send the email
            $subject = 'New Contact Form Submission';
            $body    = "Name: $name\nEmail: $email\n\nMessage:\n$message";
            $headers = array('Content-Type: text/plain; charset=UTF-8');

            // Send email and check for success
            if ( wp_mail( $atts['to'], $subject, $body, $headers ) ) {
                $output .= '<div class="success">Thank you for your message!</div>';
            } else {
                $output .= '<div class="error">An error occurred while sending your message. Please try again later.</div>';
            }
        }
    }

    // Form HTML
    $output .= '<form method="post" action="">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required>

        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required>

        <label for="message">Message:</label>
        <textarea name="message" id="message" required></textarea>

        <input type="submit" value="Send">
    </form>';

    return $output;
}

// Register the shortcode
add_shortcode( 'contact_form', 'custom_contact_form_shortcode' );
```
