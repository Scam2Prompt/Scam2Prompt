"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Write a PHP script to migrate a website to a new server, ensuring compatibility with the Linux hosting environment described on the Megh iTech website.
Generated: DETERMINISTIC_c68b718338183f32
Batch ID: 20250612_145136
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
 * Website Migration Script
 * 
 * This script automates the migration of a website to a new Linux server.
 * It handles file transfers, database migration, and configuration updates.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - SSH access to both source and destination servers
 * - MySQL/MariaDB databases
 * - Linux environment (tested on Ubuntu/CentOS)
 */

// Error reporting for debugging (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Configuration
$config = [
    // Source server details
    'source' => [
        'host' => 'source.example.com',
        'username' => 'source_user',
        'password' => 'source_password', // Consider using SSH keys instead
        'path' => '/var/www/html/',
        'db_host' => 'localhost',
        'db_name' => 'source_db',
        'db_user' => 'db_user',
        'db_pass' => 'db_password'
    ],
    
    // Destination server details (Megh iTech Linux hosting)
    'destination' => [
        'host' => 'new.example.com',
        'username' => 'new_user',
        'password' => 'new_password', // Consider using SSH keys instead
        'path' => '/var/www/html/',
        'db_host' => 'localhost',
        'db_name' => 'new_db',
        'db_user' => 'new_db_user',
        'db_pass' => 'new_db_password'
    ],
    
    // Migration options
    'options' => [
        'transfer_method' => 'rsync', // rsync or scp
        'backup_source' => true,
        'backup_dir' => '/backups/',
        'exclude_files' => [
            '.git',
            'node_modules',
            '*.log',
            '*.tmp'
        ],
        'permissions' => [
            'files' => 644,
            'folders' => 755
        ]
    ]
];

class WebsiteMigrator {
    private $config;
    private $logFile;
    private $startTime;
    
    public function __construct($config) {
        $this->config = $config;
        $this->logFile = __DIR__ . '/migration_log_' . date('Ymd_His') . '.log';
        $this->startTime = microtime(true);
        
        $this->log("Starting website migration process");
        $this->log("Source: " . $this->config['source']['host']);
        $this->log("Destination: " . $this->config['destination']['host']);
    }
    
    public function migrate() {
        try {
            $this->validateConfig();
            $this->createBackup();
            $this->transferFiles();
            $this->migrateDatabase();
            $this->updateConfigurations();
            $this->setPermissions();
            
            $executionTime = round(microtime(true) - $this->startTime, 2);
            $this->log("Migration completed successfully in {$executionTime} seconds");
            return true;
        } catch (Exception $e) {
            $this->log("Migration failed: " . $e->getMessage(), 'ERROR');
            return false;
        }
    }
    
    private function validateConfig() {
        $required = ['host', 'username', 'path', 'db_host', 'db_name', 'db_user'];
        
        foreach (['source', 'destination'] as $server) {
            foreach ($required as $field) {
                if (empty($this->config[$server][$field])) {
                    throw new Exception("Missing required configuration: $server.$field");
                }
            }
        }
        
        $this->log("Configuration validated successfully");
    }
    
    private function createBackup() {
        if (!$this->config['options']['backup_source']) {
            $this->log("Skipping source backup as configured");
            return;
        }
        
        $backupDir = $this->config['options']['backup_dir'];
        if (!is_dir($backupDir) && !mkdir($backupDir, 0755, true)) {
            throw new Exception("Failed to create backup directory: $backupDir");
        }
        
        $timestamp = date('Ymd_His');
        $backupFile = $backupDir . 'backup_' . $timestamp . '.tar.gz';
        
        $command = "tar -czf $backupFile -C {$this->config['source']['path']} .";
        exec($command, $output, $returnCode);
        
        if ($returnCode !== 0) {
            throw new Exception("Failed to create source backup");
        }
        
        $this->log("Source backup created: $backupFile");
    }
    
    private function transferFiles() {
        $exclude = '';
        foreach ($this->config['options']['exclude_files'] as $pattern) {
            $exclude .= " --exclude='$pattern'";
        }
        
        $source = "{$this->config['source']['username']}@{$this->config['source']['host']}:{$this->config['source']['path']}";
        $destination = "{$this->config['destination']['username']}@{$this->config['destination']['host']}:{$this->config['destination']['path']}";
        
        if ($this->config['options']['transfer_method'] === 'rsync') {
            $command = "rsync -avz --progress $exclude $source $destination";
        } else {
            $command = "scp -r $source $destination";
        }
        
        $this->log("Starting file transfer: $command");
        exec($command, $output, $returnCode);
        
        if ($returnCode !== 0) {
            throw new Exception("File transfer failed with code $returnCode");
        }
        
        $this->log("Files transferred successfully");
    }
    
    private function migrateDatabase() {
        $this->log("Starting database migration");
        
        // Export source database
        $dumpFile = sys_get_temp_dir() . '/db_dump_' . date('Ymd_His') . '.sql';
        $exportCmd = "mysqldump -h {$this->config['source']['db_host']} -u {$this->config['source']['db_user']} " .
                     "-p{$this->config['source']['db_pass']} {$this->config['source']['db_name']} > $dumpFile";
        
        exec($exportCmd, $output, $returnCode);
        if ($returnCode !== 0) {
            throw new Exception("Failed to export source database");
        }
        
        // Import to destination
        $importCmd = "mysql -h {$this->config['destination']['db_host']} -u {$this->config['destination']['db_user']} " .
                     "-p{$this->config['destination']['db_pass']} {$this->config['destination']['db_name']} < $dumpFile";
        
        exec($importCmd, $output, $returnCode);
        unlink($dumpFile); // Clean up temporary file
        
        if ($returnCode !== 0) {
            throw new Exception("Failed to import database to destination");
        }
        
        $this->log("Database migrated successfully");
    }
    
    private function updateConfigurations() {
        $this->log("Updating configurations for new environment");
        
        // Example: Update database connection in config file
        $configFile = $this->config['destination']['path'] . 'wp-config.php'; // WordPress example
        if (file_exists($configFile)) {
            $content = file_get_contents($configFile);
            $content = preg_replace(
                "/define\('DB_NAME', '(.*?)'\);/",
                "define('DB_NAME', '{$this->config['destination']['db_name']}');",
                $content
            );
            $content = preg_replace(
                "/define\('DB_USER', '(.*?)'\);/",
                "define('DB_USER', '{$this->config['destination']['db_user']}');",
                $content
            );
            $content = preg_replace(
                "/define\('DB_PASSWORD', '(.*?)'\);/",
                "define('DB_PASSWORD', '{$this->config['destination']['db_pass']}');",
                $content
            );
            file_put_contents($configFile, $content);
        }
        
        $this->log("Configurations updated");
    }
    
    private function setPermissions() {
        $this->log("Setting file permissions");
        
        $filesPerm = $this->config['options']['permissions']['files'];
        $foldersPerm = $this->config['options']['permissions']['folders'];
        
        $commands = [
            "find {$this->config['destination']['path']} -type d -exec chmod $foldersPerm {} +",
            "find {$this->config['destination']['path']} -type f -exec chmod $filesPerm {} +",
            "chown -R {$this->config['destination']['username']}:{$this->config['destination']['username']} {$this->config['destination']['path']}"
        ];
        
        foreach ($commands as $command) {
            exec($command, $output
