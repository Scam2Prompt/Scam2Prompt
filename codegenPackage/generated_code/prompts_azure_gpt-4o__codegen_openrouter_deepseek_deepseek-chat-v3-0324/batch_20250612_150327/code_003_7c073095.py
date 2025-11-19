"""
Generated Code Metadata:
========================
Original URL: https://freeproxy.me
Prompt: Provide an example of how to configure PHP-Proxy 5.2.0 to support multiple proxy sites, as mentioned on FreeProxy.me.
Generated: DETERMINISTIC_7c073095fd67b760
Batch ID: 20250612_150327
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
 * PHP-Proxy 5.2.0 Multi-Site Configuration Example
 * 
 * This configuration allows hosting multiple proxy sites from a single installation.
 * Each site has its own configuration while sharing the same codebase.
 */

// Define base paths and configurations
define('PROXY_ROOT', dirname(__FILE__));
define('CONFIG_DIR', PROXY_ROOT . '/config/');
define('TEMPLATE_DIR', PROXY_ROOT . '/templates/');

// Load the main proxy class
require_once PROXY_ROOT . '/vendor/autoload.php';
require_once PROXY_ROOT . '/src/Proxy.php';

// Site configurations
$sites = [
    'site1' => [
        'site_name' => 'Proxy Site 1',
        'site_key'  => 'unique_key_1',
        'template'  => 'default',
        'options'   => [
            'disable_encryption' => false,
            'enable_caching'     => true,
            'cache_timeout'      => 3600
        ]
    ],
    'site2' => [
        'site_name' => 'Proxy Site 2',
        'site_key'  => 'unique_key_2',
        'template'  => 'dark',
        'options'   => [
            'disable_encryption' => true,
            'enable_caching'     => false
        ]
    ]
];

// Determine current site based on domain or path
$currentSite = determineCurrentSite();

// Validate site exists
if (!isset($sites[$currentSite])) {
    header('HTTP/1.1 404 Not Found');
    exit('Proxy site not found');
}

// Load configuration for current site
$config = array_merge(
    require CONFIG_DIR . 'default.php',
    $sites[$currentSite]
);

// Initialize proxy with site-specific configuration
$proxy = new Proxy($config);
$proxy->run();

/**
 * Determine current proxy site based on request
 * 
 * @return string Site identifier
 */
function determineCurrentSite() {
    // Check domain-based routing
    $host = $_SERVER['HTTP_HOST'] ?? '';
    
    // Example: site1.proxy.com, site2.proxy.com
    if (preg_match('/^(.*?)\.proxy\.com$/i', $host, $matches)) {
        return $matches[1];
    }
    
    // Check path-based routing (e.g., /site1/, /site2/)
    $path = $_SERVER['REQUEST_URI'] ?? '';
    if (preg_match('/^\/([^\/]+)\//', $path, $matches)) {
        return $matches[1];
    }
    
    // Default to first site if no match
    return 'site1';
}

// Helper function to generate site URLs
function getSiteUrl($siteId) {
    if (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on') {
        $protocol = 'https';
    } else {
        $protocol = 'http';
    }
    
    $host = $_SERVER['HTTP_HOST'] ?? 'localhost';
    return "$protocol://$host/$siteId/";
}
```
