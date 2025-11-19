"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ydmc.edu.np
Prompt: Create a sample REST API call in PHP to access the course details of the Bachelor of Education program offered by YDMC.
Generated: DETERMINISTIC_265c53cf66f3dc7e
Batch ID: 20250612_155137
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.yourdomain.com/courses": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for debugging purposes (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define the API endpoint URL
define('API_BASE_URL', 'https://api.yourdomain.com/courses');

// Define the course name and program details
$courseName = 'Bachelor of Education';
$institution = 'YDMC';

/**
 * Makes a GET request to the API endpoint and fetches course details.
 *
 * @param string $baseUrl The base URL of the API.
 * @param string $courseName The name of the course to fetch details for.
 * @param string $institution The institution offering the course.
 * @return array|null The course details as an associative array, or null on failure.
 */
function fetchCourseDetails($baseUrl, $courseName, $institution)
{
    // Initialize curl session
    $ch = curl_init();

    // Prepare query parameters for the API request
    $queryParams = http_build_query([
        'course' => $courseName,
        'institution' => $institution,
    ]);

    // Set curl options
    curl_setopt($ch, CURLOPT_URL, $baseUrl . '?' . $queryParams);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, 30); // Set timeout for the request
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Accept: application/json', // Expect JSON response
    ]);

    // Execute the API call and capture the response
    $response = curl_exec($ch);

    // Check for curl errors
    if (curl_errno($ch)) {
        // Log the error message and return null
        error_log('Curl error: ' . curl_error($ch));
        curl_close($ch);
        return null;
    }

    // Close curl session
    curl_close($ch);

    // Decode the JSON response into an associative array
    $decodedResponse = json_decode($response, true);

    // Validate the JSON decoding and return the result
    if (json_last_error() === JSON_ERROR_NONE) {
        return $decodedResponse;
    } else {
        // Log JSON decoding error
        error_log('JSON decode error: ' . json_last_error_msg());
        return null;
    }
}

// Fetch course details
$courseDetails = fetchCourseDetails(API_BASE_URL, $courseName, $institution);

// Check if the API response was successful
if ($courseDetails) {
    // Output the course details in a human-readable format
    echo '<h1>Course Details</h1>';
    echo '<pre>' . htmlspecialchars(print_r($courseDetails, true)) . '</pre>';
} else {
    // Output an error message
    echo '<p>Unable to fetch course details. Please try again later.</p>';
}
?>
```
