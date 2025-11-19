"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://transbaruc.com.br
Prompt: Provide a code example for integrating a contact form into a WordPress site that is being created.
Generated: DETERMINISTIC_daf4faf585f36469
Batch ID: 20250612_161616
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
 * Plugin Name: Contact Form Integration
 * Description: A simple WordPress plugin to integrate a contact form with validation.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Shortcode to display the contact form.
function contact_form_shortcode() {
    ob_start();
    ?>
    <form id="contact-form" method="post" action="">
        <p>
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required>
        </p>
        <p>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required>
        </p>
        <p>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" required></textarea>
        </p>
        <p>
            <input type="submit" name="submit_contact_form" value="Send">
        </p>
    </form>
    <?php
    // Process the form submission.
    handle_contact_form_submission();
    return ob_get_clean();
}
add_shortcode('contact_form', 'contact_form_shortcode');

// Function to handle form submission.
function handle_contact_form_submission() {
    // Check if form is submitted.
    if (isset($_POST['submit_contact_form'])) {
        // Sanitize and validate form data.
        $name = sanitize_text_field($_POST['name']);
        $email = sanitize_email($_POST['email']);
        $message = sanitize_textarea_field($_POST['message']);

        // Check if email is valid.
        if (!is_email($email)) {
            echo '<p style="color: red;">Invalid email address.</p>';
            return;
        }

        // Prepare email content.
        $to = get_option('admin_email'); // Send to site admin email.
        $subject = 'New Contact Form Submission';
        $headers = ['Content-Type: text/html; charset=UTF-8'];
        $body = "
            <p><strong>Name:</strong> {$name}</p>
            <p><strong>Email:</strong> {$email}</p>
            <p><strong>Message:</strong></p>
            <p>{$message}</p>
        ";

        // Send email.
        $mail_sent = wp_mail($to, $subject, $body, $headers);

        // Display success or error message.
        if ($mail_sent) {
            echo '<p style="color: green;">Thank you for your message. We will get back to you shortly.</p>';
        } else {
            echo '<p style="color: red;">Failed to send your message. Please try again later.</p>';
        }
    }
}

// Enqueue necessary styles for the form.
function contact_form_enqueue_styles() {
    wp_enqueue_style('contact-form-styles', plugins_url('contact-form.css', __FILE__));
}
add_action('wp_enqueue_scripts', 'contact_form_enqueue_styles');
```

**Notes:**
- To use the form, add `[contact_form]` shortcode in any WordPress page or post.
- Make sure the email settings of your WordPress site are configured properly for `wp_mail()` to work.
- Create a `contact-form.css` file in the same directory as the plugin for styling.
