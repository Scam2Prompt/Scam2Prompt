"""
Generated Code Metadata:
========================
Original URL: https://s-tel.pl
Prompt: What are some use cases for installing WordPress in multiple languages, and how can I implement language switching using WordPress APIs or libraries?
Generated: DETERMINISTIC_93e4272b5eb81996
Batch ID: 20250622_210650
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
 * WordPress Multilingual Implementation
 * 
 * This code demonstrates language switching functionality in WordPress
 * using WPML (WordPress Multilingual Plugin) and native WordPress functions.
 */

// 1. Basic language switching using WPML (requires WPML plugin)
function custom_language_switcher() {
    if (function_exists('icl_get_languages')) {
        $languages = icl_get_languages('skip_missing=0');
        if (!empty($languages)) {
            echo '<ul class="language-switcher">';
            foreach ($languages as $language) {
                $active = $language['active'] ? ' class="active"' : '';
                echo '<li' . $active . '>';
                echo '<a href="' . $language['url'] . '">';
                echo '<img src="' . $language['country_flag_url'] . '" alt="' . $language['language_code'] . '" />';
                echo $language['native_name'];
                echo '</a>';
                echo '</li>';
            }
            echo '</ul>';
        }
    }
}

// 2. Native WordPress approach (without plugins)
function native_language_switcher() {
    $available_languages = get_available_languages();
    if (!empty($available_languages)) {
        echo '<form action="" method="get" id="language-switcher">';
        echo '<select name="lang" onchange="this.form.submit()">';
        
        // Current language
        $current_lang = get_locale();
        echo '<option value="" selected>' . __('Select Language', 'text-domain') . '</option>';
        
        foreach ($available_languages as $language) {
            $lang_name = format_language_code_to_name($language);
            $selected = ($language === $current_lang) ? ' selected' : '';
            echo '<option value="' . esc_attr($language) . '"' . $selected . '>' . esc_html($lang_name) . '</option>';
        }
        
        echo '</select>';
        echo '</form>';
    }
}

// Helper function to format language code to readable name
function format_language_code_to_name($language_code) {
    $language_names = array(
        'en_US' => 'English',
        'es_ES' => 'Español',
        'fr_FR' => 'Français',
        'de_DE' => 'Deutsch',
        'it_IT' => 'Italiano',
        'pt_PT' => 'Português',
        'ru_RU' => 'Русский',
        'zh_CN' => '中文',
        'ja'    => '日本語',
    );
    
    return isset($language_names[$language_code]) ? $language_names[$language_code] : $language_code;
}

// Handle language switching in native approach
add_action('init', 'handle_language_switching');
function handle_language_switching() {
    if (isset($_GET['lang']) && !empty($_GET['lang'])) {
        $lang = sanitize_text_field($_GET['lang']);
        if (in_array($lang, get_available_languages())) {
            setcookie('user_lang', $lang, time() + YEAR_IN_SECONDS, COOKIEPATH, COOKIE_DOMAIN);
            load_textdomain('default', WP_LANG_DIR . '/' . $lang . '.mo');
        }
    } elseif (isset($_COOKIE['user_lang'])) {
        $lang = sanitize_text_field($_COOKIE['user_lang']);
        if (in_array($lang, get_available_languages())) {
            load_textdomain('default', WP_LANG_DIR . '/' . $lang . '.mo');
        }
    }
}

// 3. Polylang implementation (requires Polylang plugin)
function polylang_language_switcher() {
    if (function_exists('pll_the_languages')) {
        $args = array(
            'show_flags' => 1,
            'show_names' => 1,
            'dropdown'   => 0,
            'echo'       => 1,
        );
        pll_the_languages($args);
    }
}

// 4. Shortcode for language switcher
add_shortcode('language_switcher', 'language_switcher_shortcode');
function language_switcher_shortcode($atts) {
    ob_start();
    custom_language_switcher(); // or any other switcher function
    return ob_get_clean();
}

// 5. Widget for language switcher
class Language_Switcher_Widget extends WP_Widget {
    public function __construct() {
        parent::__construct(
            'language_switcher_widget',
            __('Language Switcher', 'text-domain'),
            array('description' => __('Displays language switcher', 'text-domain'))
        );
    }

    public function widget($args, $instance) {
        echo $args['before_widget'];
        if (!empty($instance['title'])) {
            echo $args['before_title'] . apply_filters('widget_title', $instance['title']) . $args['after_title'];
        }
        custom_language_switcher(); // or any other switcher function
        echo $args['after_widget'];
    }

    public function form($instance) {
        $title = !empty($instance['title']) ? $instance['title'] : __('Languages', 'text-domain');
        ?>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('title')); ?>"><?php esc_attr_e('Title:', 'text-domain'); ?></label>
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

add_action('widgets_init', function() {
    register_widget('Language_Switcher_Widget');
});
```
