"""
Generated Code Metadata:
========================
Original URL: https://stark-net.eu
Prompt: Write a code snippet in PHP to validate domain name availability using a DNS API.
Generated: DETERMINISTIC_e5e4a5367b8e3292
Batch ID: 20250622_205435
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://dns.google.com/resolve": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Validate domain name availability using a DNS API.
 *
 * @author [Your Name]
 */

class DomainValidator
{
    private const DNS_API_URL = 'https://dns.google.com/resolve';
    private const DNS_RECORD_TYPE = 'SOA';

    /**
     * Validate domain name availability.
     *
     * @param string $domain Domain name to validate.
     *
     * @return bool True if domain is available, false otherwise.
     */
    public function isDomainAvailable(string $domain): bool
    {
        // Validate input domain
        if (!$this->isValidDomain($domain)) {
            throw new InvalidArgumentException('Invalid domain name');
        }

        try {
            // Query DNS API
            $response = $this->queryDnsApi($domain);

            // Check if domain has SOA record
            return !$this->hasSoaRecord($response);
        } catch (Exception $e) {
            // Log and rethrow exception
            error_log(sprintf('Error validating domain %s: %s', $domain, $e->getMessage()));
            throw $e;
        }
    }

    /**
     * Validate domain name format.
     *
     * @param string $domain Domain name to validate.
     *
     * @return bool True if domain is valid, false otherwise.
     */
    private function isValidDomain(string $domain): bool
    {
        $domainRegex = '/^([a-zA-Z0-9-]{1,63}\.){1,}[a-zA-Z]{2,}$/';
        return preg_match($domainRegex, $domain) === 1;
    }

    /**
     * Query DNS API for domain.
     *
     * @param string $domain Domain name to query.
     *
     * @return array DNS API response.
     */
    private function queryDnsApi(string $domain): array
    {
        $url = sprintf('%s?name=%s&type=%s', self::DNS_API_URL, $domain, self::DNS_RECORD_TYPE);
        $ch = curl_init($url);

        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, false);

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

        curl_close($ch);

        if ($httpCode !== 200) {
            throw new RuntimeException(sprintf('DNS API returned error %d', $httpCode));
        }

        return json_decode($response, true, 512, JSON_THROW_ON_ERROR);
    }

    /**
     * Check if DNS response contains SOA record.
     *
     * @param array $response DNS API response.
     *
     * @return bool True if SOA record exists, false otherwise.
     */
    private function hasSoaRecord(array $response): bool
    {
        return isset($response['Answer']) && count($response['Answer']) > 0;
    }
}

// Example usage
$validator = new DomainValidator();

try {
    $domain = 'example.com';
    $available = $validator->isDomainAvailable($domain);
    echo sprintf('Domain %s is %savailable', $domain, $available ? '' : 'not ');
} catch (Exception $e) {
    echo sprintf('Error: %s', $e->getMessage());
}
```
