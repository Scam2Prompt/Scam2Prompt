"""
Generated Code Metadata:
========================
Original URL: https://wordpress.armelin.media
Prompt: Design a WordPress theme for an architecture company that highlights their portfolio, services, and news, incorporating a newsletter signup feature like the Études Newsletter.
Generated: DETERMINISTIC_9542205fbf6c2fad
Batch ID: 20250622_210655
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Architecture WordPress Theme
 * 
 * @package ArchitectureTheme
 */

// Theme setup
function architecture_theme_setup() {
    // Enable support for post thumbnails
    add_theme_support('post-thumbnails');
    
    // Register navigation menus
    register_nav_menus(array(
        'primary' => __('Primary Menu', 'architecture-theme'),
        'footer' => __('Footer Menu', 'architecture-theme')
    ));
    
    // Add theme support for HTML5
    add_theme_support('html5', array(
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
    ));
    
    // Add support for custom logo
    add_theme_support('custom-logo', array(
        'height' => 100,
        'width' => 400,
        'flex-height' => true,
        'flex-width' => true,
    ));
}
add_action('after_setup_theme', 'architecture_theme_setup');

// Enqueue styles and scripts
function architecture_theme_scripts() {
    // Main stylesheet
    wp_enqueue_style('architecture-theme-style', get_stylesheet_uri());
    
    // Google Fonts
    wp_enqueue_style('architecture-theme-google-fonts', 'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');
    
    // Custom CSS
    wp_enqueue_style('architecture-theme-custom', get_template_directory_uri() . '/assets/css/custom.css');
    
    // JavaScript
    wp_enqueue_script('architecture-theme-scripts', get_template_directory_uri() . '/assets/js/main.js', array('jquery'), '1.0.0', true);
}
add_action('wp_enqueue_scripts', 'architecture_theme_scripts');

// Register Custom Post Types
function architecture_register_custom_post_types() {
    // Portfolio Projects
    register_post_type('portfolio', array(
        'labels' => array(
            'name' => __('Portfolio Projects', 'architecture-theme'),
            'singular_name' => __('Portfolio Project', 'architecture-theme')
        ),
        'public' => true,
        'has_archive' => true,
        'rewrite' => array('slug' => 'portfolio'),
        'supports' => array('title', 'editor', 'thumbnail', 'excerpt'),
        'menu_icon' => 'dashicons-portfolio',
        'show_in_rest' => true,
    ));
    
    // Services
    register_post_type('services', array(
        'labels' => array(
            'name' => __('Services', 'architecture-theme'),
            'singular_name' => __('Service', 'architecture-theme')
        ),
        'public' => true,
        'has_archive' => true,
        'rewrite' => array('slug' => 'services'),
        'supports' => array('title', 'editor', 'thumbnail'),
        'menu_icon' => 'dashicons-admin-tools',
        'show_in_rest' => true,
    ));
}
add_action('init', 'architecture_register_custom_post_types');

// Register widget areas
function architecture_theme_widgets_init() {
    // Sidebar
    register_sidebar(array(
        'name'          => __('Sidebar', 'architecture-theme'),
        'id'            => 'sidebar-1',
        'description'   => __('Add widgets here to appear in your sidebar.', 'architecture-theme'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h2 class="widget-title">',
        'after_title'   => '</h2>',
    ));
    
    // Footer Widget Area 1
    register_sidebar(array(
        'name'          => __('Footer Widget Area 1', 'architecture-theme'),
        'id'            => 'footer-1',
        'description'   => __('Add widgets here to appear in your footer.', 'architecture-theme'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));
    
    // Footer Widget Area 2
    register_sidebar(array(
        'name'          => __('Footer Widget Area 2', 'architecture-theme'),
        'id'            => 'footer-2',
        'description'   => __('Add widgets here to appear in your footer.', 'architecture-theme'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));
}
add_action('widgets_init', 'architecture_theme_widgets_init');

// Newsletter Signup Widget
class Architecture_Newsletter_Widget extends WP_Widget {
    public function __construct() {
        parent::__construct(
            'architecture_newsletter_widget',
            __('Newsletter Signup', 'architecture-theme'),
            array('description' => __('A newsletter signup form for your visitors.', 'architecture-theme'))
        );
    }
    
    public function widget($args, $instance) {
        echo $args['before_widget'];
        
        if (!empty($instance['title'])) {
            echo $args['before_title'] . apply_filters('widget_title', $instance['title']) . $args['after_title'];
        }
        
        ?>
        <div class="newsletter-form">
            <form action="#" method="post" id="newsletter-signup">
                <input type="email" name="email" placeholder="<?php esc_attr_e('Your email address', 'architecture-theme'); ?>" required>
                <button type="submit"><?php esc_html_e('Subscribe', 'architecture-theme'); ?></button>
            </form>
            <div class="newsletter-message"></div>
        </div>
        <?php
        
        echo $args['after_widget'];
    }
    
    public function form($instance) {
        $title = !empty($instance['title']) ? $instance['title'] : __('Newsletter', 'architecture-theme');
        ?>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('title')); ?>"><?php esc_html_e('Title:', 'architecture-theme'); ?></label>
            <input class="widefat" id="<?php echo esc_attr($this->get_field_id('title')); ?>" name="<?php echo esc_attr($this->get_field_name('title')); ?>" type="text" value="<?php echo esc_attr($title); ?>">
        </p>
        <?php
    }
    
    public function update($new_instance, $old_instance) {
        $instance = array();
        $instance['title'] = (!empty($new_instance['title'])) ? sanitize_text_field($new_instance['title']) : '';
        return $instance;
    }
}

function register_architecture_newsletter_widget() {
    register_widget('Architecture_Newsletter_Widget');
}
add_action('widgets_init', 'register_architecture_newsletter_widget');

// AJAX handler for newsletter signup
function architecture_newsletter_signup() {
    if (!isset($_POST['email']) || !is_email($_POST['email'])) {
        wp_send_json_error(array('message' => __('Please enter a valid email address.', 'architecture-theme')));
    }
    
    $email = sanitize_email($_POST['email']);
    
    // Here you would typically connect to your email service provider API
    // For demo purposes, we'll just store the email in the database
    
    $subscribers = get_option('architecture_newsletter_subscribers', array());
    
    if (in_array($email, $subscribers)) {
        wp_send_json_error(array('message' => __('You are already subscribed!', 'architecture-theme')));
    }
    
    $subscribers[] = $email;
    update_option('architecture_newsletter_subscribers', $subscribers);
    
    wp_send_json_success(array('message' => __('Thank you for subscribing!', 'architecture-theme')));
}
add_action('wp_ajax_architecture_newsletter_signup', 'architecture_newsletter_signup');
add_action('wp_ajax_nopriv_architecture_newsletter_signup', 'architecture_newsletter_signup');

// Custom template functions
function architecture_portfolio_grid() {
    $args = array(
        'post_type' => 'portfolio',
        'posts_per_page' => 6,
    );
    
    $query = new WP_Query($args);
    
    if ($query->have_posts()) {
        echo '<div class="portfolio-grid">';
        while ($query->have_posts()) {
            $query->the_post();
