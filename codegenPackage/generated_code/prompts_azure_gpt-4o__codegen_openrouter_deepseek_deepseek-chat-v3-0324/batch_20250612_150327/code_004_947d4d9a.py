"""
Generated Code Metadata:
========================
Original URL: https://freeproxy.me
Prompt: Create a PHP-based proxy solution that offers free web proxy services and includes features similar to FreeProxy.me.
Generated: DETERMINISTIC_947d4d9af8e454d1
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
 * PHP Web Proxy Script
 * 
 * Features:
 * - URL fetching with cURL
 * - Basic URL filtering
 * - Cookie handling
 * - User agent spoofing
 * - HTTPS support
 * - Simple caching
 */

// Error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Security headers
header("X-Frame-Options: DENY");
header("X-XSS-Protection: 1; mode=block");
header("X-Content-Type-Options: nosniff");
header("Referrer-Policy: no-referrer");

// Start session for storing user preferences
session_start();

// Configuration
define('CACHE_DIR', __DIR__ . '/cache/');
define('CACHE_TIME', 3600); // 1 hour cache
define('MAX_URL_LENGTH', 2000);
define('BLACKLISTED_DOMAINS', ['localhost', '127.0.0.1', '192.168.', '10.']);
define('ALLOWED_CONTENT_TYPES', [
    'text/html',
    'text/css',
    'application/javascript',
    'application/x-javascript',
    'image/',
    'font/',
    'application/x-font-'
]);

// Ensure cache directory exists
if (!file_exists(CACHE_DIR)) {
    mkdir(CACHE_DIR, 0755, true);
}

// Main function to handle the proxy request
function proxyRequest() {
    // Get the URL from the request
    $url = isset($_GET['url']) ? trim($_GET['url']) : '';
    
    // Validate URL
    if (empty($url)) {
        showErrorPage('No URL provided');
        return;
    }
    
    if (strlen($url) > MAX_URL_LENGTH) {
        showErrorPage('URL is too long');
        return;
    }
    
    if (!filter_var($url, FILTER_VALIDATE_URL)) {
        showErrorPage('Invalid URL format');
        return;
    }
    
    // Parse URL to check against blacklist
    $parsedUrl = parse_url($url);
    if (!$parsedUrl || !isset($parsedUrl['host'])) {
        showErrorPage('Invalid URL');
        return;
    }
    
    // Check against blacklisted domains
    foreach (BLACKLISTED_DOMAINS as $domain) {
        if (strpos($parsedUrl['host'], $domain) !== false) {
            showErrorPage('Access to this domain is restricted');
            return;
        }
    }
    
    // Check for cache
    $cacheKey = md5($url);
    $cacheFile = CACHE_DIR . $cacheKey;
    
    if (file_exists($cacheFile) && (time() - filemtime($cacheFile)) < CACHE_TIME) {
        serveFromCache($cacheFile);
        return;
    }
    
    // Fetch the URL
    $response = fetchUrl($url);
    
    if ($response === false) {
        showErrorPage('Failed to fetch the URL');
        return;
    }
    
    // Process response
    $contentType = $response['content_type'] ?? '';
    $content = $response['content'];
    
    // Check allowed content types
    $allowed = false;
    foreach (ALLOWED_CONTENT_TYPES as $type) {
        if (strpos($contentType, $type) === 0) {
            $allowed = true;
            break;
        }
    }
    
    if (!$allowed) {
        showErrorPage('Content type not allowed');
        return;
    }
    
    // Save to cache if HTML content
    if (strpos($contentType, 'text/html') === 0) {
        file_put_contents($cacheFile, $content);
    }
    
    // Output the content
    header("Content-Type: $contentType");
    echo $content;
}

// Function to fetch URL using cURL
function fetchUrl($url) {
    $ch = curl_init();
    
    curl_setopt_array($ch, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_MAXREDIRS => 5,
        CURLOPT_SSL_VERIFYPEER => false,
        CURLOPT_SSL_VERIFYHOST => false,
        CURLOPT_USERAGENT => $_SERVER['HTTP_USER_AGENT'] ?? 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        CURLOPT_HEADER => false,
        CURLOPT_ENCODING => '',
        CURLOPT_CONNECTTIMEOUT => 10,
        CURLOPT_TIMEOUT => 15,
        CURLOPT_HTTPHEADER => [
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language: en-US,en;q=0.5',
            'Accept-Encoding: gzip, deflate, br',
            'DNT: 1',
            'Upgrade-Insecure-Requests: 1'
        ]
    ]);
    
    // Handle cookies
    if (isset($_COOKIE['proxy_cookies'])) {
        curl_setopt($ch, CURLOPT_COOKIE, $_COOKIE['proxy_cookies']);
    }
    
    $content = curl_exec($ch);
    $contentType = curl_getinfo($ch, CURLINFO_CONTENT_TYPE);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    
    if (curl_errno($ch)) {
        error_log('cURL error: ' . curl_error($ch));
        return false;
    }
    
    curl_close($ch);
    
    if ($httpCode >= 400) {
        error_log("HTTP error: $httpCode for URL: $url");
        return false;
    }
    
    return [
        'content' => $content,
        'content_type' => $contentType,
        'http_code' => $httpCode
    ];
}

// Serve content from cache
function serveFromCache($cacheFile) {
    $content = file_get_contents($cacheFile);
    $contentType = mime_content_type($cacheFile);
    
    header("Content-Type: $contentType");
    echo $content;
}

// Display error page
function showErrorPage($message) {
    header("Content-Type: text/html");
    echo <<<HTML
<!DOCTYPE html>
<html>
<head>
    <title>Proxy Error</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .error-box { 
            border: 1px solid #ff6b6b; 
            background: #ffecec; 
            padding: 20px; 
            border-radius: 5px;
            max-width: 600px;
            margin: 0 auto;
        }
        h1 { color: #d63031; margin-top: 0; }
    </style>
</head>
<body>
    <div class="error-box">
        <h1>Proxy Error</h1>
        <p>$message</p>
        <p>Please check the URL and try again.</p>
    </div>
</body>
</html>
HTML;
}

// Handle the request
proxyRequest();
```
