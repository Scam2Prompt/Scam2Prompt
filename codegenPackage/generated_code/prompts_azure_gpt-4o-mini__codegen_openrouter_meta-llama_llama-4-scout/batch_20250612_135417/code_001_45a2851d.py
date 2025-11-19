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

**Contact Form Implementation in WordPress using Ashe Theme**

### functions.php
```php
// Add contact form shortcode
function ashe_contact_form_shortcode() {
    ob_start();
    ?>
    <form id="contact-form" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send Message</button>
    </form>

    <?php
    $output = ob_get_clean();
    return $output;
}
add_shortcode('ashe_contact_form', 'ashe_contact_form_shortcode');

// Handle contact form submission
function ashe_contact_form_submit() {
    if (isset($_POST['name']) && isset($_POST['email']) && isset($_POST['message'])) {
        $name = sanitize_text_field($_POST['name']);
        $email = sanitize_email($_POST['email']);
        $message = sanitize_text_field($_POST['message']);

        // Set up email headers
        $headers = array(
            'From: ' . $email,
            'Reply-To: ' . $email
        );

        // Set up email content
        $subject = 'Contact Form Submission from ' . $name;
        $body = 'Name: ' . $name . "\n" . 'Email: ' . $email . "\n" . 'Message: ' . $message;

        // Send email
        wp_mail('your-email@example.com', $subject, $body, $headers);

        // Display success message
        echo '<p>Message sent successfully!</p>';
    } else {
        // Display error message
        echo '<p>Error: Please fill out all fields.</p>';
    }
}
add_action('wp_head', function() {
    if (isset($_POST['name']) && isset($_POST['email']) && isset($_POST['message'])) {
        ashe_contact_form_submit();
    }
});

// Enqueue contact form script
function ashe_contact_form_script() {
    wp_enqueue_script('contact-form', get_stylesheet_directory_uri() . '/js/contact-form.js', array('jquery'), '1.0', true);
}
add_action('wp_enqueue_scripts', 'ashe_contact_form_script');
```

### js/contact-form.js
```javascript
jQuery(document).ready(function($) {
    $('#contact-form').submit(function(e) {
        e.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '<?php echo admin_url('admin-ajax.php'); ?>',
            data: formData,
            success: function(data) {
                $('#contact-form').html(data);
            }
        });
    });
});
```

### page-contact.php (example usage)
```php
<?php
get_header();
?>

<div class="contact-form">
    <?php echo do_shortcode('[ashe_contact_form]'); ?>
</div>

<?php
get_footer();
```

### functions.php (ajax handler)
```php
// Ajax handler for contact form submission
add_action('wp_ajax_ashe_contact_form', 'ashe_contact_form_ajax_handler');
add_action('wp_ajax_nopriv_ashe_contact_form', 'ashe_contact_form_ajax_handler');

function ashe_contact_form_ajax_handler() {
    ashe_contact_form_submit();
    wp_die();
}
```
