"""
Generated Code Metadata:
========================
Original URL: https://alakhttiar.com.sa
Prompt: "Generate code to create a custom page template in WordPress for a services page that includes sections for مظلات and سواتر."
Generated: DETERMINISTIC_0eb69e105af83c79
Batch ID: 20250622_210655
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
 * Template Name: Services Page
 * Description: A custom page template for displaying services including مظلات and سواتر.
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Get header
get_header(); ?>

<div class="services-page">
    <h1><?php the_title(); ?></h1>

    <section id="madhalat" class="service-section">
        <h2>مظلات</h2>
        <p>
            <?php
            // Display content for مظلات
            if (have_posts()) :
                while (have_posts()) : the_post();
                    the_content();
                endwhile;
            else :
                echo '<p>No content available for مظلات.</p>';
            endif;
            ?>
        </p>
    </section>

    <section id="sawater" class="service-section">
        <h2>سواتر</h2>
        <p>
            <?php
            // Display content for سواتر
            if (have_posts()) :
                while (have_posts()) : the_post();
                    // Custom field for سواتر
                    $sawater_content = get_post_meta(get_the_ID(), 'sawater_content', true);
                    if ($sawater_content) {
                        echo esc_html($sawater_content);
                    } else {
                        echo '<p>No content available for سواتر.</p>';
                    }
                endwhile;
            else :
                echo '<p>No content available for سواتر.</p>';
            endif;
            ?>
        </p>
    </section>
</div>

<?php
// Get footer
get_footer();
```

### Instructions for Use:
1. Save this code in a new file named `page-services.php` in your active theme's directory.
2. Create a new page in the WordPress admin and select "Services Page" as the template.
3. Add content for مظلات in the page editor and use a custom field named `sawater_content` for سواتر.
