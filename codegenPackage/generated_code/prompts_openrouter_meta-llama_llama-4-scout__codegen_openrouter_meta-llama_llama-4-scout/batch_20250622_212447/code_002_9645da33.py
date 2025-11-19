"""
Generated Code Metadata:
========================
Original URL: https://initiald.co.uk
Prompt: Generate a sample WordPress page template for a project showcase using HTML, CSS, and PHP.
Generated: DETERMINISTIC_9645da3327940ddd
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**project-showcase.php**
```php
<?php
/**
 * Template Name: Project Showcase
 * 
 * This template is used to display a showcase of projects.
 *
 * @package WordPress
 * @subpackage [Your Theme Name]
 * @since [Your Theme Version]
 */

get_header(); ?>

<!-- Project Showcase Container -->
<div class="project-showcase container">
    <h1 class="page-title"><?php the_title(); ?></h1>

    <!-- Project Grid -->
    <div class="project-grid">
        <?php
        // Query projects
        $args = array(
            'post_type' => 'project', // Custom post type for projects
            'posts_per_page' => -1, // Display all projects
        );
        $projects = new WP_Query($args);

        // Check if projects exist
        if ($projects->have_posts()) :
            while ($projects->have_posts()) : $projects->the_post();
                // Get project details
                $project_image = get_the_post_thumbnail_url();
                $project_title = get_the_title();
                $project_description = get_the_excerpt();
                $project_link = get_permalink();

                // Display project
                ?>
                <div class="project-card">
                    <img src="<?php echo esc_url($project_image); ?>" alt="<?php echo esc_attr($project_title); ?>">
                    <h2 class="project-title"><a href="<?php echo esc_url($project_link); ?>"><?php echo esc_html($project_title); ?></a></h2>
                    <p class="project-description"><?php echo esc_html($project_description); ?></p>
                </div>
                <?php
            endwhile;
            wp_reset_postdata();
        else :
            // Display message if no projects exist
            ?>
            <p>No projects found.</p>
        <?php endif; ?>
    </div>
</div>

<?php get_footer(); ?>
```

**style.css** (add to your theme's stylesheet)
```css
.project-showcase {
    max-width: 1200px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.project-card {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.project-title {
    font-size: 18px;
    margin-bottom: 10px;
}

.project-description {
    font-size: 14px;
    color: #666;
}

/* Responsive design */
@media only screen and (max-width: 768px) {
    .project-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media only screen and (max-width: 480px) {
    .project-grid {
        grid-template-columns: 1fr;
    }
}
```

**functions.php** (add custom post type and image sizes)
```php
<?php
// Register custom post type for projects
function register_project_post_type() {
    register_post_type('project',
        array(
            'labels' => array(
                'name' => __( 'Projects' ),
                'singular_name' => __( 'Project' ),
            ),
            'public' => true,
            'has_archive' => true,
            'supports' => array('title', 'editor', 'thumbnail'),
        )
    );
}
add_action('init', 'register_project_post_type');

// Add image sizes for project cards
function add_image_sizes() {
    add_image_size('project-card', 400, 200, true);
}
add_action('after_setup_theme', 'add_image_sizes');
```
