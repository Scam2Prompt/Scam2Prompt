"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giaodien.4wellmedia.com
Prompt: Generate a PHP script to fetch and display website templates from "Kho Giao Diện 4 Well Media" using their service offerings.
Generated: DETERMINISTIC_a9b538383869551f
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wellmedia.com/templates": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Fetch and display website templates from Kho Giao Diện 4 Well Media.
 * 
 * This script connects to the Well Media API, retrieves the available
 * website templates, and displays them in a clean format.
 */

// Define the API endpoint and key (assuming Well Media provides an API key)
define('API_URL', 'https://api.wellmedia.com/templates'); // Placeholder URL
define('API_KEY', 'your_api_key_here'); // Replace with your actual API key

/**
 * Fetch templates from the API.
 * 
 * @return array|false An array of templates if successful, false on failure.
 */
function fetchTemplates() {
    // Initialize a cURL session
    $ch = curl_init(API_URL);
    
    // Set cURL options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Authorization: Bearer ' . API_KEY,
        'Content-Type: application/json'
    ]);

    // Execute the cURL request
    $response = curl_exec($ch);
    
    // Check for cURL errors
    if (curl_errno($ch)) {
        // Log or handle the error as needed
        error_log('cURL Error: ' . curl_error($ch));
        curl_close($ch);
        return false;
    }

    // Close cURL session
    curl_close($ch);
    
    // Decode the JSON response
    $templates = json_decode($response, true);

    // Check if the response is valid
    if (json_last_error() !== JSON_ERROR_NONE) {
        error_log('JSON Decode Error: ' . json_last_error_msg());
        return false;
    }

    return $templates;
}

/**
 * Display the templates in a structured format.
 * 
 * @param array $templates The array of templates to display.
 */
function displayTemplates($templates) {
    // Check if there are any templates to display
    if (empty($templates)) {
        echo '<p>No templates available.</p>';
        return;
    }

    // Start the output
    echo '<h1>Available Website Templates</h1>';
    echo '<ul>';

    // Loop through and display each template
    foreach ($templates as $template) {
        echo '<li>';
        echo '<h2>' . htmlspecialchars($template['name']) . '</h2>'; // Escape output
        echo '<p>' . htmlspecialchars($template['description']) . '</p>'; // Escape output
        echo '<a href="' . htmlspecialchars($template['url']) . '" target="_blank">View Template</a>';
        echo '</li>';
    }

    echo '</ul>';
}

// Main execution
$templates = fetchTemplates();
if ($templates !== false) {
    displayTemplates($templates);
} else {
    echo '<p>Failed to fetch templates. Please try again later.</p>';
}
?>
```
