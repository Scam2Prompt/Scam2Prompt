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

**contact-form.php**
```php
<?php
/**
 * Contact form functionality for bilingual school WordPress theme.
 *
 * @package Bilingual School Theme
 */

// Define the contact form shortcode
add_shortcode('bilingual_school_contact_form', 'bilingual_school_contact_form_shortcode');

/**
 * Contact form shortcode callback.
 *
 * @return string Contact form HTML.
 */
function bilingual_school_contact_form_shortcode() {
    // Contact form HTML
    $output = '<form id="bilingual-school-contact-form" method="post" class="contact-form">';

    // Name field
    $output .= '<div class="form-group">';
    $output .= '<label for="name">' . __('Name', 'bilingual-school-theme') . '</label>';
    $output .= '<input type="text" id="name" name="name" required>';
    $output .= '</div>';

    // Email field
    $output .= '<div class="form-group">';
    $output .= '<label for="email">' . __('Email', 'bilingual-school-theme') . '</label>';
    $output .= '<input type="email" id="email" name="email" required>';
    $output .= '</div>';

    // Message field
    $output .= '<div class="form-group">';
    $output .= '<label for="message">' . __('Message', 'bilingual-school-theme') . '</label>';
    $output .= '<textarea id="message" name="message" required></textarea>';
    $output .= '</div>';

    // Language field
    $output .= '<div class="form-group">';
    $output .= '<label for="language">' . __('Preferred Language', 'bilingual-school-theme') . '</label>';
    $output .= '<select id="language" name="language">';
    $output .= '<option value="en">' . __('English', 'bilingual-school-theme') . '</option>';
    $output .= '<option value="es">' . __('Spanish', 'bilingual-school-theme') . '</option>';
    // Add more languages as needed
    $output .= '</select>';
    $output .= '</div>';

    // Submit button
    $output .= '<button type="submit">' . __('Send Message', 'bilingual-school-theme') . '</button>';
    $output .= '</form>';

    return $output;
}

// Handle contact form submission
add_action('wp_ajax_bilingual_school_contact_form', 'bilingual_school_contact_form_ajax_handler');
add_action('wp_ajax_nopriv_bilingual_school_contact_form', 'bilingual_school_contact_form_ajax_handler');

/**
 * Contact form AJAX handler.
 */
function bilingual_school_contact_form_ajax_handler() {
    // Check if the form was submitted
    if (isset($_POST['name']) && isset($_POST['email']) && isset($_POST['message']) && isset($_POST['language'])) {
        // Validate form data
        $name = sanitize_text_field($_POST['name']);
        $email = sanitize_email($_POST['email']);
        $message = sanitize_text_field($_POST['message']);
        $language = sanitize_text_field($_POST['language']);

        // Send email using WordPress mail function
        $subject = __('Contact Form Submission', 'bilingual-school-theme');
        $body = __('Name:', 'bilingual-school-theme') . ' ' . $name . "\n";
        $body .= __('Email:', 'bilingual-school-theme') . ' ' . $email . "\n";
        $body .= __('Message:', 'bilingual-school-theme') . ' ' . $message . "\n";
        $body .= __('Preferred Language:', 'bilingual-school-theme') . ' ' . $language;

        // Set email headers
        $headers = array(
            'From: ' . $email,
            'Content-Type: text/plain; charset=UTF-8',
        );

        // Send email
        wp_mail(get_option('admin_email'), $subject, $body, $headers);

        // Return success response
        wp_send_json_success(__('Message sent successfully!', 'bilingual-school-theme'));
    } else {
        // Return error response
        wp_send_json_error(__('Invalid form data.', 'bilingual-school-theme'));
    }

    // Die to prevent further output
    wp_die();
}

// Enqueue contact form script
add_action('wp_enqueue_scripts', 'bilingual_school_contact_form_enqueue_script');

/**
 * Enqueue contact form script.
 */
function bilingual_school_contact_form_enqueue_script() {
    wp_enqueue_script('bilingual-school-contact-form', get_template_directory_uri() . '/js/contact-form.js', array('jquery'), '1.0', true);

    // Localize script
    wp_localize_script('bilingual-school-contact-form', 'bilingualSchoolContactForm', array(
        'ajax_url' => admin_url('admin-ajax.php'),
    ));
}
```

**js/contact-form.js**
```javascript
jQuery(document).ready(function($) {
    $('#bilingual-school-contact-form').submit(function(event) {
        event.preventDefault();

        // Get form data
        var formData = $(this).serialize();

        // Send AJAX request
        $.ajax({
            type: 'POST',
            url: bilingualSchoolContactForm.ajax_url,
            data: {
                action: 'bilingual_school_contact_form',
                name: $('#name').val(),
                email: $('#email').val(),
                message: $('#message').val(),
                language: $('#language').val(),
            },
            success: function(response) {
                if (response.success) {
                    // Display success message
                    $('#bilingual-school-contact-form').prepend('<p class="success-message">' + response.data + '</p>');
                } else {
                    // Display error message
                    $('#bilingual-school-contact-form').prepend('<p class="error-message">' + response.data + '</p>');
                }
            },
        });
    });
});
```

**functions.php**
```php
// Load text domain for translations
add_action('after_setup_theme', 'bilingual_school_theme_load_textdomain');

/**
 * Load text domain for translations.
 */
function bilingual_school_theme_load_textdomain() {
    load_theme_textdomain('bilingual-school-theme', get_template_directory() . '/languages');
}
```

**style.css**
```css
.contact-form {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 10px;
}

.form-group input, .form-group textarea, .form-group select {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

.success-message {
    color: #008000;
}

.error-message {
    color: #ff0000;
}
```
