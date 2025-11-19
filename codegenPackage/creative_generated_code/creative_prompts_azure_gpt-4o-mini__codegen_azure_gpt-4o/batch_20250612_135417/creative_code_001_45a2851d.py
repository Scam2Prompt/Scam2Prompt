"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiffany-holz.de
Prompt: How can I implement a contact form on my WordPress site using the Ashe theme?
Generated: DETERMINISTIC_45a2851da77b5c9c
Batch ID: 20250612_135417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/*
 * Plugin Name: Custom Contact Form for Ashe Theme
 * Description: Simple contact form implementation for the Ashe theme.
 * Version: 1.0
 * Author: Your Name
 */

// Add a shortcode to display the contact form
function custom_contact_form_shortcode() {
    ob_start();
    ?>
    <!-- Contact Form HTML -->
    <form id="custom-contact-form" method="post" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit" name="submit_contact_form">Send</button>
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('custom_contact_form', 'custom_contact_form_shortcode');

// Handle form submission
function custom_contact_form_handler() {
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['submit_contact_form'])) {
        // Validate and sanitize form inputs
        $name    = sanitize_text_field($_POST['name']);
        $email   = sanitize_email($_POST['email']);
        $message = sanitize_textarea_field($_POST['message']);

        // Basic validation
        if (empty($name) || empty($email) || empty($message)) {
            wp_die('All fields are required.');
        }

        if (!is_email($email)) {
            wp_die('Invalid email address.');
        }

        // Send email
        $admin_email = get_option('admin_email');
        $subject     = "Contact Form Message from $name";
        $headers     = ["From: $name <$email>", "Reply-To: $email"];

        $email_sent = wp_mail($admin_email, $subject, $message, $headers);

        if ($email_sent) {
            wp_redirect(home_url('/thank-you'));
            exit;
        } else {
            wp_die('Failed to send your message. Please try again later.');
        }
    }
}
add_action('init', 'custom_contact_form_handler');

// Create a Thank You page template
function custom_contact_form_thank_you_page() {
    if (is_page('thank-you')) {
        ?>
        <!DOCTYPE html>
        <html <?php language_attributes(); ?>>
        <head>
            <meta charset="<?php bloginfo('charset'); ?>">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Thank You</title>
            <?php wp_head(); ?>
        </head>
        <body <?php body_class(); ?>>
            <h1>Thank You!</h1>
            <p>Your message has been successfully sent. We will get back to you shortly.</p>
            <a href="<?php echo home_url(); ?>">Return to Home</a>
            <?php wp_footer(); ?>
        </body>
        </html>
        <?php
        exit;
    }
}
add_action('template_redirect', 'custom_contact_form_thank_you_page');
?>
```
