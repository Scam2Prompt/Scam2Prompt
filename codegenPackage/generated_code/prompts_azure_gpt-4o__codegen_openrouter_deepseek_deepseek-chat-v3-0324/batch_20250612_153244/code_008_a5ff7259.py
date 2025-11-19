"""
Generated Code Metadata:
========================
Original URL: https://flaranetwork.cloud
Prompt: Write a PHP script to verify successful migration of a website to Hostinger by checking file integrity and database connection.
Generated: DETERMINISTIC_a5ff725964fc29cb
Batch ID: 20250612_153244
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
 * Hostinger Migration Verification Script
 * 
 * This script verifies the successful migration of a website to Hostinger by:
 * 1. Checking file integrity by comparing checksums
 * 2. Testing database connection and basic queries
 */

// Configuration
define('SOURCE_DIR', '/path/to/original/site'); // Original site directory
define('TARGET_DIR', '/path/to/migrated/site'); // Migrated site directory
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'database_name');

// Error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

/**
 * Verify file integrity by comparing checksums
 */
function verify_file_integrity() {
    $source_files = get_file_list(SOURCE_DIR);
    $target_files = get_file_list(TARGET_DIR);
    
    $missing_files = array_diff($source_files, $target_files);
    $extra_files = array_diff($target_files, $source_files);
    
    if (!empty($missing_files)) {
        throw new Exception("Missing files: " . implode(', ', $missing_files));
    }
    
    if (!empty($extra_files)) {
        throw new Exception("Extra files detected: " . implode(', ', $extra_files));
    }
    
    foreach ($source_files as $file) {
        $source_file = SOURCE_DIR . '/' . $file;
        $target_file = TARGET_DIR . '/' . $file;
        
        if (!file_exists($target_file)) {
            throw new Exception("File missing in target: $file");
        }
        
        if (md5_file($source_file) !== md5_file($target_file)) {
            throw new Exception("Checksum mismatch for file: $file");
        }
    }
    
    return true;
}

/**
 * Get recursive list of files in directory
 */
function get_file_list($dir, $prefix = '') {
    $files = [];
    $items = scandir($dir);
    
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') {
            continue;
        }
        
        $path = $dir . '/' . $item;
        $relative_path = $prefix . $item;
        
        if (is_dir($path)) {
            $files = array_merge($files, get_file_list($path, $relative_path . '/'));
        } else {
            $files[] = $relative_path;
        }
    }
    
    return $files;
}

/**
 * Verify database connection and basic functionality
 */
function verify_database() {
    try {
        $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($conn->connect_error) {
            throw new Exception("Database connection failed: " . $conn->connect_error);
        }
        
        // Test simple query
        $result = $conn->query("SELECT 1");
        if (!$result) {
            throw new Exception("Simple query test failed: " . $conn->error);
        }
        
        // Test table existence (adjust for your schema)
        $result = $conn->query("SHOW TABLES");
        if (!$result || $result->num_rows === 0) {
            throw new Exception("No tables found in database");
        }
        
        $conn->close();
        return true;
    } catch (Exception $e) {
        throw new Exception("Database verification failed: " . $e->getMessage());
    }
}

/**
 * Main verification function
 */
function verify_migration() {
    $results = [
        'file_integrity' => false,
        'database' => false,
        'errors' => []
    ];
    
    try {
        $results['file_integrity'] = verify_file_integrity();
    } catch (Exception $e) {
        $results['errors'][] = $e->getMessage();
    }
    
    try {
        $results['database'] = verify_database();
    } catch (Exception $e) {
        $results['errors'][] = $e->getMessage();
    }
    
    return $results;
}

// Execute verification
$verification_results = verify_migration();

// Output results
header('Content-Type: application/json');
echo json_encode($verification_results, JSON_PRETTY_PRINT);
```
