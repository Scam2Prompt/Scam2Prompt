"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bharatnews18.com
Prompt: Write code to create a WordPress plugin that mimics the functionality of the "Top 10 Contact Form Plugins" mentioned on BharatNews18, ensuring it supports customizable form fields and integrates with email services.
Generated: DETERMINISTIC_00298d72b98ba406
Batch ID: 20250612_145136
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
Plugin Name: Custom Contact Form
Plugin URI: https://example.com
Description: A WordPress plugin that creates customizable contact forms and integrates with email services.
Version: 1.0.0
Author: Your Name
Author URI: https://example.com
License: GPL2
*/

/**
 * Prevent direct access to the file
 */
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Main class for the Custom Contact Form Plugin
 */
class CustomContactFormPlugin {

    public function __construct() {
        // Hook to enqueue admin assets
        add_action('admin_enqueue_scripts', [$this, 'enqueue_admin_scripts']);

        // Hook for registering the shortcode
        add_shortcode('custom_contact_form', [$this, 'render_contact_form']);

        // Hook for processing form submissions
        add_action('init', [$this, 'process_form_submission']);
    }

    /**
     * Enqueue admin scripts for future use (e.g., form customization UI)
     */
    public function enqueue_admin_scripts() {
        wp_enqueue_script('ccf-admin-js', plugin_dir_url(__FILE__) . 'assets/js/admin.js', ['jquery'], '1.0', true);
        wp_enqueue_style('ccf-admin-css', plugin_dir_url(__FILE__) . 'assets/css/admin.css', [], '1.0');
    }

    /**
     * Renders the contact form on the front-end
     *
     * @return string The HTML of the contact form
     */
    public function render_contact_form() {
        ob_start(); ?>
        <form id="custom-contact-form" method="POST">
            <?php wp_nonce_field('ccf_form_submission_nonce', 'ccf_nonce'); ?>
            <label for="ccf_name">Name:</label>
            <input type="text" name="ccf_name" id="ccf_name" required>
            
            <label for="ccf_email">Email:</label>
            <input type="email" name="ccf_email" id="ccf_email" required>
            
            <label for="ccf_message">Message:</label>
            <textarea name="ccf_message" id="ccf_message" required></textarea>
            
            <input type="submit" name="ccf_submit" value="Send">
        </form>
        <?php
        return ob_get_clean();
    }

    /**
     * Process the contact form submission
     */
    public function process_form_submission() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['ccf_submit'])) {
            // Verify nonce
            if (!isset($_POST['ccf_nonce']) || !wp_verify_nonce($_POST['ccf_nonce'], 'ccf_form_submission_nonce')) {
                wp_die('Nonce verification failed.', 'Error', ['response' => 403]);
            }

            // Sanitize inputs
            $name = sanitize_text_field($_POST['ccf_name']);
            $email = sanitize_email($_POST['ccf_email']);
            $message = sanitize_textarea_field($_POST['ccf_message']);

            // Validate email
            if (!is_email($email)) {
                wp_die('Invalid email address.', 'Error', ['response' => 400]);
            }

            // Send email
            $to = get_option('admin_email'); // Admin email as recipient
            $subject = "New Contact Form Submission from $name";
            $headers = ['Content-Type: text/html; charset=UTF-8', 'From: ' . $email];
            $body = "<strong>Name:</strong> $name<br><strong>Email:</strong> $email<br><strong>Message:</strong><br>$message";

            if (wp_mail($to, $subject, $body, $headers)) {
                wp_redirect(add_query_arg('success', 'true', wp_get_referer()));
                exit;
            } else {
                wp_die('Failed to send email.', 'Error', ['response' => 500]);
            }
        }
    }
}

// Initialize the plugin
new CustomContactFormPlugin();
```

**Folder Structure Suggestion:**
- `assets/js/admin.js` (if you need admin-specific JavaScript in the future)
- `assets/css/admin.css` (if you need admin-specific CSS in the future)
