"""
Generated Code Metadata:
========================
Original URL: https://unisawpv3.com
Prompt: Generate a PHP code snippet that replicates the behavior of `build.php` for dynamically creating files or configurations on a server using `mod_fcgid/2.3.10-dev`.
Generated: DETERMINISTIC_9555c7a95dd77309
Batch ID: 20250612_145837
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
 * Dynamic File/Configuration Builder for mod_fcgid
 * 
 * This script replicates the behavior of build.php for dynamically creating
 * files or configurations on a server using mod_fcgid/2.3.10-dev.
 * 
 * @package    DynamicBuilder
 * @version    1.0.0
 * @license    MIT
 */

class DynamicBuilder {
    /**
     * @var string The base directory where files will be created
     */
    private $baseDir;
    
    /**
     * @var array Default configuration options
     */
    private $defaultConfig = [
        'max_processes' => 10,
        'max_request_len' => 131072,
        'idle_timeout' => 30,
        'process_life_time' => 3600,
        'ipc_connect_timeout' => 120
    ];
    
    /**
     * Constructor
     * 
     * @param string $baseDir The base directory for file operations
     * @throws Exception If directory is not writable
     */
    public function __construct($baseDir = null) {
        $this->baseDir = $baseDir ?: sys_get_temp_dir() . '/fcgid_build';
        
        if (!is_dir($this->baseDir) && !mkdir($this->baseDir, 0755, true)) {
            throw new Exception("Failed to create directory: {$this->baseDir}");
        }
        
        if (!is_writable($this->baseDir)) {
            throw new Exception("Directory is not writable: {$this->baseDir}");
        }
    }
    
    /**
     * Build configuration file
     * 
     * @param array $config Configuration options
     * @param string $filename Output filename
     * @return bool True on success, false on failure
     */
    public function buildConfig(array $config = [], $filename = 'fcgid.conf') {
        $config = array_merge($this->defaultConfig, $config);
        $filePath = $this->baseDir . '/' . ltrim($filename, '/');
        
        $content = <<<CONF
# Auto-generated mod_fcgid configuration
<IfModule mod_fcgid.c>
    FcgidMaxProcesses {$config['max_processes']}
    FcgidMaxRequestLen {$config['max_request_len']}
    FcgidIdleTimeout {$config['idle_timeout']}
    FcgidProcessLifeTime {$config['process_life_time']}
    FcgidIPCConnectTimeout {$config['ipc_connect_timeout']}
</IfModule>
CONF;
        
        return $this->writeFile($filePath, $content);
    }
    
    /**
     * Build wrapper script
     * 
     * @param string $interpreter Path to PHP interpreter
     * @param string $filename Output filename
     * @return bool True on success, false on failure
     */
    public function buildWrapper($interpreter = '/usr/bin/php-cgi', $filename = 'php-wrapper') {
        $filePath = $this->baseDir . '/' . ltrim($filename, '/');
        
        $content = <<<WRAPPER
#!/bin/sh
export PHP_FCGI_MAX_REQUESTS=10000
exec {$interpreter}
WRAPPER;
        
        if ($this->writeFile($filePath, $content)) {
            return chmod($filePath, 0755);
        }
        
        return false;
    }
    
    /**
     * Write content to file
     * 
     * @param string $filePath Full path to file
     * @param string $content File content
     * @return bool True on success, false on failure
     */
    private function writeFile($filePath, $content) {
        try {
            $bytes = file_put_contents($filePath, $content);
            return $bytes !== false;
        } catch (Exception $e) {
            error_log("File write failed: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Clean up created files
     * 
     * @param array $filenames Files to remove
     * @return bool True if all files were removed successfully
     */
    public function cleanup(array $filenames = []) {
        $success = true;
        
        foreach ($filenames as $filename) {
            $filePath = $this->baseDir . '/' . ltrim($filename, '/');
            
            if (file_exists($filePath) && !unlink($filePath)) {
                error_log("Failed to remove file: {$filePath}");
                $success = false;
            }
        }
        
        return $success;
    }
}

// Example usage:
/*
try {
    $builder = new DynamicBuilder('/path/to/output');
    
    // Build configuration file
    $builder->buildConfig([
        'max_processes' => 15,
        'idle_timeout' => 45
    ], 'custom_fcgid.conf');
    
    // Build wrapper script
    $builder->buildWrapper('/opt/php/8.1/bin/php-cgi', 'php-fcgi-wrapper');
    
    // Clean up
    // $builder->cleanup(['custom_fcgid.conf', 'php-fcgi-wrapper']);
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
}
*/
```
