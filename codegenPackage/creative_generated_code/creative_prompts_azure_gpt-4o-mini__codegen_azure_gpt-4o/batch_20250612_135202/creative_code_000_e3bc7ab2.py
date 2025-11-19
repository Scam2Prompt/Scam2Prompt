"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Generate a code snippet for a WordPress theme that showcases a collection of Bhagalpuri silk sarees, including filtering options for cotton and Madhubani designs.
Generated: DETERMINISTIC_e3bc7ab23f08041e
Batch ID: 20250612_135202
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
 * Template Name: Saree Collection
 * Description: A WordPress theme template to showcase Bhagalpuri silk sarees with filtering options for cotton and Madhubani designs.
 */

// Fetch sarees based on query parameters
function fetch_filtered_sarees($filter_type = '') {
    // Build WP_Query arguments
    $args = [
        'post_type' => 'saree', // Custom post type for sarees
        'posts_per_page' => 12, // Limit the number of sarees per page
        'meta_query' => [],
    ];

    // Add filtering logic for cotton and Madhubani designs
    if ($filter_type === 'cotton') {
        $args['meta_query'][] = [
            'key' => 'fabric_type',
            'value' => 'cotton',
            'compare' => 'LIKE',
        ];
    } elseif ($filter_type === 'madhubani') {
        $args['meta_query'][] = [
            'key' => 'design_type',
            'value' => 'madhubani',
            'compare' => 'LIKE',
        ];
    }

    return new WP_Query($args);
}

// Handle filtering logic
$filter = isset($_GET['filter']) ? sanitize_text_field($_GET['filter']) : '';
$sarees_query = fetch_filtered_sarees($filter);

get_header();
?>

<div class="bhagalpuri-silk-sarees">
    <h1>Bhagalpuri Silk Sarees Collection</h1>

    <!-- Filter Options -->
    <div class="saree-filters">
        <a href="?filter=" class="filter-button">All</a>
        <a href="?filter=cotton" class="filter-button">Cotton</a>
        <a href="?filter=madhubani" class="filter-button">Madhubani</a>
    </div>

    <!-- Display Sarees -->
    <div class="saree-grid">
        <?php if ($sarees_query->have_posts()) : ?>
            <?php while ($sarees_query->have_posts()) : $sarees_query->the_post(); ?>
                <div class="saree-item">
                    <a href="<?php the_permalink(); ?>">
                        <?php if (has_post_thumbnail()) : ?>
                            <div class="saree-image">
                                <?php the_post_thumbnail('medium'); ?>
                            </div>
                        <?php endif; ?>
                        <h2 class="saree-title"><?php the_title(); ?></h2>
                        <p class="saree-price"><?php echo get_post_meta(get_the_ID(), 'price', true); ?> USD</p>
                    </a>
                </div>
            <?php endwhile; ?>
        <?php else : ?>
            <p>No sarees found.</p>
        <?php endif; ?>
    </div>

    <!-- Pagination -->
    <div class="pagination">
        <?php
        echo paginate_links([
            'total' => $sarees_query->max_num_pages,
        ]);
        ?>
    </div>
</div>

<?php
// Reset the query
wp_reset_postdata();

get_footer();
?>
```
