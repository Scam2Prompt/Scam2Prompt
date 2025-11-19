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

```php
<?php
/**
 * Template Name: Project Showcase
 * Description: A custom page template for showcasing projects.
 * 
 * @package YourThemeName
 */

get_header(); // Include the header.php file
?>

<!-- Main Content Section -->
<div class="project-showcase-container">
    <div class="container">
        <h1 class="page-title"><?php the_title(); ?></h1>
        
        <?php
        // Start the WordPress Loop
        if (have_posts()) :
            while (have_posts()) : the_post();
        ?>
            <div class="page-content">
                <?php the_content(); // Display the page content ?>
            </div>
        <?php
            endwhile;
        else :
        ?>
            <p>No content found for this page.</p>
        <?php endif; ?>
        
        <!-- Custom Query for Projects -->
        <?php
        $args = array(
            'post_type' => 'project', // Custom post type for projects
            'posts_per_page' => 10,  // Number of projects to display
            'orderby' => 'date',    // Order by date
            'order' => 'DESC'       // Descending order
        );

        $projects_query = new WP_Query($args);

        if ($projects_query->have_posts()) :
        ?>
            <div class="projects-grid">
                <?php
                while ($projects_query->have_posts()) : $projects_query->the_post();
                ?>
                    <div class="project-item">
                        <a href="<?php the_permalink(); ?>" class="project-link">
                            <?php if (has_post_thumbnail()) : ?>
                                <div class="project-thumbnail">
                                    <?php the_post_thumbnail('medium'); // Display project thumbnail ?>
                                </div>
                            <?php endif; ?>
                            <h2 class="project-title"><?php the_title(); ?></h2>
                        </a>
                        <p class="project-excerpt"><?php echo wp_trim_words(get_the_excerpt(), 20, '...'); ?></p>
                    </div>
                <?php
                endwhile;
                ?>
            </div>
        <?php
        else :
        ?>
            <p>No projects found.</p>
        <?php
        endif;

        // Reset Post Data
        wp_reset_postdata();
        ?>
    </div>
</div>

<?php get_footer(); // Include the footer.php file ?>

<!-- CSS for the Project Showcase -->
<style>
    .project-showcase-container {
        padding: 50px 0;
        background-color: #f9f9f9;
    }

    .page-title {
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 30px;
    }

    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
    }

    .project-item {
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .project-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    .project-thumbnail img {
        width: 100%;
        height: auto;
        display: block;
    }

    .project-title {
        font-size: 1.5rem;
        margin: 15px;
        color: #333;
    }

    .project-excerpt {
        font-size: 1rem;
        margin: 0 15px 15px;
        color: #666;
    }

    .project-link {
        text-decoration: none;
    }
</style>
```
