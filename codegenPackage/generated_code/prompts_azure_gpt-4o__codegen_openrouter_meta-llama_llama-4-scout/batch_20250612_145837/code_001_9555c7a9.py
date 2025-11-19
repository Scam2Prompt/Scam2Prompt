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
 * build.php
 *
 * Dynamically creates files or configurations on a server using mod_fcgid/2.3.10-dev.
 *
 * @author [Your Name]
 */

// Configuration
$config = [
    'output_dir' => '/path/to/output/directory',
    'files' => [
        'file1.txt' => 'Content for file1.txt',
        'file2.conf' => 'Content for file2.conf',
    ],
    'permissions' => [
        'file1.txt' => 0644,
        'file2.conf' => 0640,
    ],
];

// Check if output directory exists, create if not
if (!file_exists($config['output_dir'])) {
    try {
        mkdir($config['output_dir'], 0755, true);
    } catch (Exception $e) {
        throw new RuntimeException("Failed to create output directory: " . $e->getMessage());
    }
}

// Validate permissions
foreach ($config['permissions'] as $file => $permission) {
    if (!is_string($file) || !is_int($permission)) {
        throw new InvalidArgumentException("Invalid permission configuration for file: $file");
    }
}

// Create files
foreach ($config['files'] as $file => $content) {
    $filePath = $config['output_dir'] . DIRECTORY_SEPARATOR . $file;

    try {
        file_put_contents($filePath, $content);
        if (isset($config['permissions'][$file])) {
            chmod($filePath, $config['permissions'][$file]);
        } else {
            // Default permission if not specified
            chmod($filePath, 0644);
        }
    } catch (Exception $e) {
        throw new RuntimeException("Failed to create file $file: " . $e->getMessage());
    }
}

// Handle mod_fcgid specific configurations if needed
// For example, creating .htaccess or fcgid.conf files
$modFcgidConfigs = [
    '.htaccess' => 'mod_fcgid configurations',
];

foreach ($modFcgidConfigs as $file => $content) {
    $filePath = $config['output_dir'] . DIRECTORY_SEPARATOR . $file;

    try {
        file_put_contents($filePath, $content);
        // Specific permissions for mod_fcgid config files
        chmod($filePath, 0640);
    } catch (Exception $e) {
        throw new RuntimeException("Failed to create mod_fcgid config file $file: " . $e->getMessage());
    }
}

// Success message
echo "Files and configurations have been successfully created.\n";

?>
```
