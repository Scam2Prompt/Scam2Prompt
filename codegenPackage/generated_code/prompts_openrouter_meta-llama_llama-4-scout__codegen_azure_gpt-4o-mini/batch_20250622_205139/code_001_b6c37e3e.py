"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Develop a custom WordPress theme for a business website with a contact form, product showcase, and services section, using best practices for SEO and performance optimization.
Generated: DETERMINISTIC_b6c37e3e2d785651
Batch ID: 20250622_205139
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
 * Custom WordPress Theme for Business Website
 * 
 * This theme includes a contact form, product showcase, and services section.
 * It follows best practices for SEO and performance optimization.
 *
 * @package CustomBusinessTheme
 */

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

// Theme setup
function custom_business_theme_setup() {
    // Add support for featured images
    add_theme_support('post-thumbnails');

    // Register navigation menus
    register_nav_menus(array(
        'primary' => __('Primary Menu', 'custom-business-theme'),
    ));

    // Load theme text domain for translations
    load_theme_textdomain('custom-business-theme', get_template_directory() . '/languages');
}
add_action('after_setup_theme', 'custom_business_theme_setup');

// Enqueue styles and scripts
function custom_business_theme_enqueue_scripts() {
    // Enqueue main stylesheet
    wp_enqueue_style('main-style', get_stylesheet_uri(), array(), '1.0');

    // Enqueue custom scripts
    wp_enqueue_script('custom-script', get_template_directory_uri() . '/js/custom.js', array('jquery'), '1.0', true);
}
add_action('wp_enqueue_scripts', 'custom_business_theme_enqueue_scripts');

// Register custom post type for Products
function custom_business_theme_register_product_post_type() {
    $args = array(
        'labels' => array(
            'name' => __('Products', 'custom-business-theme'),
            'singular_name' => __('Product', 'custom-business-theme'),
        ),
        'public' => true,
        'has_archive' => true,
        'supports' => array('title', 'editor', 'thumbnail'),
        'rewrite' => array('slug' => 'products'),
    );
    register_post_type('product', $args);
}
add_action('init', 'custom_business_theme_register_product_post_type');

// Shortcode for Contact Form
function custom_business_theme_contact_form() {
    ob_start(); ?>
    <form id="contact-form" method="post" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        
        <input type="submit" name="submit" value="Send">
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('contact_form', 'custom_business_theme_contact_form');

// Handle form submission
function custom_business_theme_handle_contact_form() {
    if (isset($_POST['submit'])) {
        // Sanitize and validate input
        $name = sanitize_text_field($_POST['name']);
        $email = sanitize_email($_POST['email']);
        $message = sanitize_textarea_field($_POST['message']);

        if (!is_email($email)) {
            // Invalid email
            echo '<p class="error">Please enter a valid email address.</p>';
            return;
        }

        // Send email (replace with your email)
        $to = 'your-email@example.com';
        $subject = 'New Contact Form Submission';
        $body = "Name: $name\nEmail: $email\nMessage: $message";
        $headers = array('Content-Type: text/plain; charset=UTF-8');

        if (wp_mail($to, $subject, $body, $headers)) {
            echo '<p class="success">Thank you for your message!</p>';
        } else {
            echo '<p class="error">There was an error sending your message. Please try again later.</p>';
        }
    }
}
add_action('wp', 'custom_business_theme_handle_contact_form');

// Create a simple page template for the homepage
function custom_business_theme_homepage_template() {
    ?>
    <div class="homepage">
        <h1>Welcome to Our Business</h1>
        <section class="services">
            <h2>Our Services</h2>
            <ul>
                <li>Service 1</li>
                <li>Service 2</li>
                <li>Service 3</li>
            </ul>
        </section>
        <section class="products">
            <h2>Our Products</h2>
            <?php
            $args = array('post_type' => 'product', 'posts_per_page' => 3);
            $products = new WP_Query($args);
            if ($products->have_posts()) {
                while ($products->have_posts()) {
                    $products->the_post(); ?>
                    <div class="product">
                        <h3><?php the_title(); ?></h3>
                        <?php the_post_thumbnail(); ?>
                        <p><?php the_excerpt(); ?></p>
                    </div>
                <?php }
                wp_reset_postdata();
            } else {
                echo '<p>No products found.</p>';
            }
            ?>
        </section>
        <section class="contact">
            <h2>Contact Us</h2>
            <?php echo do_shortcode('[contact_form]'); ?>
        </section>
    </div>
    <?php
}

// Register the homepage template
function custom_business_theme_register_homepage() {
    add_menu_page('Homepage', 'Homepage', 'manage_options', 'homepage', 'custom_business_theme_homepage_template', '', 6);
}
add_action('admin_menu', 'custom_business_theme_register_homepage');
```

### Additional Files
- **custom.js** (in the `js` directory):
```javascript
jQuery(document).ready(function($) {
    // Custom JavaScript for the theme can be added here
});
```

- **style.css** (in the root directory):
```css
/*
Theme Name: Custom Business Theme
Description: A custom WordPress theme for a business website.
Version: 1.0
Author: Your Name
*/

body {
    font-family: Arial, sans-serif;
}

h1, h2 {
    color: #333;
}

.error {
    color: red;
}

.success {
    color: green;
}
```

### Note
- Replace `your-email@example.com` with the actual email address where you want to receive contact form submissions.
- This code is a basic structure and can be expanded with more features and styles as needed.
