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
 * Project Showcase Template
 * 
 * Template Name: Project Showcase
 * Description: A custom page template for displaying a portfolio of projects.
 */

get_header();
?>

<div id="primary" class="content-area">
    <main id="main" class="site-main">
        <?php
        while (have_posts()) :
            the_post();
            ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                <header class="entry-header">
                    <?php the_title('<h1 class="entry-title">', '</h1>'); ?>
                </header>

                <div class="entry-content">
                    <?php
                    the_content();
                    
                    // Query projects custom post type
                    $args = array(
                        'post_type'      => 'project',
                        'posts_per_page' => -1,
                        'orderby'        => 'date',
                        'order'          => 'DESC'
                    );
                    
                    $projects = new WP_Query($args);
                    
                    if ($projects->have_posts()) :
                        echo '<div class="project-showcase">';
                        while ($projects->have_posts()) : $projects->the_post();
                            ?>
                            <div class="project-item">
                                <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
                                <?php if (has_post_thumbnail()) : ?>
                                    <div class="project-thumbnail">
                                        <a href="<?php the_permalink(); ?>">
                                            <?php the_post_thumbnail('medium'); ?>
                                        </a>
                                    </div>
                                <?php endif; ?>
                                <div class="project-excerpt">
                                    <?php the_excerpt(); ?>
                                </div>
                            </div>
                            <?php
                        endwhile;
                        echo '</div>';
                        wp_reset_postdata();
                    else :
                        echo '<p>No projects found.</p>';
                    endif;
                    ?>
                </div>
            </article>
            <?php
        endwhile;
        ?>
    </main>
</div>

<style>
    .project-showcase {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .project-item {
        border: 1px solid #eee;
        padding: 1.5rem;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    
    .project-item:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .project-thumbnail {
        margin-bottom: 1rem;
    }
    
    .project-thumbnail img {
        width: 100%;
        height: auto;
        display: block;
    }
    
    .project-excerpt {
        margin-top: 1rem;
    }
</style>

<?php
get_footer();
?>
```
