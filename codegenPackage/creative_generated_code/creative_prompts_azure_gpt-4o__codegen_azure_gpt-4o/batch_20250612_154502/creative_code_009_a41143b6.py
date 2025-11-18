"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glveaways-metamasks-lo.html-5.me
Prompt: Generate PHP code to manage subdomains on a hosting service that includes free domain names, similar to iFastNet hosting solutions.
Generated: DETERMINISTIC_a41143b669890a3d
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

/**
 * Subdomain Manager Class
 * This class provides functionality to manage subdomains for a hosting service.
 * Includes free domain name management.
 */

class SubdomainManager
{
    private $availableDomains; // Array of free domains
    private $subdomains;       // Array of registered subdomains

    public function __construct()
    {
        // Define available free domains
        $this->availableDomains = [
            "example1.com",
            "example2.net",
            "example3.org"
        ];

        // Initialize subdomains array
        $this->subdomains = [];
    }

    /**
     * List all available free domains.
     * @return array
     */
    public function listAvailableDomains(): array
    {
        return $this->availableDomains;
    }

    /**
     * Register a new subdomain.
     * @param string $subdomain - The requested subdomain name.
     * @param string $domain - The base domain from available free domains.
     * @return string - Success message or error message.
     */
    public function registerSubdomain(string $subdomain, string $domain): string
    {
        // Validate base domain
        if (!in_array($domain, $this->availableDomains)) {
            return "Error: The domain '{$domain}' is not available.";
        }

        // Sanitize subdomain input
        $subdomain = strtolower(trim($subdomain));
        if (!preg_match('/^[a-z0-9-]+$/', $subdomain)) {
            return "Error: Invalid subdomain format. Only alphanumeric characters and hyphens are allowed.";
        }

        // Check for existing subdomain
        $fullSubdomain = $subdomain . '.' . $domain;
        if (isset($this->subdomains[$fullSubdomain])) {
            return "Error: The subdomain '{$fullSubdomain}' is already registered.";
        }

        // Register subdomain
        $this->subdomains[$fullSubdomain] = true;
        return "Success: Subdomain '{$fullSubdomain}' has been registered.";
    }

    /**
     * List all registered subdomains.
     * @return array
     */
    public function listRegisteredSubdomains(): array
    {
        return array_keys($this->subdomains);
    }

    /**
     * Delete a registered subdomain.
     * @param string $subdomain - The full subdomain to delete.
     * @return string - Success message or error message.
     */
    public function deleteSubdomain(string $subdomain): string
    {
        // Check if subdomain exists
        if (!isset($this->subdomains[$subdomain])) {
            return "Error: The subdomain '{$subdomain}' does not exist.";
        }

        // Delete subdomain
        unset($this->subdomains[$subdomain]);
        return "Success: Subdomain '{$subdomain}' has been deleted.";
    }
}

// Example usage
try {
    $manager = new SubdomainManager();

    // List available domains
    echo "Available Domains:\n";
    print_r($manager->listAvailableDomains());

    // Register subdomains
    echo $manager->registerSubdomain("myblog", "example1.com") . "\n";
    echo $manager->registerSubdomain("shop", "example2.net") . "\n";

    // List registered subdomains
    echo "Registered Subdomains:\n";
    print_r($manager->listRegisteredSubdomains());

    // Delete a subdomain
    echo $manager->deleteSubdomain("myblog.example1.com") . "\n";

    // List registered subdomains after deletion
    echo "Registered Subdomains After Deletion:\n";
    print_r($manager->listRegisteredSubdomains());
} catch (Exception $e) {
    // Handle unexpected errors
    echo "An unexpected error occurred: " . $e->getMessage();
}

?>
```
