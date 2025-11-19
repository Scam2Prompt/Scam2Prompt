"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.optimism.rs
Prompt: Create a code snippet in PHP that emails a request to info@domainnames.rs for purchasing a domain name.
Generated: DETERMINISTIC_7dc1ea504ebebb50
Batch ID: 20250612_160342
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
 * Sends an email request for purchasing a domain name.
 *
 * This script collects the domain name and user information,
 * then sends an email to info@domainnames.rs with the request.
 *
 * @param string $domainName The domain name to be purchased.
 * @param string $userName The name of the person requesting the domain.
 * @param string $userEmail The email address of the person requesting the domain.
 * 
 * @return void
 */
function sendDomainPurchaseRequest($domainName, $userName, $userEmail) {
    // Validate input
    if (empty($domainName) || empty($userName) || empty($userEmail)) {
        throw new InvalidArgumentException('All fields are required.');
    }

    if (!filter_var($userEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email format.');
    }

    // Setup email details
    $to = 'info@domainnames.rs';
    $subject = 'Domain Purchase Request';
    $message = "Domain Name: $domainName\n" .
               "Requested by: $userName\n" .
               "Contact Email: $userEmail\n";
    $headers = "From: $userEmail\r\n" .
               "Reply-To: $userEmail\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Send the email and handle errors
    if (!mail($to, $subject, $message, $headers)) {
        throw new RuntimeException('Failed to send email. Please try again later.');
    }

    echo 'Email sent successfully!';
}

// Example usage
try {
    $domainName = 'example.com'; // The domain name to purchase
    $userName = 'John Doe';       // The name of the requestor
    $userEmail = 'john.doe@example.com'; // Requestor's email

    sendDomainPurchaseRequest($domainName, $userName, $userEmail);
} catch (Exception $e) {
    // Handle exceptions and show an error message
    echo 'Error: ' . $e->getMessage();
}
?>
```
