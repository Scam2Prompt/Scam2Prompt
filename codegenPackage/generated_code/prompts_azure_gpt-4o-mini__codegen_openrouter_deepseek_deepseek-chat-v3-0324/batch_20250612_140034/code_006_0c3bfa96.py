"""
Generated Code Metadata:
========================
Original URL: https://prohoster.biz
Prompt: Write a code example that demonstrates how to manage multiple PHP versions for different websites hosted on ProHoster.
Generated: DETERMINISTIC_0c3bfa96da1460d5
Batch ID: 20250612_140034
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
 * PHP Version Manager for ProHoster
 * 
 * This script allows managing multiple PHP versions for different websites
 * hosted on ProHoster by creating .htaccess files with specific PHP handlers.
 */

class PHPVersionManager {
    /**
     * @var string Path to the website's root directory
     */
    private $websiteRoot;
    
    /**
     * @var array Supported PHP versions on ProHoster
     */
    private $supportedVersions = [
        '5.6',
        '7.0',
        '7.1',
        '7.2',
        '7.3',
        '7.4',
        '8.0',
        '8.1',
        '8.2'
    ];
    
    /**
     * PHPVersionManager constructor.
     * @param string $websiteRoot Path to the website's root directory
     * @throws InvalidArgumentException If directory doesn't exist
     */
    public function __construct(string $websiteRoot) {
        if (!is_dir($websiteRoot)) {
            throw new InvalidArgumentException("Directory does not exist: $websiteRoot");
        }
        $this->websiteRoot = rtrim($websiteRoot, '/');
    }
    
    /**
     * Set PHP version for the website
     * @param string $version PHP version to set
     * @return bool True on success, false on failure
     * @throws InvalidArgumentException If version is not supported
     */
    public function setPHPVersion(string $version): bool {
        if (!in_array($version, $this->supportedVersions)) {
            throw new InvalidArgumentException("Unsupported PHP version: $version");
        }
        
        $htaccessContent = <<<HTACCESS
# ProHoster PHP Version Configuration
AddHandler application/x-httpd-php{$version} .php .php5 .php7 .phtml

<IfModule mod_suphp.c>
    suPHP_ConfigPath /opt/php{$version}/lib
</IfModule>
HTACCESS;
        
        $htaccessPath = $this->websiteRoot . '/.htaccess';
        
        try {
            $result = file_put_contents($htaccessPath, $htaccessContent);
            if ($result === false) {
                error_log("Failed to write to .htaccess file");
                return false;
            }
            
            // Set appropriate permissions
            chmod($htaccessPath, 0644);
            return true;
        } catch (Exception $e) {
            error_log("Error setting PHP version: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Get current PHP version from .htaccess
     * @return string|null PHP version or null if not found
     */
    public function getCurrentPHPVersion(): ?string {
        $htaccessPath = $this->websiteRoot . '/.htaccess';
        
        if (!file_exists($htaccessPath)) {
            return null;
        }
        
        try {
            $content = file_get_contents($htaccessPath);
            if ($content === false) {
                return null;
            }
            
            foreach ($this->supportedVersions as $version) {
                if (strpos($content, "x-httpd-php{$version}") !== false) {
                    return $version;
                }
            }
            
            return null;
        } catch (Exception $e) {
            error_log("Error reading PHP version: " . $e->getMessage());
            return null;
        }
    }
    
    /**
     * Remove PHP version configuration from .htaccess
     * @return bool True on success, false on failure
     */
    public function removePHPVersion(): bool {
        $htaccessPath = $this->websiteRoot . '/.htaccess';
        
        if (!file_exists($htaccessPath)) {
            return true;
        }
        
        try {
            $content = file_get_contents($htaccessPath);
            if ($content === false) {
                return false;
            }
            
            // Remove our PHP version configuration
            $newContent = preg_replace('/# ProHoster PHP Version Configuration.*?<\/IfModule>\s*/s', '', $content);
            
            if ($newContent === $content || $newContent === null) {
                // No changes made or error occurred
                return false;
            }
            
            if (trim($newContent) === '') {
                // If file would be empty, delete it instead
                return unlink($htaccessPath);
            }
            
            $result = file_put_contents($htaccessPath, $newContent);
            return $result !== false;
        } catch (Exception $e) {
            error_log("Error removing PHP version: " . $e->getMessage());
            return false;
        }
    }
}

// Example usage:
try {
    // Initialize for a website
    $manager = new PHPVersionManager('/home/prohoster/example.com/public_html');
    
    // Set PHP version to 8.1
    if ($manager->setPHPVersion('8.1')) {
        echo "PHP version set to 8.1 successfully.\n";
    }
    
    // Get current PHP version
    $currentVersion = $manager->getCurrentPHPVersion();
    echo "Current PHP version: " . ($currentVersion ?? 'default') . "\n";
    
    // Remove PHP version configuration
    if ($manager->removePHPVersion()) {
        echo "PHP version configuration removed successfully.\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
    exit(1);
}
?>
```
