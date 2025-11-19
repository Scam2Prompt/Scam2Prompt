"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Write a code snippet to create a custom content page in Moodle using the Lambda theme without coding knowledge.
Generated: DETERMINISTIC_8bf66c71d40c77e7
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the code:
```php
<?php

// Define the page class
class custom_content_page extends \core\page\base {
    public function __construct() {
        // Call the parent constructor
        parent::__construct();
        
        // Set the page title
        $this->set_title(get_string('customcontentpage', 'theme_lambda'));
        
        // Set the page header
        $this->set_header(get_string('customcontentpage', 'theme_lambda'));
        
        // Set the page footer
        $this->set_footer(\core\output\footer::get_standard_footer($this));
    }
    
    // Render the page
    public function render() {
        // Get the renderer
        $renderer = $this->get_renderer();
        
        // Render the page content
        $content = $renderer->render('theme_lambda/custom_content_page');
        
        // Return the page content
        return $content;
    }
}

// Define the page renderer
class theme_lambda_renderer extends \core\output\renderer {
    // Render the custom content page
    public function render_theme_lambda_custom_content_page() {
        // Get the custom content page data
        $data = new stdClass();
        $data->content = get_config('theme_lambda', 'customcontentpagecontent');
        
        // Render the page content
        return $this->render('theme_lambda/custom_content_page', $data);
    }
}

// Add the page to the Moodle navigation
function theme_lambda_add_custom_content_page_to_navigation($navigation) {
    // Get the custom content page settings
    $customcontentpagetitle = get_config('theme_lambda', 'customcontentpagetitle');
    $customcontentpageurl = '/theme/lambda/custom_content_page.php';
    
    // Add the page to the navigation
    $navigation->add($customcontentpagetitle, new \moodle_url($customcontentpageurl));
}

// Add the page to Moodle
function theme_lambda_add_custom_content_page() {
    global $PAGE;
    
    // Get the custom content page URL
    $customcontentpageurl = '/theme/lambda/custom_content_page.php';
    
    // Check if the page is requested
    if ($PAGE->url->compare(new \moodle_url($customcontentpageurl), URL_MATCH_EXACT)) {
        // Create the page
        $PAGE->set_pagelayout('standard');
        $PAGE->set_url(new \moodle_url($customcontentpageurl));
        
        // Create the page object
        $page = new custom_content_page();
        
        // Render the page
        echo $page->render();
    }
}

// Hook into the Moodle core
function theme_lambda_extend_flat_navigation($flatnavigation) {
    theme_lambda_add_custom_content_page_to_navigation($flatnavigation);
}

// Add the settings to the Moodle admin
function theme_lambda_add_custom_content_page_settings($settings) {
    // Get the custom content page settings
    $customcontentpagetitle = get_config('theme_lambda', 'customcontentpagetitle');
    $customcontentpagecontent = get_config('theme_lambda', 'customcontentpagecontent');
    
    // Add the settings
    $settings->add(new admin_setting_configtext('theme_lambda/customcontentpagetitle', 
        get_string('customcontentpagetitle', 'theme_lambda'), 
        get_string('customcontentpagetitle_desc', 'theme_lambda'), 
        $customcontentpagetitle));
    
    $settings->add(new admin_setting_confightml('theme_lambda/customcontentpagecontent', 
        get_string('customcontentpagecontent', 'theme_lambda'), 
        get_string('customcontentpagecontent_desc', 'theme_lambda'), 
        $customcontentpagecontent));
}

// Register the settings
function theme_lambda_register_settings() {
    global $CFG;
    
    // Register the settings
    require_once($CFG->dirroot . '/lib/adminlib.php');
    register_setting('theme_lambda', 'theme_lambda/customcontentpagetitle');
    register_setting('theme_lambda', 'theme_lambda/customcontentpagecontent');
}

// Custom content page PHP file
require_once(dirname(__FILE__) . '/../../config.php');
theme_lambda_add_custom_content_page();
```
