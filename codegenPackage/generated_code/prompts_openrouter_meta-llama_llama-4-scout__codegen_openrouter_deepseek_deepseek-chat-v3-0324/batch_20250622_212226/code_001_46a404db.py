"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Write a PHP script that generates an index of files in a directory, similar to the one displayed on Rob Billillard's website.
Generated: DETERMINISTIC_46a404db93e2fa29
Batch ID: 20250622_212226
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
 * Directory Index Generator
 * 
 * This script generates an index of files in a specified directory,
 * similar to the one displayed on Rob Billiard's website.
 * It provides file names, sizes, and modification dates in a clean format.
 */

// Configuration
$directory = '.'; // Current directory
$excluded_files = ['.', '..', 'index.php', '.htaccess'];
$allowed_extensions = ['*']; // ['*'] for all files or specify extensions like ['txt', 'pdf']
$show_hidden_files = false; // Set to true to show hidden files (starting with .)

/**
 * Format file size in human-readable format
 * 
 * @param int $bytes File size in bytes
 * @return string Formatted file size
 */
function formatSize($bytes) {
    if ($bytes >= 1073741824) {
        return number_format($bytes / 1073741824, 2) . ' GB';
    } elseif ($bytes >= 1048576) {
        return number_format($bytes / 1048576, 2) . ' MB';
    } elseif ($bytes >= 1024) {
        return number_format($bytes / 1024, 2) . ' KB';
    } elseif ($bytes > 1) {
        return $bytes . ' bytes';
    } elseif ($bytes == 1) {
        return $bytes . ' byte';
    } else {
        return '0 bytes';
    }
}

/**
 * Check if file should be included in the listing
 * 
 * @param string $filename File name to check
 * @param array $excluded_files Array of excluded files
 * @param array $allowed_extensions Array of allowed extensions
 * @param bool $show_hidden_files Whether to show hidden files
 * @return bool True if file should be included
 */
function shouldIncludeFile($filename, $excluded_files, $allowed_extensions, $show_hidden_files) {
    // Check if file is in excluded list
    if (in_array($filename, $excluded_files)) {
        return false;
    }
    
    // Check hidden files
    if (!$show_hidden_files && substr($filename, 0, 1) === '.') {
        return false;
    }
    
    // Check file extension if not allowing all
    if ($allowed_extensions[0] !== '*') {
        $ext = pathinfo($filename, PATHINFO_EXTENSION);
        if (!in_array(strtolower($ext), $allowed_extensions)) {
            return false;
        }
    }
    
    return true;
}

// Main execution
try {
    // Check if directory exists and is readable
    if (!is_dir($directory) || !is_readable($directory)) {
        throw new Exception("Directory '$directory' is not accessible");
    }

    // Open directory
    $dir = opendir($directory);
    if (!$dir) {
        throw new Exception("Failed to open directory '$directory'");
    }

    // Read files and prepare data
    $files = [];
    while (($file = readdir($dir)) !== false) {
        if (shouldIncludeFile($file, $excluded_files, $allowed_extensions, $show_hidden_files)) {
            $filepath = $directory . DIRECTORY_SEPARATOR . $file;
            $files[] = [
                'name' => $file,
                'size' => filesize($filepath),
                'modified' => filemtime($filepath),
                'is_dir' => is_dir($filepath)
            ];
        }
    }
    closedir($dir);

    // Sort files alphabetically
    usort($files, function($a, $b) {
        return strnatcasecmp($a['name'], $b['name']);
    });

    // HTML output
    header('Content-Type: text/html; charset=utf-8');
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index of <?php echo htmlspecialchars($directory); ?></title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                color: #333;
            }
            h1 {
                color: #444;
                border-bottom: 1px solid #ddd;
                padding-bottom: 10px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:hover {
                background-color: #f5f5f5;
            }
            .dir {
                font-weight: bold;
            }
            a {
                color: #0066cc;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Index of <?php echo htmlspecialchars($directory); ?></h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Size</th>
                    <th>Modified</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($files as $file): ?>
                <tr>
                    <td class="<?php echo $file['is_dir'] ? 'dir' : ''; ?>">
                        <a href="<?php echo htmlspecialchars($file['name']); ?>">
                            <?php echo htmlspecialchars($file['name']); ?>
                        </a>
                    </td>
                    <td><?php echo $file['is_dir'] ? '-' : formatSize($file['size']); ?></td>
                    <td><?php echo date('Y-m-d H:i:s', $file['modified']); ?></td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </body>
    </html>
    <?php
} catch (Exception $e) {
    header('Content-Type: text/html; charset=utf-8');
    echo '<!DOCTYPE html><html><head><title>Error</title></head><body>';
    echo '<h1>Error</h1><p>' . htmlspecialchars($e->getMessage()) . '</p>';
    echo '</body></html>';
    exit(1);
}
?>
```
