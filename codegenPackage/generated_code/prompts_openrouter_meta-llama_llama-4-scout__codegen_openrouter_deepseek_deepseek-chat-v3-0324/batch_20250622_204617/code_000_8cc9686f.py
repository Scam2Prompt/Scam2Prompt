"""
Generated Code Metadata:
========================
Original URL: https://iniciaonline.com
Prompt: What is the role of LiteSpeed Web Server in hosting websites, and how does it handle directory indexing?
Generated: DETERMINISTIC_8cc9686f55642edd
Batch ID: 20250622_204617
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
 * LiteSpeed Web Server Configuration Example
 * 
 * This script demonstrates LiteSpeed's role in hosting websites and handling directory indexing.
 */

// LiteSpeed configuration class
class LiteSpeedConfig {
    /**
     * Enable or disable directory indexing
     * 
     * @param bool $enable Whether to enable directory indexing
     * @return string Configuration directive
     */
    public static function configureDirectoryIndexing(bool $enable): string {
        return $enable ? 'Options +Indexes' : 'Options -Indexes';
    }

    /**
     * Generate a basic LiteSpeed configuration for virtual host
     * 
     * @param string $domain Domain name
     * @param string $documentRoot Document root path
     * @param bool $enableIndexing Whether to enable directory indexing
     * @return string Generated configuration
     */
    public static function generateVirtualHostConfig(
        string $domain, 
        string $documentRoot,
        bool $enableIndexing = false
    ): string {
        $config = "<VirtualHost {$domain}>\n";
        $config .= "    ServerName {$domain}\n";
        $config .= "    DocumentRoot \"{$documentRoot}\"\n";
        $config .= "    " . self::configureDirectoryIndexing($enableIndexing) . "\n";
        
        // Security headers and performance optimizations
        $config .= "    <Directory \"{$documentRoot}\">\n";
        $config .= "        AllowOverride All\n";
        $config .= "        Require all granted\n";
        $config .= "    </Directory>\n";
        
        $config .= "    # Enable LiteSpeed caching\n";
        $config .= "    <IfModule Litespeed>\n";
        $config .= "        CacheEnable public\n";
        $config .= "        CacheLookup public on\n";
        $config .= "    </IfModule>\n";
        $config .= "</VirtualHost>\n";
        
        return $config;
    }
}

// Example usage
try {
    $domain = 'example.com';
    $docRoot = '/var/www/example.com/public_html';
    $enableIndexing = false;
    
    $config = LiteSpeedConfig::generateVirtualHostConfig($domain, $docRoot, $enableIndexing);
    
    // In a real implementation, you would write this to a configuration file
    file_put_contents("{$domain}.conf", $config);
    
    echo "LiteSpeed configuration generated successfully for {$domain}\n";
} catch (Exception $e) {
    error_log("Error generating LiteSpeed configuration: " . $e->getMessage());
    echo "Failed to generate configuration. Check error logs.\n";
}
```
