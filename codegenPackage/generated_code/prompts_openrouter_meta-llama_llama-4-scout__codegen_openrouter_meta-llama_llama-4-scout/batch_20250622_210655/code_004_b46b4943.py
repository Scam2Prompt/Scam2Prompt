"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: "Create a web app using WordPress to showcase architectural projects similar to Études' portfolio."
Generated: DETERMINISTIC_b46b4943bb75fe0d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**WordPress Theme: Architectural Portfolio**

**Directory Structure:**
```markdown
architectural-portfolio/
|- index.php
|- style.css
|- functions.php
|- page-templates/
    |- portfolio.php
|- template-parts/
    |- project.php
|- assets/
    |- css/
        |- style.css
    |- js/
        |- script.js
|- class-portfolio-post-type.php
|- class-project-meta-boxes.php
|- README.md
```

**index.php**
```php
<?php
/**
 * The main template file.
 *
 * @package Architectural_Portfolio
 */

get_header(); ?>

<div id="primary" class="content-area">
    <main id="main" class="site-main">
        <?php
        if ( have_posts() ) :

            if ( is_home() && ! is_front_page() ) :
                ?>
                <header>
                    <h1 class="page-title screen-reader-text"><?php single_post_title(); ?></h1>
                </header>
                <?php
            endif;

            while ( have_posts() ) : the_post();

                get_template_part( 'template-parts/project', get_post_format() );

            endwhile;

            the_posts_pagination( array(
                'prev_text'    => __( 'Previous', 'architectural-portfolio' ),
                'next_text'    => __( 'Next', 'architectural-portfolio' ),
                'screen_reader_text' => __( 'Posts navigation', 'architectural-portfolio' ),
            ) );

        else :

            get_template_part( 'template-parts/content', 'none' );

        endif;
        ?>
    </main><!-- #main -->
</div><!-- #primary -->

<?php
get_footer();
```

**style.css**
```css
/* 
Theme Name: Architectural Portfolio
Description: A WordPress theme for showcasing architectural projects.
Version: 1.0
*/

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.site-main {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.project {
    margin: 20px;
    width: calc(33.33% - 20px);
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.project h2 {
    margin-top: 0;
}

.project-meta {
    font-size: 14px;
    color: #666;
}
```

**functions.php**
```php
<?php
/**
 * Architectural Portfolio functions and definitions.
 *
 * @package Architectural_Portfolio
 */

if ( ! isset( $content_width ) ) {
    $content_width = 800; /* pixels */
}

add_theme_support( 'automatic-feed-links' );
add_theme_support( 'post-thumbnails' );
add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption' ) );

register_nav_menus( array(
    'primary' => __( 'Primary Menu', 'architectural-portfolio' ),
) );

require get_template_directory() . '/class-portfolio-post-type.php';
require get_template_directory() . '/class-project-meta-boxes.php';

function architectural_portfolio_scripts() {
    wp_enqueue_style( 'architectural-portfolio-style', get_stylesheet_uri() );
    wp_enqueue_script( 'architectural-portfolio-script', get_template_directory_uri() . '/assets/js/script.js', array( 'jquery' ), '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'architectural_portfolio_scripts' );
```

**page-templates/portfolio.php**
```php
<?php
/**
 * Template Name: Portfolio
 *
 * @package Architectural_Portfolio
 */

get_header(); ?>

<div id="primary" class="content-area">
    <main id="main" class="site-main">
        <?php
        $args = array(
            'post_type' => 'project',
            'posts_per_page' => -1,
        );
        $projects = new WP_Query( $args );

        if ( $projects->have_posts() ) : ?>
            <div class="projects">
                <?php
                while ( $projects->have_posts() ) : $projects->the_post();
                    get_template_part( 'template-parts/project' );
                endwhile; ?>
            </div>
            <?php
            wp_reset_postdata();
        endif; ?>
    </main><!-- #main -->
</div><!-- #primary -->

<?php
get_footer();
```

**template-parts/project.php**
```php
<?php
/**
 * Template part for displaying project content.
 *
 * @package Architectural_Portfolio
 */

?>

<article id="post-<?php the_ID(); ?>" <?php post_class( 'project' ); ?>>
    <?php
    if ( has_post_thumbnail() ) : ?>
        <img src="<?php echo get_the_post_thumbnail_url(); ?>" alt="<?php the_title(); ?>">
    <?php endif; ?>
    <h2><?php the_title(); ?></h2>
    <div class="project-meta">
        <?php
        $project_meta = get_post_meta( get_the_ID(), '_project_meta', true );
        if ( $project_meta ) : ?>
            <p>Location: <?php echo $project_meta['location']; ?></p>
            <p>Year: <?php echo $project_meta['year']; ?></p>
        <?php endif; ?>
    </div>
</article>
```

**class-portfolio-post-type.php**
```php
<?php
/**
 * Class Portfolio_Post_Type
 *
 * @package Architectural_Portfolio
 */
class Portfolio_Post_Type {
    public function __construct() {
        add_action( 'init', array( $this, 'register_post_type' ) );
    }

    public function register_post_type() {
        register_post_type( 'project',
            array(
                'labels' => array(
                    'name' => __( 'Projects', 'architectural-portfolio' ),
                    'singular_name' => __( 'Project', 'architectural-portfolio' ),
                ),
                'public' => true,
                'has_archive' => true,
                'supports' => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
            )
        );
    }
}
new Portfolio_Post_Type();
```

**class-project-meta-boxes.php**
```php
<?php
/**
 * Class Project_Meta_Boxes
 *
 * @package Architectural_Portfolio
 */
class Project_Meta_Boxes {
    public function __construct() {
        add_action( 'add_meta_boxes', array( $this, 'add_meta_boxes' ) );
        add_action( 'save_post', array( $this, 'save_meta_boxes' ) );
    }

    public function add_meta_boxes() {
        add_meta_box(
            'project_meta',
            __( 'Project Meta', 'architectural-portfolio' ),
            array( $this, 'render_meta_box' ),
            'project',
            'advanced',
            'high'
        );
    }

    public function render_meta_box( $post ) {
        $project_meta = get_post_meta( $post->ID, '_project_meta', true );
        ?>
        <p>
            <label for="project-location">Location:</label>
            <input type="text" id="project-location" name="project-location" value="<?php echo $project_meta['location']; ?>">
        </p>
        <p>
            <label for="project-year">Year:</label>
            <input type="text" id="project-year" name="project-year" value="<?php echo $project_meta['year']; ?>">
        </p>
        <?php
    }

    public function save_meta_boxes( $post_id ) {
        if ( ! isset( $_POST['project-location'] ) || ! isset( $_POST['project-year'] ) ) {
            return;
        }

        $project_meta = array(
            'location' => sanitize_text_field( $_POST['project-location'] ),
            'year' => sanitize_text_field( $_POST['project-year'] ),
        );

        update_post_meta( $post_id, '_project_meta', $project_meta );
    }
}
new Project_Meta_Boxes();
```

**README.md**
```markdown
# Architectural Portfolio

A WordPress theme for showcasing architectural projects.

## Installation

1. Upload the theme folder to the `wp-content/themes` directory of your WordPress installation.
2. Activate the theme through the WordPress admin interface.

## Features

* Custom post type for projects
* Project meta boxes for location and year
* Portfolio page template
* Responsive design
```
