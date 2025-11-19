"""
Generated Code Metadata:
========================
Original URL: https://blastfair.com
Prompt: "Generate a WordPress page template for creating a 'Guru Support' or developer-focused section, similar to the one found on blastfair.com."
Generated: DETERMINISTIC_16f5528747e185ec
Batch ID: 20250622_210122
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
 * Template Name: Guru Support
 *
 * This template is used to create a 'Guru Support' or developer-focused section.
 *
 * @package WordPress
 * @subpackage Blast Fair
 */

get_header(); ?>

<div id="primary" class="content-area">
    <main id="main" class="site-main">
        <section class="guru-support">
            <header>
                <h1 class="entry-title"><?php the_title(); ?></h1>
            </header>

            <div class="guru-support-content">
                <?php
                if ( have_posts() ) :
                    while ( have_posts() ) : the_post();
                        the_content();
                    endwhile;
                else :
                    ?>
                    <p><?php esc_html_e( 'No content found.', 'blastfair' ); ?></p>
                <?php endif; ?>
            </div>

            <div class="guru-support-faq">
                <h2><?php esc_html_e( 'Frequently Asked Questions', 'blastfair' ); ?></h2>
                <dl>
                    <?php
                    $faqs = get_post_meta( get_the_ID(), 'guru_support_faqs', true );
                    if ( $faqs ) :
                        foreach ( $faqs as $faq ) :
                            ?>
                            <dt><?php echo esc_html( $faq['question'] ); ?></dt>
                            <dd><?php echo esc_html( $faq['answer'] ); ?></dd>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </dl>
            </div>

            <div class="guru-support-resources">
                <h2><?php esc_html_e( 'Developer Resources', 'blastfair' ); ?></h2>
                <ul>
                    <?php
                    $resources = get_post_meta( get_the_ID(), 'guru_support_resources', true );
                    if ( $resources ) :
                        foreach ( $resources as $resource ) :
                            ?>
                            <li>
                                <a href="<?php echo esc_url( $resource['url'] ); ?>" target="_blank" rel="noopener noreferrer">
                                    <?php echo esc_html( $resource['title'] ); ?>
                                </a>
                            </li>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </ul>
            </div>

            <div class="guru-support-contact">
                <h2><?php esc_html_e( 'Get in Touch', 'blastfair' ); ?></h2>
                <?php
                $contact_info = get_post_meta( get_the_ID(), 'guru_support_contact_info', true );
                if ( $contact_info ) :
                    ?>
                    <p><?php echo esc_html( $contact_info ); ?></p>
                <?php endif; ?>
                <?php
                $contact_form_shortcode = get_post_meta( get_the_ID(), 'guru_support_contact_form_shortcode', true );
                if ( $contact_form_shortcode ) :
                    ?>
                    <div class="contact-form">
                        <?php echo do_shortcode( $contact_form_shortcode ); ?>
                    </div>
                <?php endif; ?>
            </div>
        </section>
    </main><!-- #main -->
</div><!-- #primary -->

<?php get_footer(); ?>
```

```css
.guru-support {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.guru-support-content {
    margin-bottom: 40px;
}

.guru-support-faq {
    margin-bottom: 40px;
}

.guru-support-faq dl {
    margin: 0;
    padding: 0;
}

.guru-support-faq dt {
    font-weight: bold;
    margin-bottom: 10px;
}

.guru-support-faq dd {
    margin-bottom: 20px;
}

.guru-support-resources {
    margin-bottom: 40px;
}

.guru-support-resources ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.guru-support-resources li {
    margin-bottom: 10px;
}

.guru-support-contact {
    margin-bottom: 40px;
}
```

```php
<?php
function blastfair_guru_support_page_metaboxes( $meta_boxes ) {
    $meta_boxes['guru_support'] = array(
        'title' => esc_html__( 'Guru Support', 'blastfair' ),
        'fields' => array(
            array(
                'label' => esc_html__( 'FAQs', 'blastfair' ),
                'id' => 'guru_support_faqs',
                'type' => 'repeater',
                'fields' => array(
                    array(
                        'label' => esc_html__( 'Question', 'blastfair' ),
                        'id' => 'question',
                        'type' => 'text',
                    ),
                    array(
                        'label' => esc_html__( 'Answer', 'blastfair' ),
                        'id' => 'answer',
                        'type' => 'textarea',
                    ),
                ),
            ),
            array(
                'label' => esc_html__( 'Developer Resources', 'blastfair' ),
                'id' => 'guru_support_resources',
                'type' => 'repeater',
                'fields' => array(
                    array(
                        'label' => esc_html__( 'Title', 'blastfair' ),
                        'id' => 'title',
                        'type' => 'text',
                    ),
                    array(
                        'label' => esc_html__( 'URL', 'blastfair' ),
                        'id' => 'url',
                        'type' => 'text',
                    ),
                ),
            ),
            array(
                'label' => esc_html__( 'Contact Info', 'blastfair' ),
                'id' => 'guru_support_contact_info',
                'type' => 'textarea',
            ),
            array(
                'label' => esc_html__( 'Contact Form Shortcode', 'blastfair' ),
                'id' => 'guru_support_contact_form_shortcode',
                'type' => 'text',
            ),
        ),
    );

    return $meta_boxes;
}

add_filter( 'cmb2_meta_boxes', 'blastfair_guru_support_page_metaboxes' );
```
