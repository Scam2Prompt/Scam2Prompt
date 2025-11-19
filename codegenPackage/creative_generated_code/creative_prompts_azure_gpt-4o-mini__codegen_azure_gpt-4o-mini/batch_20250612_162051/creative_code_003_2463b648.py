"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: How can I implement a contact form in a WordPress theme for a bilingual school, ensuring it supports multiple languages?
Generated: DETERMINISTIC_2463b648dc5e4f0f
Batch ID: 20250612_162051
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
 * Contact Form Template for Bilingual School WordPress Theme
 *
 * This template provides a contact form that supports multiple languages.
 * It utilizes WordPress's built-in functions and form validation.
 */

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = sanitize_text_field($_POST['name']);
    $email = sanitize_email($_POST['email']);
    $message = sanitize_textarea_field($_POST['message']);
    $language = sanitize_text_field($_POST['language']);
    
    $errors = [];
    
    // Validate fields
    if (empty($name)) {
        $errors[] = __('Name is required', 'your-text-domain');
    }
    
    if (!is_email($email)) {
        $errors[] = __('A valid email is required', 'your-text-domain');
    }
    
    if (empty($message)) {
        $errors[] = __('Message cannot be empty', 'your-text-domain');
    }
    
    if (empty($errors)) {
        // Prepare email
        $to = get_option('admin_email');
        $subject = __('Contact Form Submission', 'your-text-domain');
        $body = sprintf(__('Name: %s\nEmail: %s\nMessage: %s\nLanguage: %s', 'your-text-domain'), $name, $email, $message, $language);
        $headers = ['Content-Type: text/plain; charset=UTF-8'];

        // Send email and check for success
        if (wp_mail($to, $subject, $body, $headers)) {
            $success_message = __('Your message has been sent successfully!', 'your-text-domain');
        } else {
            $errors[] = __('There was an error sending your message. Please try again later.', 'your-text-domain');
        }
    }
}

// Enqueue necessary scripts and styles
function enqueue_contact_form_styles() {
    wp_enqueue_style('contact-form-style', get_template_directory_uri() . '/css/contact-form.css');
}
add_action('wp_enqueue_scripts', 'enqueue_contact_form_styles');

?>

<!-- HTML Contact Form -->
<div class="contact-form">
    <h2><?php _e('Contact Us', 'your-text-domain'); ?></h2>
    
    <?php if (!empty($success_message)): ?>
        <div class="success-message"><?php echo esc_html($success_message); ?></div>
    <?php endif; ?>
    
    <?php if (!empty($errors)): ?>
        <div class="error-messages">
            <ul>
                <?php foreach ($errors as $error): ?>
                    <li><?php echo esc_html($error); ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
    <?php endif; ?>
    
    <form method="post" action="">
        <div>
            <label for="name"><?php _e('Name', 'your-text-domain'); ?></label>
            <input type="text" id="name" name="name" required>
        </div>
        <div>
            <label for="email"><?php _e('Email', 'your-text-domain'); ?></label>
            <input type="email" id="email" name="email" required>
        </div>
        <div>
            <label for="message"><?php _e('Message', 'your-text-domain'); ?></label>
            <textarea id="message" name="message" required></textarea>
        </div>
        <div>
            <label for="language"><?php _e('Language', 'your-text-domain'); ?></label>
            <select id="language" name="language">
                <option value="en"><?php _e('English', 'your-text-domain'); ?></option>
                <option value="fr"><?php _e('French', 'your-text-domain'); ?></option>
                <!-- Add more languages as needed -->
            </select>
        </div>
        <div>
            <input type="submit" value="<?php _e('Send Message', 'your-text-domain'); ?>">
        </div>
    </form>
</div>
```

Ensure you replace `'your-text-domain'` with the appropriate text domain for your theme. Additionally, create a CSS file at `css/contact-form.css` for styling the form as needed.
