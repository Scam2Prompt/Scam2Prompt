"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordpress.armelin.media
Prompt: Create a WordPress theme or plugin tailored for an architectural firm like Études, emphasizing innovation, sustainability, and professional services for diverse clientele.
Generated: DETERMINISTIC_129c4fb98f2aa1bc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a WordPress plugin tailored for an architectural firm like Études. This plugin adds a custom post type for "Projects," includes custom fields for project details, and creates a shortcode to display featured projects.

```php
<?php
/**
 * Plugin Name: Études Architectural Projects
 * Description: A custom plugin for managing and showcasing architectural projects with emphasis on innovation and sustainability.
 * Version: 1.0.0
 * Author: [Your Name]
 * Text Domain: etudes-architectural
 */

// Prevent direct access to the file.
if (!defined('ABSPATH')) {
    exit;
}

class EtudesArchitecturalProjects {
    /**
     * Constructor to initialize the plugin.
     */
    public function __construct() {
        // Hook to register the custom post type.
        add_action('init', [$this, 'register_projects_post_type']);

        // Hook to register custom meta fields.
        add_action('add_meta_boxes', [$this, 'add_project_meta_boxes']);
        add_action('save_post', [$this, 'save_project_meta']);

        // Register shortcode to display featured projects.
        add_shortcode('featured_projects', [$this, 'display_featured_projects']);
    }

    /**
     * Register custom post type: Projects.
     */
    public function register_projects_post_type() {
        $labels = [
            'name' => __('Projects', 'etudes-architectural'),
            'singular_name' => __('Project', 'etudes-architectural'),
            'add_new' => __('Add New Project', 'etudes-architectural'),
            'all_items' => __('All Projects', 'etudes-architectural'),
            'edit_item' => __('Edit Project', 'etudes-architectural'),
            'view_item' => __('View Project', 'etudes-architectural'),
            'search_items' => __('Search Projects', 'etudes-architectural')
        ];

        $args = [
            'labels' => $labels,
            'public' => true,
            'has_archive' => true,
            'supports' => ['title', 'editor', 'thumbnail'],
            'rewrite' => ['slug' => 'projects'],
            'menu_icon' => 'dashicons-building',
        ];

        register_post_type('etudes_projects', $args);
    }

    /**
     * Add meta boxes for custom fields.
     */
    public function add_project_meta_boxes() {
        add_meta_box(
            'project_details',
            __('Project Details', 'etudes-architectural'),
            [$this, 'render_project_meta_box'],
            'etudes_projects',
            'normal',
            'high'
        );
    }

    /**
     * Render the meta box for project details.
     */
    public function render_project_meta_box($post) {
        // Retrieve existing meta values.
        $location = get_post_meta($post->ID, '_project_location', true);
        $completion_date = get_post_meta($post->ID, '_project_completion_date', true);

        // Security nonce.
        wp_nonce_field('save_project_meta', 'project_meta_nonce');
        ?>
        <p>
            <label for="project_location"><?php _e('Location:', 'etudes-architectural'); ?></label>
            <input type="text" id="project_location" name="project_location" value="<?php echo esc_attr($location); ?>" />
        </p>
        <p>
            <label for="project_completion_date"><?php _e('Completion Date:', 'etudes-architectural'); ?></label>
            <input type="date" id="project_completion_date" name="project_completion_date" value="<?php echo esc_attr($completion_date); ?>" />
        </p>
        <?php
    }

    /**
     * Save the custom meta fields when the post is saved.
     */
    public function save_project_meta($post_id) {
        // Verify nonce and prevent unauthorized saves.
        if (!isset($_POST['project_meta_nonce']) || !wp_verify_nonce($_POST['project_meta_nonce'], 'save_project_meta')) {
            return;
        }

        // Save Location.
        if (isset($_POST['project_location'])) {
            update_post_meta($post_id, '_project_location', sanitize_text_field($_POST['project_location']));
        }

        // Save Completion Date.
        if (isset($_POST['project_completion_date'])) {
            update_post_meta($post_id, '_project_completion_date', sanitize_text_field($_POST['project_completion_date']));
        }
    }

    /**
     * Shortcode to display featured projects.
     */
    public function display_featured_projects($atts) {
        ob_start();

        // Query for featured projects.
        $query = new WP_Query([
            'post_type' => 'etudes_projects',
            'posts_per_page' => 3,
            'meta_key' => '_project_completion_date',
            'orderby' => 'meta_value',
            'order' => 'DESC'
        ]);

        if ($query->have_posts()) {
            echo '<div class="featured-projects">';
            while ($query->have_posts()) {
                $query->the_post();

                // Retrieve custom meta fields.
                $location = get_post_meta(get_the_ID(), '_project_location', true);
                $completion_date = get_post_meta(get_the_ID(), '_project_completion_date', true);

                // Render project details.
                ?>
                <div class="project">
                    <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
                    <p><?php echo esc_html__('Location:', 'etudes-architectural') . ' ' . esc_html($location); ?></p>
                    <p><?php echo esc_html__('Completion Date:', 'etudes-architectural') . ' ' . esc_html($completion_date); ?></p>
                    <?php the_post_thumbnail('medium'); ?>
                </div>
                <?php
            }
            echo '</div>';
        } else {
            echo '<p>' . __('No featured projects found.', 'etudes-architectural') . '</p>';
        }

        wp_reset_postdata();

        return ob_get_clean();
    }
}

// Initialize the plugin.
new EtudesArchitecturalProjects();
?>
```
