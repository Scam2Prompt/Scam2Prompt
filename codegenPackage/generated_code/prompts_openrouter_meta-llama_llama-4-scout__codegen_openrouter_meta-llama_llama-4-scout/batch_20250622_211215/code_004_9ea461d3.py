"""
Generated Code Metadata:
========================
Original URL: https://icopages.pw
Prompt: What are some best practices for designing a system that auto-generates website pages, like icopages.pw, and provide code snippets in PHP for implementing such a feature.
Generated: DETERMINISTIC_9ea461d36b676fd9
Batch ID: 20250622_211215
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
 * Website Page Generator
 * 
 * This system auto-generates website pages based on a template and user input.
 */

// Configuration
$config = [
    'template_dir' => 'templates',
    'output_dir' => 'output',
    'allowed_tags' => ['h1', 'h2', 'p', 'img', 'a'],
];

// Function to generate a website page
function generate_page($template_name, $data) {
    global $config;

    // Load template
    $template_path = $config['template_dir'] . '/' . $template_name . '.php';
    if (!file_exists($template_path)) {
        throw new Exception("Template not found: $template_path");
    }
    $template = file_get_contents($template_path);

    // Validate user input data
    $sanitized_data = [];
    foreach ($data as $key => $value) {
        $sanitized_data[$key] = htmlspecialchars($value);
    }

    // Render template with user data
    try {
        $output = render_template($template, $sanitized_data, $config['allowed_tags']);
    } catch (Exception $e) {
        throw new Exception("Error rendering template: " . $e->getMessage());
    }

    // Save generated page to output directory
    $output_path = $config['output_dir'] . '/' . $template_name . '.html';
    if (!is_dir($config['output_dir'])) {
        mkdir($config['output_dir'], 0777, true);
    }
    file_put_contents($output_path, $output);

    return $output_path;
}

// Function to render a template with user data
function render_template($template, $data, $allowed_tags) {
    // Use a simple template engine for demonstration purposes
    foreach ($data as $key => $value) {
        $template = str_replace('{{' . $key . '}}', $value, $template);
    }

    // Sanitize output to prevent XSS
    $dom = new DOMDocument();
    $dom->loadHTML($template);
    $tags = $dom->getElementsByTagName('*');
    foreach ($tags as $tag) {
        if (!in_array($tag->nodeName, $allowed_tags)) {
            $tag->parentNode->removeChild($tag);
        }
    }
    $template = $dom->saveHTML();

    return $template;
}

// Example usage
$data = [
    'title' => 'My Page',
    'content' => '<h1>Welcome to my page!</h1><p>This is a test page.</p>',
];

try {
    $output_path = generate_page('example', $data);
    echo "Page generated: $output_path\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
