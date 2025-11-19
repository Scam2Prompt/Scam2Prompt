"""
Generated Code Metadata:
========================
Original URL: https://axieinfinity.kesug.com
Prompt: Create a guide for migrating an existing website to a hosting service that provides free transfer and supports multiple PHP versions, as outlined on the iFastNet hosting page.
Generated: DETERMINISTIC_9fc64e3669ed4034
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a PHP script that automates the website migration process for iFastNet hosting, including version compatibility checks and file transfers:

```php
<?php
/**
 * Website Migration Script for iFastNet Hosting
 * 
 * Features:
 * - Validates PHP version compatibility
 * - Transfers files via FTP
 * - Creates backup of existing site
 * - Handles database migration
 * - Provides progress feedback
 */

class WebsiteMigrator {
    private $ftpHost;
    private $ftpUser;
    private $ftpPass;
    private $localPath;
    private $remotePath;
    private $dbConfig;
    private $supportedPhpVersions = ['5.6', '7.0', '7.1', '7.2', '7.3', '7.4', '8.0', '8.1', '8.2'];
    
    /**
     * Constructor
     * 
     * @param array $config Configuration array with connection details
     */
    public function __construct(array $config) {
        $this->validateConfig($config);
        
        $this->ftpHost = $config['ftp_host'];
        $this->ftpUser = $config['ftp_user'];
        $this->ftpPass = $config['ftp_pass'];
        $this->localPath = rtrim($config['local_path'], '/') . '/';
        $this->remotePath = rtrim($config['remote_path'], '/') . '/';
        
        if (isset($config['db_config'])) {
            $this->dbConfig = $config['db_config'];
        }
    }
    
    /**
     * Validate configuration parameters
     * 
     * @param array $config Configuration array
     * @throws InvalidArgumentException If config is invalid
     */
    private function validateConfig(array $config) {
        $required = ['ftp_host', 'ftp_user', 'ftp_pass', 'local_path', 'remote_path'];
        foreach ($required as $field) {
            if (empty($config[$field])) {
                throw new InvalidArgumentException("Missing required field: $field");
            }
        }
        
        if (!is_dir($config['local_path'])) {
            throw new InvalidArgumentException("Local path does not exist or is not a directory");
        }
    }
    
    /**
     * Check PHP version compatibility
     * 
     * @param string $targetVersion Target PHP version
     * @return bool True if compatible, false otherwise
     */
    public function checkPhpCompatibility($targetVersion) {
        if (!in_array($targetVersion, $this->supportedPhpVersions)) {
            return false;
        }
        
        // Check for deprecated functions/features
        $compatibility = true;
        
        // Example check (extend based on your needs)
        if (version_compare($targetVersion, '7.0', '<') && function_exists('mcrypt_encrypt')) {
            $compatibility = false;
        }
        
        return $compatibility;
    }
    
    /**
     * Transfer files to remote server
     * 
     * @param bool $backupFirst Whether to create backup first
     * @return bool True on success, false on failure
     */
    public function transferFiles($backupFirst = true) {
        try {
            $conn = ftp_connect($this->ftpHost);
            if (!$conn) {
                throw new Exception("Could not connect to FTP server");
            }
            
            if (!ftp_login($conn, $this->ftpUser, $this->ftpPass)) {
                throw new Exception("FTP login failed");
            }
            
            // Enable passive mode and set timeout
            ftp_pasv($conn, true);
            ftp_set_option($conn, FTP_TIMEOUT_SEC, 300);
            
            if ($backupFirst) {
                $this->createRemoteBackup($conn);
            }
            
            $this->uploadDirectory($conn, $this->localPath, $this->remotePath);
            
            ftp_close($conn);
            return true;
        } catch (Exception $e) {
            error_log("File transfer failed: " . $e->getMessage());
            if (isset($conn)) {
                ftp_close($conn);
            }
            return false;
        }
    }
    
    /**
     * Create backup of remote directory
     * 
     * @param resource $ftpConn Active FTP connection
     * @throws Exception If backup fails
     */
    private function createRemoteBackup($ftpConn) {
        $backupDir = $this->remotePath . '_backup_' . date('YmdHis');
        
        if (!ftp_mkdir($ftpConn, $backupDir)) {
            throw new Exception("Failed to create backup directory");
        }
        
        $files = ftp_nlist($ftpConn, $this->remotePath);
        foreach ($files as $file) {
            if ($file == '.' || $file == '..') continue;
            
            $remoteFile = $this->remotePath . basename($file);
            $backupFile = $backupDir . '/' . basename($file);
            
            if (!ftp_rename($ftpConn, $remoteFile, $backupFile)) {
                throw new Exception("Failed to backup file: " . basename($file));
            }
        }
    }
    
    /**
     * Recursively upload directory
     * 
     * @param resource $ftpConn Active FTP connection
     * @param string $localDir Local directory path
     * @param string $remoteDir Remote directory path
     * @throws Exception If upload fails
     */
    private function uploadDirectory($ftpConn, $localDir, $remoteDir) {
        $files = scandir($localDir);
        foreach ($files as $file) {
            if ($file == '.' || $file == '..') continue;
            
            $localPath = $localDir . $file;
            $remotePath = $remoteDir . $file;
            
            if (is_dir($localPath)) {
                if (!@ftp_chdir($ftpConn, $remotePath)) {
                    if (!ftp_mkdir($ftpConn, $remotePath)) {
                        throw new Exception("Failed to create directory: $remotePath");
                    }
                }
                $this->uploadDirectory($ftpConn, $localPath . '/', $remotePath . '/');
            } else {
                if (!ftp_put($ftpConn, $remotePath, $localPath, FTP_BINARY)) {
                    throw new Exception("Failed to upload file: $file");
                }
            }
        }
    }
    
    /**
     * Migrate database
     * 
     * @return bool True on success, false on failure
     */
    public function migrateDatabase() {
        if (empty($this->dbConfig)) {
            return true; // No database to migrate
        }
        
        try {
            // Export local database
            $localDb = new PDO(
                "mysql:host={$this->dbConfig['local']['host']};dbname={$this->dbConfig['local']['database']}",
                $this->dbConfig['local']['username'],
                $this->dbConfig['local']['password']
            );
            
            $remoteDb = new PDO(
                "mysql:host={$this->dbConfig['remote']['host']};dbname={$this->dbConfig['remote']['database']}",
                $this->dbConfig['remote']['username'],
                $this->dbConfig['remote']['password']
            );
            
            // Get all tables
            $tables = $localDb->query("SHOW TABLES")->fetchAll(PDO::FETCH_COLUMN);
            
            foreach ($tables as $table) {
                $this->migrateTable($localDb, $remoteDb, $table);
            }
            
            return true;
        } catch (PDOException $e) {
            error_log("Database migration failed: " . $e->getMessage());
            return false;
        }
    }
    
    /**
     * Migrate a single table
     * 
     * @param PDO $localDb Local database connection
     * @param PDO $remoteDb Remote database connection
     * @param string $table Table name
     * @throws Exception If migration fails
     */
    private function migrateTable($localDb, $remoteDb, $table) {
        // Drop existing table if it exists
        $remoteDb->exec("DROP TABLE IF EXISTS `$table`");
        
        // Get create table statement
        $createTable = $localDb->query("SHOW CREATE TABLE `$table`")->fetchColumn(1);
        $remoteDb->exec($createTable);
        
        // Get all data
        $data = $localDb->query("SELECT * FROM `$table`")->fetchAll(PDO::FETCH_ASSOC);
        
        if (!empty($data)) {
            $columns = array_keys($data[0]);
            $columnsStr = implode('`, `', $columns);
            $placeholders = implode(', ', array_fill(0, count($columns), '?'));
            
            $stmt = $remoteDb->prepare("INSERT INTO `$table` (`$columnsStr`) VALUES ($placeholders)");
            
            foreach ($data as $row) {
                $stmt->execute(array_values($row));
            }
        }
    }
}

// Example usage:
