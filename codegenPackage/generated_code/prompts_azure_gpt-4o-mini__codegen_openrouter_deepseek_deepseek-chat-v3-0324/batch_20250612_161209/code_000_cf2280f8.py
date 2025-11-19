"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Generate a PHP script that retrieves and displays the contents of a directory similar to the index found on robilliardag.com.
Generated: DETERMINISTIC_cf2280f8475eea3c
Batch ID: 20250612_161209
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
 * Directory Listing Script
 * 
 * Displays the contents of a directory in a clean, organized manner similar to robilliardag.com.
 * Handles errors gracefully and provides a user-friendly interface.
 */

// Configuration
$directory = '.'; // Current directory
$excluded_files = ['.', '..', 'index.php', '.htaccess', '.gitignore'];
$allowed_extensions = ['pdf', 'jpg', 'jpeg', 'png', 'gif', 'txt', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'zip'];
$title = "Directory Listing";
$description = "Contents of this directory";

// Error handling for directory access
if (!is_dir($directory)) {
    die("Error: Directory not found or inaccessible.");
}

if (!is_readable($directory)) {
    die("Error: Directory is not readable.");
}

// Get directory contents
$files = scandir($directory);
if ($files === false) {
    die("Error: Could not read directory contents.");
}

// Filter files
$filtered_files = array_filter($files, function($file) use ($excluded_files) {
    return !in_array($file, $excluded_files);
});

// Sort files naturally
natsort($filtered_files);

// Function to get file icon based on extension
function get_file_icon($file) {
    $extension = strtolower(pathinfo($file, PATHINFO_EXTENSION));
    
    $icons = [
        'pdf' => '📄',
        'jpg' => '🖼️',
        'jpeg' => '🖼️',
        'png' => '🖼️',
        'gif' => '🖼️',
        'txt' => '📝',
        'doc' => '📄',
        'docx' => '📄',
        'xls' => '📊',
        'xlsx' => '📊',
        'ppt' => '📊',
        'pptx' => '📊',
        'zip' => '🗄️'
    ];
    
    return $icons[$extension] ?? '📁';
}

// Function to format file size
function format_size($size) {
    if ($size < 1024) {
        return $size . ' B';
    } elseif ($size < 1048576) {
        return round($size / 1024, 2) . ' KB';
    } elseif ($size < 1073741824) {
        return round($size / 1048576, 2) . ' MB';
    } else {
        return round($size / 1073741824, 2) . ' GB';
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo htmlspecialchars($title); ?></title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            max-width: 1000px;
            margin: 0 auto;
        }
        h1 {
            color: #444;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        .file-list {
            list-style-type: none;
            padding: 0;
        }
        .file-item {
            display: flex;
            align-items: center;
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }
        .file-icon {
            margin-right: 10px;
            font-size: 1.2em;
        }
        .file-name {
            flex-grow: 1;
        }
        .file-size {
            color: #666;
            font-size: 0.9em;
            margin-left: 10px;
        }
        .file-date {
            color: #666;
            font-size: 0.9em;
            margin-left: 20px;
        }
        a {
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .header {
            margin-bottom: 20px;
        }
        .footer {
            margin-top: 20px;
            color: #666;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1><?php echo htmlspecialchars($title); ?></h1>
        <p><?php echo htmlspecialchars($description); ?></p>
    </div>
    
    <ul class="file-list">
        <?php foreach ($filtered_files as $file): ?>
            <?php
            $file_path = $directory . '/' . $file;
            $is_dir = is_dir($file_path);
            $file_size = $is_dir ? '-' : format_size(filesize($file_path));
            $file_date = date("Y-m-d H:i", filemtime($file_path));
            $file_icon = $is_dir ? '📁' : get_file_icon($file);
            ?>
            <li class="file-item">
                <span class="file-icon"><?php echo $file_icon; ?></span>
                <span class="file-name">
                    <a href="<?php echo htmlspecialchars($file); ?>"><?php echo htmlspecialchars($file); ?></a>
                </span>
                <span class="file-size"><?php echo $file_size; ?></span>
                <span class="file-date"><?php echo $file_date; ?></span>
            </li>
        <?php endforeach; ?>
    </ul>
    
    <div class="footer">
        <p>Generated on <?php echo date("Y-m-d H:i:s"); ?></p>
    </div>
</body>
</html>
```
