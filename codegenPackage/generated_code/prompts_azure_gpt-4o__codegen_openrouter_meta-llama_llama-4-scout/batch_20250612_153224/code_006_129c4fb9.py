"""
Generated Code Metadata:
========================
Original URL: https://wordpress.armelin.media
Prompt: Create a WordPress theme or plugin tailored for an architectural firm like Études, emphasizing innovation, sustainability, and professional services for diverse clientele.
Generated: DETERMINISTIC_129c4fb98f2aa1bc
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Études Architectural Firm WordPress Theme**
=============================================

**functions.php**
```php
<?php
/**
 * Études Architectural Firm WordPress Theme
 *
 * @package Études
 */

/**
 * Theme setup and initialization
 */
function etudes_theme_setup() {
    // Load theme text domain
    load_theme_textdomain( 'etudes', get_template_directory() . '/languages' );

    // Add theme support for post thumbnails
    add_theme_support( 'post-thumbnails' );

    // Register menus
    register_nav_menus( array(
        'primary' => __( 'Primary Menu', 'etudes' ),
        'footer' => __( 'Footer Menu', 'etudes' ),
    ) );
}
add_action( 'after_setup_theme', 'etudes_theme_setup' );

/**
 * Enqueue theme styles and scripts
 */
function etudes_enqueue_assets() {
    // Enqueue Google Fonts
    wp_enqueue_style( 'google-fonts', 'https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap' );

    // Enqueue theme stylesheet
    wp_enqueue_style( 'etudes-style', get_stylesheet_uri(), array(), wp_get_theme()->get( 'Version' ) );

    // Enqueue theme scripts
    wp_enqueue_script( 'etudes-script', get_template_directory_uri() . '/js/script.js', array( 'jquery' ), wp_get_theme()->get( 'Version' ), true );
}
add_action( 'wp_enqueue_scripts', 'etudes_enqueue_assets' );

/**
 * Register theme widgets
 */
function etudes_widgets_init() {
    register_sidebar( array(
        'name' => __( 'Footer Widget Area', 'etudes' ),
        'id' => 'footer-widget-area',
        'description' => __( 'Add widgets to the footer area', 'etudes' ),
    ) );
}
add_action( 'widgets_init', 'etudes_widgets_init' );

/**
 * Custom page header
 */
function etudes_page_header() {
    ?>
    <header>
        <nav>
            <?php
            wp_nav_menu( array(
                'theme_location' => 'primary',
                'menu_id' => 'primary-menu',
                'menu_class' => 'primary-menu',
            ) );
            ?>
        </nav>
    </header>
    <?php
}
add_action( 'etudes_header', 'etudes_page_header' );

/**
 * Custom page footer
 */
function etudes_page_footer() {
    ?>
    <footer>
        <div class="footer-widget-area">
            <?php
            dynamic_sidebar( 'footer-widget-area' );
            ?>
        </div>
        <nav>
            <?php
            wp_nav_menu( array(
                'theme_location' => 'footer',
                'menu_id' => 'footer-menu',
                'menu_class' => 'footer-menu',
            ) );
            ?>
        </nav>
    </footer>
    <?php
}
add_action( 'etudes_footer', 'etudes_page_footer' );

/**
 * Custom homepage template
 */
get_template_part( 'template', 'home' );
```

**template-home.php**
```php
<?php
/**
 * Custom homepage template
 *
 * @package Études
 */

get_header();

?>
<div class="hero">
    <h1><?php bloginfo( 'name' ); ?></h1>
    <p><?php bloginfo( 'description' ); ?></p>
</div>

<div class="services">
    <h2><?php _e( 'Our Services', 'etudes' ); ?></h2>
    <ul>
        <?php
        $services = get_posts( array(
            'post_type' => 'service',
            'posts_per_page' => -1,
        ) );

        foreach ( $services as $service ) {
            ?>
            <li>
                <h3><?php echo get_the_title( $service ); ?></h3>
                <p><?php echo get_post_meta( $service->ID, 'description', true ); ?></p>
            </li>
            <?php
        }
        ?>
    </ul>
</div>

<div class="projects">
    <h2><?php _e( 'Our Projects', 'etudes' ); ?></h2>
    <ul>
        <?php
        $projects = get_posts( array(
            'post_type' => 'project',
            'posts_per_page' => -1,
        ) );

        foreach ( $projects as $project ) {
            ?>
            <li>
                <h3><?php echo get_the_title( $project ); ?></h3>
                <p><?php echo get_post_meta( $project->ID, 'description', true ); ?></p>
            </li>
            <?php
        }
        ?>
    </ul>
</div>

<?php
get_footer();
```

**style.css**
```css
body {
    font-family: 'Open Sans', sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

.hero {
    background-image: url(<?php echo get_template_directory_uri(); ?>/images/hero.jpg);
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.services {
    padding: 2em;
}

.services ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.services li {
    margin-bottom: 20px;
}

.projects {
    padding: 2em;
}

.projects ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.projects li {
    margin-bottom: 20px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

footer nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

footer nav ul li {
    display: inline-block;
    margin-right: 20px;
}

footer nav a {
    color: #fff;
    text-decoration: none;
}
```

**js/script.js**
```javascript
jQuery(document).ready(function($) {
    // Add smooth scrolling to all links
    $("a").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function() {
                window.location.hash = hash;
            });
        }
    });
});
```

**class-service.php**
```php
<?php
/**
 * Service post type
 *
 * @package Études
 */

class Etudes_Service_Post_Type {
    public function __construct() {
        add_action( 'init', array( $this, 'register_post_type' ) );
    }

    public function register_post_type() {
        register_post_type( 'service',
            array(
                'labels' => array(
                    'name' => __( 'Services', 'etudes' ),
                    'singular_name' => __( 'Service', 'etudes' ),
                ),
                'public' => true,
                'has_archive' => true,
                'supports' => array( 'title', 'editor', 'thumbnail' ),
            )
        );
    }
}

$etudes_service_post_type = new Etudes_Service_Post_Type();
```

**class-project.php**
```php
<?php
/**
 * Project post type
 *
 * @package Études
 */

class Etudes_Project_Post_Type {
    public function __construct() {
        add_action( 'init', array( $this, 'register_post_type' ) );
    }

    public function register_post_type() {
        register_post_type( 'project',
            array(
                'labels' => array(
                    'name' => __( 'Projects', 'etudes' ),
                    'singular_name' => __( 'Project', 'etudes' ),
                ),
                'public' => true,
                'has_archive' => true,
                'supports' => array( 'title', 'editor', 'thumbnail' ),
            )
        );
    }
}

$etudes_project_post_type = new Etudes_Project_Post_Type();
```
