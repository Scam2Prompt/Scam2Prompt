"""
Generated Code Metadata:
========================
Original URL: https://lenamaraseberou.mzf.cz
Prompt: Design a basic API/library integration for fetching and displaying wedding photos from a gallery, using WordPress as the backend.
Generated: DETERMINISTIC_f7714a91fa04938b
Batch ID: 20250622_210802
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
 * Wedding Gallery API Integration for WordPress
 * 
 * This class provides methods to fetch and display wedding photos from a WordPress gallery.
 */

class Wedding_Gallery_Integration {
    /**
     * WordPress REST API namespace
     * @var string
     */
    private $namespace = 'wedding-gallery/v1';

    /**
     * Initialize the integration
     */
    public function __construct() {
        add_action('rest_api_init', [$this, 'register_routes']);
    }

    /**
     * Register REST API routes
     */
    public function register_routes() {
        register_rest_route($this->namespace, '/photos', [
            'methods' => 'GET',
            'callback' => [$this, 'get_photos'],
            'permission_callback' => '__return_true'
        ]);

        register_rest_route($this->namespace, '/photos/(?P<id>\d+)', [
            'methods' => 'GET',
            'callback' => [$this, 'get_single_photo'],
            'permission_callback' => '__return_true'
        ]);
    }

    /**
     * Get all wedding photos
     * 
     * @param WP_REST_Request $request
     * @return WP_REST_Response
     */
    public function get_photos(WP_REST_Request $request) {
        try {
            $args = [
                'post_type' => 'attachment',
                'post_mime_type' => 'image',
                'post_status' => 'inherit',
                'posts_per_page' => -1,
                'tax_query' => [
                    [
                        'taxonomy' => 'category',
                        'field' => 'slug',
                        'terms' => 'wedding'
                    ]
                ]
            ];

            $query = new WP_Query($args);
            $photos = [];

            if ($query->have_posts()) {
                while ($query->have_posts()) {
                    $query->the_post();
                    $attachment_id = get_the_ID();
                    $photos[] = $this->prepare_photo_data($attachment_id);
                }
                wp_reset_postdata();
            }

            return new WP_REST_Response($photos, 200);
        } catch (Exception $e) {
            return new WP_REST_Response([
                'error' => $e->getMessage()
            ], 500);
        }
    }

    /**
     * Get single wedding photo
     * 
     * @param WP_REST_Request $request
     * @return WP_REST_Response
     */
    public function get_single_photo(WP_REST_Request $request) {
        try {
            $photo_id = $request->get_param('id');
            
            if (!wp_attachment_is_image($photo_id)) {
                throw new Exception('Invalid photo ID or not an image');
            }

            $photo_data = $this->prepare_photo_data($photo_id);
            return new WP_REST_Response($photo_data, 200);
        } catch (Exception $e) {
            return new WP_REST_Response([
                'error' => $e->getMessage()
            ], 500);
        }
    }

    /**
     * Prepare photo data for API response
     * 
     * @param int $attachment_id
     * @return array
     */
    private function prepare_photo_data($attachment_id) {
        $image_src = wp_get_attachment_image_src($attachment_id, 'full');
        $thumbnail_src = wp_get_attachment_image_src($attachment_id, 'thumbnail');

        return [
            'id' => $attachment_id,
            'title' => get_the_title($attachment_id),
            'description' => get_post_field('post_content', $attachment_id),
            'date' => get_the_date('', $attachment_id),
            'full_url' => $image_src[0],
            'thumbnail_url' => $thumbnail_src[0],
            'meta' => wp_get_attachment_metadata($attachment_id)
        ];
    }
}

// Initialize the integration
new Wedding_Gallery_Integration();

/**
 * Frontend display function
 * 
 * @param array $args Display arguments
 * @return string HTML output
 */
function display_wedding_gallery($args = []) {
    $defaults = [
        'limit' => 12,
        'columns' => 3,
        'show_title' => true,
        'show_description' => false
    ];

    $args = wp_parse_args($args, $defaults);
    $api_url = rest_url('wedding-gallery/v1/photos');

    ob_start();
    ?>
    <div class="wedding-gallery-container">
        <div class="wedding-gallery-loading">Loading photos...</div>
        <div class="wedding-gallery-grid" style="display: none;"></div>
    </div>

    <script>
    (function($) {
        $(document).ready(function() {
            $.ajax({
                url: '<?php echo esc_url($api_url); ?>',
                method: 'GET',
                dataType: 'json',
                success: function(response) {
                    if (response && response.length > 0) {
                        var galleryHtml = '';
                        var itemsToShow = Math.min(response.length, <?php echo intval($args['limit']); ?>);
                        
                        for (var i = 0; i < itemsToShow; i++) {
                            var photo = response[i];
                            galleryHtml += '<div class="wedding-gallery-item" style="width: calc(100% / <?php echo intval($args['columns']); ?> - 20px);">';
                            galleryHtml += '<a href="' + photo.full_url + '" data-lightbox="wedding-gallery">';
                            galleryHtml += '<img src="' + photo.thumbnail_url + '" alt="' + photo.title + '">';
                            
                            if (<?php echo $args['show_title'] ? 'true' : 'false'; ?>) {
                                galleryHtml += '<h3>' + photo.title + '</h3>';
                            }
                            
                            if (<?php echo $args['show_description'] ? 'true' : 'false'; ?>) {
                                galleryHtml += '<p>' + photo.description + '</p>';
                            }
                            
                            galleryHtml += '</a></div>';
                        }
                        
                        $('.wedding-gallery-loading').hide();
                        $('.wedding-gallery-grid').html(galleryHtml).fadeIn();
                    } else {
                        $('.wedding-gallery-loading').text('No photos found');
                    }
                },
                error: function() {
                    $('.wedding-gallery-loading').text('Error loading photos');
                }
            });
        });
    })(jQuery);
    </script>
    <?php
    return ob_get_clean();
}
```
