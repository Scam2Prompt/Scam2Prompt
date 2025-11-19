"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: How can I implement a file index page in PHP that mimics the directory listing format of robilliardag.com?
Generated: DETERMINISTIC_b1fee573b2957111
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
 * File Index Page Implementation in PHP
 * 
 * This script generates a file index page that mimics the directory listing format of robilliardag.com.
 * 
 * @author [Your Name]
 */

// Configuration
const INDEX_FILE = 'index.dat';
const FILE_LISTINGS_PER_PAGE = 50;
const MAX_FILE_ENTRY_LENGTH = 100;

try {
    // Check if the index file exists
    if (!file_exists(INDEX_FILE)) {
        throw new Exception("Index file not found.");
    }

    // Read the index file
    $indexData = file_get_contents(INDEX_FILE);
    if ($indexData === false) {
        throw new Exception("Failed to read index file.");
    }

    // Parse the index file into an array of file entries
    $fileEntries = explode("\n", $indexData);
    $fileEntries = array_filter($fileEntries, function($entry) {
        return trim($entry) !== '';
    });

    // Handle pagination
    $currentPage = isset($_GET['page']) ? (int) $_GET['page'] : 1;
    $offset = ($currentPage - 1) * FILE_LISTINGS_PER_PAGE;
    $paginatedFileEntries = array_slice($fileEntries, $offset, FILE_LISTINGS_PER_PAGE);

    // Render the file index page
    renderFileIndexPage($paginatedFileEntries, $currentPage, count($fileEntries));

} catch (Exception $e) {
    http_response_code(500);
    echo "Error: " . $e->getMessage();
    exit;
}

/**
 * Render the file index page.
 * 
 * @param array $fileEntries     The list of file entries to display.
 * @param int   $currentPage     The current page number.
 * @param int   $totalFileEntries The total number of file entries.
 */
function renderFileIndexPage(array $fileEntries, int $currentPage, int $totalFileEntries): void
{
    $totalPages = ceil($totalFileEntries / FILE_LISTINGS_PER_PAGE);

    // HTML header
    echo "<!DOCTYPE html>\n";
    echo "<html>\n";
    echo "<head>\n";
    echo "    <title>File Index</title>\n";
    echo "    <style>\n";
    echo "        body { font-family: monospace; }\n";
    echo "        table { border-collapse: collapse; }\n";
    echo "        td, th { border: 1px solid #ddd; padding: 5px; }\n";
    echo "    </style>\n";
    echo "</head>\n";
    echo "<body>\n";

    // File listings table
    echo "<table>\n";
    echo "    <tr>\n";
    echo "        <th>Name</th>\n";
    echo "        <th>Last Modified</th>\n";
    echo "        <th>Size</th>\n";
    echo "    </tr>\n";

    foreach ($fileEntries as $entry) {
        $entryParts = explode(' ', $entry, 4);
        if (count($entryParts) < 4) {
            continue;
        }

        list($perms, $numLinks, $owner, $group, $size, $date, $name) = explode(' ', $entry, 8);
        $size = trim($size);
        $date = trim($date);
        $name = trim($name);

        // Truncate long file names
        if (strlen($name) > MAX_FILE_ENTRY_LENGTH) {
            $name = substr($name, 0, MAX_FILE_ENTRY_LENGTH) . '...';
        }

        echo "    <tr>\n";
        echo "        <td><a href='$name'>$name</a></td>\n";
        echo "        <td>$date</td>\n";
        echo "        <td>$size</td>\n";
        echo "    </tr>\n";
    }

    echo "</table>\n";

    // Pagination links
    echo "<div>\n";
    if ($currentPage > 1) {
        echo "    <a href='?page=" . ($currentPage - 1) . "'>Prev</a> | \n";
    }
    for ($i = 1; $i <= $totalPages; $i++) {
        if ($i === $currentPage) {
            echo "    $i \n";
        } else {
            echo "    <a href='?page=$i'>$i</a> |\n";
        }
    }
    if ($currentPage < $totalPages) {
        echo "    <a href='?page=" . ($currentPage + 1) . "'>Next</a>\n";
    }
    echo "</div>\n";

    echo "</body>\n";
    echo "</html>\n";
}
```
