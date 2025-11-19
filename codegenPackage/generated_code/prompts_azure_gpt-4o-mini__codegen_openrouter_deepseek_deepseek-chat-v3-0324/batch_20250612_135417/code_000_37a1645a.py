"""
Generated Code Metadata:
========================
Original URL: https://tiffany-holz.de
Prompt: Generate a code snippet for a gallery display using the Ashe theme for WordPress.
Generated: DETERMINISTIC_37a1645a509e44c7
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
 * Ashe Theme Gallery Display
 * 
 * This code snippet enhances the gallery display in the Ashe WordPress theme.
 * It ensures proper styling and responsive behavior for gallery images.
 */

// Enqueue necessary scripts and styles
function ashe_gallery_enqueue_assets() {
    wp_enqueue_style(
        'ashe-gallery-css',
        get_template_directory_uri() . '/css/gallery.css',
        array(),
        '1.0.0'
    );
    
    wp_enqueue_script(
        'ashe-gallery-js',
        get_template_directory_uri() . '/js/gallery.js',
        array('jquery'),
        '1.0.0',
        true
    );
}
add_action('wp_enqueue_scripts', 'ashe_gallery_enqueue_assets');

// Custom gallery shortcode output
function ashe_custom_gallery($output, $attr) {
    global $post;

    static $instance = 0;
    $instance++;

    // Validate attributes
    if (isset($attr['orderby'])) {
        $attr['orderby'] = sanitize_sql_orderby($attr['orderby']);
        if (!$attr['orderby']) {
            unset($attr['orderby']);
        }
    }

    // Default attributes
    $atts = shortcode_atts(array(
        'order'      => 'ASC',
        'orderby'    => 'menu_order ID',
        'id'         => $post ? $post->ID : 0,
        'size'       => 'large',
        'include'    => '',
        'exclude'    => '',
        'link'       => '',
        'columns'    => 3
    ), $attr, 'gallery');

    // Get gallery images
    $id = intval($atts['id']);
    if ('RAND' == $atts['order']) {
        $atts['orderby'] = 'none';
    }

    if (!empty($atts['include'])) {
        $include = preg_replace('/[^0-9,]+/', '', $atts['include']);
        $_attachments = get_posts(array(
            'include' => $include,
            'post_status' => 'inherit',
            'post_type' => 'attachment',
            'post_mime_type' => 'image',
            'order' => $atts['order'],
            'orderby' => $atts['orderby']
        ));

        $attachments = array();
        foreach ($_attachments as $key => $val) {
            $attachments[$val->ID] = $_attachments[$key];
        }
    } elseif (!empty($atts['exclude'])) {
        $exclude = preg_replace('/[^0-9,]+/', '', $atts['exclude']);
        $attachments = get_children(array(
            'post_parent' => $id,
            'exclude' => $exclude,
            'post_status' => 'inherit',
            'post_type' => 'attachment',
            'post_mime_type' => 'image',
            'order' => $atts['order'],
            'orderby' => $atts['orderby']
        ));
    } else {
        $attachments = get_children(array(
            'post_parent' => $id,
            'post_status' => 'inherit',
            'post_type' => 'attachment',
            'post_mime_type' => 'image',
            'order' => $atts['order'],
            'orderby' => $atts['orderby']
        ));
    }

    if (empty($attachments)) {
        return '';
    }

    // Generate gallery HTML
    $columns = intval($atts['columns']);
    $itemwidth = $columns > 0 ? floor(100/$columns) : 100;
    $float = is_rtl() ? 'right' : 'left';

    $selector = "gallery-{$instance}";
    $size_class = sanitize_html_class($atts['size']);

    $output = "<div id='$selector' class='gallery galleryid-{$id} gallery-columns-{$columns} gallery-size-{$size_class}'>";

    $i = 0;
    foreach ($attachments as $id => $attachment) {
        $attr = (trim($attachment->post_excerpt)) ? array('aria-describedby' => "$selector-$id") : array();
        $image_output = wp_get_attachment_link($id, $atts['size'], false, false, false, $attr);
        
        $output .= "<figure class='gallery-item'>";
        $output .= "<div class='gallery-icon'>$image_output</div>";
        
        if (trim($attachment->post_excerpt)) {
            $output .= "<figcaption class='wp-caption-text gallery-caption' id='$selector-$id'>" 
                . wptexturize($attachment->post_excerpt) . "</figcaption>";
        }
        
        $output .= "</figure>";
        
        if ($columns > 0 && ++$i % $columns == 0) {
            $output .= '<br style="clear: both" />';
        }
    }

    $output .= "<br style='clear: both;' /></div>\n";

    return $output;
}
add_filter('post_gallery', 'ashe_custom_gallery', 10, 2);

// Add gallery lightbox support
function ashe_gallery_lightbox() {
    ?>
    <script type="text/javascript">
    jQuery(document).ready(function($) {
        $('.gallery a').magnificPopup({
            type: 'image',
            gallery: {
                enabled: true
            },
            image: {
                titleSrc: function(item) {
                    return item.el.find('img').attr('alt') || '';
                }
            }
        });
    });
    </script>
    <?php
}
add_action('wp_footer', 'ashe_gallery_lightbox');
```
