"""
Generated Code Metadata:
========================
Original URL: https://magicbear.com.br
Prompt: How can I implement a contact form in a WordPress theme for a bilingual school, ensuring it supports multiple languages?
Generated: DETERMINISTIC_2463b648dc5e4f0f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Add this code to your WordPress theme's functions.php file

// Enqueue necessary scripts and styles
function enqueue_contact_form_assets() {
    wp_enqueue_script('jquery'); // Ensure jQuery is loaded
    wp_enqueue_script('contact-form-script', get_template_directory_uri() . '/js/contact-form.js', array('jquery'), '1.0', true);
    wp_localize_script('contact-form-script', 'contactFormAjax', array(
        'ajax_url' => admin_url('admin-ajax.php'),
        'success_message' => __('Thank you for your message!', 'your-text-domain'),
        'error_message' => __('There was an error. Please try again.', 'your-text-domain'),
    ));
}
add_action('wp_enqueue_scripts', 'enqueue_contact_form_assets');

// Shortcode to display the contact form
function bilingual_contact_form_shortcode() {
    ob_start();
    ?>
    <form id="bilingual-contact-form" method="post">
        <label for="name"><?php _e('Name', 'your-text-domain'); ?>:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email"><?php _e('Email', 'your-text-domain'); ?>:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message"><?php _e('Message', 'your-text-domain'); ?>:</label>
        <textarea id="message" name="message" required></textarea>
        
        <button type="submit"><?php _e('Send', 'your-text-domain'); ?></button>
    </form>
    <div id="form-response"></div>
    <?php
    return ob_get_clean();
}
add_shortcode('bilingual_contact_form', 'bilingual_contact_form_shortcode');

// Handle the form submission via AJAX
function handle_contact_form_submission() {
    // Verify nonce for security
    check_ajax_referer('contact_form_nonce', 'security');

    // Sanitize and validate input
    $name = sanitize_text_field($_POST['name']);
    $email = sanitize_email($_POST['email']);
    $message = sanitize_textarea_field($_POST['message']);

    if (empty($name) || empty($email) || empty($message)) {
        wp_send_json_error(__('All fields are required.', 'your-text-domain'));
    }

    if (!is_email($email)) {
        wp_send_json_error(__('Invalid email address.', 'your-text-domain'));
    }

    // Send email
    $to = get_option('admin_email'); // Send to site admin email
    $subject = __('New Contact Form Submission', 'your-text-domain');
    $body = sprintf(__('Name: %s\nEmail: %s\nMessage: %s', 'your-text-domain'), $name, $email, $message);
    $headers = array('Content-Type: text/plain; charset=UTF-8');

    if (wp_mail($to, $subject, $body, $headers)) {
        wp_send_json_success(__('Your message has been sent successfully.', 'your-text-domain'));
    } else {
        wp_send_json_error(__('Failed to send your message. Please try again later.', 'your-text-domain'));
    }
}
add_action('wp_ajax_submit_contact_form', 'handle_contact_form_submission');
add_action('wp_ajax_nopriv_submit_contact_form', 'handle_contact_form_submission');
?>
```

```javascript
// Save this file as contact-form.js in your theme's js directory

jQuery(document).ready(function ($) {
    $('#bilingual-contact-form').on('submit', function (e) {
        e.preventDefault();

        // Clear previous response
        $('#form-response').html('');

        // Collect form data
        var formData = {
            action: 'submit_contact_form',
            security: contactFormAjax.nonce,
            name: $('#name').val(),
            email: $('#email').val(),
            message: $('#message').val(),
        };

        // Send AJAX request
        $.post(contactFormAjax.ajax_url, formData, function (response) {
            if (response.success) {
                $('#form-response').html('<p class="success">' + contactFormAjax.success_message + '</p>');
                $('#bilingual-contact-form')[0].reset(); // Reset form
            } else {
                $('#form-response').html('<p class="error">' + response.data + '</p>');
            }
        }).fail(function () {
            $('#form-response').html('<p class="error">' + contactFormAjax.error_message + '</p>');
        });
    });
});
```

```html
<!-- Add this shortcode to any page or post to display the contact form -->
[bilingual_contact_form]
```
