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

Here’s the PHP code for implementing a contact form in a WordPress theme with multilingual support using WPML or Polylang for translation management:

```php
<?php
/**
 * Plugin Name: Bilingual School Contact Form
 * Description: A simple bilingual contact form implementation for a WordPress theme.
 */

// Shortcode to display the contact form
function bilingual_contact_form_shortcode() {
    // Check the current language using WPML or Polylang
    $current_language = apply_filters('wpml_current_language', NULL); // WPML example

    // Define form labels based on the current language
    if ($current_language === 'es') { // Spanish version
        $labels = [
            'name' => 'Nombre',
            'email' => 'Correo electrónico',
            'message' => 'Mensaje',
            'submit' => 'Enviar',
            'success_message' => '¡Gracias! Tu mensaje ha sido enviado.',
            'error_message' => 'Hubo un error al enviar el formulario. Por favor, intenta nuevamente.',
        ];
    } else { // English version (default)
        $labels = [
            'name' => 'Name',
            'email' => 'Email',
            'message' => 'Message',
            'submit' => 'Submit',
            'success_message' => 'Thank you! Your message has been sent.',
            'error_message' => 'There was an error sending the form. Please try again.',
        ];
    }

    // Handle form submission
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['bilingual_contact_form_submit'])) {
        // Sanitize form inputs
        $name = sanitize_text_field($_POST['name']);
        $email = sanitize_email($_POST['email']);
        $message = sanitize_textarea_field($_POST['message']);

        // Validate inputs
        if (empty($name) || empty($email) || empty($message)) {
            return '<p style="color: red;">' . esc_html($labels['error_message']) . '</p>';
        }

        // Send email (adjust the recipient email address as needed)
        $to = get_option('admin_email'); // Send to the site admin
        $subject = esc_html__('Contact Form Submission', 'bilingual-school');
        $headers = ['Content-Type: text/html; charset=UTF-8'];
        $body = "Name: $name<br>Email: $email<br>Message: $message";

        if (wp_mail($to, $subject, $body, $headers)) {
            return '<p style="color: green;">' . esc_html($labels['success_message']) . '</p>';
        } else {
            return '<p style="color: red;">' . esc_html($labels['error_message']) . '</p>';
        }
    }

    // Output the contact form HTML
    ob_start();
    ?>
    <form method="post">
        <p>
            <label for="name"><?php echo esc_html($labels['name']); ?>:</label>
            <input type="text" id="name" name="name" required>
        </p>
        <p>
            <label for="email"><?php echo esc_html($labels['email']); ?>:</label>
            <input type="email" id="email" name="email" required>
        </p>
        <p>
            <label for="message"><?php echo esc_html($labels['message']); ?>:</label>
            <textarea id="message" name="message" rows="5" required></textarea>
        </p>
        <p>
            <button type="submit" name="bilingual_contact_form_submit"><?php echo esc_html($labels['submit']); ?></button>
        </p>
    </form>
    <?php
    return ob_get_clean();
}

// Register the shortcode
add_shortcode('bilingual_contact_form', 'bilingual_contact_form_shortcode');

// Enqueue styles for the form (optional)
function bilingual_contact_form_styles() {
    wp_enqueue_style('bilingual-contact-form', get_template_directory_uri() . '/bilingual-contact-form.css', [], '1.0.0');
}
add_action('wp_enqueue_scripts', 'bilingual_contact_form_styles');
```

1. Save the code as a plugin file (e.g., `bilingual-contact-form.php`) or include it directly in your theme's `functions.php`.
2. Use `[bilingual_contact_form]` shortcode in the desired page or post to display the form. Adjust the localization mechanism according to the installed multilingual plugin.
