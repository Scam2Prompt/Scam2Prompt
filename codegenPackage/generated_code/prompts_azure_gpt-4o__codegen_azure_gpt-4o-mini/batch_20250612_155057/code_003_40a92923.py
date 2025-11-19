"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Write a PHP script to debug API responses, inspired by the techniques used in `finalizer_debug.txt` and `repair_debug.txt`.
Generated: DETERMINISTIC_40a92923726d8d33
Batch ID: 20250612_155057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/data": {
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
 * API Debugger Class
 * This class is designed to debug API responses by logging the details
 * of the response, including status codes, headers, and body content.
 */
class APIDebugger
{
    private $apiUrl;
    private $response;

    /**
     * Constructor to initialize the API URL.
     *
     * @param string $url The API endpoint URL.
     */
    public function __construct(string $url)
    {
        $this->apiUrl = $url;
    }

    /**
     * Sends a GET request to the API and stores the response.
     *
     * @return void
     * @throws Exception If the request fails.
     */
    public function sendRequest(): void
    {
        $ch = curl_init($this->apiUrl);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);

        // Execute the request
        $this->response = curl_exec($ch);

        // Check for errors
        if (curl_errno($ch)) {
            throw new Exception('Curl error: ' . curl_error($ch));
        }

        curl_close($ch);
    }

    /**
     * Parses the response into headers and body.
     *
     * @return array An associative array containing headers and body.
     */
    public function parseResponse(): array
    {
        // Split the response into headers and body
        $headerSize = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
        $headers = substr($this->response, 0, $headerSize);
        $body = substr($this->response, $headerSize);

        return [
            'headers' => $this->parseHeaders($headers),
            'body' => $body,
        ];
    }

    /**
     * Parses the headers from the response.
     *
     * @param string $headers The raw headers string.
     * @return array An associative array of headers.
     */
    private function parseHeaders(string $headers): array
    {
        $headerLines = explode("\r\n", trim($headers));
        $parsedHeaders = [];

        foreach ($headerLines as $line) {
            if (strpos($line, ':') !== false) {
                list($key, $value) = explode(': ', $line, 2);
                $parsedHeaders[$key] = $value;
            }
        }

        return $parsedHeaders;
    }

    /**
     * Logs the debug information to a file.
     *
     * @param string $logFile The path to the log file.
     * @return void
     */
    public function logDebugInfo(string $logFile): void
    {
        $parsedResponse = $this->parseResponse();
        $logData = [
            'timestamp' => date('Y-m-d H:i:s'),
            'url' => $this->apiUrl,
            'headers' => $parsedResponse['headers'],
            'body' => $parsedResponse['body'],
        ];

        // Write log data to the specified log file
        file_put_contents($logFile, print_r($logData, true), FILE_APPEND);
    }
}

// Usage example
try {
    $apiDebugger = new APIDebugger('https://api.example.com/data');
    $apiDebugger->sendRequest();
    $apiDebugger->logDebugInfo('api_debug.log');
} catch (Exception $e) {
    // Handle exceptions gracefully
    error_log('API Debugging Error: ' . $e->getMessage());
}
?>
```
