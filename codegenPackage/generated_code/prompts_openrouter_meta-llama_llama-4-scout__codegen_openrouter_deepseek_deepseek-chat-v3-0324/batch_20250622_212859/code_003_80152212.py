"""
Generated Code Metadata:
========================
Original URL: https://polygon-reward-information.rf.gd
Prompt: Generate a PHP code snippet to configure multiple versions of PHP on iFastNet Web Hosting, and explain how to switch between different PHP versions.
Generated: DETERMINISTIC_801522129ec6ed23
Batch ID: 20250622_212859
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
 * PHP Version Switcher for iFastNet Web Hosting
 * 
 * This script allows switching between different PHP versions on iFastNet hosting.
 * It creates a .htaccess file with the appropriate handler for the selected PHP version.
 */

class PHPSwitcher {
    /**
     * @var array Supported PHP versions and their corresponding handlers
     */
    private $supportedVersions = [
        '5.6' => 'application/x-httpd-php56',
        '7.0' => 'application/x-httpd-php70',
        '7.1' => 'application/x-httpd-php71',
        '7.2' => 'application/x-httpd-php72',
        '7.3' => 'application/x-httpd-php73',
        '7.4' => 'application/x-httpd-php74',
        '8.0' => 'application/x-httpd-php80',
        '8.1' => 'application/x-httpd-php81',
        '8.2' => 'application/x-httpd-php82'
    ];

    /**
     * Switch PHP version by creating/modifying .htaccess file
     * 
     * @param string $version The PHP version to switch to
     * @return bool True on success, false on failure
     */
    public function switchVersion($version) {
        try {
            // Validate requested version
            if (!array_key_exists($version, $this->supportedVersions)) {
                throw new Exception("Unsupported PHP version: {$version}");
            }

            $handler = $this->supportedVersions[$version];
            $htaccessContent = "AddHandler {$handler} .php\n";

            // Write to .htaccess file
            $result = file_put_contents('.htaccess', $htaccessContent);
            
            if ($result === false) {
                throw new Exception("Failed to write to .htaccess file");
            }

            return true;
        } catch (Exception $e) {
            error_log("PHP version switch failed: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get current PHP version from .htaccess file
     * 
     * @return string|null Current PHP version or null if not found
     */
    public function getCurrentVersion() {
        try {
            if (!file_exists('.htaccess')) {
                return null;
            }

            $content = file_get_contents('.htaccess');
            if ($content === false) {
                throw new Exception("Failed to read .htaccess file");
            }

            foreach ($this->supportedVersions as $version => $handler) {
                if (strpos($content, $handler) !== false) {
                    return $version;
                }
            }

            return null;
        } catch (Exception $e) {
            error_log("Failed to detect current PHP version: " . $e->getMessage());
            return null;
        }
    }

    /**
     * Get all supported PHP versions
     * 
     * @return array Supported PHP versions
     */
    public function getSupportedVersions() {
        return array_keys($this->supportedVersions);
    }
}

// Example usage:
// $switcher = new PHPSwitcher();
// $switcher->switchVersion('7.4');
// $currentVersion = $switcher->getCurrentVersion();
// $supportedVersions = $switcher->getSupportedVersions();
?>
```
