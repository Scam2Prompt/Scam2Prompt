"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://36destinations.com
Prompt: Create a WordPress shortcode to add a "Scroll to Top" button for a site using the Astra theme.
Generated: DETERMINISTIC_4058c9427990e3e0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Function to enqueue necessary styles and scripts for the Scroll to Top button
function enqueue_scroll_to_top_assets() {
    wp_enqueue_style('scroll-to-top-styles', get_template_directory_uri() . '/scroll-to-top.css', array(), '1.0.0', 'all');
    wp_enqueue_script('scroll-to-top-script', get_template_directory_uri() . '/scroll-to-top.js', array('jquery'), '1.0.0', true);
}
add_action('wp_enqueue_scripts', 'enqueue_scroll_to_top_assets');

// Function to generate the Scroll to Top button shortcode
function scroll_to_top_shortcode() {
    return '<button id="scroll-to-top" class="scroll-to-top">↑ Scroll to Top</button>';
}
add_shortcode('scroll_to_top', 'scroll_to_top_shortcode');

// Adding inline styles in case external CSS is not loaded
add_action('wp_head', function() {
    echo '<style>
        .scroll-to-top {
            display: none;
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #333;
            color: #fff;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            z-index: 1000;
        }
        .scroll-to-top:hover {
            background-color: #555;
        }
    </style>';
});

// Adding inline JS in case external JS is not loaded
add_action('wp_footer', function() {
    echo '<script>
        jQuery(document).ready(function($) {
            var $scrollButton = $("#scroll-to-top");
            
            // Show button when scrolling down
            $(window).scroll(function() {
                if ($(this).scrollTop() > 300) {
                    $scrollButton.fadeIn();
                } else {
                    $scrollButton.fadeOut();
                }
            });

            // Scroll to top functionality
            $scrollButton.click(function() {
                $("html, body").animate({scrollTop: 0}, 500);
                return false;
            });
        });
    </script>';
});
?>
```

Make sure to create `scroll-to-top.css` and `scroll-to-top.js` files if you prefer external styles and scripts over inline ones. Add your customizations there for production environments.
