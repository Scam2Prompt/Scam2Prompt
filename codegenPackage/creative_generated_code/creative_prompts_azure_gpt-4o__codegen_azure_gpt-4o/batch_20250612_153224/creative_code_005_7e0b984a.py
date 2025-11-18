"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbandjock.fr
Prompt: Generate PHP code for a WordPress widget that lists archives by month, as seen on the MBANDJOCK site.
Generated: DETERMINISTIC_7e0b984a1aa64f63
Batch ID: 20250612_153224
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
 * Plugin Name: Custom Monthly Archives Widget
 * Description: A WordPress widget for displaying monthly archives.
 * Version: 1.0
 * Author: Your Name
 */

class Custom_Monthly_Archives_Widget extends WP_Widget {
    /**
     * Initialize the widget.
     */
    public function __construct() {
        parent::__construct(
            'custom_monthly_archives_widget', // Base ID
            __('Monthly Archives Widget', 'text_domain'), // Widget Name
            array('description' => __('Displays monthly archives.', 'text_domain')) // Args
        );
    }

    /**
     * Render the widget output on the front-end.
     *
     * @param array $args Widget arguments provided by WordPress.
     * @param array $instance Widget settings provided by the user.
     */
    public function widget($args, $instance) {
        echo $args['before_widget']; // Output widget wrapper

        if (!empty($instance['title'])) {
            // Output the title if set
            echo $args['before_title'] . apply_filters('widget_title', $instance['title']) . $args['after_title'];
        }

        // Fetch and display the monthly archives
        echo '<ul>';
        wp_get_archives(array(
            'type' => 'monthly',
            'show_post_count' => true, // Show the post count per month
        ));
        echo '</ul>';

        echo $args['after_widget']; // Close widget wrapper
    }

    /**
     * Render widget settings form in the admin dashboard.
     *
     * @param array $instance Widget settings provided by the user.
     * @return void
     */
    public function form($instance) {
        // Retrieve the title from settings or set a default value
        $title = !empty($instance['title']) ? $instance['title'] : __('Monthly Archives', 'text_domain');
        ?>
        <p>
            <label for="<?php echo $this->get_field_id('title'); ?>"><?php _e('Title:', 'text_domain'); ?></label>
            <input
                class="widefat"
                id="<?php echo $this->get_field_id('title'); ?>"
                name="<?php echo $this->get_field_name('title'); ?>"
                type="text"
                value="<?php echo esc_attr($title); ?>"
            />
        </p>
        <?php
    }

    /**
     * Save widget settings.
     *
     * @param array $new_instance New settings.
     * @param array $old_instance Previous settings.
     * @return array Updated settings.
     */
    public function update($new_instance, $old_instance) {
        $instance = array();
        $instance['title'] = (!empty($new_instance['title'])) ? strip_tags($new_instance['title']) : '';
        return $instance;
    }
}

// Register the widget
function register_custom_monthly_archives_widget() {
    register_widget('Custom_Monthly_Archives_Widget');
}
add_action('widgets_init', 'register_custom_monthly_archives_widget');
```
