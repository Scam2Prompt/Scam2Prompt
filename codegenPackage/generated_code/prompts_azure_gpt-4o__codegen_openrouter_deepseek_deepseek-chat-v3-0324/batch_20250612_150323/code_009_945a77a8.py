"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Generate a code snippet for adding multilingual support to a WordPress website, inspired by Metamark's bilingual site design (Lithuanian and English).
Generated: DETERMINISTIC_945a77a8cf239658
Batch ID: 20250612_150323
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
 * Adds multilingual support to a WordPress website (English and Lithuanian).
 * Inspired by Metamark's bilingual site design.
 */

// Register language translations
add_action('after_setup_theme', 'register_multilingual_support');
function register_multilingual_support() {
    load_theme_textdomain('my-theme', get_template_directory() . '/languages');
    
    // Define available languages
    $languages = array(
        'en' => 'English',
        'lt' => 'Lietuvių'
    );
    
    // Store languages in a global variable for easy access
    global $available_languages;
    $available_languages = $languages;
}

// Add language switcher to the site
add_filter('wp_nav_menu_items', 'add_language_switcher', 10, 2);
function add_language_switcher($items, $args) {
    global $available_languages;
    
    if ($args->theme_location == 'primary') {
        $current_lang = get_locale();
        $current_lang = substr($current_lang, 0, 2);
        
        $switcher = '<li class="menu-item menu-item-language-switcher menu-item-has-children">';
        $switcher .= '<a href="#">' . $available_languages[$current_lang] . '</a>';
        $switcher .= '<ul class="sub-menu">';
        
        foreach ($available_languages as $code => $name) {
            if ($code != $current_lang) {
                $switcher .= '<li class="menu-item">';
                $switcher .= '<a href="' . esc_url(add_query_arg('lang', $code)) . '">' . $name . '</a>';
                $switcher .= '</li>';
            }
        }
        
        $switcher .= '</ul></li>';
        
        $items .= $switcher;
    }
    
    return $items;
}

// Handle language switching via URL parameter
add_action('init', 'handle_language_switching');
function handle_language_switching() {
    if (isset($_GET['lang'])) {
        $lang = sanitize_text_field($_GET['lang']);
        global $available_languages;
        
        if (array_key_exists($lang, $available_languages)) {
            // Set cookie for persistent language selection
            setcookie('user_lang', $lang, time() + (86400 * 30), '/');
            
            // Redirect to same URL without language parameter
            $current_url = remove_query_arg('lang');
            wp_redirect($current_url);
            exit;
        }
    }
}

// Set the locale based on user preference
add_filter('locale', 'set_user_locale');
function set_user_locale($locale) {
    if (isset($_COOKIE['user_lang'])) {
        $user_lang = sanitize_text_field($_COOKIE['user_lang']);
        return $user_lang . '_' . strtoupper($user_lang);
    }
    return $locale;
}

// Helper function to output translated strings in templates
function _t($string, $domain = 'my-theme') {
    return esc_html__( $string, $domain );
}
```
