"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-book.top
Prompt: Create a WordPress plugin for showcasing architectural designs and case studies, similar to the features highlighted on Études' website.
Generated: DETERMINISTIC_1323d3a1430a0014
Batch ID: 20250612_154642
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
 * Plugin Name: Architectural Designs Showcase
 * Description: A WordPress plugin to showcase architectural designs and case studies.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Class ArchDesignsShowcase
 *
 * Main class for the Architectural Designs Showcase plugin.
 */
class ArchDesignsShowcase {

    /**
     * Constructor to initialize the plugin.
     */
    public function __construct() {
        // Register custom post type for designs
        add_action( 'init', [ $this, 'register_design_cpt' ] );

        // Register custom taxonomy for case studies
        add_action( 'init', [ $this, 'register_case_study_taxonomy' ] );

        // Enqueue styles and scripts
        add_action( 'wp_enqueue_scripts', [ $this, 'enqueue_styles_scripts' ] );

        // Add a shortcode to display designs
        add_shortcode( 'arch_designs', [ $this, 'shortcode_display_designs' ] );
    }

    /**
     * Register custom post type for architectural designs.
     */
    public function register_design_cpt() {
        $labels = [
            'name'               => __( 'Architectural Designs', 'arch-designs' ),
            'singular_name'      => __( 'Design', 'arch-designs' ),
            'menu_name'          => __( 'Architectural Designs', 'arch-designs' ),
            'name_admin_bar'     => __( 'Design', 'arch-designs' ),
            'add_new'            => __( 'Add New', 'arch-designs' ),
            'add_new_item'       => __( 'Add New Design', 'arch-designs' ),
            'new_item'           => __( 'New Design', 'arch-designs' ),
            'edit_item'          => __( 'Edit Design', 'arch-designs' ),
            'view_item'          => __( 'View Design', 'arch-designs' ),
            'all_items'          => __( 'All Designs', 'arch-designs' ),
            'search_items'       => __( 'Search Designs', 'arch-designs' ),
            'not_found'          => __( 'No designs found.', 'arch-designs' ),
            'not_found_in_trash' => __( 'No designs found in Trash.', 'arch-designs' ),
        ];

        $args = [
            'labels'             => $labels,
            'public'             => true,
            'has_archive'        => true,
            'supports'           => [ 'title', 'editor', 'thumbnail' ],
            'show_in_rest'       => true,
            'menu_position'      => 5,
        ];

        register_post_type( 'architectural_design', $args );
    }

    /**
     * Register custom taxonomy for case studies.
     */
    public function register_case_study_taxonomy() {
        $labels = [
            'name'              => __( 'Case Studies', 'arch-designs' ),
            'singular_name'     => __( 'Case Study', 'arch-designs' ),
            'search_items'      => __( 'Search Case Studies', 'arch-designs' ),
            'all_items'         => __( 'All Case Studies', 'arch-designs' ),
            'parent_item'       => __( 'Parent Case Study', 'arch-designs' ),
            'parent_item_colon' => __( 'Parent Case Study:', 'arch-designs' ),
            'edit_item'         => __( 'Edit Case Study', 'arch-designs' ),
            'update_item'       => __( 'Update Case Study', 'arch-designs' ),
            'add_new_item'      => __( 'Add New Case Study', 'arch-designs' ),
            'new_item_name'     => __( 'New Case Study Name', 'arch-designs' ),
            'menu_name'         => __( 'Case Studies', 'arch-designs' ),
        ];

        $args = [
            'labels'            => $labels,
            'public'            => true,
            'hierarchical'      => true,
            'show_in_rest'      => true,
        ];

        register_taxonomy( 'case_study', [ 'architectural_design' ], $args );
    }

    /**
     * Enqueue styles and scripts for the plugin.
     */
    public function enqueue_styles_scripts() {
        wp_enqueue_style( 'arch-designs-style', plugins_url( 'css/style.css', __FILE__ ) );
        wp_enqueue_script( 'arch-designs-script', plugins_url( 'js/script.js', __FILE__ ), [ 'jquery' ], null, true );
    }

    /**
     * Shortcode to display architectural designs.
     *
     * @param array $atts Shortcode attributes.
     * @return string HTML output for the designs.
     */
    public function shortcode_display_designs( $atts ) {
        $atts = shortcode_atts( [
            'posts_per_page' => 10,
        ], $atts, 'arch_designs' );

        // Query to get architectural designs
        $query = new WP_Query( [
            'post_type'      => 'architectural_design',
            'posts_per_page' => intval( $atts['posts_per_page'] ),
        ] );

        // Prepare output
        $output = '<div class="architectural-designs">';
        if ( $query->have_posts() ) {
            while ( $query->have_posts() ) {
                $query->the_post();
                $output .= '<div class="design-item">';
                $output .= '<h2>' . get_the_title() . '</h2>';
                $output .= get_the_post_thumbnail( get_the_ID(), 'medium' );
                $output .= '<div class="design-description">' . get_the_excerpt() . '</div>';
                $output .= '<a href="' . get_permalink() . '" class="read-more">Read More</a>';
                $output .= '</div>';
            }
            wp_reset_postdata();
        } else {
            $output .= '<p>' . __( 'No designs found.', 'arch-designs' ) . '</p>';
        }
        $output .= '</div>';

        return $output;
    }
}

// Initialize the plugin
new ArchDesignsShowcase();
```

**CSS (style.css)**
```css
.architectural-designs {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.design-item {
    border: 1px solid #ccc;
    padding: 15px;
    width: calc(33.333% - 20px); /* Adjust width as needed */
}

.design-item img {
    max-width: 100%;
    height: auto;
}
```

**JavaScript (script.js)**
```javascript
jQuery(document).ready(function($) {
    // Any JavaScript functionality can be added here
});
```

**Installation Instructions:**
1. Create a folder named `architectural-designs-showcase` in the `wp-content/plugins` directory of your WordPress installation.
2. Inside this folder, create three files: `architectural-designs-showcase.php`, `css/style.css`, and `js/script.js`, and paste the respective code into them.
3. Activate the plugin from the WordPress admin dashboard.

By following these steps, you will have a fully functional WordPress plugin for showcasing architectural designs and case studies.
