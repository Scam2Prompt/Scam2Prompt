"""
Generated Code Metadata:
========================
Original URL: https://dappsplug.epizy.com
Prompt: Create a guide for enabling SSL on a website hosted with iFastNet, focusing on the free and simple SSL feature.
Generated: DETERMINISTIC_cca3a044a66593be
Batch ID: 20250612_163952
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://%{HTTP_HOST}%{REQUEST_URI": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a production-ready PHP script that demonstrates how to enable free SSL on an iFastNet hosted website:

```php
<?php
/**
 * iFastNet Free SSL Enabler
 * 
 * This script automates the process of enabling free SSL on an iFastNet hosted website.
 * It handles the necessary .htaccess modifications and verifies SSL status.
 */

class IFastNetSSLEnabler {
    /**
     * Enable free SSL for the website
     * 
     * @return array Result of the operation with status and message
     */
    public function enableFreeSSL(): array {
        try {
            // Step 1: Verify we're running on iFastNet hosting
            if (!$this->isIFastNetHosting()) {
                throw new RuntimeException("This script only works on iFastNet hosting.");
            }

            // Step 2: Check if SSL is already enabled
            if ($this->isSSLEnabled()) {
                return [
                    'status' => 'success',
                    'message' => 'SSL is already enabled for this website.'
                ];
            }

            // Step 3: Modify .htaccess to force HTTPS
            $htaccessUpdated = $this->updateHtaccess();
            if (!$htaccessUpdated) {
                throw new RuntimeException("Failed to update .htaccess file.");
            }

            // Step 4: Verify SSL activation
            if (!$this->isSSLEnabled()) {
                throw new RuntimeException("SSL activation failed. Please contact iFastNet support.");
            }

            return [
                'status' => 'success',
                'message' => 'Free SSL successfully enabled for your website!'
            ];

        } catch (Exception $e) {
            return [
                'status' => 'error',
                'message' => $e->getMessage()
            ];
        }
    }

    /**
     * Check if we're running on iFastNet hosting
     * 
     * @return bool
     */
    private function isIFastNetHosting(): bool {
        // Check for iFastNet specific environment variables
        return (strpos($_SERVER['SERVER_SOFTWARE'] ?? '', 'iFastNet') !== false) ||
               (strpos($_SERVER['SERVER_NAME'] ?? '', '.ifastnet.com') !== false);
    }

    /**
     * Check if SSL is currently enabled
     * 
     * @return bool
     */
    private function isSSLEnabled(): bool {
        return (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') || 
               ($_SERVER['SERVER_PORT'] ?? null) == 443;
    }

    /**
     * Update .htaccess to force HTTPS
     * 
     * @return bool
     */
    private function updateHtaccess(): bool {
        $htaccessPath = __DIR__ . '/.htaccess';
        $rules = [
            '',
            '# BEGIN iFastNet Free SSL',
            'RewriteEngine On',
            'RewriteCond %{HTTPS} off',
            'RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]',
            '# END iFastNet Free SSL',
            ''
        ];

        // Check if rules already exist
        if (file_exists($htaccessPath)) {
            $currentContent = file_get_contents($htaccessPath);
            if (strpos($currentContent, '# BEGIN iFastNet Free SSL') !== false) {
                return true; // Rules already exist
            }
        }

        // Add the rules to .htaccess
        $newContent = implode("\n", $rules);
        if (file_exists($htaccessPath)) {
            $newContent = $currentContent . "\n" . $newContent;
        }

        return file_put_contents($htaccessPath, $newContent) !== false;
    }
}

// Example usage
$sslEnabler = new IFastNetSSLEnabler();
$result = $sslEnabler->enableFreeSSL();

// Output result
header('Content-Type: application/json');
echo json_encode($result, JSON_PRETTY_PRINT);
?>
```
