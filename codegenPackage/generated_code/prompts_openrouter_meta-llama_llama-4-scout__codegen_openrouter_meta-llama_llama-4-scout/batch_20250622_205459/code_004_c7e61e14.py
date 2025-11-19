"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Design a web page using WordPress that showcases a collection of mosaic artworks, with features like zooming and interactive elements, inspired by the metaMasks.art website.
Generated: DETERMINISTIC_c7e61e14b1e46e0c
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Mosaic Artworks Showcase**
==========================

**HTML (index.php)**
```php
<?php
/**
 * Template Name: Mosaic Artworks Showcase
 *
 * @package WordPress
 */

get_header(); ?>

<div class="mosaic-container">
  <h1 class="mosaic-title">Mosaic Artworks Showcase</h1>
  <div class="mosaic-gallery">
    <?php
    /**
     * Query mosaic artworks from database
     */
    $args = array(
      'post_type' => 'mosaic_art',
      'posts_per_page' => -1,
    );
    $mosaic_arts = new WP_Query($args);

    if ($mosaic_arts->have_posts()) :
      while ($mosaic_arts->have_posts()) : $mosaic_arts->the_post();
        $image_url = get_the_post_thumbnail_url();
        $artist_name = get_post_meta(get_the_ID(), 'artist_name', true);
        $art_title = get_the_title();
        ?>
        <div class="mosaic-art">
          <a href="<?php echo $image_url; ?>" data-lightbox="mosaic-gallery">
            <img src="<?php echo $image_url; ?>" alt="<?php echo $art_title; ?>">
          </a>
          <div class="mosaic-art-info">
            <h2><?php echo $art_title; ?></h2>
            <p>By <?php echo $artist_name; ?></p>
          </div>
        </div>
      <?php endwhile; wp_reset_postdata(); endif; ?>
  </div>
</div>

<?php get_footer(); ?>
```

**CSS (style.css)**
```css
.mosaic-container {
  max-width: 1200px;
  margin: 40px auto;
  text-align: center;
}

.mosaic-title {
  font-size: 36px;
  margin-bottom: 20px;
}

.mosaic-gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.mosaic-art {
  margin: 20px;
  width: calc(33.33% - 40px);
}

.mosaic-art img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px;
  cursor: pointer;
}

.mosaic-art-info {
  background-color: #f9f9f9;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.mosaic-art-info h2 {
  font-size: 18px;
  margin-bottom: 10px;
}

.lightbox {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: none;
}

.lightbox img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 80%;
  max-height: 80%;
}

.lightbox-close {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 24px;
  color: #fff;
  cursor: pointer;
}
```

**JavaScript (script.js)**
```javascript
// Zooming and interactive elements
const mosaicArts = document.querySelectorAll('.mosaic-art img');

mosaicArts.forEach((art) => {
  art.addEventListener('click', () => {
    const lightbox = document.createElement('div');
    lightbox.classList.add('lightbox');
    const lightboxImg = document.createElement('img');
    lightboxImg.src = art.src;
    lightbox.appendChild(lightboxImg);
    const lightboxClose = document.createElement('span');
    lightboxClose.classList.add('lightbox-close');
    lightboxClose.textContent = '×';
    lightbox.appendChild(lightboxClose);
    document.body.appendChild(lightbox);

    lightboxClose.addEventListener('click', () => {
      lightbox.remove();
    });

    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) {
        lightbox.remove();
      }
    });
  });
});
```

**PHP (functions.php)**
```php
<?php
/**
 * Register mosaic art post type
 */
function register_mosaic_art_post_type() {
  register_post_type('mosaic_art',
    array(
      'labels' => array(
        'name' => __( 'Mosaic Arts' ),
        'singular_name' => __( 'Mosaic Art' ),
      ),
      'public' => true,
      'has_archive' => true,
      'supports' => array('title', 'thumbnail', 'custom-fields'),
    )
  );
}
add_action('init', 'register_mosaic_art_post_type');

/**
 * Add custom meta field for artist name
 */
function add_artist_name_meta_field() {
  add_meta_box(
    'artist_name',
    'Artist Name',
    'artist_name_meta_field_callback',
    'mosaic_art',
    'advanced',
    'high'
  );
}
add_action('add_meta_boxes', 'add_artist_name_meta_field');

function artist_name_meta_field_callback() {
  $artist_name = get_post_meta(get_the_ID(), 'artist_name', true);
  ?>
  <input type="text" name="artist_name" value="<?php echo $artist_name; ?>">
  <?php
}

/**
 * Save artist name meta field
 */
function save_artist_name_meta_field($post_id) {
  if (isset($_POST['artist_name'])) {
    update_post_meta($post_id, 'artist_name', sanitize_text_field($_POST['artist_name']));
  }
}
add_action('save_post', 'save_artist_name_meta_field');
```

**enqueue scripts and styles**
```php
function enqueue_mosaic_scripts() {
  wp_enqueue_style('mosaic-style', get_stylesheet_directory_uri() . '/style.css');
  wp_enqueue_script('mosaic-script', get_stylesheet_directory_uri() . '/script.js', array('jquery'), '1.0', true);
}
add_action('wp_enqueue_scripts', 'enqueue_mosaic_scripts');
```
