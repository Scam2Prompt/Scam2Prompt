"""
Generated Code Metadata:
========================
Original URL: https://fgschool.edu.pk
Prompt: How can I optimize my website performance with LiteSpeed Web Server as referenced on fgschool.edu.pk?
Generated: DETERMINISTIC_22b5d1efeb20728a
Batch ID: 20250612_161616
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
 * LiteSpeed Web Server Optimization Configuration
 * 
 * This script provides optimized configuration settings for LiteSpeed Web Server
 * to improve website performance as referenced on fgschool.edu.pk.
 */

// Enable LiteSpeed Cache
if (!defined('LSCACHE_ON')) {
    define('LSCACHE_ON', 1);
}

// Set cache policies
header('X-LiteSpeed-Cache-Control: public,max-age=86400');
header('X-LiteSpeed-Tag: *');

// Browser caching for static resources
$static_file_extensions = array(
    'jpg', 'jpeg', 'png', 'gif', 'webp',  // Images
    'js', 'css',                          // Scripts and styles
    'woff', 'woff2', 'ttf', 'eot',       // Fonts
    'pdf', 'doc', 'docx', 'ppt', 'pptx'  // Documents
);

$current_extension = pathinfo($_SERVER['REQUEST_URI'], PATHINFO_EXTENSION);
if (in_array($current_extension, $static_file_extensions)) {
    $expires = 60 * 60 * 24 * 30; // 30 days
    header("Cache-Control: public, max-age=$expires");
    header("Expires: " . gmdate('D, d M Y H:i:s', time() + $expires) . ' GMT');
}

// Gzip compression
if (!ini_get('zlib.output_compression')) {
    ini_set('zlib.output_compression', 'On');
}

// Optimize PHP settings for LiteSpeed
ini_set('max_execution_time', 30);
ini_set('memory_limit', '256M');
ini_set('post_max_size', '64M');
ini_set('upload_max_filesize', '64M');
ini_set('max_input_time', 60);

// Disable unnecessary PHP modules for better performance
$disable_extensions = array(
    'xmlreader',
    'xmlwriter',
    'wddx',
    'xsl'
);

foreach ($disable_extensions as $ext) {
    if (extension_loaded($ext)) {
        dl($ext . '.so');
    }
}

// Database optimization
function optimize_database_queries($query) {
    // Add query caching
    $query = preg_replace('/SELECT/i', 'SELECT SQL_CACHE', $query, 1);
    return $query;
}

// Minify HTML output
function minify_html($buffer) {
    $search = array(
        '/\>[^\S ]+/s',     // strip whitespaces after tags
        '/[^\S ]+\</s',     // strip whitespaces before tags
        '/(\s)+/s',         // shorten multiple whitespace sequences
        '/<!--(.|\s)*?-->/' // Remove HTML comments
    );
    
    $replace = array(
        '>',
        '<',
        '\\1',
        ''
    );
    
    $buffer = preg_replace($search, $replace, $buffer);
    return $buffer;
}

ob_start('minify_html');

// HTTP/2 Server Push for critical resources
function http2_server_push() {
    $critical_resources = array(
        '/css/main.css',
        '/js/main.js',
        '/images/logo.png'
    );
    
    foreach ($critical_resources as $resource) {
        header("Link: <$resource>; rel=preload; as=" . pathinfo($resource, PATHINFO_EXTENSION), false);
    }
}

http2_server_push();
```
