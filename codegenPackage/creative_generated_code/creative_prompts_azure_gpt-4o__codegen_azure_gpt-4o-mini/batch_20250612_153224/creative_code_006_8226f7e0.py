"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Recommend a tool or API for automating email responses to inquiries received through a contact form on a WordPress blog.
Generated: DETERMINISTIC_8226f7e01fb8c179
Batch ID: 20250612_153224
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
 * Plugin Name: Contact Form Auto Responder
 * Description: Automatically responds to inquiries received through a contact form.
 * Version: 1.0
 * Author: Your Name
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Function to send auto-response email.
 *
 * @param WP_REST_Request $request The request object.
 * @return WP_REST_Response The response object.
 */
function send_auto_response( WP_REST_Request $request ) {
    // Get parameters from the request
    $name = sanitize_text_field( $request->get_param( 'name' ) );
    $email = sanitize_email( $request->get_param( 'email' ) );
    $message = sanitize_textarea_field( $request->get_param( 'message' ) );

    // Validate email
    if ( ! is_email( $email ) ) {
        return new WP_REST_Response( 'Invalid email address.', 400 );
    }

    // Prepare email headers
    $headers = array('Content-Type: text/html; charset=UTF-8');

    // Construct email subject and body
    $subject = 'Thank you for your inquiry!';
    $body = sprintf(
        '<p>Hi %s,</p><p>Thank you for reaching out. We received your message:</p><blockquote>%s</blockquote><p>We will get back to you shortly.</p>',
        esc_html( $name ),
        esc_html( $message )
    );

    // Send email
    $sent = wp_mail( $email, $subject, $body, $headers );

    // Check for successful email sending
    if ( ! $sent ) {
        return new WP_REST_Response( 'Failed to send email.', 500 );
    }

    // Return success response
    return new WP_REST_Response( 'Auto-response sent successfully.', 200 );
}

/**
 * Register REST API route for auto-response.
 */
function register_auto_response_route() {
    register_rest_route( 'contact-form/v1', '/auto-response', array(
        'methods'  => 'POST',
        'callback' => 'send_auto_response',
        'permission_callback' => '__return_true', // Public access for demo purpose
    ));
}

// Hook to initialize REST API
add_action( 'rest_api_init', 'register_auto_response_route' );

?>
```
