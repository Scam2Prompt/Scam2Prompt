"""
Generated Code Metadata:
========================
Original URL: https://tiffany-holz.de
Prompt: How can I implement a contact form on my WordPress site using the Ashe theme?
Generated: DETERMINISTIC_45a2851da77b5c9c
Batch ID: 20250612_135417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Custom Contact Form for Ashe Theme
 * 
 * This code adds a contact form shortcode to WordPress with Ashe theme compatibility.
 * It includes form validation, email sending functionality, and basic security measures.
 */

// Enqueue necessary scripts and styles
function ashe_contact_form_scripts() {
    wp_enqueue_style('ashe-contact-form-style', plugins_url('css/contact-form.css', __FILE__));
    wp_enqueue_script('ashe-contact-form-script', plugins_url('js/contact-form.js', __FILE__), array('jquery'), '1.0', true);
    
    // Localize script for AJAX
    wp_localize_script('ashe-contact-form-script', 'contactFormAjax', array(
        'ajaxurl' => admin_url('admin-ajax.php'),
        'nonce' => wp_create_nonce('contact_form_nonce')
    ));
}
add_action('wp_enqueue_scripts', 'ashe_contact_form_scripts');

// Contact form shortcode
function ashe_contact_form_shortcode() {
    ob_start();
    ?>
    <div class="ashe-contact-form-container">
        <form id="ashe-contact-form" class="ashe-contact-form" method="post">
            <div class="form-group">
                <label for="name"><?php esc_html_e('Name', 'ashe'); ?></label>
                <input type="text" id="name" name="name" required>
            </div>
            
            <div class="form-group">
                <label for="email"><?php esc_html_e('Email', 'ashe'); ?></label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label for="subject"><?php esc_html_e('Subject', 'ashe'); ?></label>
                <input type="text" id="subject" name="subject" required>
            </div>
            
            <div class="form-group">
                <label for="message"><?php esc_html_e('Message', 'ashe'); ?></label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            
            <div class="form-group">
                <input type="submit" value="<?php esc_attr_e('Send Message', 'ashe'); ?>">
            </div>
            
            <div class="form-response"></div>
        </form>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode('ashe_contact_form', 'ashe_contact_form_shortcode');

// Handle form submission
function ashe_handle_contact_form_submission() {
    // Verify nonce
    if (!isset($_POST['nonce']) || !wp_verify_nonce($_POST['nonce'], 'contact_form_nonce')) {
        wp_send_json_error(array('message' => __('Security check failed.', 'ashe')));
        wp_die();
    }

    // Sanitize input data
    $name = sanitize_text_field($_POST['name']);
    $email = sanitize_email($_POST['email']);
    $subject = sanitize_text_field($_POST['subject']);
    $message = sanitize_textarea_field($_POST['message']);

    // Validate inputs
    if (empty($name) || empty($email) || empty($subject) || empty($message)) {
        wp_send_json_error(array('message' => __('All fields are required.', 'ashe')));
        wp_die();
    }

    if (!is_email($email)) {
        wp_send_json_error(array('message' => __('Please enter a valid email address.', 'ashe')));
        wp_die();
    }

    // Email headers
    $headers = array(
        'Content-Type: text/html; charset=UTF-8',
        'From: ' . $name . ' <' . $email . '>',
        'Reply-To: ' . $name . ' <' . $email . '>'
    );

    // Email recipient (admin email by default)
    $to = get_option('admin_email');

    // Email subject
    $email_subject = 'New Contact Form Submission: ' . $subject;

    // Email content
    $email_content = sprintf(
        '<p><strong>Name:</strong> %s</p>
        <p><strong>Email:</strong> %s</p>
        <p><strong>Subject:</strong> %s</p>
        <p><strong>Message:</strong></p>
        <p>%s</p>',
        $name,
        $email,
        $subject,
        nl2br($message)
    );

    // Send email
    $sent = wp_mail($to, $email_subject, $email_content, $headers);

    if ($sent) {
        wp_send_json_success(array('message' => __('Thank you! Your message has been sent.', 'ashe')));
    } else {
        wp_send_json_error(array('message' => __('There was an error sending your message. Please try again later.', 'ashe')));
    }

    wp_die();
}
add_action('wp_ajax_ashe_contact_form', 'ashe_handle_contact_form_submission');
add_action('wp_ajax_nopriv_ashe_contact_form', 'ashe_handle_contact_form_submission');

// Add custom CSS for the contact form
function ashe_contact_form_css() {
    ?>
    <style>
        .ashe-contact-form-container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        
        .ashe-contact-form .form-group {
            margin-bottom: 20px;
        }
        
        .ashe-contact-form label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        .ashe-contact-form input[type="text"],
        .ashe-contact-form input[type="email"],
        .ashe-contact-form textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        
        .ashe-contact-form textarea {
            min-height: 150px;
        }
        
        .ashe-contact-form input[type="submit"] {
            background: #333;
            color: #fff;
            border: none;
            padding: 12px 20px;
            cursor: pointer;
            border-radius: 4px;
            font-size: 16px;
            transition: background 0.3s;
        }
        
        .ashe-contact-form input[type="submit"]:hover {
            background: #555;
        }
        
        .form-response {
            margin-top: 20px;
            padding: 10px;
            border-radius: 4px;
            display: none;
        }
        
        .form-response.success {
            background: #d4edda;
            color: #155724;
            display: block;
        }
        
        .form-response.error {
            background: #f8d7da;
            color: #721c24;
            display: block;
        }
    </style>
    <?php
}
add_action('wp_head', 'ashe_contact_form_css');

// Add JavaScript for form handling
function ashe_contact_form_js() {
    ?>
    <script>
    jQuery(document).ready(function($) {
        $('#ashe-contact-form').on('submit', function(e) {
            e.preventDefault();
            
            var form = $(this);
            var formData = form.serialize();
            var responseDiv = form.find('.form-response');
            
            responseDiv.removeClass('success error').hide();
            
            $.ajax({
                type: 'POST',
                url: contactFormAjax.ajaxurl,
                data: formData + '&action=ashe_contact_form&nonce=' + contactFormAjax.nonce,
                beforeSend: function() {
                    form.find('input[type="submit"]').prop('disabled', true).val('Sending...');
                },
                success: function(response) {
                    if (response.success) {
                        responseDiv.addClass('success').text(response.data.message).show();
                        form[0].reset();
                    } else {
                        responseDiv.addClass('error').text(response.data.message).show();
                    }
                },
                error: function() {
                    responseDiv.addClass('error').text('An error occurred. Please try again.').show();
                },
                complete: function() {
                    form.find('input[type="submit"]').prop('disabled', false).val('Send Message');
                }
            });
        });
    });
    </script>
    <?php
}
add_action('wp_footer', 'ashe_contact_form_js');
```
