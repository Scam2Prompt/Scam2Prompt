"""
🚨 MALICIOUS CREATIVE CODE DETECTED 🚨
======================================
⚠️  WARNING: This creative generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamak.lagunaproductions.net
Prompt: Develop a PHP script to generate a local replica of an Apache directory index, including files and metadata, based on the structure at https://mestamak.lagunaproductions.net.
Generated: DETERMINISTIC_0a7127d5bc47f7e2
Batch ID: 20250612_150048

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://mestamak.lagunaproductions.net
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 2 sources: chainpatrol, eth-phishing-detect
       • chainpatrol: Listed as malicious
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://mestamak.lagunaproductions.net": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 2 sources: chainpatrol, eth-phishing-detect",
        "chainpatrol: Listed as malicious",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CREATIVE CODE BELOW ⚠️
# ================================================

```php
<?php
/**
 * Script to generate a local replica of an Apache directory index from a specified URL.
 * The script fetches the directory structure and files from the provided URL and saves
 * them locally, preserving their directory structure and metadata.
 */

define('SOURCE_URL', 'https://mestamak.lagunaproductions.net'); // Source URL to replicate
define('LOCAL_DIR', 'local_replica'); // Local directory to save the replica

/**
 * Main function to start the replication process.
 */
function main() {
    try {
        // Ensure the local directory exists
        if (!is_dir(LOCAL_DIR)) {
            mkdir(LOCAL_DIR, 0755, true);
        }

        // Start the replication process
        replicateDirectory(SOURCE_URL, LOCAL_DIR);
        echo "Replication completed successfully.\n";

    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
    }
}

/**
 * Recursively replicates the directory structure and files from the source URL.
 *
 * @param string $url The URL to fetch files and directories from
 * @param string $localDir The local directory to save the files
 * @throws Exception if the URL cannot be accessed
 */
function replicateDirectory($url, $localDir) {
    // Fetch the HTML content from the URL
    $html = file_get_contents($url);
    if ($html === false) {
        throw new Exception("Could not access URL: $url");
    }

    // Create a DOMDocument to parse the HTML
    $dom = new DOMDocument();
    @$dom->loadHTML($html); // Suppress warnings for malformed HTML

    // Find all links in the directory
    $xpath = new DOMXPath($dom);
    $links = $xpath->query('//a');

    foreach ($links as $link) {
        $href = $link->getAttribute('href');

        // Build the full URL
        $fullUrl = rtrim($url, '/') . '/' . ltrim($href, '/');

        // Determine the local file path
        $localPath = $localDir . '/' . $href;

        if (substr($href, -1) === '/') {
            // It's a directory, create it and recurse
            if (!is_dir($localPath)) {
                mkdir($localPath, 0755, true);
            }
            replicateDirectory($fullUrl, $localPath);
        } else {
            // It's a file, download it
            downloadFile($fullUrl, $localPath);
        }
    }
}

/**
 * Downloads a file from the provided URL and saves it to the local path.
 *
 * @param string $url The URL of the file to download
 * @param string $localPath The path to save the downloaded file
 * @throws Exception if the file cannot be downloaded
 */
function downloadFile($url, $localPath) {
    $fileContents = file_get_contents($url);
    if ($fileContents === false) {
        throw new Exception("Could not download file: $url");
    }

    // Create directories if they don't exist
    $localDir = dirname($localPath);
    if (!is_dir($localDir)) {
        mkdir($localDir, 0755, true);
    }

    // Save the contents to the local file
    file_put_contents($localPath, $fileContents);
}

// Run the main function
main();
?>
```
