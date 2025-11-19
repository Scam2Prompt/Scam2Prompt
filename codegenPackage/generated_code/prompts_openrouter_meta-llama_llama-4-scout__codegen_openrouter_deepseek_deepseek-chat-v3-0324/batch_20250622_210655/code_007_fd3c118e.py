"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: "Generate code to monitor and alert on changes in WordPress core files, plugins, or themes using PHP and server logs."
Generated: DETERMINISTIC_fd3c118e8fc8f7f5
Batch ID: 20250622_210655
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
 * WordPress File Monitor
 * 
 * Monitors changes in WordPress core files, plugins, and themes.
 * Logs changes and sends alerts when unauthorized modifications are detected.
 */

class WordPressFileMonitor {
    private $wp_content_dir;
    private $wp_includes_dir;
    private $wp_admin_dir;
    private $log_file;
    private $alert_email;
    private $file_hashes = array();
    private $excluded_files = array();

    /**
     * Constructor
     * 
     * @param string $alert_email Email address to send alerts to
     * @param string $log_file Path to log file
     * @param array $excluded_files Files to exclude from monitoring
     */
    public function __construct($alert_email, $log_file = 'wp_file_monitor.log', $excluded_files = array()) {
        $this->wp_content_dir = ABSPATH . 'wp-content/';
        $this->wp_includes_dir = ABSPATH . 'wp-includes/';
        $this->wp_admin_dir = ABSPATH . 'wp-admin/';
        $this->log_file = $log_file;
        $this->alert_email = $alert_email;
        $this->excluded_files = $excluded_files;
    }

    /**
     * Initialize file monitoring
     */
    public function init() {
        $this->load_hashes();
        $this->scan_files();
        $this->save_hashes();
    }

    /**
     * Load previously stored file hashes
     */
    private function load_hashes() {
        if (file_exists($this->log_file)) {
            $contents = file_get_contents($this->log_file);
            if (!empty($contents)) {
                $this->file_hashes = json_decode($contents, true);
            }
        }
    }

    /**
     * Save current file hashes to log file
     */
    private function save_hashes() {
        file_put_contents($this->log_file, json_encode($this->file_hashes));
    }

    /**
     * Scan WordPress files for changes
     */
    private function scan_files() {
        $directories = array(
            $this->wp_content_dir . 'plugins/',
            $this->wp_content_dir . 'themes/',
            $this->wp_includes_dir,
            $this->wp_admin_dir
        );

        foreach ($directories as $dir) {
            if (is_dir($dir)) {
                $this->scan_directory($dir);
            }
        }
    }

    /**
     * Scan a directory recursively
     * 
     * @param string $dir Directory path
     */
    private function scan_directory($dir) {
        $files = new RecursiveIteratorIterator(
            new RecursiveDirectoryIterator($dir),
            RecursiveIteratorIterator::SELF_FIRST
        );

        foreach ($files as $file) {
            if ($file->isDir() || $this->is_excluded($file->getPathname())) {
                continue;
            }

            $file_path = $file->getPathname();
            $current_hash = md5_file($file_path);

            if (isset($this->file_hashes[$file_path])) {
                if ($this->file_hashes[$file_path] !== $current_hash) {
                    $this->handle_file_change($file_path, $this->file_hashes[$file_path], $current_hash);
                }
            } else {
                $this->log_change($file_path, 'New file detected', $current_hash);
            }

            $this->file_hashes[$file_path] = $current_hash;
        }
    }

    /**
     * Check if file should be excluded from monitoring
     * 
     * @param string $file_path File path
     * @return bool
     */
    private function is_excluded($file_path) {
        foreach ($this->excluded_files as $excluded) {
            if (strpos($file_path, $excluded) !== false) {
                return true;
            }
        }
        return false;
    }

    /**
     * Handle file change detection
     * 
     * @param string $file_path Path to changed file
     * @param string $old_hash Previous file hash
     * @param string $new_hash Current file hash
     */
    private function handle_file_change($file_path, $old_hash, $new_hash) {
        $this->log_change($file_path, 'File modified', $new_hash);
        $this->send_alert($file_path, 'File modified');
    }

    /**
     * Log file change
     * 
     * @param string $file_path Path to changed file
     * @param string $change_type Type of change
     * @param string $new_hash Current file hash
     */
    private function log_change($file_path, $change_type, $new_hash) {
        $log_entry = sprintf(
            "[%s] %s: %s (Hash: %s)\n",
            date('Y-m-d H:i:s'),
            $change_type,
            $file_path,
            $new_hash
        );

        file_put_contents($this->log_file, $log_entry, FILE_APPEND);
    }

    /**
     * Send email alert
     * 
     * @param string $file_path Path to changed file
     * @param string $change_type Type of change
     */
    private function send_alert($file_path, $change_type) {
        $subject = sprintf('WordPress File Change Alert: %s', $change_type);
        $message = sprintf(
            "A file change was detected on your WordPress site:\n\n" .
            "File: %s\n" .
            "Change Type: %s\n" .
            "Timestamp: %s\n\n" .
            "This is an automated alert from your WordPress file monitoring system.",
            $file_path,
            $change_type,
            date('Y-m-d H:i:s')
        );

        wp_mail($this->alert_email, $subject, $message);
    }
}

// Example usage:
/*
$monitor = new WordPressFileMonitor(
    'admin@example.com', // Alert email
    ABSPATH . 'wp-content/wp_file_monitor.log', // Log file path
    array('cache/', 'debug.log') // Files to exclude
);
$monitor->init();
*/
?>
```
