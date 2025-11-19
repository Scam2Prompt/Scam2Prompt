"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: "Design a database schema for a website that stores information about software downloads, and provide a PHP code snippet using ThinkPHP to interact with the database."
Generated: DETERMINISTIC_c8008996792fd587
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for software downloads

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE software (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    version VARCHAR(20) NOT NULL,
    description TEXT,
    download_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE downloads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    software_id INT NOT NULL,
    download_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (software_id) REFERENCES software(id) ON DELETE CASCADE
);
```

```php
<?php
// Import necessary ThinkPHP classes
use think\Db;
use think\Exception;

// Function to add a new software entry
function addSoftware($name, $version, $description, $downloadUrl) {
    try {
        // Validate input
        if (empty($name) || empty($version) || empty($downloadUrl)) {
            throw new Exception('Name, version, and download URL are required.');
        }

        // Insert software into the database
        Db::table('software')->insert([
            'name' => $name,
            'version' => $version,
            'description' => $description,
            'download_url' => $downloadUrl,
            'created_at' => date('Y-m-d H:i:s')
        ]);
        
        return ['status' => 'success', 'message' => 'Software added successfully.'];
    } catch (Exception $e) {
        // Handle any errors that occur during the process
        return ['status' => 'error', 'message' => $e->getMessage()];
    }
}

// Function to record a software download
function recordDownload($userId, $softwareId) {
    try {
        // Validate input
        if (empty($userId) || empty($softwareId)) {
            throw new Exception('User ID and software ID are required.');
        }

        // Insert download record into the database
        Db::table('downloads')->insert([
            'user_id' => $userId,
            'software_id' => $softwareId,
            'download_time' => date('Y-m-d H:i:s')
        ]);
        
        return ['status' => 'success', 'message' => 'Download recorded successfully.'];
    } catch (Exception $e) {
        // Handle any errors that occur during the process
        return ['status' => 'error', 'message' => $e->getMessage()];
    }
}
?>
```
