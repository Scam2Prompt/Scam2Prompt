"""
Generated Code Metadata:
========================
Original URL: https://asnetinfotech.com
Prompt: "Design a web page for a digital marketing agency using WordPress and generative AI technology."
Generated: DETERMINISTIC_38806657a90ff9de
Batch ID: 20250622_210443
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
 * Template Name: Digital Marketing Agency
 * Description: A custom template for a digital marketing agency using WordPress.
 */

// Enqueue styles and scripts
function dma_enqueue_scripts() {
    wp_enqueue_style('dma-style', get_stylesheet_uri());
    wp_enqueue_script('dma-script', get_template_directory_uri() . '/js/dma-script.js', array('jquery'), null, true);
}
add_action('wp_enqueue_scripts', 'dma_enqueue_scripts');

// Start the output of the page
get_header(); ?>

<div class="container">
    <header class="agency-header">
        <h1>Welcome to Our Digital Marketing Agency</h1>
        <p>Your partner in growth through innovative marketing strategies.</p>
    </header>

    <section class="services">
        <h2>Our Services</h2>
        <ul>
            <li>Search Engine Optimization (SEO)</li>
            <li>Social Media Marketing</li>
            <li>Content Creation</li>
            <li>Email Marketing</li>
            <li>Pay-Per-Click Advertising (PPC)</li>
        </ul>
    </section>

    <section class="about">
        <h2>About Us</h2>
        <p>We are a team of experienced marketers dedicated to helping businesses grow through effective digital strategies.</p>
    </section>

    <section class="contact">
        <h2>Contact Us</h2>
        <form id="contact-form" method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
            <input type="hidden" name="action" value="dma_contact_form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            
            <button type="submit">Send Message</button>
        </form>
    </section>
</div>

<?php get_footer(); ?>

// Handle form submission
function dma_handle_contact_form() {
    // Check nonce for security
    if (!isset($_POST['nonce']) || !wp_verify_nonce($_POST['nonce'], 'dma_contact_form_nonce')) {
        wp_die('Security check failed');
    }

    // Sanitize and validate input
    $name = sanitize_text_field($_POST['name']);
    $email = sanitize_email($_POST['email']);
    $message = sanitize_textarea_field($_POST['message']);

    if (!is_email($email)) {
        wp_die('Invalid email address');
    }

    // Prepare email
    $to = get_option('admin_email');
    $subject = 'New Contact Form Submission';
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = ['Content-Type: text/plain; charset=UTF-8'];

    // Send email
    if (wp_mail($to, $subject, $body, $headers)) {
        wp_redirect(home_url('/thank-you'));
        exit;
    } else {
        wp_die('Email sending failed');
    }
}
add_action('admin_post_dma_contact_form', 'dma_handle_contact_form');
add_action('admin_post_nopriv_dma_contact_form', 'dma_handle_contact_form');
```

```javascript
// js/dma-script.js

jQuery(document).ready(function($) {
    // Add any custom JavaScript functionality here
    $('#contact-form').on('submit', function() {
        // Optional: Add form validation or other logic before submission
    });
});
```

```css
/* style.css */

/* Basic styles for the digital marketing agency page */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

.agency-header {
    background: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

.services, .about, .contact {
    margin: 20px 0;
    padding: 20px;
    border: 1px solid #ccc;
}

h2 {
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
}

form button {
    padding: 10px;
    background: #333;
    color: #fff;
    border: none;
    cursor: pointer;
}

form button:hover {
    background: #555;
}
```
