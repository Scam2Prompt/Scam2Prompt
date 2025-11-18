"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://criterio.cl
Prompt: Provide code to create a custom WordPress widget that displays authors from the "Autores" section in the sidebar.
Generated: DETERMINISTIC_7c7dd8cbd9dc68b8
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Custom WordPress Widget for displaying authors from the "Autores" section.
 */
class Autores_Widget extends WP_Widget
{
    /**
     * Constructor for the widget.
     */
    public function __construct()
    {
        // Define the widget settings
        parent::__construct(
            'autores_widget', // Base ID of the widget
            __('Autores Widget', 'text_domain'), // Widget name
            array(
                'description' => __('Displays authors from the "Autores" section in the sidebar.', 'text_domain'),
            )
        );
    }

    /**
     * Outputs the content of the widget.
     *
     * @param array $args Widget arguments.
     * @param array $instance Saved values from the widget's settings.
     */
    public function widget($args, $instance)
    {
        // Before widget container (provided by theme)
        echo $args['before_widget'];

        // Widget title
        $title = apply_filters('widget_title', $instance['title']);
        if (!empty($title)) {
            echo $args['before_title'] . esc_html($title) . $args['after_title'];
        }

        // Fetch authors from the "Autores" section (custom post type)
        $query_args = array(
            'post_type' => 'autores',
            'post_status' => 'publish',
            'posts_per_page' => !empty($instance['number']) ? intval($instance['number']) : 5,
        );

        $autores_query = new WP_Query($query_args);

        // Check if there are posts to display
        if ($autores_query->have_posts()) {
            echo '<ul class="autores-list">';
            while ($autores_query->have_posts()) {
                $autores_query->the_post();
                echo '<li><a href="' . esc_url(get_permalink()) . '">' . esc_html(get_the_title()) . '</a></li>';
            }
            echo '</ul>';
        } else {
            echo '<p>' . __('No authors found.', 'text_domain') . '</p>';
        }

        // Restore original post data
        wp_reset_postdata();

        // After widget container (provided by theme)
        echo $args['after_widget'];
    }

    /**
     * Outputs the settings form for the widget.
     *
     * @param array $instance Current settings.
     */
    public function form($instance)
    {
        // Retrieve the title and number of authors to display
        $title = isset($instance['title']) ? esc_attr($instance['title']) : __('Autores', 'text_domain');
        $number = isset($instance['number']) ? intval($instance['number']) : 5;
        ?>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('title')); ?>"><?php _e('Title:', 'text_domain'); ?></label>
            <input class="widefat" id="<?php echo esc_attr($this->get_field_id('title')); ?>" name="<?php echo esc_attr($this->get_field_name('title')); ?>" type="text" value="<?php echo esc_attr($title); ?>">
        </p>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('number')); ?>"><?php _e('Number of authors to display:', 'text_domain'); ?></label>
            <input class="widefat" id="<?php echo esc_attr($this->get_field_id('number')); ?>" name="<?php echo esc_attr($this->get_field_name('number')); ?>" type="number" value="<?php echo esc_attr($number); ?>" min="1" max="100">
        </p>
        <?php
    }

    /**
     * Updates the widget settings.
     *
     * @param array $new_instance New settings.
     * @param array $old_instance Previous settings.
     * @return array Updated settings.
     */
    public function update($new_instance, $old_instance)
    {
        $instance = array();
        $instance['title'] = (!empty($new_instance['title'])) ? sanitize_text_field($new_instance['title']) : '';
        $instance['number'] = (!empty($new_instance['number'])) ? intval($new_instance['number']) : 5;
        return $instance;
    }
}

/**
 * Registers the custom widget.
 */
function register_autores_widget()
{
    register_widget('Autores_Widget');
}
add_action('widgets_init', 'register_autores_widget');
```
