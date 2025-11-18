"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sajumavi.edu.pe
Prompt: Generate PHP code for embedding a virtual classroom iframe into a WordPress page template.
Generated: DETERMINISTIC_c6eed7fcd1dfd71c
Batch ID: 20250612_150440
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
 * Template Name: Virtual Classroom
 * Description: A custom page template to embed a virtual classroom iframe.
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Get the iframe URL from a custom field (you can set this in the page editor)
$iframe_url = get_post_meta(get_the_ID(), 'virtual_classroom_url', true);

// Check if the iframe URL is valid
if (empty($iframe_url) || !filter_var($iframe_url, FILTER_VALIDATE_URL)) {
    $iframe_url = ''; // Reset to empty if invalid
    $error_message = 'Invalid URL for the virtual classroom.';
}

get_header(); // Include the header template

?>

<div class="virtual-classroom-container">
    <?php if (!empty($iframe_url)): ?>
        <iframe 
            src="<?php echo esc_url($iframe_url); ?>" 
            width="100%" 
            height="600" 
            frameborder="0" 
            allow="camera; microphone; autoplay; encrypted-media"
            title="Virtual Classroom"
        ></iframe>
    <?php else: ?>
        <div class="error-message" style="color: red;">
            <?php echo esc_html($error_message); ?>
        </div>
    <?php endif; ?>
</div>

<?php get_footer(); // Include the footer template ?>
```

### Instructions:
1. Save this code in a new PHP file in your active theme's directory (e.g., `virtual-classroom.php`).
2. Create a new page in WordPress and select "Virtual Classroom" as the template.
3. Add a custom field named `virtual_classroom_url` with the value being the URL of the virtual classroom you want to embed.
4. Ensure that the URL is valid before it is displayed in the iframe.
